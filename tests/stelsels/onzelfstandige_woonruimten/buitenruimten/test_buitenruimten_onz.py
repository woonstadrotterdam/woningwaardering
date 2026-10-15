"""Buitenruimten, onzelfstandige woonruimten (rubriek 8)."""

import pytest

from tests.input import ruimte
from tests.utils import (
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Buitenruimten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort


@pytest.fixture()
def buitenruimten(peildatum):
    return Buitenruimten(peildatum=peildatum)


def test_Buitenruimten_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Buitenruimten,
    )


# Privé-buitenruimten


def test_prive_buitenruimte_krijgt_2_punten_plus_035_punt_per_m2(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een privé-buitenruimte krijgt 2 punten plus 0,35 punt per m².

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.1; wettekst,
    Bijlage I onder B, onderdeel 8.
    """
    # Het voorbeeld uit 2.8.1: 10 m² privé-buitenruimte.
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.balkon, oppervlakte=10)]
    )

    groep = buitenruimten.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Ruimtedetailsoort.balkon.naam] == 3.5
    assert punten["Privé buitenruimten aanwezig"] == 2.0
    assert groep.punten == 5.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_prive_buitenruimte_onder_de_minimumafmeting_wordt_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een privé-buitenruimte wordt ook gewaardeerd als zij onder de minimumafmeting voor gemeenschappelijke buitenruimten blijft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.1.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Het balkon van 2 × 0,5 m uit het rekenvoorbeeld bij de wettekst, smaller dan 1,5 m.
            ruimte(
                Ruimtedetailsoort.balkon,
                oppervlakte=1,
                lengte=2000,
                breedte=500,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Ruimtedetailsoort.balkon.naam] == 0.35
    assert punten["Privé buitenruimten aanwezig"] == 2.0
    # Samen 2,35 punten, afgerond op kwartpunten 2,25.
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    "detail_soort",
    [
        pytest.param(Ruimtedetailsoort.carport, id="carport"),
        pytest.param(Ruimtedetailsoort.parkeerplaats, id="parkeerplaats"),
    ],
)
def test_prive_carport_of_parkeerplaats_wordt_als_prive_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie, detail_soort
):
    """Een privé-carport of privé-parkeerplaats wordt als privé-buitenruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.1;
    implementatietoelichting onzelfstandige woonruimten, 2.8.3; wettekst,
    Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    # Niet gedeeld met andere adressen of woonruimten, dus privé.
    eenheid = EenhedenEenheid(ruimten=[ruimte(detail_soort, oppervlakte=12)])

    groep = buitenruimten.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[detail_soort.naam] == 4.2
    assert punten["Privé buitenruimten aanwezig"] == 2.0
    # Samen 6,2 punten, afgerond op kwartpunten 6,25.
    assert groep.punten == 6.25
    vergelijk_met_testreferentie(eenheid, groep)


# Gemeenschappelijke buitenruimten


def test_gemeenschappelijke_buitenruimte_op_hetzelfde_adres_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_onzelfstandige_woonruimten(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte op hetzelfde adres krijgt 0,75 punt per m², gedeeld door het aantal onzelfstandige woonruimten dat toegang heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder B, onderdeel 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.balkon,
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 2 onzelfstandige woonruimten": {
            Ruimtedetailsoort.balkon.naam: 2.25
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_buitenruimte_gedeeld_met_meerdere_adressen_wordt_door_het_aantal_adressen_en_daarna_door_het_aantal_onzelfstandige_woonruimten_gedeeld(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte die met meerdere adressen wordt gedeeld, krijgt 0,75 punt per m², gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder B, onderdeel 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Twee tuinen, elk gedeeld door haar eigen aantal adressen.
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin1",
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin2",
                oppervlakte=6,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    # Tuin1: 4,5 punten gedeeld door 2 adressen en 2 woonruimten is 1,125 punt:
    # in het rapport 1,13.
    assert punten["Gedeeld met 2 adressen"] == {"Tuin1": 1.13}
    # Tuin2: 4,5 punten gedeeld door 3 adressen en 2 woonruimten is 0,75 punt.
    assert punten["Gedeeld met 3 adressen"] == {"Tuin2": 0.75}
    # Samen 1,875 punt, afgerond op kwartpunten 2.
    assert groep.punten == 2.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_buitenruimte_gedeeld_met_meerdere_adressen_zonder_aantal_onzelfstandige_woonruimten_wordt_alleen_door_het_aantal_adressen_gedeeld(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte die met meerdere adressen wordt gedeeld en zonder aantal onzelfstandige woonruimten is aangeleverd, wordt alleen door het aantal adressen gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4;
    implementatietoelichting onzelfstandige woonruimten, 2.8.2.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Zonder aantal onzelfstandige woonruimten: alleen het aantal adressen van elke tuin is de deler.
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin1",
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin2",
                oppervlakte=6,
                gedeeld_met_aantal_adressen=3,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 2 adressen": {"Tuin1": 2.25},
        "Gedeeld met 3 adressen": {"Tuin2": 1.5},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_buitenruimte_zonder_afmetingen_wordt_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte zonder lengte, breedte en hoogte wordt gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.tuin,
                oppervlakte=30,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    # 22,5 punten gedeeld door 4 woonruimten is 5,625 punt: in het rapport 5,63
    # en afgerond op kwartpunten 5,75.
    assert punten_per_naam(groep)[Ruimtedetailsoort.tuin.naam] == 5.63
    assert groep.punten == 5.75
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    (
        "detail_soort",
        "oppervlakte",
        "lengte_mm",
        "breedte_mm",
        "verwachte_punten",
        "verwacht_totaal",
    ),
    [
        pytest.param(
            Ruimtedetailsoort.tuin,
            30,
            10000,
            3000,
            # 22,5 punten gedeeld door 4 woonruimten is 5,625 punt: in het
            # rapport 5,63 en afgerond op kwartpunten 5,75.
            5.63,
            5.75,
            id="boven_de_minimumafmeting",
        ),
        pytest.param(
            Ruimtedetailsoort.balkon,
            4.5,
            3000,
            1500,
            # 3,375 punt gedeeld door 4 woonruimten is 0,84375 punt: in het
            # rapport 0,84 en afgerond op kwartpunten 0,75.
            0.84,
            0.75,
            id="breedte_precies_1500_mm",
            marks=pytest.mark.toelichting(
                "de breedte van 1,5 meter is precies de minimumafmeting; het "
                "balkon is het gemeenschappelijke balkon uit het rekenvoorbeeld "
                "in de toelichting bij de wettekst"
            ),
        ),
    ],
)
def test_gemeenschappelijke_buitenruimte_vanaf_de_minimumafmeting_wordt_gewaardeerd(
    buitenruimten,
    vergelijk_met_testreferentie,
    detail_soort,
    oppervlakte,
    lengte_mm,
    breedte_mm,
    verwachte_punten,
    verwacht_totaal,
):
    """Een gemeenschappelijke buitenruimte met een lengte en breedte van ten minste de minimumafmeting wordt gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Gedeeld, want alleen een gemeenschappelijke buitenruimte heeft een minimumafmeting.
            ruimte(
                detail_soort,
                oppervlakte=oppervlakte,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                lengte=lengte_mm,
                breedte=breedte_mm,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep)[detail_soort.naam] == verwachte_punten
    assert groep.punten == verwacht_totaal
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_buitenruimte_onder_de_minimumafmeting_wordt_niet_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte die in lengte, breedte of hoogte onder de minimumafmeting blijft, wordt niet gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Elke tuin zit op één afmeting één millimeter onder het minimum.
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin1",
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                lengte=1499,
                breedte=1500,
                hoogte=2000,
            ),
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin2",
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                lengte=1500,
                breedte=1499,
                hoogte=2000,
            ),
            ruimte(
                Ruimtedetailsoort.tuin,
                naam="Tuin3",
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                lengte=1500,
                breedte=1500,
                hoogte=1999,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_carport_of_parkeerplaats_wordt_niet_als_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke carport of parkeerplaats wordt niet als buitenruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3; wettekst,
    Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Binnen het eigen adres gedeeld telt ook als gemeenschappelijk (implementatietoelichting 2.10.2).
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
            # Gedeeld met een ander adres is gemeenschappelijk.
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Optellen en afronden


def test_punten_van_alle_buitenruimten_worden_na_het_optellen_afgerond_op_een_kwart_punt(
    buitenruimten, vergelijk_met_testreferentie
):
    """De punten van privé- en gemeenschappelijke buitenruimten worden pas na het optellen afgerond op een kwart punt.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.6; wettekst,
    Bijlage I onder B, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Het rekenvoorbeeld uit de toelichting bij de wettekst.
            ruimte(Ruimtedetailsoort.balkon, naam="Balkon1", oppervlakte=1),
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon2",
                oppervlakte=4.5,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
            ruimte(
                Ruimtedetailsoort.dakterras,
                oppervlakte=52,
                gedeeld_met_aantal_adressen=5,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Privé": {"Balkon1": 0.35, "Privé buitenruimten aanwezig": 2.0},
        # Balkon2 krijgt 0,84375 punt: in het rapport 0,84.
        "Gedeeld met 4 onzelfstandige woonruimten": {"Balkon2": 0.84},
        "Gedeeld met 5 adressen": {Ruimtedetailsoort.dakterras.naam: 1.95},
        # Het verschil tussen de 5,14 punten hierboven en het totaal.
        None: {"Afronding op kwartpunten": 0.11},
    }
    assert groep.punten == 5.25
    vergelijk_met_testreferentie(eenheid, groep)


# Maximum


def test_buitenruimten_krijgen_samen_hooguit_15_punten(
    buitenruimten, vergelijk_met_testreferentie
):
    """Buitenruimten krijgen samen hooguit 15 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8; wettekst,
    Bijlage I onder B, onderdeel 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Samen meer dan 15 punten, zodat het maximum de uitkomst begrenst.
            ruimte(
                Ruimtedetailsoort.tuin,
                oppervlakte=30,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.balkon,
                oppervlakte=15,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        # 22,5 punten gedeeld door 2 woonruimten.
        Ruimtedetailsoort.tuin.naam: 11.25,
        # Het balkon krijgt 5,625 punt en de aftrek is 1,875 punt: in het
        # rapport 5,63 en -1,88.
        Ruimtedetailsoort.balkon.naam: 5.63,
        "Maximaal 15 punten": -1.88,
    }
    assert groep.punten == 15.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_van_15_punten_geldt_voor_prive_en_gemeenschappelijke_buitenruimten_samen(
    buitenruimten, vergelijk_met_testreferentie
):
    """Privé- en gemeenschappelijke buitenruimten krijgen samen hooguit 15 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8; wettekst,
    Bijlage I onder B, onderdeel 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.balkon, oppervlakte=20),
            # Een privé- en een gemeenschappelijke buitenruimte, samen boven het maximum.
            ruimte(
                Ruimtedetailsoort.tuin,
                oppervlakte=30,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        Ruimtedetailsoort.balkon.naam: 7.0,
        "Privé buitenruimten aanwezig": 2.0,
        Ruimtedetailsoort.tuin.naam: 11.25,
        # Samen 20,25 punten, dus 5,25 punten boven het maximum.
        "Maximaal 15 punten": -5.25,
    }
    assert groep.punten == 15.0
    vergelijk_met_testreferentie(eenheid, groep)


# Geen buitenruimte


def test_woonruimte_zonder_buitenruimte_krijgt_geen_aftrek(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een onzelfstandige woonruimte zonder buitenruimte krijgt geen aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8; wettekst,
    Bijlage I onder B, onderdeel 8.
    """
    eenheid = EenhedenEenheid(ruimten=[])

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


# Onvolledige of onjuiste input


def test_buitenruimte_zonder_oppervlakte_geeft_een_waarschuwing(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte zonder oppervlakte geeft een waarschuwing over incomplete input."""
    eenheid = EenhedenEenheid(
        ruimten=[
            # Zonder oppervlakte, daarom rechtstreeks als EenhedenRuimte opgebouwd.
            EenhedenRuimte(
                id="balkon",
                naam="Balkon",
                soort=Ruimtesoort.buitenruimte,
                detail_soort=Ruimtedetailsoort.balkon,
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen oppervlakte") as waarschuwingen:
        groep = buitenruimten.waardeer(eenheid)

    # Het balkon wordt niet gewaardeerd. Het is privé, dus de woonruimte krijgt
    # ook de 2 punten voor de aanwezigheid van een privé-buitenruimte niet.
    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Als gemeenschappelijke ruimte aangeleverd, maar een balkon is een buitenruimte.
            ruimte(
                Ruimtedetailsoort.balkon,
                soort=Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = buitenruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 2 onzelfstandige woonruimten": {
            Ruimtedetailsoort.balkon.naam: 2.25
        }
    }
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
