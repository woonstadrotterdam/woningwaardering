"""Tests voor de waardering van een inbouwkoelvriescombinatie."""

from decimal import Decimal

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.keuken.keuken import waardeer_keuken
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
    Referentiedata,
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

AANRECHT_PUNTEN = 7


def _keuken_met_installaties(installaties: list[Referentiedata]) -> EenhedenRuimte:
    return EenhedenRuimte(
        id="keuken",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.keuken,
        naam="Keuken",
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                id="aanrecht",
                soort=Bouwkundigelementsoort.voorziening,
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=2500,
            )
        ],
        installaties=installaties,
    )


def _waardeer(installaties: list[Referentiedata]):
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.keuken,
    )
    return waardeer_keuken(
        _keuken_met_installaties(installaties),
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=builder,
    )


def _punten_voor_installatie(waarderingen, installatie: Referentiedata) -> Decimal:
    suffix = f"extra_voorziening_{installatie.name}"
    for waardering in waarderingen:
        if waardering.criterium_id and waardering.criterium_id.endswith(suffix):
            assert waardering.punten is not None
            return Decimal(str(waardering.punten))
    return Decimal("0")


def test_koelvriescombinatie_telt_als_twee_voorzieningen():
    waarderingen = _waardeer([Installatiesoort.inbouw_koelvriescombinatie])
    assert _punten_voor_installatie(
        waarderingen, Installatiesoort.inbouw_koelvriescombinatie
    ) == Decimal("1.75")
