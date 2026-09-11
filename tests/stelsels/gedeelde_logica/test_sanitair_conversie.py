from datetime import date

import pytest

from woningwaardering.stelsels.zelfstandige_woonruimten import Sanitair
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen import (
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    BouwkundigelementdetailsoortReferentiedata,
    Bouwkundigelementsoort,
    Installatiesoort,
    InstallatiesoortReferentiedata,
    Ruimtedetailsoort,
    Ruimtesoort,
)


def _badkamer(
    elementen: list[BouwkundigelementdetailsoortReferentiedata],
    installaties: list[InstallatiesoortReferentiedata] | None = None,
    *,
    gedeeld_met_aantal_adressen: int | None = None,
) -> EenhedenEenheid:
    return EenhedenEenheid(
        id="eenheid",
        ruimten=[
            EenhedenRuimte(
                id="badkamer",
                naam="Badkamer",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.badkamer,
                oppervlakte=6.0,
                gedeeld_met_aantal_adressen=gedeeld_met_aantal_adressen,
                bouwkundige_elementen=[
                    BouwkundigElementenBouwkundigElement(
                        id=f"element_{index}",
                        soort=Bouwkundigelementsoort.voorziening,
                        detail_soort=detail_soort,
                    )
                    for index, detail_soort in enumerate(elementen)
                ],
                installaties=list(installaties or []),
            )
        ],
    )


def _aantal_en_punten(
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
    installatiesoort: InstallatiesoortReferentiedata,
) -> tuple[float | None, float | None]:
    waardering = next(
        w
        for w in groep.woningwaarderingen or []
        if w.criterium is not None and w.criterium.naam == installatiesoort.naam
    )
    return waardering.aantal, waardering.punten


@pytest.mark.parametrize(
    "elementen, installaties, verwacht_aantal",
    [
        ([Bouwkundigelementdetailsoort.wastafel], [], 1.0),
        (
            [
                Bouwkundigelementdetailsoort.wastafel,
                Bouwkundigelementdetailsoort.wastafel,
            ],
            [],
            2.0,
        ),
        # Fontein telt als wastafel en mag niet wegvallen tegen een afgeleide wastafel.
        (
            [
                Bouwkundigelementdetailsoort.wastafel,
                Bouwkundigelementdetailsoort.fontein,
            ],
            [],
            2.0,
        ),
        # Zelfde voorziening dubbel gemodelleerd: hoogste van beide aantallen.
        (
            [Bouwkundigelementdetailsoort.wastafel],
            [Installatiesoort.wastafel],
            1.0,
        ),
        (
            [
                Bouwkundigelementdetailsoort.wastafel,
                Bouwkundigelementdetailsoort.wastafel,
            ],
            [Installatiesoort.wastafel],
            2.0,
        ),
        (
            [Bouwkundigelementdetailsoort.wastafel],
            [Installatiesoort.wastafel, Installatiesoort.wastafel],
            2.0,
        ),
    ],
)
def test_max_regel_per_installatiesoort(
    peildatum: date,
    elementen: list[BouwkundigelementdetailsoortReferentiedata],
    installaties: list[InstallatiesoortReferentiedata],
    verwacht_aantal: float,
):
    eenheid = _badkamer(elementen, installaties)

    groep = Sanitair(peildatum=peildatum).waardeer(eenheid)

    aantal, _punten = _aantal_en_punten(groep, Installatiesoort.wastafel)
    assert aantal == verwacht_aantal
    assert eenheid.ruimten is not None
    assert list(eenheid.ruimten[0].installaties or []) == list(installaties)


@pytest.mark.parametrize(
    "element, installatiesoort, aantal, punten",
    [
        (Bouwkundigelementdetailsoort.douche, Installatiesoort.douche, 1.0, 4.0),
        (Bouwkundigelementdetailsoort.bad, Installatiesoort.bad, 1.0, 6.0),
        (
            Bouwkundigelementdetailsoort.closetcombinatie,
            Installatiesoort.staand_toilet,
            1.0,
            2.0,
        ),
        (Bouwkundigelementdetailsoort.fontein, Installatiesoort.wastafel, 1.0, 1.0),
    ],
)
def test_mapping_bouwkundig_element(
    peildatum: date,
    element: BouwkundigelementdetailsoortReferentiedata,
    installatiesoort: InstallatiesoortReferentiedata,
    aantal: float,
    punten: float,
):
    groep = Sanitair(peildatum=peildatum).waardeer(_badkamer([element]))

    assert _aantal_en_punten(groep, installatiesoort) == (aantal, punten)


def test_bouwkundige_kast_levert_kastruimtepunten(peildatum: date):
    # Extra voorzieningen vragen om wastafel én douche; die komen als installatie mee.
    groep = Sanitair(peildatum=peildatum).waardeer(
        _badkamer(
            [Bouwkundigelementdetailsoort.kast],
            [Installatiesoort.wastafel, Installatiesoort.douche],
        )
    )

    assert _aantal_en_punten(groep, Installatiesoort.kastruimte) == (1.0, 0.75)


def test_aanrecht_levert_geen_wastafelpunten(peildatum: date):
    groep = Sanitair(peildatum=peildatum).waardeer(
        _badkamer([Bouwkundigelementdetailsoort.aanrecht])
    )

    assert groep.punten in (None, 0.0)


def test_gvv_waardeert_bouwkundig_sanitair_zonder_voorafgaande_mutatie(
    peildatum: date,
):
    groep = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=peildatum
    ).waardeer(
        _badkamer(
            [
                Bouwkundigelementdetailsoort.wastafel,
                Bouwkundigelementdetailsoort.douche,
            ],
            gedeeld_met_aantal_adressen=2,
        )
    )

    assert _aantal_en_punten(groep, Installatiesoort.wastafel) == (1.0, 0.5)
    assert _aantal_en_punten(groep, Installatiesoort.douche) == (1.0, 2.0)
    assert groep.punten == 5.5
