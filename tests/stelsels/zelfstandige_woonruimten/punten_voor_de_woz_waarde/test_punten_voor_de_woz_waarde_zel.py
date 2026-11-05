"""Punten voor de WOZ-waarde, zelfstandige woonruimten (rubriek 11)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.input import (
    meergezinswoning_van_71_m2,
    ruimte,
)
from tests.utils import (
    aantal_per_bovenliggende,
    aantal_per_naam,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenRenovatie,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Ruimtedetailsoort,
)


@pytest.fixture()
def punten_voor_de_woz_waarde(peildatum):
    return PuntenVoorDeWozWaarde(peildatum=peildatum)


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


# De berekening van onderdeel I en II


def test_punten_voor_de_woz_waarde_zijn_de_som_van_onderdeel_i_en_ii_afgerond_op_een_kwart_punt(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """De punten voor de WOZ-waarde zijn de som van onderdeel I en onderdeel II, afgerond op een kwart punt.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.2
    """
    # Dezelfde WOZ-waarde en oppervlakte als in het rekenvoorbeeld, zodat de uitkomst te vergelijken is.
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2025, 1, 1), vastgestelde_waarde=300000
            ),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=60.0, verwarmd=True)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2025": 300000.0,
        "Factor I": 16954.0,
        "Oppervlakte van vertrekken en overige ruimten": 60.0,
        "Factor II": 268.0,
    }
    # 17,69 + 18,66 = 36,35, afgerond op 36,25: de afronding is het verschil, -0,10.
    assert punten_per_naam(groep) == {
        "Onderdeel I": 17.69,
        "Onderdeel II": 18.66,
        "Afronding op kwartpunten": -0.1,
    }
    assert groep.punten == 36.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_onderdeel_i_en_ii_worden_niet_afgerond_voordat_ze_worden_opgeteld(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """De punten van onderdeel I en onderdeel II worden niet afgerond voordat ze bij elkaar worden opgeteld.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.2
    """
    # Een WOZ-waarde en oppervlakte waarbij eerder afronden een ander totaal geeft.
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1980,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2025, 1, 1), vastgestelde_waarde=50000
            ),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=26.0, verwarmd=True)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert punten_per_naam(groep) == {
        "Onderdeel I": 2.95,
        "Onderdeel II": 7.18,
        "Afronding op kwartpunten": -0.13,
    }
    # Onafgerond tellen de onderdelen op tot 10,1248 en dat wordt 10 punten.
    # Waren ze eerst op twee decimalen afgerond, dan was de som 10,13 en werd
    # dat 10,25 punten.
    assert groep.punten == 10.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# De WOZ-waarde waarmee wordt gerekend


def test_woz_waarde_onder_de_minimum_woz_waarde_wordt_niet_verhoogd_tot_dat_minimum(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een vastgestelde WOZ-waarde die lager is dan de minimum WOZ-waarde van € 85.806, wordt niet tot dat minimum verhoogd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.1
    - wettekst, Bijlage I onder A, onderdeel 11.1
    """
    # Eén euro onder de minimum WOZ-waarde.
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=85805
            ),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=28.0)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 85805.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 28.0,
        "Factor II": 242.0,
    }
    # € 85.805 / € 15.329 = 5,60 en € 85.805 / 28 m² / € 242 = 12,66: samen 18,26,
    # afgerond op 18,25 punten.
    assert punten_per_naam(groep) == {
        "Onderdeel I": 5.6,
        "Onderdeel II": 12.66,
        "Afronding op kwartpunten": -0.01,
    }
    assert groep.punten == 18.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woz_eenheid_zonder_vastgestelde_waarde_wordt_overgeslagen(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een WOZ-eenheid zonder vastgestelde waarde slaat de package over: zij rekent met de meest recente WOZ-waarde die wel is vastgesteld.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.1
    - wettekst, Bijlage I onder A, onderdeel 11.1
    """
    # De WOZ-eenheid van 1 januari 2025 heeft geen waarde, die van 2024 wel.
    eenheid = EenhedenEenheid(
        id="eenheid",
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=100000
            ),
            EenhedenWozEenheid(waardepeildatum=date(2025, 1, 1)),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=10.0)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 100000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 10.0,
        "Factor II": 242.0,
    }
    # € 100.000 / € 15.329 + € 100.000 / 10 m² / € 242 = 47,85, afgerond 47,75
    assert groep.punten == 47.75
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_eenheid_zonder_woz_waarde_wordt_met_waarschuwing_gewaardeerd_met_de_minimum_woz_waarde(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid zonder WOZ-waarde wordt met een waarschuwing gewaardeerd met de minimum WOZ-waarde van € 85.806.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.1
    - wettekst, Bijlage I onder A, onderdeel 11.1
    """
    # Een woning zonder WOZ-waarde, buiten de nieuwbouwjaren 2015 tot en met 2019.
    eenheid = meergezinswoning_van_71_m2(bouwjaar=1981)

    with pytest.warns(
        UserWarning, match="geen WOZ-waarde aangeleverd"
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    # Bij de minimumwaarde horen de kengetallen van waardepeildatum 1 januari 2025.
    assert aantal_per_bovenliggende(groep) == {
        None: {"Minimum WOZ-waarde (geen relevante WOZ-waarde beschikbaar)": 85806.0},
        "Onderdeel I": {
            "Minimum WOZ-waarde gebruikt voor berekening": 85806.0,
            "Factor I": 16954.0,
        },
        "Onderdeel II": {
            "Minimum WOZ-waarde gebruikt voor berekening": 85806.0,
            "Oppervlakte van vertrekken en overige ruimten": 60.0,
            "Factor II": 268.0,
        },
    }
    # 5,06 + 5,34 = 10,40, afgerond op 10,50 punten
    assert punten_per_naam(groep) == {
        "Onderdeel I": 5.06,
        "Onderdeel II": 5.34,
        "Afronding op kwartpunten": 0.1,
    }
    assert groep.punten == 10.5
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# De oppervlakte in onderdeel II


def test_onderdeel_ii_rekent_met_de_oppervlakte_van_vertrekken_overige_ruimten_en_parkeerplekken_type_i(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """In onderdeel II telt de oppervlakte mee van de vertrekken en overige ruimten uit rubriek 1 en 2 en van de parkeerplekken type I uit rubriek 10.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.2
    - wettekst, Bijlage I onder A, onderdeel 11.1

    Van een parkeerplek type I telt de oppervlakte gedeeld door het aantal
    adressen dat toegang heeft tot de parkeerplek.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.2
    """
    # Een toiletruimte van 1,9 m² en een parkeerplek van 10 m² tellen niet mee.
    eenheid = EenhedenEenheid(
        id="eenheid",
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=100000
            ),
        ],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte1", oppervlakte=10.0
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte2", oppervlakte=1.9
            ),
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=10.0),
            # `aantal` geeft aan hoeveel van deze specifieke ruimte er zijn.
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                naam="Parkeerplek1",
                oppervlakte=20.0,
                aantal=3,
                gedeeld_met_aantal_adressen=4,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                naam="Parkeerplek2",
                oppervlakte=10.0,
                aantal=2,
                gedeeld_met_aantal_adressen=4,
            ),
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    # 10 (woonkamer) + 10 (Toiletruimte1) + 3 x 20 / 4 adressen (Parkeerplek1) = 35 m²
    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 100000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 35.0,
        "Factor II": 242.0,
    }
    # € 100.000 / 35 m² / € 242
    assert punten_per_naam(groep)["Onderdeel II"] == 11.81
    assert groep.punten == 18.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Kleine nieuwbouwwoningen in het COROP-gebied Amsterdam of Utrecht


@pytest.mark.parametrize(
    ("woonplaatscode", "bouwjaar"),
    [
        pytest.param("3594", 2018, id="amsterdam_gebouwd_in_2018"),
        pytest.param("3295", 2022, id="utrecht_gebouwd_in_2022"),
    ],
)
def test_woning_kleiner_dan_40_m2_gebouwd_in_2018_tot_en_met_2022_in_corop_gebied_amsterdam_of_utrecht_krijgt_in_onderdeel_ii_het_lagere_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie, woonplaatscode, bouwjaar
):
    """Een woning kleiner dan 40 m² die in 2018 tot en met 2022 is gebouwd en in het COROP-gebied Amsterdam of Utrecht ligt, krijgt in onderdeel II het lagere kengetal van € 103.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.6
    - wettekst, Bijlage I onder A, onderdeel 11.1
    """
    eenheid = EenhedenEenheid(
        bouwjaar=bouwjaar,
        adres=EenhedenEenheidadres(woonplaats=EenhedenWoonplaats(code=woonplaatscode)),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        # Eén m² onder de grens van 40 m².
        gebruiksoppervlakte=39,
        monumenten=[],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=39.0)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 310000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 39.0,
        "Factor II": 103.0,
    }
    # € 310.000 / 39 m² / € 103
    assert punten_per_naam(groep)["Onderdeel II"] == 77.17
    assert groep.punten == 97.5
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


@pytest.mark.parametrize(
    ("woonplaatscode", "bouwjaar", "gebruiksoppervlakte"),
    [
        pytest.param("3594", 2017, 39, id="gebouwd_in_2017"),
        pytest.param("3594", 2023, 39, id="gebouwd_in_2023"),
        pytest.param("3594", 2018, 40, id="precies_40_m2"),
        pytest.param("3086", 2018, 39, id="buiten_corop_gebied"),
    ],
)
def test_woning_die_niet_aan_alle_eisen_voor_het_lagere_kengetal_voldoet_krijgt_in_onderdeel_ii_het_gewone_kengetal(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    woonplaatscode,
    bouwjaar,
    gebruiksoppervlakte,
):
    """Een woning die niet aan alle eisen voor het lagere kengetal van onderdeel II voldoet, krijgt in onderdeel II het gewone kengetal van € 242.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.6
    - wettekst, Bijlage I onder A, onderdeel 11.1
    """
    # Elk geval wijkt op één eis af van Amsterdam, 2018 en 39 m², die het lagere kengetal krijgen.
    eenheid = EenhedenEenheid(
        bouwjaar=bouwjaar,
        adres=EenhedenEenheidadres(woonplaats=EenhedenWoonplaats(code=woonplaatscode)),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        gebruiksoppervlakte=gebruiksoppervlakte,
        monumenten=[],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=39.0)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 310000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 39.0,
        "Factor II": 242.0,
    }
    # € 310.000 / 39 m² / € 242
    assert punten_per_naam(groep)["Onderdeel II"] == 32.85
    assert groep.punten == 53.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woning_kleiner_dan_40_m2_gebouwd_in_2018_tot_en_met_2022_zonder_adres_krijgt_met_waarschuwing_het_gewone_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Zonder adres krijgt een woning kleiner dan 40 m² die in 2018 tot en met 2022 is gebouwd, met een waarschuwing in onderdeel II het gewone kengetal van € 242.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.6
    """
    # Zonder adres is het COROP-gebied niet te bepalen.
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=2018,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        gebruiksoppervlakte=39,
        monumenten=[],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=39.0)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert any(
        "geen adres gevonden voor COROP-gebied" in str(w.message)
        for w in waarschuwingen
    )
    assert aantal_per_naam(groep)["Factor II"] == 242.0
    # € 310.000 / 39 m² / € 242
    assert punten_per_naam(groep)["Onderdeel II"] == 32.85
    assert groep.punten == 53.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Het minimum van 40 punten voor woningen uit 2015 tot en met 2019


@pytest.mark.parametrize(
    "bouwjaar",
    [
        pytest.param(2015, id="gebouwd_in_2015"),
        pytest.param(2019, id="gebouwd_in_2019"),
    ],
)
def test_woning_gebouwd_in_2015_tot_en_met_2019_met_minstens_110_punten_krijgt_minimaal_40_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie, bouwjaar
):
    """Een woning gebouwd in 2015 tot en met 2019 die voor de rubrieken 1 tot en met 10 en 12 minstens 110 punten haalt, krijgt minimaal 40 punten voor de WOZ-waarde.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    """
    # Een woning met meer dan 110 punten voor rubriek 1 tot en met 10 en 12.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=bouwjaar,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=259999
            ),
        ],
    )

    with pytest.warns(UserWarning, match="energieprestaties") as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    # Onderdeel I en II geven samen minder dan 40 punten; de waardering vult aan tot 40.
    assert punten_per_naam(groep)["Nieuwbouw: min. 40 punten"] == 5.13
    assert groep.punten == 40.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woning_gebouwd_in_2015_tot_en_met_2019_met_minder_dan_110_punten_krijgt_geen_minimum_van_40_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning gebouwd in 2015 tot en met 2019 die voor de rubrieken 1 tot en met 10 en 12 minder dan 110 punten haalt, krijgt geen minimum van 40 punten voor de WOZ-waarde.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    """
    # Een woning van 2016 die met energielabel C minder dan 110 punten haalt.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=2016,
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 2, 23),
                einddatum=date(2031, 2, 23),
                label=Energielabel.c,
            )
        ],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=259999
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert "Nieuwbouw: min. 40 punten" not in punten_per_naam(groep)
    assert groep.punten == 34.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_verbouw_in_2015_tot_en_met_2019_geeft_geen_minimum_van_40_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """De package past het minimum van 40 punten voor de WOZ-waarde alleen toe op het bouwjaar, niet op een verbouw in 2015 tot en met 2019.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    """
    # Een woning van 1912 met meer dan 110 punten, verbouwd in 2016.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=1912,
        renovatie=EenhedenRenovatie(
            omschrijving="hoogniveau renovatie", datum=date(2016, 1, 1)
        ),
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Energielabel.ap4,
            )
        ],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=259999
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert "Nieuwbouw: min. 40 punten" not in punten_per_naam(groep)
    assert groep.punten == 34.75
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    "bouwjaar",
    [
        pytest.param(2014, id="gebouwd_in_2014"),
        pytest.param(2020, id="gebouwd_in_2020"),
    ],
)
def test_woning_gebouwd_buiten_2015_tot_en_met_2019_krijgt_geen_minimum_van_40_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie, bouwjaar
):
    """Een woning gebouwd buiten 2015 tot en met 2019 die voor de rubrieken 1 tot en met 10 en 12 minstens 110 punten haalt, krijgt geen minimum van 40 punten voor de WOZ-waarde.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    """
    # Een woning met meer dan 110 punten voor rubriek 1 tot en met 10 en 12.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=bouwjaar,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=259999
            ),
        ],
    )

    with pytest.warns(UserWarning, match="energieprestaties") as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert "Nieuwbouw: min. 40 punten" not in punten_per_naam(groep)
    assert groep.punten == 34.75
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# De cap op de WOZ


def test_woz_punten_worden_beperkt_tot_33_procent_van_de_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """De punten voor de WOZ-waarde zijn niet meer dan 33 procent van de waardering van een woning die zonder die beperking 187 punten of meer heeft.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.2
    - implementatietoelichting zelfstandige woonruimten, 2.11.7
    - wettekst, Bijlage I onder A, onderdeel 11.3

    Bij de beperking wordt het aantal punten voor de WOZ-waarde naar beneden
    afgerond op hele punten.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.2
    - wettekst, Bijlage I onder A, toelichting rubriek 11
    """
    # 135,75 punten in de andere rubrieken: ook mét de beperking boven 186 punten.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=1981,
        aanrecht_mm=None,
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 3, 27),
                einddatum=date(2031, 3, 27),
                label=Energielabel.ap3,
                waarde="170",
            )
        ],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=613900
            ),
        ],
    )

    with pytest.warns(UserWarning, match="aanrecht") as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    # Met 135,75 punten in de andere rubrieken zijn hoogstens 66,86 punten voor de
    # WOZ-waarde toegestaan, afgerond naar beneden op 66.
    assert punten_per_naam(groep)["Maximering WOZ-punten tot 33% van totaal"] == -16.33
    assert groep.punten == 66.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woning_die_door_de_cap_onder_187_punten_komt_krijgt_186_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning die zonder de cap op de WOZ meer dan 186 punten heeft en met de cap minder dan 187, krijgt een waardering van 186 punten.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.7
    - wettekst, Bijlage I onder A, onderdeel 11.3
    """
    # 119,75 punten in de andere rubrieken: mét de beperking onder 187 punten.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=1981,
        aanrecht_mm=None,
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 3, 27),
                einddatum=date(2031, 3, 27),
                label=Energielabel.a,
                waarde="170",
            )
        ],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=713900
            ),
        ],
    )

    with pytest.warns(UserWarning, match="aanrecht") as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert (
        punten_per_naam(groep)["Maximering WOZ-punten tot 186 punten totaal"] == -29.5
    )
    # 119,75 punten in de andere rubrieken + 66,25 voor de WOZ-waarde = 186 punten
    assert groep.punten == 66.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
