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

    Bron: wettekst, Bijlage I onder A, rubriek 10: "Type I Parkeerplek in
    afgesloten parkeergarage behorende tot het complex 9 punten gedeeld door het
    aantal adressen dat toegang en gebruiksrecht heeft.", "Type II Parkeerplek
    buiten behorende tot het complex met dak 6 punten gedeeld door het aantal
    adressen dat toegang en gebruiksrecht heeft." en "Type III Parkeerplek
    buiten behorende tot het complex zonder dak 4 punten gedeeld door het aantal
    adressen dat toegang en gebruiksrecht heeft."

    Welke ruimtedetailsoort bij welk type hoort, staat in de
    implementatietoelichting. Een parkeerplek in een uitpandige afgesloten
    parkeergarage is net als een inpandige Type I.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Type I:
    `Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage`
    (`PIP`) en
    `Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage`
    (`PUP`). Bepalend is de afgesloten parkeergarage, niet of die in- of
    uitpandig is: de wettekst maakt dat onderscheid niet.", "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex`
    (`PBD`)" en "Type III:
    `Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`)".
    """
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

    Bron: beleidsboek zelfstandige woonruimten, 2.10.3: "Type II: een
    parkeerplek buiten behorende tot het complex of de woning met dak
    (hieronder telt een carpoort)".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
    en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

    Bron: wettekst, Bijlage I onder A, rubriek 10: "Type II Parkeerplek buiten
    behorende tot het complex met dak 6 punten gedeeld door het aantal adressen
    dat toegang en gebruiksrecht heeft."
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

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 3 adressen": {"Carport (Type II)": 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_parkeerplaats_wordt_als_type_iii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke parkeerplaats wordt als Type III gewaardeerd.

    De package waarschuwt dat bij een gemeenschappelijke parkeerplek een
    Type-detailsoort hoort.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Type III:
    `Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`) en,
    wanneer die gemeenschappelijk is, `Ruimtedetailsoort.parkeerplaats` (`PAR`).
    Bij die laatste volgt een `UserWarning` dat een Type-detailsoort meer op
    zijn plaats is: `PAR` legt het type niet vast."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder A, rubriek 10: "Type III Parkeerplek buiten
    behorende tot het complex zonder dak 4 punten gedeeld door het aantal
    adressen dat toegang en gebruiksrecht heeft."
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Indien er sprake
    is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee
    punten extra per parkeerplek met laadpaal." en "Daarna wordt dit
    puntentotaal gedeeld door het aantal adressen dat gebruik kan maken van de
    parkeerplek(ken)."

    Bron: beleidsboek zelfstandige woonruimten, 2.10.5: "Als de parkeerplek
    beschikt over een laadpaal voor elektrisch rijden, die exclusief is voor
    gebruik door bewoners, dan worden 2 extra punten toegekend, gedeeld door het
    aantal adressen dat toegang en gebruiksrecht heeft."
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
    # Met de 2 punten van de carport samen 2,67 punten, afgerond op kwartpunten
    # 2,75.
    assert groep.punten == 2.75
    vergelijk_met_testreferentie(eenheid, groep)


# Rekenmethode


def test_rekenvoorbeeld_met_meerdere_parkeerplekken_uit_de_wettekst(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Het rekenvoorbeeld uit de wettekst: tien adressen die vijf Type II-parkeerplekken met laadpaal en twee Type III-parkeerplekken delen, krijgen elk 4,75 punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Tien adressen
    delen vijf type II-parkeerplekken met laadpaal en twee type
    III-parkeerplekken zonder laadpaal.", "Vijf parkeerplekken type II (zes
    punten) + elke een laadpaal (twee punten) en twee parkeerplekken type III
    (vier punten) = 5 x (6+2)+ 2 x 4 = 48 punten.", "48 / 10 adressen = 4,8
    punten per adres." en "Afronden geschiedt op een kwart punt per adres op
    4,75 punten."

    De vijf Type II-parkeerplekken zijn een gemeenschappelijke carport met
    `aantal` 5 en één laadpaal. De package telt die laadpaal voor elke
    parkeerplek van de ruimte.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4: "Hierdoor
    is het mogelijk om aan te geven tot hoeveel van elk parkeerplektype de
    eenheid toegang heeft zonder dat elk parkeervak van een parkeergarage of
    parkeerterrein meegegeven dient te worden. Wanneer een laadpaal als
    bouwkundig element wordt meegegeven, wordt deze bij de ruimte meegeteld voor
    de berekening van de punten, waarbij het aantal wordt bepaald door
    `Eenhedenruimte.aantal`."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
    en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."
    """
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

    De carport is een privé-buitenruimte en hoort in rubriek 8.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
    parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
    exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
    rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
    rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
    woning)."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.3: "Een
    `carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
    gewaardeerd, gemeenschappelijk in rubriek 10".

    De laadpaal volgt de carport en hoort dan in rubriek 12.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3: "Krijgt die
    ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in alle
    andere gevallen hier, met dezelfde deler (aantal adressen)."
    """
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

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Minimale oppervlakte


def test_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek met een oppervlakte onder 12 m² krijgt geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."
    """
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

    De gemeenschappelijke carport van 10 m² krijgt zelf geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."

    De laadpaal volgt de carport en hoort dan in rubriek 12.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3: "Krijgt die
    ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in alle
    andere gevallen hier, met dezelfde deler (aantal adressen)."
    """
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

    Dat de waarschuwing ook onder 12 m² volgt, is een keuze van de package die
    in geen bron staat.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.3: "Bij die
    laatste volgt een `UserWarning` dat een Type-detailsoort meer op zijn plaats
    is: `PAR` legt het type niet vast."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."
    """
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

    De package waarschuwt dat `gedeeld_met_aantal_adressen` ontbreekt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4: "Dit
    attribuut dient ook op elk type parkeerplek meegegeven te worden. Ontbreekt
    het, dan volgt een `UserWarning` en gaan we uit van niet gedeeld met andere
    adressen."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    De twee parkeerplekken van Type III worden ook voor één adres in deze
    rubriek gewaardeerd: hun punten worden opgeteld en door 1 gedeeld.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.2:
    "waarderen we altijd in deze rubriek, ook wanneer de plek aan één adres is
    toegewezen."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Bij meerdere
    parkeerplekken worden de punten bij elkaar opgeteld." en "Indien sprake is
    van een privé parkeerplek voor één adres, wordt gedeeld door 1."

    Bron: wettekst, Bijlage I onder A, rubriek 10: "Type III Parkeerplek buiten
    behorende tot het complex zonder dak 4 punten".
    """
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

    assert punten_per_bovenliggende(groep) == {
        "Privé": {"Parkeerplek buiten behorend bij complex (Type III)": 8.0}
    }
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_carport_zonder_aantal_adressen_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

    De package leest het ontbrekende aantal als niet gedeeld met andere
    adressen. De carport is dan een privé-buitenruimte en hoort in rubriek 8.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.8.3: "Een
    `carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
    gewaardeerd, gemeenschappelijk in rubriek 10".

    De implementatietoelichting zegt dat bij een ontbrekend aantal adressen een
    waarschuwing volgt. Bij een carport geeft de package die in deze rubriek
    niet; de test legt het huidige gedrag vast.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4: "Dit
    attribuut dient ook op elk type parkeerplek meegegeven te worden. Ontbreekt
    het, dan volgt een `UserWarning` en gaan we uit van niet gedeeld met andere
    adressen."
    """
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

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_parkeerplek_zonder_oppervlakte_geeft_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek zonder oppervlakte is incomplete input en wordt niet gewaardeerd.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Zonder oppervlakte is niet vast te stellen of de parkeerplek de minimale
    oppervlakte heeft.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."
    """
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

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
