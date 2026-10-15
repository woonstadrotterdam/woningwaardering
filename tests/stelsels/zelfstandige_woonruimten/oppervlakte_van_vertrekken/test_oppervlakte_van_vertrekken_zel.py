"""Oppervlakte van vertrekken, zelfstandige woonruimten (rubriek 1)."""

import pytest

from tests.input import element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import (
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
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        OppervlakteVanVertrekken,
    )


# Afronding


def test_oppervlakte_wordt_afgerond_na_optellen_van_alle_vertrekken(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """De oppervlakten van alle vertrekken worden eerst opgeteld en dan afgerond op hele m².

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
    """
    # Het rekenvoorbeeld uit de toelichting bij de wettekst.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=15.49),
            ruimte(Ruimtedetailsoort.keuken, oppervlakte=11.24),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        Ruimtedetailsoort.woonkamer.naam: 15.49,
        Ruimtedetailsoort.keuken.naam: 11.24,
    }
    assert groep.punten == 27.0
    vergelijk_met_testreferentie(eenheid, groep)


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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
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


@pytest.mark.parametrize(
    ("oppervlakte_zonder_kast", "verwachte_aantallen", "verwachte_punten"),
    [
        pytest.param(
            3.5,
            {"Slaapkamer (+1 kast)": 4.0},
            4.0,
            id="samen_precies_4m2",
            marks=pytest.mark.toelichting(
                "het vertrek van 3,50 m² en de kast van 0,50 m² zijn samen precies "
                "4,00 m², de minimale oppervlakte van een vertrek"
            ),
        ),
        pytest.param(
            3.49,
            {},
            0.0,
            id="samen_net_onder_4m2",
            marks=pytest.mark.toelichting(
                "het vertrek van 3,49 m² en de kast van 0,50 m² zijn samen 3,99 m², "
                "net onder de minimale oppervlakte van een vertrek"
            ),
        ),
    ],
)
def test_kast_telt_mee_voor_de_minimale_oppervlakte_van_een_vertrek(
    oppervlakte_van_vertrekken,
    vergelijk_met_testreferentie,
    oppervlakte_zonder_kast,
    verwachte_aantallen,
    verwachte_punten,
):
    """Een ruimte kleiner dan 4 m² is een vertrek als zij met haar kast 4 m² of groter is.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
    """
    # De slaapkamer haalt de 4 m² alleen met de kast van 0,5 m² erbij, of net niet.
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.5)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=oppervlakte_zonder_kast,
                verbonden_ruimten=[kast],
            )
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == verwachte_aantallen
    assert groep.punten == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


# Aangeleverde ruimtesoort


def test_keuken_aangeleverd_als_overige_ruimte_is_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken die als overige ruimte is aangeleverd, wordt als vertrek gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
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


def test_schuur_aangeleverd_als_vertrek_is_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een schuur die als vertrek is aangeleverd, wordt als vertrek gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2.
    """
    # Een schuur kan in rubriek 1 of 2 horen, dus de aangeleverde ruimtesoort beslist.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.schuur, soort=Ruimtesoort.vertrek, oppervlakte=6)
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.schuur.naam: 6.0}
    assert groep.punten == 6.0
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte


def test_zoldervertrek_is_een_vertrek_tenzij_er_alleen_een_vlizotrap_is(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een zoldervertrek is een vertrek, tenzij het alleen via een vlizotrap bereikbaar is.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.3;
    implementatietoelichting zelfstandige woonruimten, 2.2.2.3; wettekst,
    Bijlage I onder A, toelichting rubriek 1.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
    """
    # Als vertrek en als overige ruimte aangeleverd: de ruimtesoort verandert niets.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder1", soort=Ruimtesoort.vertrek),
            # Aangeleverd als overige ruimte, en daarvoor met 1 m² te klein.
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder2", oppervlakte=1),
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {}
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
