from decimal import Decimal

from woningwaardering.stelsels import utils
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)


def _waardering(
    *,
    criterium_id: str,
    aantal: float | None = None,
    bovenliggende_id: str | None = None,
) -> WoningwaarderingResultatenWoningwaardering:
    bovenliggende = None
    if bovenliggende_id is not None:
        bovenliggende = WoningwaarderingCriteriumSleutels(id=bovenliggende_id)
    return WoningwaarderingResultatenWoningwaardering(
        aantal=aantal,
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            id=criterium_id,
            bovenliggende_criterium=bovenliggende,
        ),
    )


def test_som_effectieve_aantal_waarderingen_een_gedeeld_met_laag() -> None:
    parent_id = "oppervlakte_van_vertrekken__gedeeld_met_3_onzelfstandige_woonruimten"
    waarderingen = [
        _waardering(criterium_id=parent_id),
        _waardering(
            criterium_id=f"{parent_id}__Space_1",
            aantal=10.0,
            bovenliggende_id=parent_id,
        ),
    ]
    assert utils.som_effectieve_aantal_waarderingen(waarderingen) == Decimal("3.33")


def test_som_effectieve_aantal_waarderingen_twee_gedeeld_met_lagen() -> None:
    parent_id = (
        "gemeenschappelijke_parkeerruimten__"
        "gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
    )
    waarderingen = [
        _waardering(
            criterium_id=(
                "gemeenschappelijke_parkeerruimten__"
                "gedeeld_met_4_onzelfstandige_woonruimten"
            )
        ),
        _waardering(
            criterium_id=parent_id,
            bovenliggende_id=(
                "gemeenschappelijke_parkeerruimten__"
                "gedeeld_met_4_onzelfstandige_woonruimten"
            ),
        ),
        _waardering(
            criterium_id=f"{parent_id}__1",
            aantal=40.0,
            bovenliggende_id=parent_id,
        ),
    ]
    assert utils.som_effectieve_aantal_waarderingen(waarderingen) == Decimal("1.00")
