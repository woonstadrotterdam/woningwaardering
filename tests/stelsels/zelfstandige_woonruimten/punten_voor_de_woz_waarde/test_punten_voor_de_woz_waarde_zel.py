"""Punten voor de WOZ-waarde, zelfstandige woonruimten (rubriek 11)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.input import (
    aanrecht,
    element,
    elementen,
    meergezinswoning_van_71_m2,
    ruimte,
)
from tests.utils import (
    aantal_per_bovenliggende,
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.vera.bvg.generated import (
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRenovatie,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Energielabel,
    Energieprestatiesoort,
    EnergieprestatiesoortReferentiedata,
    Energieprestatiestatus,
    Pandsoort,
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


def test_PuntenVoorDeWozWaarde_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PuntenVoorDeWozWaarde,
    )


# De berekening van onderdeel I en II


def test_punten_voor_de_woz_waarde_zijn_de_som_van_onderdeel_i_en_ii_afgerond_op_een_kwart_punt(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """De punten voor de WOZ-waarde zijn de som van onderdeel I en onderdeel II, afgerond op een kwart punt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2.
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
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een vastgestelde WOZ-waarde die lager is dan de minimum WOZ-waarde van € 85.806, wordt niet tot dat minimum verhoogd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.

    De package rekent met de meest recent vastgestelde WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.
    """
    # De meest recente WOZ-waarde (€ 79.999) is lager dan het minimum van € 85.806.
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=59999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=69999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=79999
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 22),
                einddatum=date(2028, 6, 22),
                label=Energielabel.c,
                waarde="1.67",
            )
        ],
        monumenten=[],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=3.59507,
                verwarmd=True,
                elementen=[aanrecht(2100)],
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=3.13436,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                    Bouwkundigelementdetailsoort.closetcombinatie,
                ),
            ),
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=21.4327, verwarmd=True),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    # De drie ruimten zijn samen 28,16 m², afgerond op 28 m².
    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 79999.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 28.0,
        "Factor II": 242.0,
    }
    # € 79.999 / € 15.329 = 5,22 en € 79.999 / 28 m² / € 242 = 11,81: samen 17,02,
    # afgerond op 17 punten.
    punten = punten_per_naam(groep)
    assert punten["Onderdeel I"] == 5.22
    assert punten["Onderdeel II"] == 11.81
    assert groep.punten == 17.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_woz_eenheid_zonder_vastgestelde_waarde_wordt_overgeslagen(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een WOZ-eenheid zonder vastgestelde waarde slaat de package over: zij rekent met de meest recente WOZ-waarde die wel is vastgesteld.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.
    """
    # De WOZ-eenheid van 1 januari 2025 heeft geen waarde, die van 2024 wel.
    eenheid = EenhedenEenheid(
        id="eenheid",
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=100000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=100000
            ),
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.

    Een woning gebouwd in 2015 tot en met 2019 die voor de rubrieken 1 tot en
    met 10 en 12 minstens 110 punten haalt, krijgt minimaal 40 punten voor de
    WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
    Bijlage I onder A, onderdeel 11.2.
    """
    # Een woning van 2016 zonder WOZ-waarde, zodat ook het minimum van 40 punten geldt.
    # De vaste kasten tellen mee in de 60 m²: hun oppervlakte komt bij de ruimte met de deur.
    eenheid = meergezinswoning_van_71_m2(bouwjaar=2016)

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
    # 5,06 + 5,34 + 29,60 = 40 punten
    assert punten_per_naam(groep) == {
        "Onderdeel I": 5.06,
        "Onderdeel II": 5.34,
        "Nieuwbouw: min. 40 punten": 29.6,
    }
    assert groep.punten == 40.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# De oppervlakte in onderdeel II


def test_onderdeel_ii_rekent_met_de_oppervlakte_van_vertrekken_overige_ruimten_en_parkeerplekken_type_i(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """In onderdeel II telt de oppervlakte mee van de vertrekken en overige ruimten uit rubriek 1 en 2 en van de parkeerplekken type I uit rubriek 10.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2; wettekst,
    Bijlage I onder A, onderdeel 11.1.

    Van een parkeerplek type I telt de oppervlakte gedeeld door het aantal
    adressen dat toegang heeft tot de parkeerplek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2.
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
                aantal=2,
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

    # 10 (woonkamer) + 10 (Toiletruimte1) + 2 x 20 / 4 adressen (Parkeerplek1) = 30 m²
    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 100000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 30.0,
        "Factor II": 242.0,
    }
    assert punten_per_naam(groep)["Onderdeel II"] == 13.77
    assert groep.punten == 20.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Kleine nieuwbouwwoningen in het COROP-gebied Amsterdam of Utrecht


def test_woning_tot_40_m2_gebouwd_in_2018_tot_en_met_2022_in_corop_gebied_amsterdam_krijgt_in_onderdeel_ii_het_lagere_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning tot 40 m² die in 2018 tot en met 2022 is gebouwd en in het COROP-gebied Amsterdam ligt, krijgt in onderdeel II het lagere kengetal van € 103.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6; wettekst,
    Bijlage I onder A, onderdeel 11.1.

    De package rekent met de meest recent vastgestelde WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.
    """
    # Onder de 40 m² en gebouwd in 2020, zodat het lagere kengetal geldt; woonplaatscode 3594 ligt in COROP-gebied Groot-Amsterdam.
    eenheid = EenhedenEenheid(
        bouwjaar=2020,
        adres=EenhedenEenheidadres(
            huisnummer="1",
            huisnummer_toevoeging="",
            postcode="1012LG",
            woonplaats=EenhedenWoonplaats(code="3594", naam="Amsterdam"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0363010012111931"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=300000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                # De soortcode is geen VERA-code (die is "EI"). De package
                # gebruikt deze energieprestatie daardoor niet en waardeert de
                # energieprestatie naar het bouwjaar.
                soort=EnergieprestatiesoortReferentiedata(
                    code="energie_index", naam="Energie-index"
                ),
                status=Energieprestatiestatus.definitief,
                label=Energielabel.c,
                waarde="1.2",
                begindatum=date(2020, 1, 1),
                einddatum=date(2030, 1, 1),
            )
        ],
        gebruiksoppervlakte=35,
        monumenten=[],
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=20.0, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=8.0,
                verwarmd=True,
                elementen=[aanrecht(1800)],
            ),
            ruimte(Ruimtedetailsoort.badkamer, oppervlakte=4.0, verwarmd=True),
            ruimte(Ruimtedetailsoort.toiletruimte, oppervlakte=3.0),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 310000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 35.0,
        "Factor II": 103.0,
    }
    # € 310.000 / 35 m² / € 103
    assert punten_per_naam(groep)["Onderdeel II"] == 85.99
    assert groep.punten == 106.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_woning_tot_40_m2_gebouwd_in_2018_tot_en_met_2022_in_corop_gebied_utrecht_krijgt_in_onderdeel_ii_het_lagere_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning tot 40 m² die in 2018 tot en met 2022 is gebouwd en in het COROP-gebied Utrecht ligt, krijgt in onderdeel II het lagere kengetal van € 103.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6; wettekst,
    Bijlage I onder A, onderdeel 11.1.

    De package rekent met de meest recent vastgestelde WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.
    """
    # Onder de 40 m² en gebouwd in 2021, zodat het lagere kengetal geldt; woonplaatscode 3295 ligt in COROP-gebied Utrecht.
    eenheid = EenhedenEenheid(
        bouwjaar=2021,
        adres=EenhedenEenheidadres(
            huisnummer="100",
            huisnummer_toevoeging="",
            postcode="3511AD",
            woonplaats=EenhedenWoonplaats(code="3295", naam="Utrecht"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0344010000000001"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=280000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=290000
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                # De soortcode is geen VERA-code (die is "EI"). De package
                # gebruikt deze energieprestatie daardoor niet en waardeert de
                # energieprestatie naar het bouwjaar.
                soort=EnergieprestatiesoortReferentiedata(
                    code="energie_index", naam="Energie-index"
                ),
                status=Energieprestatiestatus.definitief,
                label=Energielabel.c,
                waarde="1.2",
                begindatum=date(2021, 1, 1),
                einddatum=date(2031, 1, 1),
            )
        ],
        gebruiksoppervlakte=38,
        monumenten=[],
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=22.0, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=9.0,
                verwarmd=True,
                elementen=[aanrecht(2000)],
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=4.5,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                ),
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                oppervlakte=2.5,
                elementen=[element(Bouwkundigelementdetailsoort.closetcombinatie)],
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 290000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 38.0,
        "Factor II": 103.0,
    }
    # € 290.000 / 38 m² / € 103
    assert punten_per_naam(groep)["Onderdeel II"] == 74.09
    assert groep.punten == 93.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_woning_tot_40_m2_gebouwd_na_2022_in_corop_gebied_amsterdam_krijgt_in_onderdeel_ii_het_gewone_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning tot 40 m² in het COROP-gebied Amsterdam die na 2022 is gebouwd, krijgt in onderdeel II het gewone kengetal van € 242.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6; wettekst,
    Bijlage I onder A, onderdeel 11.1.

    De package rekent met de meest recent vastgestelde WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
    Bijlage I onder A, onderdeel 11.1.
    """
    # Onder de 40 m² maar na 2022 gebouwd, zodat het lagere kengetal niet geldt; woonplaatscode 3594 ligt in Amsterdam.
    eenheid = EenhedenEenheid(
        bouwjaar=2023,
        adres=EenhedenEenheidadres(
            huisnummer="2",
            huisnummer_toevoeging="",
            postcode="1012LG",
            woonplaats=EenhedenWoonplaats(code="3594", naam="Amsterdam"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0363010000000002"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=300000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                # De soortcode is geen VERA-code (die is "EI"). De package
                # gebruikt deze energieprestatie daardoor niet en waardeert de
                # energieprestatie naar het bouwjaar.
                soort=EnergieprestatiesoortReferentiedata(
                    code="energie_index", naam="Energie-index"
                ),
                status=Energieprestatiestatus.definitief,
                label=Energielabel.c,
                waarde="1.2",
                begindatum=date(2023, 1, 1),
                einddatum=date(2033, 1, 1),
            )
        ],
        gebruiksoppervlakte=35,
        monumenten=[],
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=20.0, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=8.0,
                verwarmd=True,
                elementen=[aanrecht(1800)],
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=4.0,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                ),
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                oppervlakte=3.0,
                elementen=[element(Bouwkundigelementdetailsoort.closetcombinatie)],
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 310000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 35.0,
        "Factor II": 242.0,
    }
    # € 310.000 / 35 m² / € 242
    assert punten_per_naam(groep)["Onderdeel II"] == 36.6
    assert groep.punten == 56.75
    vergelijk_met_testreferentie(eenheid, groep)


# Het minimum van 40 punten voor woningen uit 2015 tot en met 2019


def test_woning_gebouwd_in_2015_tot_en_met_2019_met_minstens_110_punten_krijgt_minimaal_40_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning gebouwd in 2015 tot en met 2019 die voor de rubrieken 1 tot en met 10 en 12 minstens 110 punten haalt, krijgt minimaal 40 punten voor de WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
    Bijlage I onder A, onderdeel 11.2.
    """
    # Een woning van 2016 met meer dan 110 punten voor rubriek 1 tot en met 10 en 12.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=2016,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=219999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=239999
            ),
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
    Bijlage I onder A, onderdeel 11.2.
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
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=219999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=239999
            ),
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
    ("renovatiedatum", "energieprestatie"),
    [
        pytest.param(
            date(2019, 1, 1),
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Energielabel.ap4,
                waarde="1.48",
            ),
            id="renovatie_2019_label_a4plus",
        ),
        pytest.param(
            date(2021, 1, 1),
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Energielabel.app,
                waarde="0.3",
            ),
            id="renovatie_2021_waarde_0_3",
        ),
    ],
)
def test_gerenoveerde_woning_gebouwd_in_2015_tot_en_met_2019_met_minstens_110_punten_krijgt_minimaal_40_punten(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    renovatiedatum,
    energieprestatie,
):
    """Een gerenoveerde woning gebouwd in 2015 tot en met 2019 die voor de rubrieken 1 tot en met 10 en 12 minstens 110 punten haalt, krijgt minimaal 40 punten voor de WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
    Bijlage I onder A, onderdeel 11.2.
    """
    # Een woning van 2016 met meer dan 110 punten; de renovatie verschilt per geval.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=2016,
        renovatie=EenhedenRenovatie(
            omschrijving="hoogniveau renovatie",
            datum=renovatiedatum,
            bedrag_investering=10000,
        ),
        energieprestaties=[energieprestatie],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=219999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=239999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=259999
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep)["Nieuwbouw: min. 40 punten"] == 5.13
    assert groep.punten == 40.0
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    "renovatiedatum",
    [
        pytest.param(date(2014, 12, 31), id="renovatie_eind_2014"),
        pytest.param(date(2022, 1, 1), id="renovatie_2022"),
    ],
)
def test_woning_gebouwd_voor_2015_met_renovatie_buiten_2015_tot_en_met_2019_krijgt_geen_minimum_van_40_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie, renovatiedatum
):
    """Een woning gebouwd voor 2015 die buiten 2015 tot en met 2019 is gerenoveerd, krijgt geen minimum van 40 punten voor de WOZ-waarde.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
    Bijlage I onder A, onderdeel 11.2.
    """
    # Een woning van 1912 met meer dan 110 punten, gerenoveerd buiten 2015-2019.
    eenheid = meergezinswoning_van_71_m2(
        bouwjaar=1912,
        renovatie=EenhedenRenovatie(
            omschrijving="hoogniveau renovatie",
            datum=renovatiedatum,
            bedrag_investering=10000,
        ),
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Energielabel.ap4,
                waarde="1.48",
            )
        ],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=219999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=239999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=259999
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert "Nieuwbouw: min. 40 punten" not in punten_per_naam(groep)
    assert groep.punten == 34.75
    vergelijk_met_testreferentie(eenheid, groep)


# De cap op de WOZ


def test_woz_punten_worden_beperkt_tot_33_procent_van_de_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """De punten voor de WOZ-waarde zijn niet meer dan 33 procent van de waardering van een woning die zonder die beperking 187 punten of meer heeft.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2;
    implementatietoelichting zelfstandige woonruimten, 2.11.7; wettekst, Bijlage
    I onder A, onderdeel 11.3.

    Bij de beperking wordt het aantal punten voor de WOZ-waarde naar beneden
    afgerond op hele punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2; wettekst,
    Bijlage I onder A, toelichting rubriek 11.
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
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=497000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=553900
            ),
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.7; wettekst,
    Bijlage I onder A, onderdeel 11.3.
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
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=597000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=653900
            ),
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
