import warnings

import pytest

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.gemeenschappelijke_parkeerruimten import (
    waardeer_gemeenschappelijke_parkeerruimte,
    wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _ruimte(
    id: str,
    detail_soort=Ruimtedetailsoort.carport,
    oppervlakte: float | None = 15.0,
    gedeeld_met_aantal_adressen: int | None = None,
    gedeeld_met_aantal_onzelfstandige_woonruimten: int | None = None,
    laadpaal: bool = False,
) -> EenhedenRuimte:
    return EenhedenRuimte(
        id=id,
        naam=id,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        aantal=1,
        gedeeld_met_aantal_adressen=gedeeld_met_aantal_adressen,
        gedeeld_met_aantal_onzelfstandige_woonruimten=gedeeld_met_aantal_onzelfstandige_woonruimten,
        bouwkundige_elementen=(
            [
                BouwkundigElementenBouwkundigElement(
                    id=f"{id}_laadpaal",
                    detail_soort=Bouwkundigelementdetailsoort.laadpaal,
                )
            ]
            if laadpaal
            else []
        ),
    )


def _punten_in_rubriek_10(ruimte: EenhedenRuimte) -> float:
    """Waardeer de ruimte in rubriek 10 en tel de toegekende punten op."""
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
        stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,
    )
    with warnings.catch_warnings():
        # Ontbrekende detailsoort of oppervlakte levert een UserWarning op. Die
        # semantiek wordt elders getest; hier gaat het alleen om het puntenresultaat.
        warnings.simplefilter("ignore", UserWarning)
        waardeer_gemeenschappelijke_parkeerruimte(
            ruimte, waarderingsgroep_builder=waarderingsgroep_builder
        )
    return sum(
        float(waardering.punten or 0)
        for waardering in waarderingsgroep_builder.alle_waarderingen()
    )


@pytest.mark.parametrize(
    "ruimte",
    [
        _ruimte("carport_zonder_gedeeld_met_aantal_adressen"),
        _ruimte("carport_prive", gedeeld_met_aantal_adressen=1),
        _ruimte("carport_gedeeld_met_2_adressen", gedeeld_met_aantal_adressen=2),
        _ruimte("carport_met_laadpaal", laadpaal=True),
        _ruimte(
            "carport_gedeeld_met_4_onzelfstandige_woonruimten",
            gedeeld_met_aantal_onzelfstandige_woonruimten=4,
        ),
        _ruimte("carport_precies_12m2", oppervlakte=12.0),
        _ruimte("carport_onder_12m2", oppervlakte=11.99),
        _ruimte("carport_zonder_oppervlakte", oppervlakte=None),
        _ruimte("ruimte_zonder_detailsoort", detail_soort=None),
        _ruimte(
            "generieke_parkeerplaats", detail_soort=Ruimtedetailsoort.parkeerplaats
        ),
        _ruimte(
            "vervallen_parkeergarage_detailsoort",
            detail_soort=Ruimtedetailsoort.parkeergarage_niet_specifieke_plek,
        ),
        _ruimte(
            "inpandige_afgesloten_parkeergarage",
            detail_soort=Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
        ),
        _ruimte(
            "parkeerplek_buiten_behorend_bij_complex",
            detail_soort=Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
        ),
        _ruimte("woonkamer", detail_soort=Ruimtedetailsoort.woonkamer),
    ],
)
def test_wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten_volgt_de_waardering(
    ruimte: EenhedenRuimte,
) -> None:
    """``wordt_gewaardeerd_…`` moet exact aangeven of rubriek 10 punten toekent.

    Rubriek 12 slaat de laadpaalpunten voor onzelfstandige woonruimten over wanneer
    deze predicate ``True`` teruggeeft (2.12.3), omdat rubriek 10 die punten dan zelf
    al toekent (2.10.5). Loopt de predicate uit de pas met
    ``waardeer_gemeenschappelijke_parkeerruimte``, dan verdwijnen laadpaalpunten of
    worden ze dubbel geteld. Deze test legt die koppeling vast.

    De predicate wordt alleen gebruikt voor onzelfstandige woonruimten; wordt daar een
    stelsel of voorwaarde aan toegevoegd, dan hoort die hier meegenomen te worden.
    """
    assert wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(ruimte) == (
        _punten_in_rubriek_10(ruimte) > 0
    )
