from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    rond_af_op_kwart,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


def waardeer_oppervlakte_van_overige_ruimte(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    if classificeer_ruimte(ruimte) != Ruimtesoort.overige_ruimten:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )
        return

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
    )

    woningwaardering = WoningwaarderingResultatenWoningwaardering()
    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        meeteenheid=Meeteenheid.vierkante_meter_m2,
        naam=criterium_naam,
    )

    woningwaardering.aantal = float(rond_af(ruimte.oppervlakte, decimalen=2))

    yield woningwaardering

    if ruimte.detail_soort == Ruimtedetailsoort.zolder:
        # Corrigeer met -5 punten als de zolder niet bereikbaar is met een vaste trap
        # Note: Op dit moment kan de zolder alleen een
        # Bouwkundigelementdetailsoort.trap (vast) of Bouwkundigelementdetailsoort.vlizotrap (niet vast)
        # hebben vanwege classificeer_ruimte in utils.py.
        if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.vlizotrap):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): maximaal correctie van -5 punten: zolder is niet bereikbaar via een vaste trap."
            )
            woningwaardering_correctie = WoningwaarderingResultatenWoningwaardering()
            woningwaardering_correctie.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Correctie: zolder zonder vaste trap",
                )
            )

            # corrigeeer niet met meer punten dan de oppervlakte voor stelselgroep overige ruimten zou opleveren
            correctie = min(
                Decimal("5"),
                rond_af_op_kwart(
                    rond_af(ruimte.oppervlakte, decimalen=2) * Decimal("0.75")
                ),
            )

            woningwaardering_correctie.punten = float(correctie * Decimal("-1"))
            yield woningwaardering_correctie
