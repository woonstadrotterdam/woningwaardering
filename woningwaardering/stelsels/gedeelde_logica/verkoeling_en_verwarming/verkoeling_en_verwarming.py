from collections.abc import Callable
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.builders import WaarderingBuilder
from woningwaardering.stelsels.criterium import maximering_naam
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_adressen,
    gedeeld_met_onzelfstandige_woonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen

SUBGROEPEN: dict[str, str] = {
    "verwarmde_vertrekken": "Verwarmde vertrekken",
    "verkoelde_vertrekken": "Verkoelde vertrekken",
    "verwarmde_overige_en_verkeersruimten": "Verwarmde overige en verkeersruimten",
}

# Ruimtedetailsoorten die de keukenfunctie al in zich hebben (geen aparte
# aanrechtlengte-check nodig voor de open-keukenbonus).
_OPEN_KEUKEN_DETAILSOORTEN = (
    Ruimtedetailsoort.woonkamer_en_of_keuken,
    Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken,
)

# Minimale aanrechtlengte voor open-keukenbonus in een woon-/slaapvertrek,
# gelijk aan de keuken-basisvoorziening (wettekst Bijlage I A rubriek 5:
# "aanrechtblad met een aaneengesloten lengte van minimaal 1 m").
_MINIMALE_AANRECHTLENGTE_OPEN_KEUKEN_MM = 1000


def _subgroep(
    subgroep: Callable[[EenhedenRuimte, str, str], WaarderingBuilder],
    ruimte: EenhedenRuimte,
    subgroep_id: str,
) -> WaarderingBuilder:
    return subgroep(ruimte, subgroep_id, SUBGROEPEN[subgroep_id])


def _ruimte_gedeeld(ruimte: EenhedenRuimte) -> bool:
    return gedeeld_met_adressen(ruimte) or gedeeld_met_onzelfstandige_woonruimten(
        ruimte
    )


def waardeer_verkoeling_en_verwarming(
    ruimten: list[EenhedenRuimte],
    *,
    subgroep: Callable[[EenhedenRuimte, str, str], WaarderingBuilder],
) -> Iterator[tuple[EenhedenRuimte, WaarderingBuilder]]:
    """Classificeer ruimten, pas maximering toe en bouw waarderingen op hun plek.

    De maximering (max. 4 punten verwarmde overige ruimten, max. 2 punten
    verkoelde vertrekken) telt over álle meegegeven ruimten samen en wordt hier in
    één doorloop met lokale tellers toegepast.

    ``subgroep`` bepaalt per ruimte onder welke builder een subgroep (bijv.
    "verwarmde vertrekken") in de hiërarchie hangt. De helper roept het aan met
    (ruimte, subgroep_id, subgroep_naam) op het moment dat een waardering wordt
    aangemaakt, zodat de laag lazy en op de juiste plek ontstaat.
    """
    yield from _waardeer_verkoeld_en_of_verwarmd_vertrek(ruimten, subgroep)
    yield from _waardeer_verwarmde_overige_ruimte(ruimten, subgroep)


def _heeft_open_keuken(ruimte: EenhedenRuimte) -> bool:
    """Of een vertrek een open keuken heeft voor rubriek verkoeling en verwarming.

    2.3.2 Open keuken in een vertrek of overige ruimte
    "Ook een aanrecht dat is geplaatst in een woon- of slaapvertrek is een open
    keuken, ook als er geen duidelijke afscheiding is tussen het keukengedeelte
    en de rest van het vertrek."

    Omdat we niet (kunnen) controleren op keukenkastjes, geldt de aanname dat
    een aanrecht vanaf 1 meter (minimaal 1 m, gelijk aan de keuken-
    basisvoorziening) als open keuken telt. Detailsoorten die de keuken al in
    zich hebben (WOK, WSK) tellen altijd als open keuken.
    """
    if ruimte.detail_soort in _OPEN_KEUKEN_DETAILSOORTEN:
        return True

    if ruimte.detail_soort not in (
        Ruimtedetailsoort.woonkamer,
        Ruimtedetailsoort.woon_en_of_slaapkamer,
        Ruimtedetailsoort.slaapkamer,
    ):
        return False

    return any(
        aanrecht.lengte is not None
        and aanrecht.lengte >= _MINIMALE_AANRECHTLENGTE_OPEN_KEUKEN_MM
        for aanrecht in get_bouwkundige_elementen(
            ruimte, Bouwkundigelementdetailsoort.aanrecht
        )
    )


def _waardeer_verwarmde_overige_ruimte(
    ruimten: list[EenhedenRuimte],
    subgroep: Callable[[EenhedenRuimte, str, str], WaarderingBuilder],
) -> Iterator[tuple[EenhedenRuimte, WaarderingBuilder]]:
    """
    Verwarmde overige ruimten tellen als 1 punt voor verwarmde overige ruimten tot een maximum van 4 punten.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen
        subgroep (Callable[[EenhedenRuimte, str, str], WaarderingBuilder]): Bepaalt per ruimte onder welke builder de subgroep hangt

    Yields:
        tuple[EenhedenRuimte, WaarderingBuilder]: Tuple van ruimte en waardering voor verwarmde overige ruimten
    """
    subgroep_id = "verwarmde_overige_en_verkeersruimten"
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
                _subgroep(subgroep, ruimte, subgroep_id).met_onderliggend(
                    id=ruimte.id,
                    naam=ruimte.naam or ruimte.id or "",
                    punten=1.0,
                ),
            )
            totaal_punten += 1
            if totaal_punten > 4:
                yield (
                    ruimte,
                    _subgroep(subgroep, ruimte, subgroep_id).met_onderliggend(
                        id="max_aantal_punten",
                        naam=maximering_naam(
                            gedeeld=_ruimte_gedeeld(ruimte),
                            met_puntental="Maximaal 4 punten",
                        ),
                        punten=-1,
                    ),
                )


def _waardeer_verkoeld_en_of_verwarmd_vertrek(
    ruimten: list[EenhedenRuimte],
    subgroep: Callable[[EenhedenRuimte, str, str], WaarderingBuilder],
) -> Iterator[tuple[EenhedenRuimte, WaarderingBuilder]]:
    """
    Verkoelde en verwarmde vertrekken tellen voor 2 punten per verwarmd vertrek.
    Een open keuken telt als afzonderlijk verwarmd vertrek voor 2 extra punten.
    Deze punten worden in de output samengevoegd met het verwarmde vertrek.
    Indien een verwarmd vertrek ook verkoeld is, wordt er 1 punt extra toegekend.
    Het maximum aantal extra punten voor vertrekken die verkoeld en verwarmd zijn is 2.

    Args:
        ruimten (list[EenhedenRuimte]): Lijst van ruimten om te waarderen
        subgroep (Callable[[EenhedenRuimte, str, str], WaarderingBuilder]): Bepaalt per ruimte onder welke builder de subgroep hangt

    Yields:
        tuple[EenhedenRuimte, WaarderingBuilder]: Tuple van ruimte en waardering voor verkoelde en verwarmde vertrekken
    """
    totaal_punten_verkoeld = 0
    for ruimte in ruimten:
        if not ruimte.verwarmd:
            continue

        ruimtesoort = classificeer_ruimte(ruimte)
        if ruimtesoort == Ruimtesoort.vertrek:
            heeft_open_keuken = _heeft_open_keuken(ruimte)
            naam = ruimte.naam or ruimte.id or ""
            if (
                heeft_open_keuken
                and ruimte.detail_soort not in _OPEN_KEUKEN_DETAILSOORTEN
            ):
                naam = f"{naam} met open keuken"

            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            if heeft_open_keuken:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt ook als open keuken mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
            yield (
                ruimte,
                _subgroep(subgroep, ruimte, "verwarmde_vertrekken").met_onderliggend(
                    id=ruimte.id,
                    naam=naam,
                    punten=4 if heeft_open_keuken else 2,
                ),
            )

            if ruimte.verkoeld:
                totaal_punten_verkoeld += 1
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
                )
                yield (
                    ruimte,
                    _subgroep(
                        subgroep, ruimte, "verkoelde_vertrekken"
                    ).met_onderliggend(
                        id=ruimte.id,
                        naam=ruimte.naam or ruimte.id or "",
                        punten=1,
                    ),
                )
                if totaal_punten_verkoeld > 2:
                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximaal aantal punten voor verkoelde vertrekken overschreden ({totaal_punten_verkoeld} > 2). Een aftrek van 1 punt wordt toegepast."
                    )
                    yield (
                        ruimte,
                        _subgroep(
                            subgroep, ruimte, "verkoelde_vertrekken"
                        ).met_onderliggend(
                            id="max_aantal_punten",
                            naam=maximering_naam(
                                gedeeld=_ruimte_gedeeld(ruimte),
                                met_puntental="Maximaal 2 punten",
                            ),
                            punten=-1,
                        ),
                    )
