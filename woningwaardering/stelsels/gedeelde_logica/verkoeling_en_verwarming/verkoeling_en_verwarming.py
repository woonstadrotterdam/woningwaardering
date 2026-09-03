from collections.abc import Callable
from enum import Enum
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.builders import WaarderingBuilder
from woningwaardering.stelsels.criterium import maximering_naam
from woningwaardering.stelsels.gedeelde_logica.aanrecht import heeft_valide_aanrecht
from woningwaardering.stelsels.gedeelde_logica.keuken import (
    OPEN_KEUKEN_DETAIL_SOORTEN,
)
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    deler,
    gedeeld_met_adressen,
    gedeeld_met_onzelfstandige_woonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)

# Vertrekken waarin per definitie geen open keuken ligt. §2.3.2 maakt van een
# aanrecht alleen in een "woon- of slaapvertrek" een open keuken: in een keuken,
# bijkeuken, badkamer of doucheruimte wordt niet gewoond of geslapen, en een
# `keuken` ís bovendien de keuken zelf en telt al als afzonderlijk verwarmd
# vertrek. Elke andere ruimte die als vertrek wordt gewaardeerd, telt wél mee.
GEEN_OPEN_KEUKEN_DETAIL_SOORTEN = frozenset(
    {
        Ruimtedetailsoort.keuken,
        Ruimtedetailsoort.bijkeuken,
        Ruimtedetailsoort.badkamer,
        Ruimtedetailsoort.badkamer_met_toilet,
        Ruimtedetailsoort.doucheruimte,
    }
)

SUBGROEPEN: dict[str, str] = {
    "verwarmde_vertrekken": "Verwarmde vertrekken",
    "verkoelde_vertrekken": "Verkoelde vertrekken",
    "verwarmde_overige_en_verkeersruimten": "Verwarmde overige en verkeersruimten",
}


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


def _is_verwarmde_overige_of_verkeersruimte(ruimte: EenhedenRuimte) -> bool:
    if not ruimte.verwarmd:
        return False
    return classificeer_ruimte(ruimte) in (
        Ruimtesoort.overige_ruimten,
        Ruimtesoort.verkeersruimte,
    )


def _is_verwarmd_vertrek(ruimte: EenhedenRuimte) -> bool:
    if not ruimte.verwarmd:
        return False
    return classificeer_ruimte(ruimte) == Ruimtesoort.vertrek


def _rangschik_voor_maximering(
    ruimten: list[EenhedenRuimte],
) -> list[EenhedenRuimte]:
    """Kleinste deler eerst; bij gelijke deler blijft de invoervolgorde staan."""
    return sorted(
        ruimten,
        key=lambda ruimte: deler(ruimte),
    )


def waardeer_verkoeling_en_verwarming(
    ruimten: list[EenhedenRuimte],
    *,
    subgroep: Callable[[EenhedenRuimte, str, str], WaarderingBuilder],
) -> Iterator[tuple[EenhedenRuimte, WaarderingBuilder]]:
    """Classificeer ruimten, pas maximering toe en bouw waarderingen op hun plek.

    De maximering (max. 4 punten verwarmde overige ruimten, max. 2 punten
    verkoelde vertrekken) telt over álle meegegeven ruimten samen. Privé en
    gemeenschappelijk delen die teller tot #293 is beslist. Elke ruimte krijgt
    1 punt; ruimten boven het maximum krijgen −1. De teller loopt in rangorde
    (kleinste deler, daarna invoervolgorde), zodat dezelfde ruimten hetzelfde
    totaal geven.
    Deling gebeurt daarna in de aanroeper. De outputvolgorde volgt die rangorde.

    ``subgroep`` bepaalt per ruimte onder welke builder een subgroep (bijv.
    "verwarmde vertrekken") in de hiërarchie hangt. De helper roept het aan met
    (ruimte, subgroep_id, subgroep_naam) op het moment dat een waardering wordt
    aangemaakt, zodat de laag lazy en op de juiste plek ontstaat.
    """
    yield from _waardeer_verkoeld_en_of_verwarmd_vertrek(ruimten, subgroep)
    yield from _waardeer_verwarmde_overige_ruimte(ruimten, subgroep)


class _OpenKeukenSoort(Enum):
    inherente_keuken = "inherente_keuken"
    impliciete_open_keuken = "impliciete_open_keuken"


def _classificeer_open_keuken(ruimte: EenhedenRuimte) -> _OpenKeukenSoort | None:
    """Bepaalt of in dit vertrek een open keuken ligt, en op welke grond.

    §2.3.2 spreekt over "een aanrecht dat is geplaatst in een woon- of
    slaapvertrek". Wij lezen dat als de eis dat de ruimte als vertrek wordt
    gewaardeerd — de aanroeper controleert dat — en niet als een eis aan de
    detailsoort. Elk vertrek waarin een aanrecht vanaf 1 meter staat, heeft
    daarom een open keuken, behalve de vertrekken uit
    :data:`GEEN_OPEN_KEUKEN_DETAIL_SOORTEN`.


    Args:
        ruimte (EenhedenRuimte): De ruimte om te classificeren.

    Returns:
        _OpenKeukenSoort | None: De grond voor de open keuken, of None wanneer de
        ruimte geen open keuken heeft.
    """
    if ruimte.detail_soort in GEEN_OPEN_KEUKEN_DETAIL_SOORTEN:
        return None
    if ruimte.detail_soort in OPEN_KEUKEN_DETAIL_SOORTEN:
        return _OpenKeukenSoort.inherente_keuken
    # §2.3.2: aanname open keuken bij aanrecht vanaf 1 meter,
    # gelijk aan de keuken-basisvoorziening (wettekst Bijlage I A rubriek 5).
    if heeft_valide_aanrecht(ruimte):
        return _OpenKeukenSoort.impliciete_open_keuken
    return None


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
    for ruimte in _rangschik_voor_maximering(
        [r for r in ruimten if _is_verwarmde_overige_of_verkeersruimte(r)]
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
    for ruimte in _rangschik_voor_maximering(
        [r for r in ruimten if _is_verwarmd_vertrek(r)]
    ):
        open_keuken = _classificeer_open_keuken(ruimte)
        naam = ruimte.naam or ruimte.id or ""
        if open_keuken == _OpenKeukenSoort.impliciete_open_keuken:
            naam = f"{naam} met open keuken"

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verwarmd vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
        )
        if open_keuken is not None:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt ook als open keuken mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
        yield (
            ruimte,
            _subgroep(subgroep, ruimte, "verwarmde_vertrekken").met_onderliggend(
                id=ruimte.id,
                naam=naam,
                punten=4 if open_keuken is not None else 2,
            ),
        )

        if ruimte.verkoeld:
            totaal_punten_verkoeld += 1
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt als verkoeld vertrek mee voor {Woningwaarderingstelselgroep.verkoeling_en_verwarming.naam}"
            )
            yield (
                ruimte,
                _subgroep(subgroep, ruimte, "verkoelde_vertrekken").met_onderliggend(
                    id=ruimte.id,
                    naam=ruimte.naam or ruimte.id or "",
                    punten=1,
                ),
            )
            if totaal_punten_verkoeld > 2:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximaal aantal punten voor verkoelde vertrekken overschreden. Een aftrek van 1 punt wordt toegepast."
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
