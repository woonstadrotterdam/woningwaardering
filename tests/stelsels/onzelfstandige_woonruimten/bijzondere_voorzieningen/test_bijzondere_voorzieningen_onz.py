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


def test_zorgwoning_krijgt_35_procent_van_de_punten_van_de_rubrieken_1_tot_en_met_11_als_verhoging(
    bijzondere_voorzieningen,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een zorgwoning krijgt 35% van de punten van de rubrieken 1 tot en met 11 als verhoging.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12; wettekst,
    Bijlage I onder B, onderdeel 12.
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        # De doelgroep zorg maakt de eenheid een zorgwoning; de package
        # waardeert de rubrieken 1 tot en met 11 zelf.
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
    """De 10 punten voor een rijksmonument met een huurovereenkomst van vóór de inwerkingtreding van de Wet betaalbare huur tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12;
    implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
    artikel 8a, tweede lid; wettekst, Bijlage I onder B, onderdeel 12.

    Een rijksmonument krijgt in rubriek 4 geen minpunten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
    wettekst, Bijlage I onder B, onderdeel 4.2.
    """
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        # Artikel 8a geldt alleen bij een huurovereenkomst van vóór de Wet
        # betaalbare huur; het bouwjaar geeft zonder monument minpunten. De
        # package waardeert de rubrieken 1 tot en met 11 zelf.
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.2; wettekst,
    Bijlage I onder B, onderdeel 12.
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3; wettekst,
    Bijlage I onder B, onderdeel 12.

    Een garage van één adres krijgt in rubriek 10 geen punten; de laadpalen
    worden daarom in deze rubriek gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3; wettekst,
    Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B,
    toelichting, inleiding).
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
