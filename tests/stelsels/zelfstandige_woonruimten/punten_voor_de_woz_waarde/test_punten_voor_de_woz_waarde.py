from datetime import date
from decimal import Decimal

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde.punten_voor_de_woz_waarde import (
    PuntenVoorDeWozWaarde,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _maak_resultaat_met_overige_punten(
    *groep_punten: tuple[Woningwaarderingstelselgroep, float],
) -> WoningwaarderingResultatenWoningwaarderingResultaat:
    return WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[
            WoningwaarderingResultatenWoningwaarderingGroep(
                criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                    stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
                    stelselgroep=stelselgroep,
                ),
                punten=punten,
            )
            for stelselgroep, punten in groep_punten
        ]
    )


def _corrigeer(
    overige_punten: float,
    woz_punten: Decimal,
    *,
    bouwjaar: int = 1980,
) -> WaarderingsgroepBuilder:
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    eenheid = EenhedenEenheid(id="test", bouwjaar=bouwjaar)
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, overige_punten),
    )
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )
    svc._corrigeer_woz_punten(builder, eenheid, resultaat, woz_punten)
    return builder


def _maximering(builder: WaarderingsgroepBuilder) -> WaarderingBuilder | None:
    return next(
        (
            w
            for w in builder.alle_waarderingen()
            if w.segment == "maximering_woz_punten"
        ),
        None,
    )


def test_corrigeer_woz_punten_geen_cap_bij_woningwaardering_onder_187():
    """11.3: 100 + 86,25 → 186,25 → woningwaardering 186 → geen cap."""
    overige = Decimal("100")
    woz = Decimal("86.25")
    assert utils.rond_af(overige + utils.rond_af_op_kwart(woz), 0) == Decimal("186")
    assert _maximering(_corrigeer(100.0, woz)) is None


def test_corrigeer_woz_punten_186_vloer_bij_186_5():
    """#327: WOZ-rubriek op kwartpunten, 187-toets op de woningwaardering.

    100 + 86,5 = 186,50 → 2.1.5 maakt 187 → cap wél, vloer 186.
    """
    woz = Decimal("86.5")
    assert utils.rond_af_op_kwart(woz) == Decimal("86.5")
    assert utils.rond_af(Decimal("100") + woz, 0) == Decimal("187")

    maximering = _maximering(_corrigeer(100.0, woz))
    assert maximering is not None
    assert maximering.naam == "Maximering WOZ-punten tot 186 punten totaal"
    assert Decimal(str(maximering.punten)) == Decimal("-0.5")


def test_corrigeer_woz_punten_rond_woz_niet_apart_op_hele_punten_af():
    """#327 blijft gelden voor de WOZ-rubriek: niet `rond_af(woz, 0)` vóór de som.

    100 + 86,4: op hele punten alleen de WOZ → 186 (geen cap); rubriek op kwart
    plus woningwaardering → 186,50 → 187 (wel cap, vloer 186).
    """
    woz = Decimal("86.4")
    assert utils.rond_af(woz, 0) == Decimal("86")
    assert utils.rond_af_op_kwart(woz) == Decimal("86.5")
    assert utils.rond_af(Decimal("100") + Decimal("86.5"), 0) == Decimal("187")

    maximering = _maximering(_corrigeer(100.0, woz))
    assert maximering is not None
    assert maximering.naam == "Maximering WOZ-punten tot 186 punten totaal"


def test_corrigeer_woz_punten_33_procent_boven_187():
    maximering = _maximering(_corrigeer(134.0, Decimal("134")))
    assert maximering is not None
    assert maximering.naam == "Maximering WOZ-punten tot 33% van totaal"


def test_cap_punten_alleen_33_procent():
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    assert svc._cap_punten(Decimal("134"), Decimal("134")) is not None
    assert svc._cap_punten(Decimal("10"), Decimal("100")) is None


def test_corrigeer_woz_punten_cap_bij_nieuwbouw_zonder_minimum():
    """#326: nieuwbouw 2015-2019 met ≥110 punten maar WOZ > 40 → cap wél toepassen."""
    builder = _corrigeer(135.75, Decimal("82.33"), bouwjaar=2016)
    segmenten = [w.segment for w in builder.alle_waarderingen()]
    assert "maximering_woz_punten" in segmenten
    assert "nieuwbouw_minimum_punten" not in segmenten
