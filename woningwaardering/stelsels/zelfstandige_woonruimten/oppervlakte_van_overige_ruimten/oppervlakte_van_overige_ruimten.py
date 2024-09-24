import warnings
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import Stelselgroep
from woningwaardering.stelsels.utils import naar_tabel, rond_af, rond_af_op_kwart
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    classificeer_ruimte,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.utils import heeft_bouwkundig_element


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.value,
            ),
        )

        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        for ruimte in ruimten:
            woningwaarderingen = (
                OppervlakteVanOverigeRuimten.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep
                )
            )

            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        punten = rond_af_op_kwart(
            (
                rond_af(
                    sum(
                        Decimal(str(woningwaardering.aantal))
                        for woningwaardering in woningwaardering_groep.woningwaarderingen
                        or []
                        if woningwaardering.aantal is not None
                    ),
                    decimalen=0,
                )
                * Decimal("0.75")
            )
            + sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte, stelselgroep: Woningwaarderingstelselgroep
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if not ruimte.detail_soort:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detail soort.",
                UserWarning,
            )
            return

        if not ruimte.detail_soort.code:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detail soort code.",
                UserWarning,
            )
            return

        if not classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten:
            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is geen overige ruimte en komt niet aanmerking voor stelselgroep {stelselgroep.naam}."
            )
            return

        if not ruimte.oppervlakte:
            warnings.warn(
                f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte",
                UserWarning,
            )
            return

        criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

        logger.info(
            f"Ruimte {ruimte.naam} ({ruimte.id}) is een overige ruimte met oppervlakte {ruimte.oppervlakte}m2 en wordt gewaardeerd onder stelselgroep {stelselgroep.naam}."
        )

        woningwaardering = WoningwaarderingResultatenWoningwaardering()
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                naam=criterium_naam,
            )
        )

        woningwaardering.aantal = float(rond_af(ruimte.oppervlakte, decimalen=2))

        yield woningwaardering

        if ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
            # Corrigeer met -5 punten als de zolder niet bereikbaar is met een vaste trap
            # Note: Op dit moment kan de zolder alleen een
            # Bouwkundigelementdetailsoort.trap (vast) of Bouwkundigelementdetailsoort.vlizotrap (niet vast)
            # hebben vanwege classificeer_ruimte in utils.py.
            if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.vlizotrap):
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) krijgt een correctie van -5 punten maximaal: de zolder is niet bereikbaar via een vaste trap."
                )
                woningwaardering_correctie = (
                    WoningwaarderingResultatenWoningwaardering()
                )
                woningwaardering_correctie.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Correctie: zolder zonder vaste trap",
                    )
                )

                # corrigeeer niet met meer punten dan de oppervlakte voor stelselgroep overige ruimten zou opleveren
                correctie = min(
                    5.0,
                    float(
                        rond_af_op_kwart(
                            rond_af(ruimte.oppervlakte, decimalen=2) * Decimal("0.75")
                        )
                    ),
                )

                woningwaardering_correctie.punten = correctie * -1.0
                yield woningwaardering_correctie


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    oppervlakte_van_overige_ruimten = OppervlakteVanOverigeRuimten(
        peildatum=date(2024, 7, 1)
    )
    with open(
        "tests/data/zelfstandige_woonruimten/input/71211000027.json", "r+"
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = oppervlakte_van_overige_ruimten.bereken(eenheid)

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = naar_tabel(woningwaardering_resultaat)

        print(tabel)
