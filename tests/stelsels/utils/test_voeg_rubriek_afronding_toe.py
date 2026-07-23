from woningwaardering.stelsels.utils import voeg_rubriek_afronding_toe
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _groep(
    *,
    punten: float | None,
    waarderingen: list[WoningwaarderingResultatenWoningwaardering] | None = None,
    stelselgroep: Woningwaarderingstelselgroep = Woningwaarderingstelselgroep.energieprestatie,
) -> WoningwaarderingResultatenWoningwaarderingGroep:
    return WoningwaarderingResultatenWoningwaarderingGroep(
        criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
            stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
            stelselgroep=stelselgroep,
        ),
        punten=punten,
        woningwaarderingen=waarderingen,
    )


def _waardering(
    *,
    criterium_id: str,
    naam: str,
    punten: float,
) -> WoningwaarderingResultatenWoningwaardering:
    return WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            id=criterium_id,
            naam=naam,
        ),
        punten=punten,
    )


def test_voeg_rubriek_afronding_toe_voegt_delta_toe() -> None:
    groep = _groep(
        punten=8.5,
        waarderingen=[
            _waardering(
                criterium_id="energieprestatie__bouwjaar",
                naam="Bouwjaar 1998",
                punten=8.58,
            )
        ],
    )

    voeg_rubriek_afronding_toe(groep)

    assert groep.punten == 8.5
    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 2
    afronding = groep.woningwaarderingen[-1]
    assert afronding.criterium is not None
    assert afronding.criterium.id == "energieprestatie__afronding"
    assert afronding.criterium.naam == "Afronding"
    assert afronding.criterium.bovenliggende_criterium is None
    assert afronding.punten == -0.08


def test_voeg_rubriek_afronding_toe_geen_regel_bij_delta_nul() -> None:
    groep = _groep(
        punten=2.0,
        waarderingen=[
            _waardering(
                criterium_id="energieprestatie__label",
                naam="Label",
                punten=2.0,
            )
        ],
    )

    voeg_rubriek_afronding_toe(groep)

    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1
    assert groep.woningwaarderingen[0].criterium is not None
    assert groep.woningwaarderingen[0].criterium.id == "energieprestatie__label"


def test_voeg_rubriek_afronding_toe_skip_bij_punten_none() -> None:
    groep = _groep(
        punten=None,
        waarderingen=[
            _waardering(
                criterium_id="energieprestatie__label",
                naam="Label",
                punten=1.0,
            )
        ],
    )

    voeg_rubriek_afronding_toe(groep)

    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1


def test_voeg_rubriek_afronding_toe_skip_zonder_detailpunten() -> None:
    """Oppervlakte-achtig: alleen aantal op regels, punten uitsluitend op de groep."""
    groep = _groep(
        punten=25.0,
        waarderingen=[
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    id="oppervlakte_van_vertrekken__prive__Space_1",
                    naam="Slaapkamer",
                ),
                aantal=20.04,
            )
        ],
        stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )

    voeg_rubriek_afronding_toe(groep)

    assert groep.punten == 25.0
    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1
    assert groep.woningwaarderingen[0].punten is None


def test_voeg_rubriek_afronding_toe_negatieve_groep() -> None:
    groep = _groep(
        punten=-1.25,
        waarderingen=[
            _waardering(
                criterium_id="aftrekpunten__geen_cv",
                naam="Geen cv",
                punten=-1.3,
            )
        ],
        stelselgroep=Woningwaarderingstelselgroep.aftrekpunten,
    )

    voeg_rubriek_afronding_toe(groep)

    assert groep.punten == -1.25
    assert groep.woningwaarderingen is not None
    afronding = groep.woningwaarderingen[-1]
    assert afronding.criterium is not None
    assert afronding.criterium.id == "aftrekpunten__afronding"
    assert afronding.punten == 0.05


def test_voeg_rubriek_afronding_toe_idempotent() -> None:
    groep = _groep(
        punten=8.5,
        waarderingen=[
            _waardering(
                criterium_id="energieprestatie__bouwjaar",
                naam="Bouwjaar 1998",
                punten=8.58,
            )
        ],
    )

    voeg_rubriek_afronding_toe(groep)
    voeg_rubriek_afronding_toe(groep)

    assert groep.woningwaarderingen is not None
    afrondingen = [
        w
        for w in groep.woningwaarderingen
        if w.criterium is not None and w.criterium.id == "energieprestatie__afronding"
    ]
    assert len(afrondingen) == 1
    assert afrondingen[0].punten == -0.08
