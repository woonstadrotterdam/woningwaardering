"""Prijsopslag monumenten, onzelfstandige woonruimten (rubriek 14)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.utils import (
    assert_stelselgroep_output,
    opslagpercentage_per_naam,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.prijsopslag_monumenten import (
    PrijsopslagMonumenten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import Eenheidmonument


@pytest.fixture()
def prijsopslag_monumenten(peildatum):
    return PrijsopslagMonumenten(peildatum=peildatum)


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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
    artikel 8a, eerste lid.
    """
    # Precies op de dag van inwerkingtreding van de Wet betaalbare huur.
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


def test_rijksmonument_met_huurovereenkomst_voor_1_juli_2024_krijgt_10_punten(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een rijksmonument waarvan de huurovereenkomst vóór 1 juli 2024 is afgesloten, krijgt 10 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
    artikel 8a, tweede lid.
    """
    # Eén dag vóór de inwerkingtreding van de Wet betaalbare huur.
    eenheid = EenhedenEenheid(
        datum_afsluiten_huurovereenkomst=date(2024, 6, 30),
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
    artikel 8a, eerste lid.
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        monumenten=[Eenheidmonument.rijksmonument],
    )

    with pytest.warns(
        UserWarning, match="'datum_afsluiten_huurovereenkomst' is niet gespecificeerd"
    ) as waarschuwingen:
        groep = prijsopslag_monumenten.waardeer(eenheid)

    # De peildatum (1 juli 2026) valt na de inwerkingtreding van de Wet
    # betaalbare huur, dus het rijksmonument krijgt 35% opslag.
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.5; wettekst,
    artikel 8a, derde lid.
    """
    eenheid = EenhedenEenheid(monumenten=[Eenheidmonument.gemeentelijk_monument])

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        "Gemeentelijk of provinciaal monument": 0.15
    }
    assert groep.opslagpercentage == 0.15
    vergelijk_met_testreferentie(eenheid, groep)


def test_provinciaal_monument_krijgt_15_procent_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een provinciaal monument krijgt 15% opslag op de maximale huurprijs.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.5; wettekst,
    artikel 8a, derde lid.
    """
    eenheid = EenhedenEenheid(monumenten=[Eenheidmonument.provinciaal_monument])

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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6; wettekst,
    artikel 8a, vijfde lid.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=bouwjaar,
        monumenten=[Eenheidmonument.rijksbeschermd_stadsgezicht],
    )

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == verwachte_opslag
    assert groep.opslagpercentage == verwacht_opslagpercentage
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksbeschermd_dorpsgezicht_krijgt_bij_bouwjaar_voor_1965_5_procent_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een woonruimte in een rijksbeschermd dorpsgezicht die vóór 1965 is gebouwd, krijgt 5% opslag op de maximale huurprijs.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6; wettekst,
    artikel 8a, vijfde lid.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1964,
        monumenten=[Eenheidmonument.rijksbeschermd_dorpsgezicht],
    )

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        "Rijksbeschermd stads- of dorpsgezicht": 0.05
    }
    assert groep.opslagpercentage == 0.05
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeentelijk_beschermd_stads_of_dorpsgezicht_krijgt_geen_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een woonruimte in een gemeentelijk beschermd stads- of dorpsgezicht krijgt geen opslag.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6; wettekst,
    artikel 8a, vijfde lid.
    """
    # Het bouwjaar voldoet aan de eis; alleen de soort gezicht sluit de opslag uit.
    eenheid = EenhedenEenheid(
        bouwjaar=1964,
        monumenten=[
            Eenheidmonument.gemeentelijk_beschermd_stadsgezicht,
            Eenheidmonument.gemeentelijk_beschermd_dorpsgezicht,
        ],
    )

    groep = prijsopslag_monumenten.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksbeschermd_stadsgezicht_zonder_bouwjaar_krijgt_met_waarschuwing_geen_opslag(
    prijsopslag_monumenten, vergelijk_met_testreferentie
):
    """Een woonruimte in een rijksbeschermd stadsgezicht zonder bouwjaar krijgt met een waarschuwing geen opslag."""
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.1;
    implementatietoelichting onzelfstandige woonruimten, 2.14.6; wettekst,
    artikel 8a, vijfde lid.

    Een rijksmonument krijgt 35% opslag op de maximale huurprijs.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
    artikel 8a, eerste lid.
    """
    # Het bouwjaar voldoet aan de eis; alleen het rijksmonument sluit de opslag uit.
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

    # Zonder datum van afsluiten rekent de package met de peildatum (1 juli 2026),
    # dus het rijksmonument krijgt 35% opslag.
    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Monumenten niet opgegeven


def test_eenheid_zonder_opgegeven_monumenten_geeft_een_waarschuwing(
    prijsopslag_monumenten, vergelijk_met_testreferentie, monkeypatch
):
    """Een eenheid waarvan `monumenten` niet is opgegeven, geeft een waarschuwing."""
    # De package `monumenten` is optioneel; zonder haar geeft de waardering een
    # tweede waarschuwing. Met deze vervanger verloopt de waardering in elke
    # omgeving hetzelfde: zonder BAG-identificatie wordt `MonumentenClient`
    # niet aangeroepen.
    monkeypatch.setitem(
        sys.modules, "monumenten", SimpleNamespace(MonumentenClient=None)
    )
    # Zonder BAG-identificatie zoekt de package de monumentstatus niet zelf op.
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
