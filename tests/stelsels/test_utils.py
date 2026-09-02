from decimal import Decimal

import pytest

from woningwaardering.stelsels import utils
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort


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


def test_som_effectieve_aantal_waarderingen_subtotaal_zonder_aantal() -> None:
    """Ruimteregels onder gedeeld-met plus een sibling-subtotaal zonder aantal.

    Het subtotaal draagt alleen punten. De helper telt werkelijke m² na delen.
    Zie #403.
    """
    prive = "oppervlakte_van_overige_ruimten__prive"
    gedeeld = (
        "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten"
    )
    waarderingen = [
        _waardering(criterium_id=prive),
        _waardering(
            criterium_id=f"{prive}__berging",
            aantal=10.4,
            bovenliggende_id=prive,
        ),
        _waardering(criterium_id=gedeeld),
        _waardering(
            criterium_id=f"{gedeeld}__zolder",
            aantal=40.4,
            bovenliggende_id=gedeeld,
        ),
        WoningwaarderingResultatenWoningwaardering(
            punten=15.75,
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                id="oppervlakte_van_overige_ruimten__subtotaal",
            ),
        ),
    ]
    assert utils.som_effectieve_aantal_waarderingen(waarderingen) == Decimal("20.50")


def test_oppervlakte_inclusief_verbonden_kasten():
    ruimte = EenhedenRuimte(
        oppervlakte=3.5,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        verbonden_ruimten=[
            EenhedenRuimte(oppervlakte=0.5, detail_soort=Ruimtedetailsoort.kast)
        ],
    )
    assert utils.oppervlakte_inclusief_verbonden_kasten(ruimte) == Decimal("4.0")


def test_classificeer_ruimte_telt_kast_mee_bij_vertrekdrempel():
    ruimte = EenhedenRuimte(
        id="slaapkamer",
        naam="Slaapkamer",
        oppervlakte=3.5,
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        verbonden_ruimten=[
            EenhedenRuimte(oppervlakte=0.5, detail_soort=Ruimtedetailsoort.kast)
        ],
    )
    assert utils.classificeer_ruimte(ruimte) == Ruimtesoort.vertrek


def test_verbonden_kast_wordt_na_naamhelper_niet_dubbel_geteld():
    ruimte = EenhedenRuimte(
        id="slaapkamer",
        naam="Slaapkamer",
        oppervlakte=3.5,
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        verbonden_ruimten=[
            EenhedenRuimte(oppervlakte=0.5, detail_soort=Ruimtedetailsoort.kast)
        ],
    )

    criterium_naam = utils.voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    assert criterium_naam == "Slaapkamer (+1 kast)"
    assert ruimte.oppervlakte == 3.5
    assert utils.oppervlakte_inclusief_verbonden_kasten(ruimte) == Decimal("4.0")
    assert utils.classificeer_ruimte(ruimte) == Ruimtesoort.vertrek


@pytest.mark.parametrize(
    "aantal_adressen, aantal_onzelfstandige_woonruimten, verwacht_prive",
    [
        (1, 1, True),
        (0, 0, True),
        (None, None, True),
        (2, 1, False),
        (1, 2, False),
        (3, 4, False),
    ],
)
def test_is_prive(
    aantal_adressen, aantal_onzelfstandige_woonruimten, verwacht_prive
) -> None:
    ruimte = EenhedenRuimte(
        gedeeldMetAantalAdressen=aantal_adressen,
        gedeeldMetAantalOnzelfstandigeWoonruimten=aantal_onzelfstandige_woonruimten,
    )
    assert utils.is_prive(ruimte) is verwacht_prive


def test_toegerekende_oppervlakte_prive() -> None:
    ruimte = EenhedenRuimte(oppervlakte=10.4, detail_soort=Ruimtedetailsoort.slaapkamer)
    assert utils.toegerekende_oppervlakte(ruimte) == Decimal("10.40")


def test_toegerekende_oppervlakte_gedeeld() -> None:
    ruimte = EenhedenRuimte(
        oppervlakte=40.4,
        detail_soort=Ruimtedetailsoort.woonkamer,
        gedeeld_met_aantal_onzelfstandige_woonruimten=4,
    )
    assert utils.toegerekende_oppervlakte(ruimte) == Decimal("10.10")
