"""Prijsopslag monumenten en nieuwbouw, zelfstandige woonruimten (rubriek 13)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.input import meergezinswoning_van_79_m2, woz_eenheden_voor_149_punten
from tests.utils import (
    assert_stelselgroep_output,
    opslagpercentage_per_naam,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.prijsopslag_monumenten_en_nieuwbouw import (
    PrijsopslagMonumentenEnNieuwbouw,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
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
    """Een rijksmonument waarvan de huurovereenkomst op of na 1 juli 2024 is afgesloten, krijgt 35% opslag op de maximale huurprijs.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.4
    - wettekst, artikel 8a, eerste lid
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


def test_rijksmonument_met_huurovereenkomst_voor_1_juli_2024_krijgt_50_punten(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een rijksmonument waarvan de huurovereenkomst vóór 1 juli 2024 is afgesloten, krijgt 50 punten.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.4
    - wettekst, artikel 8a, tweede lid
    """
    # Eén dag vóór de inwerkingtreding van de Wet betaalbare huur.
    eenheid = EenhedenEenheid(
        datum_afsluiten_huurovereenkomst=date(2024, 6, 30),
        monumenten=[Eenheidmonument.rijksmonument],
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert punten_per_naam(groep) == {Eenheidmonument.rijksmonument.naam: 50.0}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksmonument_zonder_datum_van_de_huurovereenkomst_wordt_met_waarschuwing_naar_de_peildatum_gewaardeerd(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Zonder datum van afsluiten van de huurovereenkomst waardeert de package een rijksmonument met een waarschuwing alsof de huurovereenkomst op de peildatum is afgesloten.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.4
    - implementatietoelichting datamodel-uitbreidingen, "Datum afsluiten huurovereenkomst"
    - wettekst, artikel 8a, eerste lid
    """
    # Zonder datum waarschuwt de package en valt ze terug op de peildatum.
    eenheid = EenhedenEenheid(
        id="eenheid",
        monumenten=[Eenheidmonument.rijksmonument],
    )

    with pytest.warns(
        UserWarning, match="'datum_afsluiten_huurovereenkomst' is niet gespecificeerd"
    ) as waarschuwingen:
        groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    # De peildatum van de waardering (1 juli 2026) valt na de inwerkingtreding van
    # de Wet betaalbare huur, dus 35%.
    assert opslagpercentage_per_naam(groep) == {
        Eenheidmonument.rijksmonument.naam: 0.35
    }
    assert groep.opslagpercentage == 0.35
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Gemeentelijke en provinciale monumenten


@pytest.mark.parametrize(
    "monument",
    [
        pytest.param(Eenheidmonument.gemeentelijk_monument, id="gemeentelijk_monument"),
        pytest.param(Eenheidmonument.provinciaal_monument, id="provinciaal_monument"),
    ],
)
def test_gemeentelijk_of_provinciaal_monument_krijgt_15_procent_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie, monument
):
    """Een gemeentelijk of provinciaal monument krijgt 15% opslag op de maximale huurprijs.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.5
    - wettekst, artikel 8a, derde lid
    """
    eenheid = EenhedenEenheid(monumenten=[monument])

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {
        "Gemeentelijk of provinciaal monument": 0.15
    }
    assert groep.opslagpercentage == 0.15
    vergelijk_met_testreferentie(eenheid, groep)


# Beschermd stads- en dorpsgezicht


@pytest.mark.parametrize(
    ("monument", "bouwjaar", "verwachte_opslag", "verwacht_opslagpercentage"),
    [
        pytest.param(
            Eenheidmonument.rijksbeschermd_stadsgezicht,
            1964,
            {"Rijksbeschermd stads- of dorpsgezicht": 0.05},
            0.05,
            id="stadsgezicht_bouwjaar_1964",
        ),
        pytest.param(
            Eenheidmonument.rijksbeschermd_stadsgezicht,
            1965,
            {},
            0.0,
            id="stadsgezicht_bouwjaar_1965",
            marks=pytest.mark.toelichting(
                "een woning uit 1965 is niet vóór 1965 gebouwd, dus de woonruimte "
                "krijgt geen opslag"
            ),
        ),
        pytest.param(
            Eenheidmonument.rijksbeschermd_dorpsgezicht,
            1964,
            {"Rijksbeschermd stads- of dorpsgezicht": 0.05},
            0.05,
            id="dorpsgezicht_bouwjaar_1964",
        ),
    ],
)
def test_rijksbeschermd_stads_of_dorpsgezicht_krijgt_alleen_bij_bouwjaar_voor_1965_opslag(
    prijsopslag_monumenten_en_nieuwbouw,
    vergelijk_met_testreferentie,
    monument,
    bouwjaar,
    verwachte_opslag,
    verwacht_opslagpercentage,
):
    """Een woonruimte in een rijksbeschermd stads- of dorpsgezicht krijgt alleen 5% opslag op de maximale huurprijs als de woning vóór 1965 is gebouwd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.6
    - wettekst, artikel 8a, vijfde lid
    """
    eenheid = EenhedenEenheid(bouwjaar=bouwjaar, monumenten=[monument])

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == verwachte_opslag
    assert groep.opslagpercentage == verwacht_opslagpercentage
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeentelijk_beschermd_stads_of_dorpsgezicht_krijgt_geen_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een woonruimte in een gemeentelijk beschermd stads- of dorpsgezicht krijgt geen opslag.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.6
    - wettekst, artikel 8a, vijfde lid
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1964,
        monumenten=[
            Eenheidmonument.gemeentelijk_beschermd_stadsgezicht,
            Eenheidmonument.gemeentelijk_beschermd_dorpsgezicht,
        ],
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_rijksbeschermd_stadsgezicht_zonder_bouwjaar_krijgt_met_waarschuwing_geen_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een woonruimte in een rijksbeschermd stadsgezicht zonder bouwjaar krijgt met een waarschuwing geen opslag."""
    # Zonder bouwjaar is niet te toetsen of de woning voor 1965 is gebouwd.
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


def test_nieuwbouwwoning_in_de_middensector_krijgt_10_procent_opslag(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie
):
    """Een woning in de middensector die na 1 juli 2024 voor het eerst in gebruik is genomen en waarvan de bouw voor 1 januari 2028 is gestart, krijgt 10 procent opslag.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.7.1
    - wettekst, artikel 8a, vierde lid
    """
    # De WOZ-waarden geven 149 punten, binnen de middensector (144 t/m 186).
    eenheid = meergezinswoning_van_79_m2(
        begin_bouwdatum=date(2023, 1, 1),
        in_exploitatiedatum=date(2024, 8, 1),
        woz_eenheden=woz_eenheden_voor_149_punten(),
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.7.1
    - wettekst, artikel 8a, vierde lid
    """
    # Op de grens: eerste ingebruikname op 1 juli 2024, niet erna.
    eenheid = meergezinswoning_van_79_m2(
        begin_bouwdatum=date(2023, 1, 1),
        in_exploitatiedatum=date(2024, 7, 1),
        woz_eenheden=woz_eenheden_voor_149_punten(),
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


# Samenloop van opslagen


@pytest.mark.parametrize(
    ("monument", "verwachte_opslag", "verwacht_opslagpercentage"),
    [
        pytest.param(
            Eenheidmonument.rijksmonument,
            {Eenheidmonument.rijksmonument.naam: 0.35},
            0.35,
            id="rijksmonument",
            marks=pytest.mark.toelichting("het rijksmonument krijgt zelf 35% opslag"),
        ),
        pytest.param(
            Eenheidmonument.gemeentelijk_monument,
            {"Gemeentelijk of provinciaal monument": 0.15},
            0.15,
            id="gemeentelijk_monument",
            marks=pytest.mark.toelichting(
                "het gemeentelijk monument krijgt zelf 15% opslag"
            ),
        ),
        pytest.param(
            Eenheidmonument.provinciaal_monument,
            {"Gemeentelijk of provinciaal monument": 0.15},
            0.15,
            id="provinciaal_monument",
            marks=pytest.mark.toelichting(
                "het provinciaal monument krijgt zelf 15% opslag"
            ),
        ),
    ],
)
def test_monument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht(
    prijsopslag_monumenten_en_nieuwbouw,
    vergelijk_met_testreferentie,
    monument,
    verwachte_opslag,
    verwacht_opslagpercentage,
):
    """Een monument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.6
    - wettekst, artikel 8a, vijfde lid
    """
    # Gebouwd vóór 1965: alleen het monument sluit de opslag voor het stadsgezicht uit.
    eenheid = EenhedenEenheid(
        bouwjaar=1964,
        datum_afsluiten_huurovereenkomst=date(2024, 7, 1),
        monumenten=[monument, Eenheidmonument.rijksbeschermd_stadsgezicht],
    )

    groep = prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid)

    assert opslagpercentage_per_naam(groep) == verwachte_opslag
    assert groep.opslagpercentage == verwacht_opslagpercentage
    vergelijk_met_testreferentie(eenheid, groep)


# Monumenten niet opgegeven


def test_eenheid_zonder_opgegeven_monumenten_geeft_een_waarschuwing(
    prijsopslag_monumenten_en_nieuwbouw, vergelijk_met_testreferentie, monkeypatch
):
    """Een eenheid waarvan `monumenten` niet is opgegeven, geeft een waarschuwing."""
    # Vervangt de optionele package monumenten, zodat elke omgeving gelijk werkt.
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

    # Na de waarschuwing zoekt de package de monumentstatus op met de
    # BAG-identificatie; deze eenheid heeft er geen en krijgt geen waardering.
    assert opslagpercentage_per_naam(groep) == {}
    assert punten_per_naam(groep) == {}
    assert groep.opslagpercentage == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
