"""Test voor de maximering van extra keukenvoorzieningen."""

from decimal import Decimal

import pytest

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.keuken.keuken import (
    _max_punten_voorzieningen,
    waardeer_keuken,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_keuken_max_extra_voorzieningen_op_basispunten():
    ruimte = EenhedenRuimte(
        id="keuken",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.keuken,
        oppervlakte=10,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                id="a1",
                soort=Bouwkundigelementsoort.voorziening,
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=900,
            ),
            BouwkundigElementenBouwkundigElement(
                id="a2",
                soort=Bouwkundigelementsoort.voorziening,
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=1500,
            ),
        ],
        installaties=[Installatiesoort.inbouw_koelkast] * 5,
    )
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
        Woningwaarderingstelselgroep.keuken,
    )
    waarderingen = waardeer_keuken(
        ruimte,
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
        waarderingsgroep_builder=builder,
    )
    assert _max_punten_voorzieningen(
        ruimte, Woningwaarderingstelsel.onzelfstandige_woonruimten
    ) == Decimal("4")
    assert sum(Decimal(str(w.punten)) for w in waarderingen if w.punten) == Decimal("8")
