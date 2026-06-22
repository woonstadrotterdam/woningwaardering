from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.stelsels.woningwaardering_groep import (
    Waardering,
    WoningwaarderingGroep,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element

_STELSELGROEP_ID = CriteriumId.voor_stelselgroep(
    Woningwaarderingstelselgroep.verkoeling_en_verwarming
)
_VERWARMDE_OVERIGE = _STELSELGROEP_ID.met_onderliggend(
    "verwarmde_overige_en_verkeersruimten"
)
_VERKOELDE_EN_VERWARMDE = _STELSELGROEP_ID.met_onderliggend(
    "verkoelde_en_verwarmde_vertrekken"
)
_VERWARMDE_VERTREKKEN = _STELSELGROEP_ID.met_onderliggend("verwarmde_vertrekken")
_OPEN_KEUKEN = _STELSELGROEP_ID.met_onderliggend("open_keuken")


VerkoelingEnVerwarmingResultaat = tuple[
    EenhedenRuimte, WoningwaarderingResultatenWoningwaardering
]


def waardeer_verkoeling_en_verwarming(
    ruimten: list[EenhedenRuimte],
) -> Iterator[VerkoelingEnVerwarmingResultaat]:
    yield from _waardeer_verkoeld_en_of_verwarmd_vertrek(ruimten)
    yield from _waardeer_verwarmde_overige_ruimte(ruimten)
    yield from _waardeer_open_keuken(ruimten)


def bouw_verkoeling_en_verwarming(
    verkoeling_resultaten: list[VerkoelingEnVerwarmingResultaat],
    subgroep_parent: Waardering | WoningwaarderingGroep,
    deler: Decimal = Decimal("1"),
) -> None:
    """Re-emit leaf-verkoeling onder ``subgroep_parent`` via de fluent keten.

    De caller bepaalt de parent-handle: direct onder de stelselgroep-root (standalone
    zelfstandig), onder ``gedeeld_met_*`` (standalone onzelfstandig), of onder een
    geneste stelselgroep-laag (GEM/GBA). Leaf-id's worden gestript tot
    ``subgroep__ruimte_criterium``; punten worden gedeeld door ``deler``.

    Args:
        verkoeling_resultaten (list[VerkoelingEnVerwarmingResultaat]): Output van ``waardeer_verkoeling_en_verwarming``.
        subgroep_parent (Waardering | WoningwaarderingGroep): Handle waaronder groeperingscriteria (bijv.
            ``verwarmde_vertrekken``) nesten.
        deler (Decimal): Deler voor punten (``1`` zelfstandig, ``onz_aantal`` onzelfstandig,
            ``onz × adressen`` in GEM).
    """
    naam_key = Woningwaarderingstelselgroep.verkoeling_en_verwarming.name
    subgroepen: dict[str, Waardering] = {}

    for _ruimte, bron in verkoeling_resultaten:
        if bron.criterium is None or bron.criterium.id is None:
            continue
        onderliggend_id = utils.criteriumid_onder_stelselgroep(
            bron.criterium.id, naam_key
        )
        if onderliggend_id is None or "__" not in onderliggend_id:
            continue

        detail_punten = (
            float(utils.rond_af(Decimal(str(bron.punten)) / deler, decimalen=2))
            if bron.punten is not None
            else None
        )
        if detail_punten is None and bron.aantal is None:
            continue

        # bijv. ``verwarmde_vertrekken__Space_1``
        # subgroep = ``verwarmde_vertrekken``
        # ruimte_criterium = ``Space_1``
        subgroep, ruimte_criterium = onderliggend_id.split("__", 1)
        subgroep_waardering = subgroepen.get(subgroep)
        if subgroep_waardering is None:
            subgroep_waardering = subgroep_parent.met_onderliggend(subgroep)
            subgroepen[subgroep] = subgroep_waardering

        subgroep_waardering.met_onderliggend(
            ruimte_criterium,
            naam=bron.criterium.naam,
            meeteenheid=bron.criterium.meeteenheid,
            aantal=bron.aantal,
            punten=detail_punten,
        )


def _waardeer_verwarmde_overige_ruimte(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Verwarmde overige ruimten tellen als 1 punt voor verwarmde overige ruimten tot een maximum van 4 punten.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor verwarmde overige ruimten
    """
    totaal_punten = 0
    for ruimte in ruimten:
        if not ruimte.verwarmd:
            continue

        ruimtesoort = classificeer_ruimte(ruimte)
        if ruimtesoort in (
            Ruimtesoort.overige_ruimten,
            Ruimtesoort.verkeersruimte,
        ):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmde overige- of verkeersruimte mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            yield (
                ruimte,
                _VERWARMDE_OVERIGE.met_onderliggend(ruimte.id).met_waardering(
                    naam=ruimte.naam, punten=1.0
                ),
            )
            totaal_punten += 1
            if totaal_punten > 4:
                yield (
                    ruimte,
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam}: Maximaal 4 punten",
                            id=str(
                                _VERWARMDE_OVERIGE.met_onderliggend(
                                    f"{ruimte.id}__max_aantal_punten"
                                )
                            ),
                            bovenliggende_criterium=_VERWARMDE_OVERIGE.naar_criterium_sleutels(),
                        ),
                        punten=-1,
                    ),
                )


def _waardeer_verkoeld_en_of_verwarmd_vertrek(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Verkoelde en verwarmde vertrekken tellen voor 2 punten per verwarmd vertrek.
    Indien een verwarmd vertrek ook verkoeld is, wordt er 1 punt extra toegekend.
    Het maximum aantal extra punten voor vertrekken die verkoeld en verwarmd zijn is 2.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor verkoelde en verwarmde vertrekken
    """
    totaal_punten_verkoeld_en_verwarmd = 0
    for ruimte in ruimten:
        if not ruimte.verwarmd:
            continue

        punten = 2
        ruimtesoort = classificeer_ruimte(ruimte)
        if ruimtesoort == Ruimtesoort.vertrek:
            if ruimte.verkoeld:
                totaal_punten_verkoeld_en_verwarmd += 1
                punten += 1  # 1 punt extra per vertrek wanneer verwarmd en verkoeld
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld en verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
                yield (
                    ruimte,
                    _VERKOELDE_EN_VERWARMDE.met_onderliggend(ruimte.id).met_waardering(
                        naam=ruimte.naam, punten=punten
                    ),
                )
                if totaal_punten_verkoeld_en_verwarmd > 2:
                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximaal aantal extra punten voor verwarmde en verkoelde vertrekken overschreden ({totaal_punten_verkoeld_en_verwarmd} > 2). Een aftrek van 1 punt wordt toegepast."
                    )
                    yield (
                        ruimte,
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam}: Maximaal 2 extra punten",
                                id=str(
                                    _VERKOELDE_EN_VERWARMDE.met_onderliggend(
                                        f"{ruimte.id}__max_aantal_extra_punten"
                                    )
                                ),
                                bovenliggende_criterium=_VERKOELDE_EN_VERWARMDE.naar_criterium_sleutels(),
                            ),
                            punten=-1,
                        ),
                    )
            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
                yield (
                    ruimte,
                    _VERWARMDE_VERTREKKEN.met_onderliggend(ruimte.id).met_waardering(
                        naam=ruimte.naam, punten=punten
                    ),
                )


def _waardeer_open_keuken(
    ruimten: list[EenhedenRuimte],
) -> Iterator[tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]]:
    """
    Open keuken tellen voor 2 punten per verwarmd vertrek.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen

    Yields:
        tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]: Tuple van ruimte en waardering voor open keuken
    """
    for ruimte in ruimten:
        if ruimte.verwarmd and (
            ruimte.detail_soort == Ruimtedetailsoort.woonkamer_en_of_keuken
            or (
                ruimte.detail_soort
                in [
                    Ruimtedetailsoort.woonkamer,
                    Ruimtedetailsoort.woon_en_of_slaapkamer,
                    Ruimtedetailsoort.slaapkamer,
                ]
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.aanrecht
                )
            )
        ):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als open keuken mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            yield (
                ruimte,
                _OPEN_KEUKEN.met_onderliggend(ruimte.id).met_waardering(
                    naam=ruimte.naam, punten=2.0
                ),
            )
