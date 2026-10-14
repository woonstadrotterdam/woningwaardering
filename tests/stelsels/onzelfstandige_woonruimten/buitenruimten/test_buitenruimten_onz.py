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


def test_prive_buitenruimte_van_1_m2_krijgt_2_punten_plus_035_punt(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een privé-buitenruimte van 1 m² krijgt 2 punten plus 0,35 punt.

    Het balkon is de privé-buitenruimte uit het rekenvoorbeeld in de
    toelichting bij de wettekst.

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Privé buitenruimte(n)", "2
    punten + 0,35 punt per m²".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 8: "De woning van A
    beschikt over een privé-buitenruimte van 2 m x 0,5 m = 1 m². Dit resulteert
    in 2 punten + 0,35 punt x 1 m² = 2,35 punten."
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(Ruimtedetailsoort.balkon, oppervlakte=1)])

    groep = buitenruimten.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Ruimtedetailsoort.balkon.naam] == 0.35
    assert punten["Privé buitenruimten aanwezig"] == 2.0
    # Samen 2,35 punten, afgerond op kwartpunten 2,25.
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_prive_buitenruimte_onder_de_minimumafmeting_wordt_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een privé-buitenruimte met een breedte onder de minimumafmeting voor gemeenschappelijke buitenruimten wordt gewaardeerd.

    Het balkon is de privé-buitenruimte uit het rekenvoorbeeld in de
    toelichting bij de wettekst: 2 meter lang en een halve meter breed.

    Bron: beleidsboek onzelfstandige woonruimten, 2.8.1: "Voor de
    privé-buitenruimte(n) geldt géén minimumafmeting."

    Bron: beleidsboek onzelfstandige woonruimten, 2.8.2: "er moet sprake zijn
    van een minimumafmeting van 2,00 meter x 1,50 meter, 1,50 meter (hoogte,
    breedte, diepte)".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 8: "De woning van A
    beschikt over een privé-buitenruimte van 2 m x 0,5 m = 1 m². Dit resulteert
    in 2 punten + 0,35 punt x 1 m² = 2,35 punten."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Wanneer zich
    binnen de privé-buitenruimte een parkeerplek bevindt, geldt de parkeerplek
    en de weg daar naartoe als privé-buitenruimte."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
    `carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
    gewaardeerd, gemeenschappelijk in rubriek 10".

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Privé buitenruimte(n)", "2
    punten + 0,35 punt per m²".
    """
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

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
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

    Tuin1 wordt met 2 adressen gedeeld en Tuin2 met 3 adressen; tot beide
    hebben 2 onzelfstandige woonruimten op het adres toegang.

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimten gedeeld met meerdere adressen", "0,75 punt per m², gedeeld
    door het aantal adressen dat toegang en gebruiksrecht heeft, en daarna
    gedeeld door het aantal onzelfstandige woonruimten op dat adres".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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
    # Tuin1 krijgt 1,125 punt: in het rapport 1,13.
    assert punten["Gedeeld met 2 adressen"] == {"Tuin1": 1.13}
    assert punten["Gedeeld met 3 adressen"] == {"Tuin2": 0.75}
    # Samen 1,875 punt, afgerond op kwartpunten 2.
    assert groep.punten == 2.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_buitenruimte_gedeeld_met_meerdere_adressen_zonder_aantal_onzelfstandige_woonruimten_wordt_alleen_door_het_aantal_adressen_gedeeld(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte die met meerdere adressen wordt gedeeld en zonder aantal onzelfstandige woonruimten is aangeleverd, wordt alleen door het aantal adressen gedeeld.

    De package leest een ontbrekend aantal onzelfstandige woonruimten als één
    woonruimte met toegang; die lezing staat in geen bron. Tuin1 wordt met 2
    adressen gedeeld en Tuin2 met 3 adressen.

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimten gedeeld met meerdere adressen", "0,75 punt per m², gedeeld
    door het aantal adressen dat toegang en gebruiksrecht heeft, en daarna
    gedeeld door het aantal onzelfstandige woonruimten op dat adres".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
    adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
    een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
    aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
    het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
    toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
    voorziening(en)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    De package toetst de minimumafmeting alleen op de afmetingen die zijn
    ingevuld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2: "Alleen
    als een waarde is ingevuld wordt deze getoetst tegen 2000 × 1500 × 1500
    mm."

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
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

    De buitenruimte wordt met 4 onzelfstandige woonruimten op hetzelfde adres
    gedeeld.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
    minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
    diepte)."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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
    """Een gemeenschappelijke buitenruimte die in lengte en breedte onder de minimumafmeting blijft, wordt niet gewaardeerd.

    De tuin is 1 meter lang en 1 meter breed; de hoogte van 2,5 meter voldoet
    wel aan de minimumafmeting.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
    minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
    diepte)."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2: "Indien
    een van deze afmetingen kleiner is dan noodzakelijk voor waardering leidt
    dat ertoe dat de ruimte niet wordt gewaardeerd."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.tuin,
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                lengte=1000,
                breedte=1000,
                hoogte=2500,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_carport_of_parkeerplaats_wordt_niet_als_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke carport of parkeerplaats wordt niet als buitenruimte gewaardeerd.

    De carport wordt met 3 onzelfstandige woonruimten op hetzelfde adres
    gedeeld, de parkeerplaats met 2 adressen.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Gedeelde
    buitenruimte die als parkeerplek bedoeld is, wordt gewaardeerd volgens
    rubriek 10."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
    `carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
    gewaardeerd, gemeenschappelijk in rubriek 10".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Voor
    een onzelfstandige woonruimte telt daarnaast
    `Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` groter dan 1
    als gemeenschappelijk: de plek wordt dan binnen het eigen adres gedeeld."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
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

    De input is het rekenvoorbeeld uit de toelichting bij de wettekst: Balkon1
    is privé, Balkon2 wordt met 4 onzelfstandige woonruimten op hetzelfde adres
    gedeeld en het dakterras met 5 adressen en met 4 onzelfstandige
    woonruimten op het adres.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 8: "Voor huurder A
    resulteert dit in 2,35 punt + 0,84375 punt + 1,95 punt = 5,14375 punten,
    afgerond 5,25 punten."

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 8: "Het balkon wordt
    gedeeld door vier onzelfstandige woonruimten op hetzelfde adres, dus 3,375
    punt/4 = 0,84375 punt." en "Het dakterras wordt gedeeld door vijf adressen,
    dus 39 punten/5 = 7,8 punt. Op het adres van huurder A zijn vier
    onzelfstandige woonruimten, dus 7,8 punt/4 = 1,95 punt."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    De tuin en het balkon worden elk met 2 onzelfstandige woonruimten op
    hetzelfde adres gedeeld.

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Maximaal 15 punten te
    behalen".

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    De tuin wordt met 2 onzelfstandige woonruimten op hetzelfde adres gedeeld.

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Maximaal 15 punten te
    behalen".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.balkon, oppervlakte=20),
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
        "Maximaal 15 punten": -5.25,
    }
    assert groep.punten == 15.0
    vergelijk_met_testreferentie(eenheid, groep)


# Geen buitenruimte


def test_woonruimte_zonder_buitenruimte_krijgt_geen_aftrek(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een onzelfstandige woonruimte zonder buitenruimte krijgt geen aftrek.

    De test legt het huidige gedrag van de package vast. De tabel voor
    onzelfstandige woonruimten noemt in rubriek 8 geen aftrek, de tabel voor
    zelfstandige woonruimten wel. De toelichting onder A noemt de aftrek ook
    en is voor onzelfstandige woonruimten van overeenkomstige toepassing,
    tenzij ervan wordt afgeweken. De package kent de aftrek niet toe; die
    keuze staat in geen implementatietoelichting.

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Maximaal 15 punten te
    behalen", "Privé buitenruimte(n)", "Gemeenschappelijke buitenruimte(n) op
    hetzelfde adres" en "Gemeenschappelijke buitenruimten gedeeld met meerdere
    adressen".

    Bron: wettekst, Bijlage I onder A, rubriek 8: "indien in het geheel géén
    punten in deze rubriek (geen buitenruimte): af: 5 punten".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Indien de woning
    in het geheel geen privé-buitenruimte, geen gemeenschappelijke buitenruimte
    of loggia heeft, wordt een aftrek toegepast van vijf punten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "De toelichting
    behorende tot bijlage I, onder A, het waarderingsstelsel voor woonruimte
    welke een zelfstandige woning vormt, is voor onzelfstandige woonruimten van
    overeenkomstige toepassing, tenzij hiervan wordt afgeweken."
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
    """Een buitenruimte zonder oppervlakte geeft een waarschuwing over incomplete input.

    De package waardeert het balkon niet. Het balkon is privé: de woonruimte
    krijgt daardoor ook de 2 punten voor de aanwezigheid van een
    privé-buitenruimte niet. Die keuze van de package staat in geen bron.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

    De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
    ruimtesoort waarmee het balkon is gewaardeerd. Dat de package het balkon
    naar zijn detailsoort waardeert, is een keuze die in geen bron staat.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
    buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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
