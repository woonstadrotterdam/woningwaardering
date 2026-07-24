import warnings

from loguru import logger

from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)


def waardeer_oppervlakte_van_vertrek(
    ruimte: EenhedenRuimte,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> list[WaarderingBuilder]:
    if not classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
        )
        return []

    if not ruimte.oppervlakte:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
            UserWarning,
        )
        return []

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
    )

    return [
        waarderingsgroep_builder.met_onderliggend(
            id=ruimte.id,
            naam=criterium_naam,
            meeteenheid=Meeteenheid.vierkante_meter_m2,
            aantal=float(rond_af(ruimte.oppervlakte, decimalen=2)),
        )
    ]
