"""Tests voor toiletten in een doucheruimte.

§2.6.1 [ZEL]: toiletten buiten toiletruimte of badkamer zijn n.v.t.
Een VERA-doucheruimte valt daaronder; douche en wastafel blijven wel meetellen.
"""

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    waardeer_sanitair,
)
from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _doucheruimte_met_toilet_douche_wastafel() -> EenhedenRuimte:
    return EenhedenRuimte(
        id="Space_doucheruimte_toilet",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.doucheruimte,
        naam="Doucheruimte",
        installaties=[
            Installatiesoort.staand_toilet,
            Installatiesoort.douche,
            Installatiesoort.wastafel,
        ],
    )


def test_toilet_in_doucheruimte_geen_keyerror():
    """Toilet in doucheruimte mag waardeer_sanitair niet laten crashen."""
    ruimte = _doucheruimte_met_toilet_douche_wastafel()
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.sanitair,
    )

    waarderingen = waardeer_sanitair(
        ruimte,
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=builder,
    )

    assert waarderingen


def test_toilet_in_doucheruimte_geen_toiletpunten():
    """§2.6.1: toilet buiten toiletruimte/badkamer → n.v.t. (0 punten)."""
    ruimte = _doucheruimte_met_toilet_douche_wastafel()
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.sanitair,
    )

    waarderingen = waardeer_sanitair(
        ruimte,
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=builder,
    )

    toilet_ids = {
        Installatiesoort.staand_toilet.name,
        Installatiesoort.hangend_toilet.name,
    }
    toilet_waarderingen = [
        w
        for w in waarderingen
        if w.criterium_id and w.criterium_id.split("__")[-1] in toilet_ids
    ]

    assert toilet_waarderingen == []


def test_douche_en_wastafel_in_doucheruimte_blijven_gewaardeerd():
    """Douche en wastafel in dezelfde doucheruimte blijven gewaardeerd."""
    ruimte = _doucheruimte_met_toilet_douche_wastafel()
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.sanitair,
    )

    waarderingen = waardeer_sanitair(
        ruimte,
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        waarderingsgroep_builder=builder,
    )

    punten_per_soort = {
        w.criterium_id.split("__")[-1]: w.punten
        for w in waarderingen
        if w.criterium_id and w.punten is not None
    }

    assert punten_per_soort.get(Installatiesoort.douche.name) == 4.0
    assert punten_per_soort.get(Installatiesoort.wastafel.name) == 1.0
