"""Bijzondere voorzieningen, onzelfstandige woonruimten (rubriek 12)."""

from datetime import date

import pytest

from tests.input import elementen, ruimte, zorgwoning_van_71_m2
from tests.utils import (
    aantal_per_naam,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    BijzondereVoorzieningen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Eenheidmonument,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def bijzondere_voorzieningen(peildatum):
    return BijzondereVoorzieningen(peildatum=peildatum)


# Zorgwoning


def test_zorgwoning_krijgt_35_procent_van_de_punten_van_de_rubrieken_1_tot_en_met_11_als_verhoging(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Een zorgwoning krijgt 35% van de punten van de rubrieken 1 tot en met 11 als verhoging.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.12
    - wettekst, Bijlage I onder B, onderdeel 12
    """
    eenheid = zorgwoning_van_71_m2(bouwjaar=1960)

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = bijzondere_voorzieningen.waardeer(eenheid)

    # 35% van 92,75 punten, afgerond op een kwart punt.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 32.5}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_10_punten_voor_een_rijksmonument_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """De 10 punten voor een rijksmonument met een huurovereenkomst van vóór de inwerkingtreding van de Wet betaalbare huur tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.12
    - implementatietoelichting onzelfstandige woonruimten, 2.14.4
    - wettekst, artikel 8a, tweede lid
    - wettekst, Bijlage I onder B, onderdeel 12
    """
    # Artikel 8a geldt alleen bij een huurovereenkomst van vóór de Wet betaalbare huur.
    eenheid = zorgwoning_van_71_m2(
        bouwjaar=1960,
        monumenten=[Eenheidmonument.rijksmonument],
        datum_afsluiten_huurovereenkomst=date(2024, 1, 1),
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        groep = bijzondere_voorzieningen.waardeer(eenheid)

    # 35% van 101,75 punten, afgerond op een kwart punt.
    assert punten_per_naam(groep) == {"Zorgwoning 35% puntenverhoging": 35.5}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Aanbelfunctie


def test_aanbelfunctie_met_video_en_audioverbinding_krijgt_0_25_punt(
    bijzondere_voorzieningen, vergelijk_met_testreferentie
):
    """Een aanbelfunctie met video- en audioverbinding krijgt 0,25 punt.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.12.2
    - wettekst, Bijlage I onder B, onderdeel 12
    """
    eenheid = EenhedenEenheid(
        id="aanbelfunctie",
        # Zonder voordeur: de package controleert niet of de voordeur vanuit de woning opengaat.
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.aanbelfunctie_met_video_en_audioverbinding,
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.12.3
    - wettekst, Bijlage I onder B, onderdeel 12

    Een garage van één adres krijgt in rubriek 10 geen punten; de laadpalen
    worden daarom in deze rubriek gewaardeerd.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.12.3
    - wettekst, Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B, toelichting, inleiding)
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
            )
        ],
    )

    groep = bijzondere_voorzieningen.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Laadpalen": 2.0}
    # 2 laadpalen x 2 punten, niet gedeeld
    assert punten_per_bovenliggende(groep) == {"Privé": {"Laadpalen": 4.0}}
    vergelijk_met_testreferentie(eenheid, groep)
