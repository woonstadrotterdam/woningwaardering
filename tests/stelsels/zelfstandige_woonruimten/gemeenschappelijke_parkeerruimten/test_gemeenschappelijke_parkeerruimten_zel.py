"""Gemeenschappelijke parkeerruimten, zelfstandige woonruimten (rubriek 10)."""

import pytest

from tests.input import element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def gemeenschappelijke_parkeerruimten(peildatum):
    return GemeenschappelijkeParkeerruimten(peildatum=peildatum)


def test_GemeenschappelijkeParkeerruimten_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeParkeerruimten,
    )


# Type parkeerplek


def test_parkeerplek_krijgt_9_6_of_4_punten_naar_type_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek krijgt 9 punten als Type I, 6 punten als Type II en 4 punten als Type III, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
    Bijlage I onder A, onderdeel 10.
    """
    # Vier plekken die alleen in type verschillen, met dezelfde deler.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 9 punten gedeeld door 10 adressen is 0,9; voor Type II is dat 0,6 en voor
    # Type III 0,4.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 10 adressen": {
            "Parkeerplek in inpandige afgesloten parkeergarage (Type I)": 0.9,
            "Parkeerplek in uitpandige afgesloten parkeergarage (Type I)": 0.9,
            "Parkeerplek buiten met dak behorend bij complex (Type II)": 0.6,
            "Parkeerplek buiten behorend bij complex (Type III)": 0.4,
        },
        # Samen 2,8 punten, afgerond op kwartpunten 2,75.
        None: {"Afronding op kwartpunten": -0.05},
    }
    assert groep.punten == 2.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_carport_wordt_als_type_ii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke carport wordt als Type II gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
    Bijlage I onder A, onderdeel 10.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Type II: 6 punten gedeeld door 3 adressen.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 3 adressen": {"Carport (Type II)": 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_parkeerplaats_wordt_als_type_iii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke parkeerplaats wordt als Type III gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
    Bijlage I onder A, onderdeel 10.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    with pytest.warns(UserWarning, match="Gebruik Type I, II of III") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 4 punten gedeeld door 3 adressen is 1,333… punt: in het rapport 1,33 en
    # afgerond op kwartpunten 1,25.
    assert punten_per_bovenliggende(groep)["Gedeeld met 3 adressen"] == {
        "Parkeerplaats (Type III)": 1.33
    }
    assert groep.punten == 1.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Laadpaal


def test_laadpaal_bij_parkeerplek_krijgt_2_punten_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek krijgt 2 punten extra, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.5; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 2 punten gedeeld door 3 adressen is 0,666… punt: in het rapport 0,67.
    assert punten_per_naam(groep)["Laadpaal"] == 0.67
    # Met de 2 punten van de carport (Type II: 6 punten gedeeld door 3 adressen)
    # samen 2,67 punten, afgerond op kwartpunten 2,75.
    assert groep.punten == 2.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_elke_parkeerplek_met_laadpaal_krijgt_eigen_punten_voor_de_laadpaal(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Elke parkeerplek met laadpaal krijgt 2 punten extra, ook als de plekken met dezelfde adressen worden gedeeld.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.5; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                naam="Carport1",
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=4,
            ),
            ruimte(
                Ruimtedetailsoort.carport,
                naam="Carport2",
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=4,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Beide laadpalen staan onder "Gedeeld met 4 adressen" en heten "Laadpaal";
    # vergelijk_met_testreferentie controleert dat hun criterium-id's
    # verschillen. 2 punten gedeeld door 4 adressen is 0,5 punt per laadpaal.
    laadpalen = [
        waardering.punten
        for waardering in groep.woningwaarderingen or []
        if waardering.criterium and waardering.criterium.naam == "Laadpaal"
    ]
    assert laadpalen == [0.5, 0.5]
    # Twee carports van 6 punten en twee laadpalen van 2 punten, gedeeld door 4
    # adressen.
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


# Rekenmethode


def test_punten_van_parkeerplekken_en_laadpalen_worden_gedeeld_door_het_aantal_adressen_en_afgerond_op_een_kwart_punt(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """De punten van parkeerplekken en laadpalen worden opgeteld, gedeeld door het aantal adressen en afgerond op een kwart punt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    # De vijf Type II-plekken zijn één carport met `aantal` 5 en één laadpaal; de
    # twee Type III-plekken zijn één ruimte met `aantal` 2.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                aantal=5,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                aantal=2,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Carport (Type II)": 5.0,
        "Laadpaal": 5.0,
        "Parkeerplek buiten behorend bij complex (Type III)": 2.0,
    }
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 10 adressen": {
            "Carport (Type II)": 3.0,
            "Laadpaal": 1.0,
            "Parkeerplek buiten behorend bij complex (Type III)": 0.8,
        },
        # Samen 4,8 punten, afgerond op kwartpunten 4,75.
        None: {"Afronding op kwartpunten": -0.05},
    }
    assert groep.punten == 4.75
    vergelijk_met_testreferentie(eenheid, groep)


# Parkeerruimte van één adres


def test_carport_met_laadpaal_van_een_adres_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport met laadpaal van één adres krijgt in deze rubriek geen punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.2; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    # Carport van één adres: niet gemeenschappelijk.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=12,
                gedeeld_met_aantal_adressen=1,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # De carport is een privé-buitenruimte en wordt in rubriek 8 gewaardeerd.
    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Minimale oppervlakte


def test_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek met een oppervlakte onder 12 m² krijgt geen punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    # Onder de minimale 12 m², verder een gewone gemeenschappelijke plek.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=11,
                gedeeld_met_aantal_adressen=10,
                aantal=2,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_laadpaal_bij_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek met een oppervlakte onder 12 m² krijgt in deze rubriek geen punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    # De carport is te klein voor een parkeerplek en krijgt zelf geen punten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=10,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Onvolledige of onjuiste input


def test_gemeenschappelijke_parkeerplaats_kleiner_dan_12_m2_geeft_ook_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke parkeerplaats geeft de waarschuwing over haar detailsoort ook wanneer zij met een oppervlakte onder 12 m² geen punten krijgt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    # Parkeerplaats (geen Type-detailsoort) onder de minimale 12 m².
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=10,
                gedeeld_met_aantal_adressen=3,
            )
        ]
    )

    with pytest.warns(UserWarning, match="Gebruik Type I, II of III") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_parkeerplek_zonder_aantal_adressen_wordt_als_parkeerplek_van_een_adres_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek zonder aantal adressen wordt gewaardeerd als een parkeerplek van één adres.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    # Zonder aantal adressen; twee plekken (`aantal` 2) tonen het optellen.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                aantal=2,
            )
        ]
    )

    with pytest.warns(
        UserWarning, match="geen 'gedeeld_met_aantal_adressen'"
    ) as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 2 plekken van 4 punten, gedeeld door 1 adres.
    assert punten_per_bovenliggende(groep) == {
        "Privé": {"Parkeerplek buiten behorend bij complex (Type III)": 8.0}
    }
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_carport_zonder_aantal_adressen_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4;
    implementatietoelichting zelfstandige woonruimten, 2.8.3.
    """
    # Zonder aantal adressen is de carport niet gedeeld.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=12,
                aantal=5,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # De carport is een privé-buitenruimte en wordt in rubriek 8 gewaardeerd.
    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_parkeerplek_zonder_oppervlakte_geeft_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek zonder oppervlakte geeft een waarschuwing over incomplete input."""
    # Zonder oppervlakte is niet vast te stellen of de plek de minimale 12 m² haalt.
    eenheid = EenhedenEenheid(
        ruimten=[
            EenhedenRuimte(
                id="parkeerplek",
                naam="Parkeerplek",
                soort=Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
                detail_soort=Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                gedeeld_met_aantal_adressen=10,
                aantal=2,
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen oppervlakte") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Zonder oppervlakte waardeert de package de parkeerplek niet.
    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
