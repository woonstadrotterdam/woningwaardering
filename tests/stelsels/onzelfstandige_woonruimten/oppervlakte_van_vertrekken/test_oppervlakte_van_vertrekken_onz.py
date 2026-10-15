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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.1;
    wettekst, Bijlage I onder B, toelichting rubriek 1.

    De oppervlakte per vertrek wordt afgerond op twee decimalen, en die van
    alle vertrekken samen na saldering op hele vierkante meters.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # Gebaseerd op het rekenvoorbeeld uit de toelichting bij de wettekst, met de
    # keuken als gemeenschappelijk vertrek van drie onzelfstandige woonruimten.
    # Afronden per soort vertrek of één keer na het optellen geeft beide 19 punten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=15.4912),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=11.2395,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    # 15,49 m² privé plus 11,24 m² gedeeld door 3 woonruimten (ongeveer 3,75 m²) is
    # ongeveer 19,24 m², afgerond 19.
    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 15.49},
        "Gedeeld met 3 onzelfstandige woonruimten": {
            Ruimtedetailsoort.keuken.naam: 11.24
        },
    }
    assert groep.punten == 19.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijk_vertrek_wordt_gedeeld_door_aantal_woonruimten_met_toegang(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een gemeenschappelijk vertrek wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot dat vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1;
    implementatietoelichting onzelfstandige woonruimten, 2.1.5; wettekst,
    Bijlage I onder B, onderdeel 1; wettekst, Bijlage I onder B,
    toelichting, inleiding.
    """
    # Een woonkamer gedeeld met 6 en een slaapkamer gedeeld met 5 woonruimten: elk
    # vertrek heeft een eigen aantal.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    # 10 m² gedeeld door 6 en 10 m² gedeeld door 5 is samen ongeveer 3,67 m²,
    # afgerond 4.
    assert aantal_per_bovenliggende(groep) == {
        "Gedeeld met 6 onzelfstandige woonruimten": {
            Ruimtedetailsoort.woonkamer.naam: 10.0
        },
        "Gedeeld met 5 onzelfstandige woonruimten": {
            Ruimtedetailsoort.slaapkamer.naam: 10.0
        },
    }
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_1(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een vertrek dat niet met een ander adres wordt gedeeld, wordt in rubriek 1 gewaardeerd en niet in rubriek 9.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2;
    wettekst, Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # Een `gedeeld_met_aantal_adressen` van 1 betekent dat alleen dit adres de
    # ruimte gebruikt; pas vanaf twee adressen hoort een ruimte in rubriek 9.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=5,
                gedeeld_met_aantal_adressen=1,
            )
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 5.0}
    }
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.2;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
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


def test_keuken_en_badkamer_zijn_ook_onder_4m2_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken en een badkamer zijn ook onder de 4 m² een vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # Een keuken en een badkamer van 2 m², kleiner dan de 4 m² van een vertrek.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.keuken, oppervlakte=2),
            ruimte(Ruimtedetailsoort.badkamer_met_toilet, oppervlakte=2),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        Ruimtedetailsoort.keuken.naam: 2.0,
        Ruimtedetailsoort.badkamer_met_toilet.naam: 2.0,
    }
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


# Aangeleverde ruimtesoort


def test_keuken_aangeleverd_als_overige_ruimte_is_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken die als overige ruimte is aangeleverd, wordt als vertrek gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.2;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # De keuken is als overige ruimte aangeleverd, om te laten zien dat de
    # aangeleverde ruimtesoort niet bepaalt of hij als vertrek telt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=1,
            )
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.keuken.naam: 1.0}
    assert groep.punten == 1.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Zolderruimte


def test_zoldervertrek_is_een_vertrek_tenzij_er_alleen_een_vlizotrap_is(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een zoldervertrek is een vertrek, tenzij het alleen via een vlizotrap bereikbaar is.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # De drie gevallen laten zien dat alleen een vlizotrap een zoldervertrek als
    # vertrek uitsluit.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek1",
                elementen=[element(Bouwkundigelementdetailsoort.trap)],
            ),
            # Zonder trap als bouwkundig element: de detailsoort gaat uit van
            # een vaste trap.
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # De zolder wordt zowel als vertrek als als overige ruimte aangeleverd, om te
    # laten zien dat de aangeleverde ruimtesoort niets verandert.
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
