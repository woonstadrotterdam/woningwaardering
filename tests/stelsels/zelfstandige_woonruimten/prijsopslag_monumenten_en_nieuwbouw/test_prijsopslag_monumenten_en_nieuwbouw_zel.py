"""Prijsopslag monumenten en nieuwbouw, zelfstandige woonruimten (rubriek 13)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.input import meergezinswoning_van_79_m2
from tests.utils import (
    assert_stelselgroep_output,
    opslagpercentage_per_naam,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.prijsopslag_monumenten_en_nieuwbouw import (
    PrijsopslagMonumentenEnNieuwbouw,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenWozEenheid
from woningwaardering.vera.referentiedata import Eenheidmonument


@pytest.fixture()
def prijsopslag_monumenten_en_nieuwbouw(peildatum):
    return PrijsopslagMonumentenEnNieuwbouw(peildatum=peildatum)


def test_PrijsopslagMonumentenEnNieuwbouw_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PrijsopslagMonumentenEnNieuwbouw,
    )


# Rijksmonumenten


def test_rijksmonument_met_huurovereenkomst_van_1_juli_2024_krijgt_35_procent_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een rijksmonument waarvan de huurovereenkomst op 1 juli 2024 is afgesloten, krijgt 35% opslag op de maximale huurprijs.

    Bron: wettekst, artikel 8a, eerste lid: "De maximale huurprijsgrens wordt
    met 35% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
    een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet en de
    huurovereenkomst betreffende die woonruimte is afgesloten na het tijdstip
    van inwerkingtreding van de Wet betaalbare huur."

    Bron: beleidsboek zelfstandige woonruimten, 2.13.4: "als de
    huurovereenkomst is afgesloten op of na het tijdstip van inwerkingtreding
    van de Wet betaalbare huur (vanaf 1 juli 2024) dan wordt de maximale
    huurprijs vermeerderd met 35%."
    """
    eenheid = EenhedenEenheid(
        datum_afsluiten_huurovereenkomst=date(2024, 7, 1),
        monumenten=[Eenheidmonument.rijksmonument],
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksmonument_met_huurovereenkomst_van_1_januari_2024_krijgt_50_punten(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een rijksmonument waarvan de huurovereenkomst op 1 januari 2024 is afgesloten, krijgt 50 punten.

    Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
    of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
    Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
    voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
    waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
    punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
    bijlage I, onder B, met 10 punten vermeerderd."

    Bron: beleidsboek zelfstandige woonruimten, 2.13.4: "als de
    huurovereenkomst is afgesloten vóór 1 juli 2024 dan worden 50 punten extra
    toegekend."
    """
    eenheid = EenhedenEenheid(
        datum_afsluiten_huurovereenkomst=date(2024, 1, 1),
        monumenten=[Eenheidmonument.rijksmonument],
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert punten_per_naam(groep) == {Eenheidmonument.rijksmonument.naam: 50.0}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksmonument_zonder_datum_van_de_huurovereenkomst_krijgt_met_waarschuwing_35_procent_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een rijksmonument zonder datum van afsluiten van de huurovereenkomst krijgt met een waarschuwing 35% opslag op de maximale huurprijs.

    De waardering van een rijksmonument hangt af van de datum waarop de
    huurovereenkomst is afgesloten; de package vraagt die datum daarom op.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.13.4: "De datum
    van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor
    rijksmonumenten."

    Bron: implementatietoelichting, datamodel-uitbreidingen, "Datum afsluiten
    huurovereenkomst": "Voor een correcte waardering van rijksmonumenten dient
    de afsluitings datum van de huurovereenkomst opgegeven te worden."

    Ontbreekt de datum, dan rekent de package met de peildatum van de
    waardering, hier 1 juli 2026. De implementatietoelichting noemt die keuze
    niet; de test legt het huidige gedrag vast.

    Bron: wettekst, artikel 8a, eerste lid: "De maximale huurprijsgrens wordt
    met 35% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
    een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet en de
    huurovereenkomst betreffende die woonruimte is afgesloten na het tijdstip
    van inwerkingtreding van de Wet betaalbare huur."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        monumenten=[Eenheidmonument.rijksmonument],
    )

    with pytest.warns(
        UserWarning, match="'datum_afsluiten_huurovereenkomst' is niet gespecificeerd"
    ) as waarschuwingen:
        groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Gemeentelijke en provinciale monumenten


def test_gemeentelijk_monument_krijgt_15_procent_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een gemeentelijk monument krijgt 15% opslag op de maximale huurprijs.

    Bron: wettekst, artikel 8a, derde lid: "De maximale huurprijsgrens wordt
    met 15% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
    een door het college van burgemeester en wethouders aangewezen gemeentelijk
    monument of een door gedeputeerde staten aangewezen provinciaal monument."
    """
    eenheid = EenhedenEenheid(monumenten=[Eenheidmonument.gemeentelijk_monument])

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        "Gemeentelijk of provinciaal monument": 0.15
    }
    assert groep.opslagpercentage == 0.15
    vergelijk_met_testreferentie(eenheid, groep)


# Beschermd stads- en dorpsgezicht


@pytest.mark.parametrize(
    ("bouwjaar", "verwachte_opslag", "verwacht_opslagpercentage"),
    [
        pytest.param(
            1964,
            {"Rijksbeschermd stads- of dorpsgezicht": 0.05},
            0.05,
            id="bouwjaar_1964",
        ),
        pytest.param(
            1965,
            {},
            0.0,
            id="bouwjaar_1965",
            marks=pytest.mark.toelichting(
                "een woning uit 1965 is niet vóór 1965 gebouwd, dus de woonruimte "
                "krijgt geen opslag"
            ),
        ),
    ],
)
def test_rijksbeschermd_stadsgezicht_krijgt_alleen_bij_bouwjaar_voor_1965_opslag(
    prijsopslag_monumenten_en_nieuwbouw,
    vergelijk_met_testreferentie,
    bouwjaar,
    verwachte_opslag,
    verwacht_opslagpercentage,
):
    """Een woonruimte in een rijksbeschermd stadsgezicht krijgt alleen 5% opslag op de maximale huurprijs als de woning vóór 1965 is gebouwd.

    Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
    met 5% vermeerderd indien:", "a. die woonruimte behoort tot een
    rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34, vierde
    lid, van de Omgevingswet," en "b. de woonruimte behoort tot een woning die
    is gebouwd voor 1965; en".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=bouwjaar,
        monumenten=[Eenheidmonument.rijksbeschermd_stadsgezicht],
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == verwachte_opslag
    assert groep.opslagpercentage == verwacht_opslagpercentage
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksbeschermd_stadsgezicht_zonder_bouwjaar_krijgt_met_waarschuwing_geen_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een woonruimte in een rijksbeschermd stadsgezicht zonder bouwjaar krijgt met een waarschuwing geen opslag.

    De opslag geldt alleen voor een woning die vóór 1965 is gebouwd. Zonder
    bouwjaar kan de package die voorwaarde niet toetsen.

    Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
    met 5% vermeerderd indien:" en "b. de woonruimte behoort tot een woning die
    is gebouwd voor 1965; en".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.13.6: "Het
    bouwjaar is van belang omdat alleen woningen gebouwd vóór 1965 in
    aanmerking komen voor de opslag van 5%."

    De implementatietoelichting noemt niet dat de package bij een ontbrekend
    bouwjaar waarschuwt en geen opslag toekent; de test legt het huidige gedrag
    vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        monumenten=[Eenheidmonument.rijksbeschermd_stadsgezicht],
    )

    with pytest.warns(UserWarning, match="geen bouwjaar gevonden") as waarschuwingen:
        groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Nieuwbouw


def test_nieuwbouwwoning_met_149_punten_krijgt_10_procent_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een woning met 149 punten die na 1 juli 2024 voor het eerst in gebruik is genomen en waarvan de bouw voor 1 januari 2028 is gestart, krijgt 10 procent opslag.

    Bron: wettekst, artikel 8a, vierde lid: "wordt met 10% vermeerderd indien
    die woonruimte na 1 juli 2024 voor het eerst in gebruik wordt genomen als
    woonruimte en de bouw van deze woonruimte, of de verbouw van een ruimte met
    een andere gebruiksfunctie dan een woonfunctie naar een woonruimte met een
    woonfunctie, voor 1 januari 2028 is gestart."

    De opslag geldt voor een woning in de middensector. De woning haalt zonder
    opslag 149 punten en valt daarmee in de middensector.

    Bron: implementatietoelichting zelfstandige woonruimten, 1.3.1: "Hoger dan
    € 932,93 maar maximaal € 1.228,07 of 144 t/m 186 punten"

    De keuken heeft geen aanrecht en de woning heeft geen bouwjaar. Daarvoor
    waarschuwen de rubrieken keuken en punten voor de WOZ-waarde, die de
    package voor het puntentotaal meewaardeert.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = meergezinswoning_van_79_m2(
        begin_bouwdatum=date(2023, 1, 1),
        in_exploitatiedatum=date(2024, 8, 1),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=313000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=307000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=341000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2021, 1, 1), vastgestelde_waarde=283000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2020, 1, 1), vastgestelde_waarde=273000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2019, 1, 1), vastgestelde_waarde=237000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2018, 1, 1), vastgestelde_waarde=201000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2017, 1, 1), vastgestelde_waarde=163000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2016, 1, 1), vastgestelde_waarde=142000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2015, 1, 1), vastgestelde_waarde=135000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2014, 1, 1), vastgestelde_waarde=125000
            ),
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {"Nieuwbouw": 0.1}
    assert groep.opslagpercentage == 0.1
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woning_die_op_1_juli_2024_voor_het_eerst_in_gebruik_is_genomen_krijgt_geen_opslag_voor_nieuwbouw(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een woning die op 1 juli 2024 voor het eerst in gebruik is genomen, krijgt geen opslag voor nieuwbouw.

    Bron: wettekst, artikel 8a, vierde lid: "wordt met 10% vermeerderd indien
    die woonruimte na 1 juli 2024 voor het eerst in gebruik wordt genomen als
    woonruimte".

    De package leest de datum van ingebruikname uit `in_exploitatiedatum`.
    """
    eenheid = meergezinswoning_van_79_m2(
        begin_bouwdatum=date(2023, 1, 1),
        in_exploitatiedatum=date(2024, 7, 1),
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


# Samenloop van opslagen


def test_rijksmonument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een rijksmonument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

    Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
    met 5% vermeerderd indien:" en "c. de woonruimte niet bestaat of deel
    uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet
    of van een door het college van burgemeester en wethouders aangewezen
    gemeentelijk monument of een door gedeputeerde staten aangewezen
    provinciaal monument."

    Bron: beleidsboek zelfstandige woonruimten, 2.13.1: "Zo kunnen de
    monumentenopslag (zowel de Rijksmonumenten als provinciale en gemeentelijke
    monumenten) en de opslag voor een beschermd stads- of dorpsgezicht niet
    tegelijkertijd voor dezelfde woonruimte worden toegekend".

    De woning is uit 1964 en voldoet daarmee aan de voorwaarde voor het
    bouwjaar; alleen de status van rijksmonument sluit de opslag voor het
    stadsgezicht uit.

    Bron: wettekst, artikel 8a, vijfde lid: "b. de woonruimte behoort tot een
    woning die is gebouwd voor 1965; en".

    De eenheid heeft geen datum van afsluiten van de huurovereenkomst. De
    package waarschuwt daarvoor en rekent met de peildatum van de waardering,
    hier 1 juli 2026; het rijksmonument krijgt daarmee 35% opslag. De
    implementatietoelichting noemt de keuze voor de peildatum niet; de test
    legt het huidige gedrag vast.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.13.4: "De datum
    van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor
    rijksmonumenten."

    Bron: wettekst, artikel 8a, eerste lid: "De maximale huurprijsgrens wordt
    met 35% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
    een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet en de
    huurovereenkomst betreffende die woonruimte is afgesloten na het tijdstip
    van inwerkingtreding van de Wet betaalbare huur."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1964,
        monumenten=[
            Eenheidmonument.rijksmonument,
            Eenheidmonument.rijksbeschermd_stadsgezicht,
        ],
    )

    with pytest.warns(
        UserWarning, match="'datum_afsluiten_huurovereenkomst' is niet gespecificeerd"
    ) as waarschuwingen:
        groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Monumenten niet opgegeven


def test_eenheid_zonder_opgegeven_monumenten_geeft_een_waarschuwing(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie, monkeypatch
):
    """Een eenheid waarvan `monumenten` niet is opgegeven, geeft een waarschuwing.

    De package vraagt om een lege lijst wanneer de eenheid geen monumentstatus
    heeft. De implementatietoelichting noemt die keuze niet; de test legt het
    huidige gedrag vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Na de waarschuwing zoekt de package de monumentstatus zelf op met de
    BAG-identificatie van de eenheid (README.md, Installatie). Deze eenheid
    heeft geen BAG-identificatie en krijgt geen waardering.
    """
    # De package `monumenten` is optioneel; zonder haar geeft de waardering een
    # tweede waarschuwing. Met deze vervanger verloopt de waardering in elke
    # omgeving hetzelfde: zonder BAG-identificatie wordt `MonumentenClient`
    # niet aangeroepen.
    monkeypatch.setitem(
        sys.modules, "monumenten", SimpleNamespace(MonumentenClient=None)
    )
    eenheid = EenhedenEenheid(id="eenheid")

    with pytest.warns(
        UserWarning, match="'monumenten' is niet gespecificeerd"
    ) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid.model_copy())

    assert opslagpercentage_per_naam(groep) == {}
    assert punten_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
