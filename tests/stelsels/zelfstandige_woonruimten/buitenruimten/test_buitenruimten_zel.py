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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.1; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Het rekenvoorbeeld uit de toelichting bij de wettekst.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.tuin,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
                lengte=10000,
                breedte=2000,
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2; wettekst,
    Bijlage I onder A, toelichting rubriek 8.

    Een woning zonder gewaardeerde buitenruimte krijgt 5 punten aftrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Elk balkon blijft op één afmeting onder de minimumafmeting:
            # Balkon1 in lengte, Balkon2 in breedte en Balkon3 in hoogte.
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon1",
                oppervlakte=3.14196,
                gedeeld_met_aantal_adressen=2,
                lengte=1150,
                breedte=2800,
                hoogte=3170,
            ),
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon2",
                oppervlakte=3.14196,
                gedeeld_met_aantal_adressen=2,
                lengte=2800,
                breedte=1150,
                hoogte=3170,
            ),
            ruimte(
                Ruimtedetailsoort.balkon,
                naam="Balkon3",
                oppervlakte=3.14196,
                gedeeld_met_aantal_adressen=2,
                lengte=3170,
                breedte=2800,
                hoogte=1150,
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Twee privé-buitenruimten die samen boven het maximum uitkomen.
            ruimte(Ruimtedetailsoort.tuin, oppervlakte=30),
            ruimte(Ruimtedetailsoort.balkon, oppervlakte=15),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    # Samen 45 m²: 45 x 0,35 = 15,75 punten plus 2 punten is 17,75; maximaal 15.
    assert punten_per_naam(groep) == {
        "Privé": 15.75,
        "Privé buitenruimten aanwezig": 2.0,
        "Maximaal 15 punten": -2.75,
    }
    assert groep.punten == 15.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_van_15_punten_geldt_voor_prive_en_gemeenschappelijke_buitenruimten_samen(
    buitenruimten, vergelijk_met_testreferentie
):
    """Privé- en gemeenschappelijke buitenruimten krijgen samen hooguit 15 punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.tuin, oppervlakte=30),
            ruimte(
                Ruimtedetailsoort.dakterras,
                oppervlakte=30,
                gedeeld_met_aantal_adressen=3,
            ),
        ]
    )

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Privé": 10.5,
        "Privé buitenruimten aanwezig": 2.0,
        "Gedeeld met 3 adressen": 7.5,
        "Maximaal 15 punten": -5.0,
    }
    assert groep.punten == 15.0
    vergelijk_met_testreferentie(eenheid, groep)


# Geen buitenruimte


def test_woning_zonder_buitenruimte_krijgt_5_punten_aftrek(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een woning zonder buitenruimte krijgt 5 punten aftrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
    eenheid = EenhedenEenheid(ruimten=[])

    groep = buitenruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Geen buitenruimten": -5.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Onvolledige of onjuiste input


def test_buitenruimte_zonder_oppervlakte_geeft_een_waarschuwing(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte zonder oppervlakte geeft een waarschuwing over incomplete input.

    Een woning zonder gewaardeerde buitenruimte krijgt 5 punten aftrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5; wettekst,
    Bijlage I onder A, toelichting rubriek 8.
    """
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

    assert punten_per_naam(groep) == {"Geen buitenruimten": -5.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd(
    buitenruimten, vergelijk_met_testreferentie
):
    """Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Als gemeenschappelijke ruimte aangeleverd, maar een dakterras is een
            # buitenruimte.
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
