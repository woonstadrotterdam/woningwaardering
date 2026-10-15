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
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen import (
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


def test_BijzondereVoorzieningen_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        BijzondereVoorzieningen,
    )


# Zorgwoning


def test_zorgwoning_krijgt_35_procent_van_de_punten_van_de_rubrieken_1_tot_en_met_11_1_als_verhoging(
    bijzondere_voorzieningen,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een zorgwoning krijgt 35% van de punten van de rubrieken 1 tot en met 11.1 als verhoging.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12; wettekst,
    Bijlage I onder A, onderdeel 12.
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        # De doelgroep zorg maakt de eenheid een zorgwoning; de package
        # waardeert de rubrieken 1 tot en met 11.1 zelf.
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
    """De 50 punten voor een rijksmonument met een huurovereenkomst van vóór de inwerkingtreding van de Wet betaalbare huur tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12;
    implementatietoelichting zelfstandige woonruimten, 2.13.4; wettekst, artikel
    8a, tweede lid; wettekst, Bijlage I onder A, onderdeel 12.
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        # Artikel 8a geldt alleen bij een huurovereenkomst van vóór de Wet
        # betaalbare huur. De package waardeert de rubrieken 1 tot en met 11.1
        # zelf.
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


def test_punten_van_het_minimum_voor_nieuwbouw_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning(
    bijzondere_voorzieningen,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """De punten waarmee het minimum voor nieuwbouw de punten voor de WOZ-waarde aanvult, tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12; wettekst,
    Bijlage I onder A, onderdeel 12.

    Het minimum voor nieuwbouw is 40 punten voor de WOZ-waarde bij een woning
    uit 2015 tot en met 2019 met minimaal 110 punten in de andere rubrieken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
    Bijlage I onder A, onderdeel 11.2.
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        # Het bouwjaar en de grote woonkamer maken de woning nieuwbouw met genoeg
        # punten voor het minimum. De package waardeert de rubrieken 1 tot en met
        # 11 zelf.
        bouwjaar=2018,
        doelgroep=Doelgroep.zorg,
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=100.0,
                verwarmd=True,
                verkoeld=False,
            )
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = bijzondere_voorzieningen.waardeer(eenheid.model_copy())

    # De rubrieken 1 tot en met 11.1 geven samen 108,25 punten: 100 voor de
    # woonkamer (rubriek 1), 2 voor het verwarmde vertrek (rubriek 3), 5
    # minpunten omdat een buitenruimte ontbreekt (rubriek 8), 3 voor de
    # gemeenschappelijke ruimten van een zorgwoning (rubriek 9) en 8,25 voor de
    # minimum WOZ-waarde (rubriek 11.1). 35% daarvan is 37,89 punten; op een kwart
    # punt afgerond is dat 38. Met het minimum voor nieuwbouw had rubriek 11 40
    # punten gekregen en was het 35% van 140 punten geweest: 49 punten.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 38.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Aanbelfunctie


def test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.2; wettekst,
    Bijlage I onder A, onderdeel 12.
    """
    eenheid = EenhedenEenheid(
        id="aanbelfunctie",
        # Zonder voordeur in de input: de package controleert niet of de
        # voordeur vanuit de woning kan worden geopend.
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


def test_laadpaal_bij_een_garage_van_een_adres_krijgt_2_punten(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Een laadpaal bij een garage van één adres krijgt 2 punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3; wettekst,
    Bijlage I onder A, onderdeel 12.

    Een garage van één adres krijgt in rubriek 10 geen punten; de laadpalen
    worden daarom in deze rubriek gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3; wettekst,
    Bijlage I onder A, toelichting rubriek 10.
    """
    eenheid = EenhedenEenheid(
        id="2 laadpalen",
        # De garage is van één adres, zodat ze in rubriek 10 geen punten krijgt.
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
    # 2 laadpalen x 2 punten, niet gedeeld
    assert punten_per_bovenliggende(groep) == {"Privé": {"Laadpalen": 4.0}}
    vergelijk_met_testreferentie(eenheid, groep)
