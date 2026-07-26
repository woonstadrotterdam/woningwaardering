"""Tests voor verbonden kasten in gemeenschappelijke ruimten."""

from datetime import date

import pytest

from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen import (
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort

PEILDATUM = date(2026, 7, 1)


def _kast(oppervlakte: float) -> EenhedenRuimte:
    return EenhedenRuimte(
        id="kast",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.kast,
        naam="Kast",
        oppervlakte=oppervlakte,
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_gemeenschappelijk_vertrek_met_kast() -> None:
    eenheid = EenhedenEenheid(
        id="gemeenschappelijk_vertrek_kast",
        ruimten=[
            EenhedenRuimte(
                id="woonkamer",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.woonkamer,
                naam="Woonkamer",
                oppervlakte=10.0,
                gedeeld_met_aantal_adressen=2,
                verbonden_ruimten=[_kast(2.0)],
            )
        ],
    )

    groep = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=PEILDATUM
    ).waardeer(eenheid)

    assert groep.punten == 6.0


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_gemeenschappelijke_berging_met_kast_boven_drempel() -> None:
    eenheid = EenhedenEenheid(
        id="gemeenschappelijke_berging_kast",
        ruimten=[
            EenhedenRuimte(
                id="berging",
                soort=Ruimtesoort.overige_ruimten,
                detail_soort=Ruimtedetailsoort.berging,
                naam="Berging",
                oppervlakte=8.0,
                gedeeld_met_aantal_adressen=2,
                verbonden_ruimten=[_kast(2.0)],
            )
        ],
    )

    groep = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=PEILDATUM
    ).waardeer(eenheid)

    assert groep.punten == 3.75


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_gemeenschappelijke_berging_onder_drempel_zonder_kast() -> None:
    eenheid = EenhedenEenheid(
        id="gemeenschappelijke_berging_te_klein",
        ruimten=[
            EenhedenRuimte(
                id="berging",
                soort=Ruimtesoort.overige_ruimten,
                detail_soort=Ruimtedetailsoort.berging,
                naam="Berging",
                oppervlakte=3.0,
                gedeeld_met_aantal_adressen=2,
            )
        ],
    )

    groep = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=PEILDATUM
    ).waardeer(eenheid)

    assert groep.punten == 0.0


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_gemeenschappelijke_berging_boven_drempel_met_kast() -> None:
    eenheid = EenhedenEenheid(
        id="gemeenschappelijke_berging_met_kast",
        ruimten=[
            EenhedenRuimte(
                id="berging",
                soort=Ruimtesoort.overige_ruimten,
                detail_soort=Ruimtedetailsoort.berging,
                naam="Berging",
                oppervlakte=3.0,
                gedeeld_met_aantal_adressen=2,
                verbonden_ruimten=[_kast(2.0)],
            )
        ],
    )

    groep = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=PEILDATUM
    ).waardeer(eenheid)

    assert groep.punten == 2.0
