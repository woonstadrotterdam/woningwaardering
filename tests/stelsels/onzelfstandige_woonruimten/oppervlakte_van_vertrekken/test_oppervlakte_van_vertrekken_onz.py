"""Oppervlakte van vertrekken, onzelfstandige woonruimten (rubriek 1)."""

import pytest

from tests.input import element, ruimte
from tests.utils import (
    aantal_per_bovenliggende,
    aantal_per_naam,
    assert_stelselgroep_output,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def oppervlakte_van_vertrekken(peildatum):
    return OppervlakteVanVertrekken(peildatum=peildatum)


def test_OppervlakteVanVertrekken_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        OppervlakteVanVertrekken,
    )


# Gemeenschappelijke vertrekken


def test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """De oppervlakte van privévertrekken en de toe te rekenen oppervlakte van gemeenschappelijke vertrekken worden opgeteld.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.1
    - wettekst, Bijlage I onder B, toelichting rubriek 1

    De oppervlakte van alle vertrekken samen wordt na saldering afgerond op hele
    vierkante meters.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.1
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Het voorbeeld uit 2.2.1.1: apart afronden zou 20 punten geven.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=10.4),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=40.4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 10.4},
        "Gedeeld met 4 onzelfstandige woonruimten": {
            Ruimtedetailsoort.keuken.naam: 40.4
        },
    }
    # 10,40 m² privé plus 40,40 m² gedeeld door 4 (10,10 m²) is 20,50 m², afgerond 21.
    assert groep.punten == 21.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijk_vertrek_wordt_gedeeld_door_aantal_woonruimten_met_toegang(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een gemeenschappelijk vertrek wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot dat vertrek.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1
    - wettekst, Bijlage I onder B, onderdeel 1
    """
    # Elk vertrek heeft een eigen aantal woonruimten; één deler voor alle vertrekken geeft een ander totaal.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=12,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=20,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Gedeeld met 6 onzelfstandige woonruimten": {
            Ruimtedetailsoort.woonkamer.naam: 12.0
        },
        "Gedeeld met 4 onzelfstandige woonruimten": {
            Ruimtedetailsoort.slaapkamer.naam: 20.0
        },
    }
    # 12 / 6 + 20 / 4 = 2 + 5 = 7 m².
    assert groep.punten == 7.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_1(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een vertrek dat niet met een ander adres wordt gedeeld, wordt in rubriek 1 gewaardeerd en niet in rubriek 9.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2
    - wettekst, Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Slaapkamer1 is alleen van dit adres, Slaapkamer2 wordt met een tweede adres gedeeld.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                oppervlakte=5,
                gedeeld_met_aantal_adressen=1,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {"Privé": {"Slaapkamer1": 5.0}}
    assert groep.punten == 5.0
    vergelijk_met_testreferentie(eenheid, groep)


# Afronding


@pytest.mark.parametrize(
    ("oppervlakte", "verwachte_punten"),
    [
        pytest.param(10.49, 10.0, id="net_onder_een_halve_m2"),
        pytest.param(10.5, 11.0, id="precies_een_halve_m2"),
    ],
)
def test_oppervlakte_wordt_vanaf_een_halve_m2_naar_boven_afgerond(
    oppervlakte_van_vertrekken,
    vergelijk_met_testreferentie,
    oppervlakte,
    verwachte_punten,
):
    """De oppervlakte van de vertrekken wordt vanaf 0,5 m² naar boven afgerond op hele m².

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.1
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Net onder en precies op de grens van 0,5 m².
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=oppervlakte)]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.woonkamer.naam: oppervlakte}
    assert groep.punten == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


# Voorwaarden van een vertrek


def test_vertrek_moet_minimaal_4m2_groot_zijn(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een ruimte kleiner dan 4 m² wordt niet als vertrek gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.2
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # 0,01 m² onder de grens van 4 m² en precies op de grens.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer1", oppervlakte=3.99),
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer2", oppervlakte=4),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Slaapkamer2": 4.0}
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_keuken_badkamer_en_doucheruimte_zijn_ook_onder_4m2_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken, badkamer en doucheruimte zijn ook onder de 4 m² een vertrek.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Elk van de vier ruimten is 0,01 m² onder de 4 m² van een vertrek.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.keuken, oppervlakte=3.99),
            ruimte(Ruimtedetailsoort.badkamer, oppervlakte=3.99),
            ruimte(Ruimtedetailsoort.badkamer_met_toilet, oppervlakte=3.99),
            ruimte(Ruimtedetailsoort.doucheruimte, oppervlakte=3.99),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        Ruimtedetailsoort.keuken.naam: 3.99,
        Ruimtedetailsoort.badkamer.naam: 3.99,
        Ruimtedetailsoort.badkamer_met_toilet.naam: 3.99,
        Ruimtedetailsoort.doucheruimte.naam: 3.99,
    }
    # 4 × 3,99 m² is 15,96 m², afgerond 16.
    assert groep.punten == 16.0
    vergelijk_met_testreferentie(eenheid, groep)


# Aangeleverde ruimtesoort


def test_keuken_aangeleverd_als_overige_ruimte_is_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken die als overige ruimte is aangeleverd, wordt als vertrek gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.2
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Als overige ruimte aangeleverd: de ruimtesoort bepaalt niet of een keuken een vertrek is.
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, soort=Ruimtesoort.overige_ruimten)]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.keuken.naam: 10.0}
    assert groep.punten == 10.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Zolderruimte


def test_zoldervertrek_is_een_vertrek_tenzij_er_alleen_een_vlizotrap_is(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een zoldervertrek is een vertrek, tenzij het alleen via een vlizotrap bereikbaar is.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.3
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Alleen een vlizotrap sluit een zoldervertrek als vertrek uit.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek1",
                elementen=[element(Bouwkundigelementdetailsoort.trap)],
            ),
            # Zonder trap als element: de detailsoort gaat uit van een vaste trap.
            ruimte(Ruimtedetailsoort.zoldervertrek, naam="Zoldervertrek2"),
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek3",
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Zoldervertrek1": 10.0,
        "Zoldervertrek2": 10.0,
    }
    assert groep.punten == 20.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_zolder_is_nooit_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een zolderruimte met de detailsoort `zolder` wordt nooit als vertrek gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.2.1.3
    - wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Als vertrek en als overige ruimte aangeleverd: de ruimtesoort verandert niets.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder1", soort=Ruimtesoort.vertrek),
            # Aangeleverd als overige ruimte.
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder2", oppervlakte=1),
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {}
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
