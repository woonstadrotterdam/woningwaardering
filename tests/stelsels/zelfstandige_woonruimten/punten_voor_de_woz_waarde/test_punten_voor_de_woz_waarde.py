from decimal import Decimal

import pytest

from tests.input import element, ruimte
from tests.peildatum import REFERENTIE_PEILDATUM
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
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Ruimtedetailsoort,
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
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=REFERENTIE_PEILDATUM)
    eenheid = EenhedenEenheid(id="test", bouwjaar=1980)
    return stelselgroep._cap_punten(eenheid, woz_punten, overige_punten)


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
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=REFERENTIE_PEILDATUM)
    eenheid = EenhedenEenheid(id="test", bouwjaar=1980)
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 100.0),
    )
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )

    stelselgroep._corrigeer_woz_punten(builder, eenheid, resultaat, Decimal("86.5"))

    maximering = next(
        w for w in builder.alle_waarderingen() if w.segment == "maximering_woz_punten"
    )
    assert maximering.naam == "Maximering WOZ-punten tot 186 punten totaal"
    assert Decimal(str(maximering.punten)) == Decimal("-0.5")


def test_corrigeer_woz_punten_cap_bij_nieuwbouw_zonder_minimum():
    """#326: nieuwbouw 2015-2019 met ≥110 punten maar WOZ > 40 → cap wél toepassen."""
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=REFERENTIE_PEILDATUM)
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

    stelselgroep._corrigeer_woz_punten(builder, eenheid, resultaat, Decimal("82.33"))

    segmenten = [w.segment for w in builder.alle_waarderingen()]
    assert "maximering_woz_punten" in segmenten
    assert "nieuwbouw_minimum_punten" not in segmenten


@pytest.mark.parametrize(
    ("overige_punten", "verwacht_minimum"),
    [
        pytest.param(110.0, Decimal("40"), id="precies_110_punten"),
        pytest.param(109.75, Decimal("0"), id="een_kwart_punt_onder_110_punten"),
    ],
)
def test_minimum_van_40_punten_geldt_vanaf_110_punten_voor_de_rubrieken_1_tot_en_met_10_en_12(
    overige_punten, verwacht_minimum
):
    """Het minimum van 40 punten voor de WOZ-waarde geldt vanaf 110 punten voor de rubrieken 1 tot en met 10 en 12.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=REFERENTIE_PEILDATUM)
    eenheid = EenhedenEenheid(id="test", bouwjaar=2016)
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 60.0),
        (Woningwaarderingstelselgroep.keuken, 30.0),
        (Woningwaarderingstelselgroep.sanitair, overige_punten - 90.0),
    )

    assert (
        stelselgroep._bereken_minimum_punten_nieuwbouw(
            # Zonder WOZ-punten: het minimum hangt hier alleen van rubriek 1-10 af.
            eenheid,
            resultaat,
            Decimal("0"),
        )
        == verwacht_minimum
    )


@pytest.mark.parametrize(
    ("woz_punten", "verwacht_minimum"),
    [
        pytest.param(Decimal("27.5"), Decimal("40"), id="met_woz_punten_110_of_meer"),
        pytest.param(Decimal("0"), Decimal("0"), id="zonder_woz_punten_onder_110"),
    ],
)
def test_de_verhoging_van_een_zorgwoning_in_de_110_puntentoets_rekent_over_de_rubrieken_1_tot_en_met_11_1(
    woz_punten, verwacht_minimum
):
    """De 35%-verhoging van een zorgwoning telt mee in de 110-puntentoets van het nieuwbouwminimum en rekent over de rubrieken 1 tot en met 11.1.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    - wettekst, Bijlage I onder A, onderdeel 12
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=REFERENTIE_PEILDATUM)
    # Een zorgwoning uit 2016 met 80 punten voor rubriek 1-10.
    eenheid = EenhedenEenheid(id="test", bouwjaar=2016, doelgroep=Doelgroep.zorg)
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 80.0),
    )

    # Met WOZ-punten: 80 + 35% × (80 + 27,5) = 80 + 37,75 = 117,75, dus minimum.
    # Zonder WOZ-punten: 80 + 35% × 80 = 80 + 28 = 108, dus geen minimum.
    assert (
        stelselgroep._bereken_minimum_punten_nieuwbouw(eenheid, resultaat, woz_punten)
        == verwacht_minimum
    )


@pytest.mark.parametrize(
    ("aantal_laadpalen", "verwacht_minimum"),
    [
        pytest.param(1, Decimal("40"), id="met_laadpaal"),
        pytest.param(0, Decimal("0"), id="zonder_laadpaal"),
    ],
)
def test_een_laadpaal_in_rubriek_12_telt_mee_in_de_110_puntentoets(
    aantal_laadpalen, verwacht_minimum
):
    """Een laadpaal die in rubriek 12 punten krijgt, telt mee in de 110-puntentoets van het nieuwbouwminimum.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    - wettekst, Bijlage I onder A, onderdeel 12
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=REFERENTIE_PEILDATUM)
    # Een privé-parkeerplek met laadpaal krijgt geen punten in rubriek 10, dus 2 punten in rubriek 12.
    eenheid = EenhedenEenheid(
        id="test",
        bouwjaar=2016,
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)]
                * aantal_laadpalen,
            )
        ],
    )
    resultaat = _maak_resultaat_met_overige_punten(
        (Woningwaarderingstelselgroep.oppervlakte_van_vertrekken, 108.0),
    )

    # 108 + 2 = 110: precies op de drempel.
    assert (
        stelselgroep._bereken_minimum_punten_nieuwbouw(eenheid, resultaat, Decimal("0"))
        == verwacht_minimum
    )
