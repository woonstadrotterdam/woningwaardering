"""Buitenruimten, zelfstandige woonruimten (rubriek 8)."""

import pytest

from tests.input import ruimte
from tests.utils import assert_stelselgroep_output, punten_per_naam
from woningwaardering.stelsels.zelfstandige_woonruimten import Buitenruimten
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort


@pytest.fixture()
def buitenruimten(peildatum):
    return Buitenruimten(peildatum=peildatum)


def test_Buitenruimten_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Buitenruimten,
    )


# Privé-buitenruimten


def test_prive_buitenruimte_krijgt_2_punten_plus_035_punt_per_m2(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een privé-buitenruimte krijgt 2 punten plus 0,35 punt per m².

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Voor
    privébuitenruimten worden in ieder geval twee punten toegekend, en daarna
    per vierkante meter 0,35 punt."
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(Ruimtedetailsoort.tuin, oppervlakte=30)])

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Privé": 10.5,
        "Privé buitenruimten aanwezig": 2.0,
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Gemeenschappelijke buitenruimten


def test_gemeenschappelijke_buitenruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen dat toegang heeft.

    De input is het rekenvoorbeeld uit de wettekst.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
    meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
    het aantal adressen dat toegang heeft tot de buitenruimte." en "Voorbeeld:
    een woongebouw met een gemeenschappelijk dakterras van 30 m² waartoe drie
    adressen toegang hebben, wordt gewaardeerd met: (0,75 x 30) / 3 = 7,5
    punten."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.dakterras,
                oppervlakte=30,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Gedeeld met 3 adressen": 7.5}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_buitenruimten_worden_elk_door_hun_eigen_aantal_adressen_gedeeld(
    buitenruimten, vergelijk_met_testreferentie
):
    """Van gemeenschappelijke buitenruimten met een verschillend aantal adressen worden de punten per buitenruimte door haar eigen aantal adressen gedeeld.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
    meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
    het aantal adressen dat toegang heeft tot de buitenruimte."
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

    assert punten_per_naam(groep) == {
        "Gedeeld met 2 adressen": 2.25,
        "Gedeeld met 3 adressen": 1.5,
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_buitenruimte_zonder_afmetingen_wordt_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte zonder lengte, breedte en hoogte wordt gewaardeerd.

    De package toetst de minimumafmeting alleen op de afmetingen die zijn
    ingevuld.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2: "Alleen als
    een waarde is ingevuld wordt deze getoetst tegen 2000 × 1500 × 1500 mm."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
    meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
    het aantal adressen dat toegang heeft tot de buitenruimte."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.dakterras,
                oppervlakte=20,
                gedeeld_met_aantal_adressen=2,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Gedeeld met 2 adressen": 7.5}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_buitenruimte_boven_de_minimumafmeting_wordt_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte met een lengte en breedte boven de minimumafmeting wordt gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
    minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
    diepte)."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
    meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
    het aantal adressen dat toegang heeft tot de buitenruimte."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.tuin,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
                lengte_mm=10000,
                breedte_mm=2000,
            )
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Gedeeld met 2 adressen": 2.25}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_buitenruimte_onder_de_minimumafmeting_wordt_niet_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke buitenruimte die in lengte, breedte of hoogte onder de minimumafmeting blijft, wordt niet gewaardeerd.

    Geen van de drie balkons wordt gewaardeerd. De woning heeft daardoor geen
    gewaardeerde buitenruimte en krijgt de aftrek van 5 punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
    minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
    diepte)."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2: "Indien een
    van deze afmetingen kleiner is dan noodzakelijk voor waardering leidt dat
    ertoe dat de ruimte niet wordt gewaardeerd."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5: "Daarom
    passen we −5 alleen toe als er geen enkele gewaardeerde buitenruimte is
    (bijv. te kleine gedeelde ruimten of privé zonder oppervlakte leveren geen
    punten en tellen dus niet mee tegen de aftrek)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon1",
                oppervlakte=3.14196,
                gedeeld_met_aantal_adressen=2,
                lengte_mm=1150,
                breedte_mm=2800,
                hoogte_mm=3170,
            ),
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon2",
                oppervlakte=3.14196,
                gedeeld_met_aantal_adressen=2,
                lengte_mm=2800,
                breedte_mm=1150,
                hoogte_mm=3170,
            ),
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon3",
                oppervlakte=3.14196,
                gedeeld_met_aantal_adressen=2,
                lengte_mm=3170,
                breedte_mm=2800,
                hoogte_mm=1150,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Geen buitenruimten": -5.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Maximum


def test_buitenruimten_krijgen_samen_hooguit_15_punten(
    buitenruimten, vergelijk_met_testreferentie
):
    """Buitenruimten krijgen samen hooguit 15 punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Voor de rubriek
    buitenruimten (rubriek 8) kan in totaal maximaal vijftien punten worden
    toegekend."

    De punten vóór het maximum volgen uit de opgetelde oppervlakte van de tuin
    en het balkon.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Indien sprake is
    van meerdere buitenruimten die allen tot dezelfde categorie behoren, zijnde
    allen gemeenschappelijk of privé, dan worden de oppervlaktes van die
    buitenruimtes bij elkaar opgeteld." en "Voor privébuitenruimten worden in
    ieder geval twee punten toegekend, en daarna per vierkante meter 0,35
    punt."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.tuin, oppervlakte=30),
            ruimte(Ruimtedetailsoort.balkon, oppervlakte=15),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Privé": 15.75,
        "Privé buitenruimten aanwezig": 2.0,
        "Maximaal 15 punten": -2.75,
    }
    assert groep.punten == 15.0
    vergelijk_met_testreferentie(eenheid, groep)


# Geen buitenruimte


def test_woning_zonder_buitenruimte_krijgt_5_punten_aftrek(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een woning zonder buitenruimte krijgt 5 punten aftrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Indien de woning
    in het geheel geen privé-buitenruimte, geen gemeenschappelijke buitenruimte
    of loggia heeft, wordt een aftrek toegepast van vijf punten."
    """
    eenheid = EenhedenEenheid(ruimten=[])

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Geen buitenruimten": -5.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Onvolledige of onjuiste input


def test_buitenruimte_zonder_oppervlakte_geeft_een_waarschuwing(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte zonder oppervlakte is incomplete input en wordt niet gewaardeerd.

    De woning heeft daardoor geen gewaardeerde buitenruimte en krijgt de aftrek
    van 5 punten.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5: "Daarom
    passen we −5 alleen toe als er geen enkele gewaardeerde buitenruimte is
    (bijv. te kleine gedeelde ruimten of privé zonder oppervlakte leveren geen
    punten en tellen dus niet mee tegen de aftrek)."
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

    assert punten_per_naam(groep) == {"Geen buitenruimten": -5.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

    De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
    ruimtesoort waarmee het dakterras is gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Voorbeeld: een
    woongebouw met een gemeenschappelijk dakterras van 30 m² waartoe drie
    adressen toegang hebben, wordt gewaardeerd met: (0,75 x 30) / 3 = 7,5
    punten."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.dakterras,
                soort=Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
                oppervlakte=30,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Gedeeld met 3 adressen": 7.5}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
