"""Bijzondere voorzieningen, onzelfstandige woonruimten (rubriek 12)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.input import elementen, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    BijzondereVoorzieningen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Eenheidmonument,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def bijzondere_voorzieningen(peildatum):
    return BijzondereVoorzieningen(peildatum=peildatum)


@pytest.fixture()
def vervanger_voor_package_monumenten(monkeypatch):
    """Vervang de optionele package `monumenten` door een lege vervanger.

    Is `monumenten` op de eenheid niet opgegeven, dan zoekt de package de
    monumentstatus op met de package `monumenten`. Die is optioneel; zonder haar
    geeft de waardering een extra waarschuwing. Met deze vervanger verloopt de
    waardering in elke omgeving hetzelfde: zonder BAG-identificatie wordt
    `MonumentenClient` niet aangeroepen.
    """
    monkeypatch.setitem(
        sys.modules, "monumenten", SimpleNamespace(MonumentenClient=None)
    )


def test_BijzondereVoorzieningenZorgwoning_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        BijzondereVoorzieningen,
    )


# Zorgwoning


def test_zorgwoning_met_113_punten_in_de_rubrieken_1_tot_en_met_11_krijgt_39_5_punten_verhoging(
    bijzondere_voorzieningen,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een zorgwoning met 113 punten in de rubrieken 1 tot en met 11 krijgt 35% daarvan als verhoging: op een kwart punt afgerond 39,5 punten.

    Bron: wettekst, Bijlage I onder B, rubriek 12: "Uitsluitend bij
    zorgwoningen" en "bij: 35% van de ingevolge de onderdelen 1 tot en met 11
    toegekende punten."

    De verhoging is het totaal van deze rubriek en wordt op een kwart punt
    afgerond.

    Bron: beleidsboek onzelfstandige woonruimten, 2.1.6: "Het totaal aantal
    punten wordt per rubriek afgerond op 0,25 punt, waarbij vanaf een achtste
    (1/8) punt naar boven wordt afgerond."

    De package leest aan de doelgroep af dat de eenheid een zorgwoning is. De
    implementatietoelichting voor onzelfstandige woonruimten noemt dat niet;
    die voor zelfstandige woonruimten wel.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.1: "Wanneer
    een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als
    zorgwoning gewaardeerd."

    De eenheid heeft alleen de doelgroep zorg en een verwarmde woonkamer. De
    test geeft geen eerder resultaat mee; de package waardeert de andere
    rubrieken daarom zelf en waarschuwt voor de monumenten, de energieprestatie
    en de WOZ-waarde die ontbreken. Dat de gegevens voor de andere rubrieken
    daarvoor in het model moeten staan, zegt alleen de implementatietoelichting
    voor zelfstandige woonruimten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12: "De extra
    attributen in het model (zoals de WOZ-waarde, energielabel,
    ruimtegegevens, etc.) zijn van belang omdat de 35% opslag voor zorgwoningen
    wordt berekend over het totale puntenaantal van de rubrieken 1 t/m 11."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        doelgroep=Doelgroep.zorg,
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=98,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = bijzondere_voorzieningen.waardeer(eenheid.model_copy())

    # De rubrieken 1 tot en met 11 geven samen 113 punten: 98 voor de
    # woonkamer van 98 m² (rubriek 1), 2 voor het verwarmde vertrek (rubriek
    # 3), 3 voor de gemeenschappelijke ruimten van een zorgwoning (rubriek 9)
    # en 10 omdat een WOZ-waarde ontbreekt (rubriek 11). Zonder energielabel en
    # zonder bouwjaar geeft rubriek 4 geen punten. 35% van 113 punten is 39,55
    # punten; op een kwart punt afgerond is dat 39,5.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 39.5}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_10_punten_voor_een_rijksmonument_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """De 10 punten voor een rijksmonument met een huurovereenkomst van 1 januari 2024 tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    De 10 punten komen op grond van artikel 8a bij de waardering. De verhoging
    voor een zorgwoning is een percentage van de punten van de onderdelen 1 tot
    en met 11.

    Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
    of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
    Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
    voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
    waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
    punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
    bijlage I, onder B, met 10 punten vermeerderd."

    Bron: wettekst, Bijlage I onder B, rubriek 12: "bij: 35% van de ingevolge
    de onderdelen 1 tot en met 11 toegekende punten."

    De eenheid heeft bouwjaar 1960 en geen energielabel. Bij dat bouwjaar geeft
    rubriek 4 minpunten, maar niet aan een rijksmonument: de rubriek draagt 0
    punten bij aan de punten waarover de verhoging wordt berekend.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.2: "Indien de woonruimte
    bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal
    monument of een gemeentelijke monument als bedoeld in artikel 8a worden
    voor deze rubriek geen minpunten toegekend."

    De eenheid heeft verder de doelgroep zorg, de datum van de
    huurovereenkomst en een verwarmde woonkamer. De test geeft geen eerder
    resultaat mee; de package waardeert de andere rubrieken daarom zelf en
    waarschuwt voor de energieprestatie en de WOZ-waarde die ontbreken. Dat de
    verhoging van de gegevens voor de andere rubrieken afhangt, staat alleen in
    de implementatietoelichting voor zelfstandige woonruimten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12: "De extra
    attributen in het model (zoals de WOZ-waarde, energielabel,
    ruimtegegevens, etc.) zijn van belang omdat de 35% opslag voor zorgwoningen
    wordt berekend over het totale puntenaantal van de rubrieken 1 t/m 11."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        datum_afsluiten_huurovereenkomst=date(2024, 1, 1),
        bouwjaar=1960,
        doelgroep=Doelgroep.zorg,
        monumenten=[Eenheidmonument.rijksmonument],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=98,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = bijzondere_voorzieningen.waardeer(eenheid)

    # De rubrieken 1 tot en met 11 geven samen 113 punten: 98 voor de
    # woonkamer van 98 m² (rubriek 1), 2 voor het verwarmde vertrek (rubriek
    # 3), 0 voor de energieprestatie van het rijksmonument (rubriek 4), 3 voor
    # de gemeenschappelijke ruimten van een zorgwoning (rubriek 9) en 10 omdat
    # een WOZ-waarde ontbreekt (rubriek 11). 35% van 113 punten is 39,55
    # punten; op een kwart punt afgerond is dat 39,5. Met de 10 punten van het
    # rijksmonument erbij was het 35% van 123 punten geweest: 43,05 punten,
    # afgerond 43.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 39.5}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Aanbelfunctie


def test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

    Bron: wettekst, Bijlage I onder B, rubriek 12: "Aanbelfunctie met video- en
    audioverbinding waarbij de voordeur automatisch kan worden geopend vanuit
    de woning" en "0,25 punt".

    De aanbelfunctie is een installatie van een ruimte, hier de woonkamer.

    Bron: implementatietoelichting, datamodel-uitbreidingen, "Installaties":
    "Op dit moment gebruiken wij `installaties` als attribuut op ruimte met als
    type `Optional[list[Installatiesoort]]`."

    Of de voordeur vanuit de woonruimte kan worden geopend, controleert de
    package niet. De implementatietoelichting voor onzelfstandige woonruimten
    neemt die voorwaarde ongewijzigd over en zegt niet dat ze niet wordt
    gecontroleerd. De test legt het huidige gedrag vast.

    Bron: beleidsboek onzelfstandige woonruimten, 2.12.2: "Daarbij dient er ook
    sprake te zijn van de mogelijkheid tot het openen van de
    (gemeenschappelijke) voordeur vanuit de woonruimte (op afstand) die toegang
    geeft tot het complex waarvan de woning onderdeel uitmaakt."
    """
    eenheid = EenhedenEenheid(
        id="aanbelfunctie",
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.aanbelfunctie_met_video_en_audioverbinding,
                oppervlakte=19.1488,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    groep = bijzondere_voorzieningen.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        Installatiesoort.aanbelfunctie_met_video_en_audioverbinding.naam: 0.25
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Laadpalen


def test_twee_laadpalen_bij_een_garage_krijgen_samen_4_punten(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Twee laadpalen bij een privégarage krijgen elk 2 punten: samen 4 punten.

    Bron: wettekst, Bijlage I onder B, rubriek 12: "Laadpaal t.b.v. elektrisch
    opladen" en "2 punten gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft."

    De laadpalen zijn bouwkundige elementen van de garage. De garage wordt niet
    met andere adressen en niet met andere onzelfstandige woonruimten gedeeld;
    de punten worden daarom niet gedeeld. Een garage van één adres krijgt in
    rubriek 10 geen punten; de laadpalen worden daarom in deze rubriek
    gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
    parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
    exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
    rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
    rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
    woning)."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3: "Krijgt
    die ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in
    alle andere gevallen hier, met dezelfde deler (aantal adressen × aantal
    onzelfstandige woonruimten)."
    """
    eenheid = EenhedenEenheid(
        id="2 laadpalen",
        ruimten=[
            ruimte(
                Ruimtedetailsoort.garage,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.laadpaal,
                    Bouwkundigelementdetailsoort.laadpaal,
                ),
                oppervlakte=19.1488,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    groep = bijzondere_voorzieningen.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Laadpalen": 2.0}
    assert punten_per_bovenliggende(groep) == {"Privé": {"Laadpalen": 4.0}}
    vergelijk_met_testreferentie(eenheid, groep)
