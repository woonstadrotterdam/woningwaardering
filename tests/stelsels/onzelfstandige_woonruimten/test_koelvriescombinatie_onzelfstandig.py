"""Tests voor de waardering van een inbouwkoelvriescombinatie."""

from datetime import date
from decimal import Decimal

import pytest

from woningwaardering.stelsels.onzelfstandige_woonruimten import Keuken
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_koelvriescombinatie_telt_mee():
    eenheid = EenhedenEenheid(
        id="koelvriescombinatie",
        ruimten=[
            EenhedenRuimte(
                id="keuken",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.keuken,
                oppervlakte=9.0,
                bouwkundige_elementen=[
                    BouwkundigElementenBouwkundigElement(
                        id="aanrecht",
                        soort=Bouwkundigelementsoort.voorziening,
                        detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                        lengte=2500,
                    )
                ],
                installaties=[Installatiesoort.inbouw_koelvriescombinatie],
            )
        ],
    )
    groep = Keuken(peildatum=date(2026, 7, 1)).waardeer(eenheid)
    assert groep.punten == 7 + 1.75
    koelvries = sum(
        Decimal(str(w.punten))
        for w in groep.woningwaarderingen or []
        if w.criterium and w.criterium.id and "koelvriescombinatie" in w.criterium.id
    )
    assert koelvries == Decimal("1.75")
