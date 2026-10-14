"""Bijzondere voorzieningen, zelfstandige woonruimten (rubriek 12)."""

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
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen import (
    BijzondereVoorzieningen,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen.bijzondere_voorzieningen import (
    UITGESLOTEN_ZORGWONING_GRONDSLAG_CRITERIUM_IDS,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde.punten_voor_de_woz_waarde import (
    NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID,
    NIEUWBOUW_MINIMUM_PUNTEN_ID,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Eenheidmonument,
    Installatiesoort,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
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


def test_BijzondereVoorzieningen_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        BijzondereVoorzieningen,
    )


# Zorgwoning


def test_zorgwoning_met_41_punten_in_de_rubrieken_1_tot_en_met_11_1_krijgt_14_25_punten_verhoging(
    bijzondere_voorzieningen,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een zorgwoning met 41 punten in de rubrieken 1 tot en met 11.1 krijgt 35% daarvan als verhoging: op een kwart punt afgerond 14,25 punten.

    Bron: wettekst, Bijlage I onder A, rubriek 12: "Uitsluitend bij
    zorgwoningen" en "bij: 35% van de ingevolge de onderdelen 1 tot en met 11.1
    toegekende punten."

    De verhoging is het totaal van deze rubriek en wordt op een kwart punt
    afgerond.

    Bron: beleidsboek zelfstandige woonruimten, 2.1.4: "Het totaal aantal
    punten wordt per rubriek afgerond op 0,25 punt, waarbij vanaf een achtste
    (1/8) punt naar boven wordt afgerond."

    De package leest aan de doelgroep af dat de eenheid een zorgwoning is.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.1: "Wanneer
    een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als
    zorgwoning gewaardeerd."

    De eenheid heeft alleen de doelgroep zorg en een verwarmde woonkamer. De
    test geeft geen eerder resultaat mee; de package waardeert de andere
    rubrieken daarom zelf en waarschuwt voor de energieprestatie, de
    monumenten, de pandsoort, de keuken, de WOZ-waarde en het bouwjaar die
    ontbreken.

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
                oppervlakte=19.1488,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = bijzondere_voorzieningen.waardeer(eenheid.model_copy())

    # De rubrieken 1 tot en met 11.1 geven samen 41 punten: 19 voor de
    # woonkamer van 19,1488 m² (rubriek 1), 2 voor het verwarmde vertrek
    # (rubriek 3), 5 minpunten omdat een buitenruimte ontbreekt (rubriek 8), 3
    # voor de gemeenschappelijke ruimten van een zorgwoning (rubriek 9) en 22
    # voor de minimum WOZ-waarde van € 85.806 (rubriek 11.1). 35% van 41 punten
    # is 14,35 punten; op een kwart punt afgerond is dat 14,25.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 14.25}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_50_punten_voor_een_rijksmonument_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """De 50 punten voor een rijksmonument met een huurovereenkomst van 1 januari 2024 tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    De 50 punten komen op grond van artikel 8a bij de waardering. De verhoging
    voor een zorgwoning is een percentage van de punten van de onderdelen 1 tot
    en met 11.1.

    Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
    of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
    Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
    voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
    waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
    punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
    bijlage I, onder B, met 10 punten vermeerderd."

    Bron: wettekst, Bijlage I onder A, rubriek 12: "bij: 35% van de ingevolge
    de onderdelen 1 tot en met 11.1 toegekende punten."

    De eenheid heeft de doelgroep zorg, de monumentstatus, de datum van de
    huurovereenkomst, een bouwjaar en een verwarmde woonkamer. De test geeft
    geen eerder resultaat mee; de package waardeert de andere rubrieken daarom
    zelf en waarschuwt voor de energieprestatie, de pandsoort, de keuken en de
    WOZ-waarde die ontbreken.

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
                oppervlakte=19.1488,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = bijzondere_voorzieningen.waardeer(eenheid)

    # De rubrieken 1 tot en met 11.1 geven samen 41 punten: 19 voor de
    # woonkamer van 19,1488 m² (rubriek 1), 2 voor het verwarmde vertrek
    # (rubriek 3), 5 minpunten omdat een buitenruimte ontbreekt (rubriek 8), 3
    # voor de gemeenschappelijke ruimten van een zorgwoning (rubriek 9) en 22
    # voor de minimum WOZ-waarde van € 85.806 (rubriek 11.1). 35% van 41 punten
    # is 14,35 punten; op een kwart punt afgerond is dat 14,25. Met de 50
    # punten van het rijksmonument erbij was het 35% van 91 punten geweest:
    # 31,85 punten, afgerond 31,75.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 14.25}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_BijzondereVoorzieningen_zorgwoninggrondslag_sluit_nieuwbouwminimum_uit(
    peildatum,
):
    """De punten waarmee het minimum voor nieuwbouw de punten voor de WOZ-waarde aanvult (onderdeel 11.2), tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    Bron: wettekst, Bijlage I onder A, rubriek 12: "bij: 35% van de ingevolge
    de onderdelen 1 tot en met 11.1 toegekende punten."

    Bron: beleidsboek zelfstandige woonruimten, 2.12: "Dit betekent dat punten
    die eventueel worden toegekend op basis van rubriek 11.2 (paragraaf 2.11.5
    van dit hoofdstuk) niet worden meegenomen in de berekening."

    Het eerdere resultaat is in de test zelf opgebouwd: 120 punten voor de
    oppervlakte van vertrekken en 30 punten voor de WOZ-waarde, waarvan 10
    punten van het minimum voor nieuwbouw.
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        doelgroep=Doelgroep.zorg,
        woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )

    oppervlakte_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )
    oppervlakte_builder.met_onderliggend(
        id="vertrekken", naam="Vertrekken", punten=120.0
    )

    woz_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )
    woz_builder.met_onderliggend(id="woz_basis", naam="WOZ basis", punten=20.0)
    woz_builder.met_onderliggend(
        id=NIEUWBOUW_MINIMUM_PUNTEN_ID,
        naam="Nieuwbouw: min. 30 punten",
        punten=10.0,
    )

    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[oppervlakte_builder.build(), woz_builder.build()]
    )

    groep = BijzondereVoorzieningen(peildatum=peildatum).waardeer(
        eenheid, woningwaardering_resultaat
    )

    assert UITGESLOTEN_ZORGWONING_GRONDSLAG_CRITERIUM_IDS == [
        NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID
    ]
    assert groep.punten == 49.0
    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1
    assert groep.woningwaarderingen[0].criterium is not None
    assert (
        groep.woningwaarderingen[0].criterium.id
        == "bijzondere_voorzieningen__zorgwoning_puntenverhoging"
    )
    assert groep.woningwaarderingen[0].punten == 49.0


# Aanbelfunctie


def test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

    Bron: wettekst, Bijlage I onder A, rubriek 12: "Aanbelfunctie met video- en
    audioverbinding waarbij de voordeur automatisch kan worden geopend vanuit
    de woning." en "0,25 punt".

    De aanbelfunctie is een installatie van een ruimte, hier de woonkamer. Of
    de voordeur vanuit de woning kan worden geopend, controleert de package
    niet: de implementatietoelichting haalt die voorwaarde door en houdt de
    waardering over. De test legt het huidige gedrag vast.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.2: "wordt de
    aanbelfunctie gewaardeerd met 0,25 punt."
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
    """Twee laadpalen bij een garage die niet met andere adressen wordt gedeeld, krijgen elk 2 punten: samen 4 punten.

    Bron: wettekst, Bijlage I onder A, rubriek 12: "Laadpaal t.b.v. elektrisch
    opladen" en "2 punten gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft."

    De laadpalen zijn bouwkundige elementen van de garage. Een garage van één
    adres krijgt in rubriek 10 geen punten; de laadpalen worden daarom in deze
    rubriek gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
    parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
    exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
    rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
    rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
    woning)."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3: "Krijgt
    die ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in
    alle andere gevallen hier, met dezelfde deler (aantal adressen)."
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
