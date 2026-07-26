"""Tests voor extra voorzieningen bij een drempelloze inrijdouche.

Bron: docs/implementatietoelichtingen/onzelfstandige-woonruimten.md §2.6.1 en §2.6.2
"""

from datetime import date

import pytest

from woningwaardering.stelsels.onzelfstandige_woonruimten import Sanitair
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)

PEILDATUM = date(2026, 7, 1)


def _doucheruimte_met_inrijdouche() -> EenhedenEenheid:
    return EenhedenEenheid(
        id="drempelloze_inrijdouche",
        ruimten=[
            EenhedenRuimte(
                id="doucheruimte",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.doucheruimte,
                naam="Doucheruimte",
                oppervlakte=6.0,
                installaties=[
                    Installatiesoort.drempelloze_inrijdouche,
                    Installatiesoort.wastafel,
                    Installatiesoort.handdoekenradiator,
                ],
            )
        ],
    )


def _punten_voor_segment(groep, segment: str) -> float:
    for waardering in groep.woningwaarderingen or []:
        if waardering.criterium and waardering.criterium.id:
            if segment in waardering.criterium.id:
                assert waardering.punten is not None
                return waardering.punten
    return 0.0


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_drempelloze_inrijdouche_extra_voorzieningen():
    """§2.6.2: drempelloze inrijdouche telt als douche voor extra voorzieningen.

    Verwacht: 3 (douche) + 1 (wastafel) + 0,75 (handdoekenradiator) = 4,75.
    """
    groep = Sanitair(peildatum=PEILDATUM).waardeer(_doucheruimte_met_inrijdouche())

    assert _punten_voor_segment(groep, "drempelloze_inrijdouche") == 3.0
    assert _punten_voor_segment(groep, "wastafel") == 1.0
    assert _punten_voor_segment(groep, "handdoekenradiator") == 0.75
    assert groep.punten == 4.75
