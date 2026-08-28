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


def test_cap_punten_geen_cap_bij_totaal_onder_187_kwartafronding():
    """#327: overige 100 + WOZ 86,5 → totaal 186,50 → geen cap."""
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    eenheid = EenhedenEenheid(id="test", bouwjaar=1980)
    overige_punten = Decimal("100")
    woz_punten = Decimal("86.5")
    totaal_punten_zonder_cap = utils.rond_af_op_kwart(overige_punten + woz_punten)

    assert totaal_punten_zonder_cap == Decimal("186.5")
    assert (
        svc._cap_punten(
            eenheid,
            woz_punten,
            overige_punten,
            WoningwaarderingResultatenWoningwaarderingResultaat(),
            totaal_punten_zonder_cap,
        )
        is None
    )


def test_cap_punten_wel_cap_boven_187_drempel():
    svc = PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1))
    eenheid = EenhedenEenheid(id="test", bouwjaar=1980)
    overige_punten = Decimal("134")
    woz_punten = Decimal("134")
    totaal_punten_zonder_cap = utils.rond_af_op_kwart(overige_punten + woz_punten)

    assert totaal_punten_zonder_cap >= Decimal("187")
    assert (
        svc._cap_punten(
            eenheid,
            woz_punten,
            overige_punten,
            WoningwaarderingResultatenWoningwaarderingResultaat(),
            totaal_punten_zonder_cap,
        )
        is not None
    )


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
    woz_punten_onafgerond = Decimal("82.33")

    svc._corrigeer_woz_punten(builder, eenheid, resultaat, woz_punten_onafgerond)

    segmenten = [w.segment for w in builder.alle_waarderingen()]
    assert "maximering_woz_punten" in segmenten
    assert "nieuwbouw_minimum_punten" not in segmenten
