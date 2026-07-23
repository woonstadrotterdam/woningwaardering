import warnings
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
)


def waardeer_oppervlakte_van_vertrek(
    ruimte: EenhedenRuimte,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata | None = None,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    stelselgroep = (
        stelselgroep or Woningwaarderingstelselgroep.oppervlakte_van_vertrekken
    )
    if not classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {stelselgroep.naam}"
        )
        return

    if not ruimte.oppervlakte:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
            UserWarning,
        )
        return

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {stelselgroep.naam}"
    )

    woningwaardering = WoningwaarderingResultatenWoningwaardering()
    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        meeteenheid=Meeteenheid.vierkante_meter_m2,
        naam=criterium_naam,
        id=str(CriteriumId.blad_ruimte(stelselgroep, ruimte.id)),
    )
    woningwaardering.aantal = float(rond_af(ruimte.oppervlakte, decimalen=2))

    yield woningwaardering
