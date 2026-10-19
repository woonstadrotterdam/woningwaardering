"""Gemeenschappelijke parkeerruimten, onzelfstandige woonruimten (rubriek 10)."""

import pytest

from tests.input import element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
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
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeParkeerruimten,
    )


# Type parkeerplek


def test_parkeerplek_krijgt_9_6_of_4_punten_naar_type_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek krijgt 9 punten als Type I, 6 punten als Type II en 4 punten als Type III, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft en daarna door het aantal onzelfstandige woonruimten op het adres.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.3
    - implementatietoelichting onzelfstandige woonruimten, 2.10.4
    - wettekst, Bijlage I onder B, onderdeel 10
    """
    # Vier plekken die alleen in type verschillen, met dezelfde deler.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 9 punten gedeeld door 10 adressen en door 2 onzelfstandige woonruimten is
    # 0,45; voor Type II is dat 0,3 en voor Type III 0,2.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 10 adressen": {
            "Parkeerplek in inpandige afgesloten parkeergarage (Type I)": 0.45,
            "Parkeerplek in uitpandige afgesloten parkeergarage (Type I)": 0.45,
            "Parkeerplek buiten met dak behorend bij complex (Type II)": 0.3,
            "Parkeerplek buiten behorend bij complex (Type III)": 0.2,
        },
        # Samen 1,4 punten, afgerond op kwartpunten 1,5.
        None: {"Afronding op kwartpunten": 0.1},
    }
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_carport_wordt_als_type_ii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke carport wordt als Type II gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.3
    """
    # Eén woonruimte op het adres, zodat alleen het aantal adressen deelt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Type II: 6 punten gedeeld door 3 adressen en door 1 onzelfstandige
    # woonruimte.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 3 adressen": {"Carport (Type II)": 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_parkeerplaats_wordt_als_type_iii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke parkeerplaats wordt als Type III gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.3
    """
    # Eén woonruimte op het adres, zodat alleen het aantal adressen deelt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
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


# Rekenmethode


def test_parkeerplekken_worden_elk_door_hun_eigen_aantal_adressen_en_onzelfstandige_woonruimten_gedeeld(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Parkeerplekken met een verschillend aantal adressen en onzelfstandige woonruimten worden elk door hun eigen aantallen gedeeld.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.4
    - wettekst, Bijlage I onder B, toelichting, inleiding
    """
    # Per plek een andere combinatie van adressen en onzelfstandige woonruimten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=5,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Type I: 9 punten gedeeld door 3 adressen en door 2 onzelfstandige
    # woonruimten is 1,5. Type II: 6 gedeeld door 4 en door 3 is 0,5.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 3 adressen": {
            "Parkeerplek in inpandige afgesloten parkeergarage (Type I)": 1.5
        },
        "Gedeeld met 4 adressen": {"Carport (Type II)": 0.5},
        # 4 punten gedeeld door 5 adressen en door 3 woonruimten is 0,266… punt:
        # in het rapport 0,27.
        "Gedeeld met 5 adressen": {
            "Parkeerplek buiten behorend bij complex (Type III)": 0.27
        },
        # Samen 2,266… punten, afgerond op kwartpunten 2,25.
        None: {"Afronding op kwartpunten": -0.02},
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_punten_van_meerdere_parkeerplekken_worden_opgeteld_en_gedeeld_door_de_adressen_en_de_onzelfstandige_woonruimten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """De punten van meerdere parkeerplekken worden opgeteld, gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.4
    - wettekst, Bijlage I onder B, toelichting rubriek 10
    """
    # De vijf Type III-parkeerplekken zijn één ruimte met `aantal` 5.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                aantal=5,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Parkeerplek buiten behorend bij complex (Type III)": 5.0
    }
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 10 adressen": {
            "Parkeerplek buiten behorend bij complex (Type III)": 0.5
        }
    }
    assert groep.punten == 0.5
    vergelijk_met_testreferentie(eenheid, groep)


# Laadpaal


def test_laadpaal_bij_parkeerplek_krijgt_2_punten_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek krijgt 2 punten extra, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.5
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Eén woonruimte op het adres, zodat alleen het aantal adressen deelt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.5
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Twee plekken met dezelfde deler: elke plek krijgt een eigen laadpaal.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                naam="Carport1",
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            ),
            ruimte(
                Ruimtedetailsoort.carport,
                naam="Carport2",
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
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


# Parkeerruimte gedeeld binnen het eigen adres


def test_carport_gedeeld_met_onzelfstandige_woonruimten_op_hetzelfde_adres_wordt_als_type_ii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, wordt in deze rubriek als Type II gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.2
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)

    De punten van een parkeerplek worden na de verdeling over de adressen
    gedeeld door het aantal onzelfstandige woonruimten op het adres.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.4
    - wettekst, Bijlage I onder B, toelichting rubriek 10
    """
    # Alleen binnen het eigen adres gedeeld, met meerdere woonruimten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=1,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Type II: 6 punten gedeeld door 1 adres en door 2 onzelfstandige
    # woonruimten.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 2 onzelfstandige woonruimten": {"Carport (Type II)": 3.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_laadpaal_bij_parkeerplek_op_hetzelfde_adres_krijgt_2_punten_gedeeld_door_het_aantal_onzelfstandige_woonruimten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, krijgt 2 punten extra, gedeeld door het aantal onzelfstandige woonruimten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.12.3
    - implementatietoelichting onzelfstandige woonruimten, 2.10.5
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    - wettekst, Bijlage I onder B, toelichting rubriek 10
    """
    # Alleen binnen het eigen adres gedeeld, zodat de woonruimten de deler zijn.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=12,
                gedeeld_met_aantal_adressen=1,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 2 punten gedeeld door 1 adres en door 2 onzelfstandige woonruimten.
    assert punten_per_naam(groep)["Laadpaal"] == 1.0
    # Met de 3 punten van de carport samen 4 punten.
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


# Privé-parkeerruimte


def test_prive_carport_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een privé-carport krijgt in deze rubriek geen punten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.8.3
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Eén adres en geen woonruimten om mee te delen: niet gemeenschappelijk.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.3
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Onder de minimale 12 m², verder een gewone gemeenschappelijke plek.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=11.99,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.5
    - implementatietoelichting onzelfstandige woonruimten, 2.10.3
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # De carport is te klein voor een parkeerplek en krijgt zelf geen punten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=11.99,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.3
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Parkeerplaats (geen Type-detailsoort) onder de minimale 12 m².
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                oppervlakte=11.99,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    with pytest.warns(UserWarning, match="Gebruik Type I, II of III") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_parkeerplek_zonder_aantal_adressen_wordt_als_prive_parkeerplek_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek zonder aantal adressen wordt gewaardeerd als een privé-parkeerplek van één adres.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.2
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Zonder gedeeld_met_aantal_adressen, zodat de package van één adres uitgaat.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
            )
        ]
    )

    with pytest.warns(
        UserWarning, match="geen 'gedeeld_met_aantal_adressen'"
    ) as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # Type III: 4 punten gedeeld door 1 adres.
    assert punten_per_bovenliggende(groep) == {
        "Privé": {"Parkeerplek buiten behorend bij complex (Type III)": 4.0}
    }
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_carport_zonder_aantal_adressen_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.10.2
    - implementatietoelichting onzelfstandige woonruimten, 2.8.3
    """
    # Zonder aantallen voor de deling is de carport niet gedeeld.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
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


def test_open_parkeergarage_niet_specifieke_plek_geeft_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een ruimte met de detailsoort open parkeergarage, niet specifieke plek, geeft een waarschuwing dat een andere detailsoort nodig is.

    Bron:
    - implementatietoelichting datamodel-uitbreidingen, "Parkeergelegenheden"
    """
    # Groot genoeg (100 m²) en gedeeld, zodat alleen de detailsoort de reden is.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.open_parkeergarage_niet_specifieke_plek,
                oppervlakte=100,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    with pytest.warns(
        UserWarning, match="heeft als ruimtedetailsoort"
    ) as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # De package waardeert de ruimte niet.
    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
