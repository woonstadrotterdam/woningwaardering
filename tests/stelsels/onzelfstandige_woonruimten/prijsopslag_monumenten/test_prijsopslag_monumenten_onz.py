"""Prijsopslag monumenten, onzelfstandige woonruimten (rubriek 14)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.utils import assert_stelselgroep_output, punten_per_naam
from woningwaardering.stelsels.onzelfstandige_woonruimten.prijsopslag_monumenten import (
    PrijsopslagMonumenten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Eenheidmonument


@pytest.fixture()
def prijsopslag_monumenten(peildatum):
    return PrijsopslagMonumenten(peildatum=peildatum)


def opslagpercentage_per_naam(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> dict[str, float]:
    """Geef het opslagpercentage van elke waardering met een opslag, op naam van het criterium."""
    return {
        waardering.criterium.naam or "": waardering.opslagpercentage
        for waardering in groep.woningwaarderingen or []
        if waardering.opslagpercentage is not None and waardering.criterium is not None
    }


def test_PrijsopslagMonumenten_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PrijsopslagMonumenten,
    )


# Rijksmonumenten


def test_rijksmonument_met_huurovereenkomst_van_1_juli_2024_krijgt_35_procent_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een rijksmonument waarvan de huurovereenkomst op 1 juli 2024 is afgesloten, krijgt 35% opslag op de maximale huurprijs.

    Bron: wettekst, artikel 8a, eerste lid: "De maximale huurprijsgrens wordt
    met 35% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
    een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet en de
    huurovereenkomst betreffende die woonruimte is afgesloten na het tijdstip
    van inwerkingtreding van de Wet betaalbare huur."

    Bron: beleidsboek onzelfstandige woonruimten, 2.14.4: "als de
    huurovereenkomst is afgesloten op of na het tijdstip van inwerkingtreding
    van de Wet betaalbare huur (vanaf 1 juli 2024) dan wordt de maximale
    huurprijs vermeerderd met 35%."
    """
    eenheid = EenhedenEenheid(
        datum_afsluiten_huurovereenkomst=date(2024, 7, 1),
        monumenten=[Eenheidmonument.rijksmonument],
    )

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksmonument_met_huurovereenkomst_van_1_januari_2024_krijgt_10_punten(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een rijksmonument waarvan de huurovereenkomst op 1 januari 2024 is afgesloten, krijgt 10 punten.

    Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
    of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
    Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
    voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
    waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
    punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
    bijlage I, onder B, met 10 punten vermeerderd."

    Bron: beleidsboek onzelfstandige woonruimten, 2.14.4: "als de
    huurovereenkomst is afgesloten vóór 1 juli 2024 dan worden 10 punten extra
    toegekend."
    """
    eenheid = EenhedenEenheid(
        datum_afsluiten_huurovereenkomst=date(2024, 1, 1),
        monumenten=[Eenheidmonument.rijksmonument],
    )

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert punten_per_naam(groep) == {Eenheidmonument.rijksmonument.naam: 10.0}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksmonument_zonder_datum_van_de_huurovereenkomst_krijgt_met_waarschuwing_35_procent_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een rijksmonument zonder datum van afsluiten van de huurovereenkomst krijgt met een waarschuwing 35% opslag op de maximale huurprijs.

    De waardering van een rijksmonument hangt af van de datum waarop de
    huurovereenkomst is afgesloten; de package vraagt die datum daarom op.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4: "De datum
    van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor
    Rijksmonumenten."

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
        groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Gemeentelijke en provinciale monumenten


def test_gemeentelijk_monument_krijgt_15_procent_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een gemeentelijk monument krijgt 15% opslag op de maximale huurprijs.

    Bron: wettekst, artikel 8a, derde lid: "De maximale huurprijsgrens wordt
    met 15% vermeerderd indien de woonruimte bestaat uit of deel uitmaakt van
    een door het college van burgemeester en wethouders aangewezen gemeentelijk
    monument of een door gedeputeerde staten aangewezen provinciaal monument."
    """
    eenheid = EenhedenEenheid(monumenten=[Eenheidmonument.gemeentelijk_monument])

    groep = prijsopslag_monumenten.waardeer(eenheid)

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
    prijsopslag_monumenten,
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

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == verwachte_opslag
    assert groep.opslagpercentage == verwacht_opslagpercentage
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksbeschermd_stadsgezicht_zonder_bouwjaar_krijgt_met_waarschuwing_geen_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een woonruimte in een rijksbeschermd stadsgezicht zonder bouwjaar krijgt met een waarschuwing geen opslag.

    De opslag geldt alleen voor een woning die vóór 1965 is gebouwd. Zonder
    bouwjaar kan de package die voorwaarde niet toetsen.

    Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
    met 5% vermeerderd indien:" en "b. de woonruimte behoort tot een woning die
    is gebouwd voor 1965; en".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6: "Het
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
        groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Samenloop van opslagen


def test_rijksmonument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een rijksmonument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

    Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
    met 5% vermeerderd indien:" en "c. de woonruimte niet bestaat of deel
    uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet
    of van een door het college van burgemeester en wethouders aangewezen
    gemeentelijk monument of een door gedeputeerde staten aangewezen
    provinciaal monument."

    Bron: beleidsboek onzelfstandige woonruimten, 2.14.1: "Zo kunnen de
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4: "De datum
    van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor
    Rijksmonumenten."

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
        groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Monumenten niet opgegeven


def test_eenheid_zonder_opgegeven_monumenten_geeft_een_waarschuwing(
    prijsopslag_monumenten, vergelijk_met_testreferentie, monkeypatch
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
        groep = prijsopslag_monumenten.waardeer(eenheid.model_copy())

    assert opslagpercentage_per_naam(groep) == {}
    assert punten_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
