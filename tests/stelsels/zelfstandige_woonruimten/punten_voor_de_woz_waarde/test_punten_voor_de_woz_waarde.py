from datetime import date
from decimal import Decimal

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
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


def _cap_punten(woz_punten: Decimal, overige_punten: Decimal) -> Decimal | None:
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    eenheid = EenhedenEenheid(id="test", bouwjaar=1980)
    return svc._cap_punten(
        eenheid,
        woz_punten,
        overige_punten,
        WoningwaarderingResultatenWoningwaarderingResultaat(),
    )


def test_cap_punten_geen_cap_bij_woningwaardering_onder_187():
    """11.3: 100 + 86,25 → 186,25 → woningwaardering 186 → geen cap."""
    overige = Decimal("100")
    woz = Decimal("86.25")
    assert utils.rond_af(overige + utils.rond_af_op_kwart(woz), 0) == Decimal("186")
    assert _cap_punten(woz, overige) is None


def test_cap_punten_wel_cap_bij_186_5_naar_187():
    """#327: WOZ-rubriek op kwartpunten, 187-toets op de woningwaardering.

    100 + 86,5 = 186,50 → 2.1.5 maakt 187 → cap wél. Niet: 186,50 < 187 dus geen cap.
    """
    overige = Decimal("100")
    woz = Decimal("86.5")
    assert utils.rond_af_op_kwart(woz) == Decimal("86.5")
    assert utils.rond_af(overige + woz, 0) == Decimal("187")
    assert _cap_punten(woz, overige) is not None


def test_cap_punten_rond_woz_niet_apart_op_hele_punten_af():
    """#327 blijft gelden voor de WOZ-rubriek: niet `rond_af(woz, 0)` vóór de som.

    100 + 86,4: op hele punten alleen de WOZ → 186 (geen cap); rubriek op kwart
    plus woningwaardering → 186,50 → 187 (wel cap).
    """
    overige = Decimal("100")
    woz = Decimal("86.4")
    assert utils.rond_af(woz, 0) == Decimal("86")
    assert utils.rond_af_op_kwart(woz) == Decimal("86.5")
    assert utils.rond_af(overige + Decimal("86.5"), 0) == Decimal("187")
    assert _cap_punten(woz, overige) is not None


def test_cap_punten_wel_cap_boven_187_drempel():
    assert _cap_punten(Decimal("134"), Decimal("134")) is not None


def test_corrigeer_woz_punten_186_vloer_bij_186_5():
    """11.3: 186,50 zonder cap wordt 187, cap trekt onder 187, vloer is 186."""
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    eenheid = EenhedenEenheid(id="test", bouwjaar=1980)
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 100.0),
    )
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )

    svc._corrigeer_woz_punten(builder, eenheid, resultaat, Decimal("86.5"))

    maximering = next(
        w for w in builder.alle_waarderingen() if w.segment == "maximering_woz_punten"
    )
    assert maximering.naam == "Maximering WOZ-punten tot 186 punten totaal"
    assert Decimal(str(maximering.punten)) == Decimal("-0.5")


def test_corrigeer_woz_punten_cap_bij_nieuwbouw_zonder_minimum():
    """#326: nieuwbouw 2015-2019 met ≥110 punten maar WOZ > 40 → cap wél toepassen."""
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    eenheid = EenhedenEenheid(id="test", bouwjaar=2016)
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 60.0),
        (Woningwaarderingstelselgroep.keuken, 55.0),
        (Woningwaarderingstelselgroep.sanitair, 20.75),
    )
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )

    svc._corrigeer_woz_punten(builder, eenheid, resultaat, Decimal("82.33"))

    segmenten = [w.segment for w in builder.alle_waarderingen()]
    assert "maximering_woz_punten" in segmenten
    assert "nieuwbouw_minimum_punten" not in segmenten
