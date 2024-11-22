import warnings
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    _bouwkundige_elementen_naar_installaties,
    _waardeer_baden_en_douches,
    _waardeer_installaties,
    _waardeer_toiletten,
    _waardeer_wastafels,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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


class Sanitair(Stelselgroep):
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
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        for ruimte in ruimten:
            woningwaardering_groep.woningwaarderingen.extend(
                Sanitair.genereer_woningwaarderingen(ruimte, self.stelselgroep)
            )

        totaal_punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )
        woningwaardering_groep.punten = float(totaal_punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte,
        stelselgroep: Woningwaarderingstelselgroep,
        stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if ruimte.detail_soort is None:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort."
            )
            return

        _bouwkundige_elementen_naar_installaties(ruimte)

        yield from _waardeer_toiletten(ruimte)

        yield from _waardeer_wastafels(ruimte, stelsel)

        baden_en_douches_waarderingen = list(
            _waardeer_baden_en_douches(ruimte, stelsel)
        )
        totaal_punten_bad_en_douche = Decimal(
            sum(
                woningwaardering.punten
                for woningwaardering in baden_en_douches_waarderingen
                if woningwaardering.punten is not None
            )
        )
        yield from baden_en_douches_waarderingen

        voorziening_waarderingen = list(_waardeer_installaties(ruimte, stelsel))
        totaal_punten_voorzieningen = Decimal(
            sum(
                woningwaardering.punten
                for woningwaardering in voorziening_waarderingen
                if woningwaardering.punten is not None
            )
        )
        yield from voorziening_waarderingen

        maximering = min(
            utils.rond_af(totaal_punten_bad_en_douche - totaal_punten_voorzieningen, 2),
            Decimal("0"),
        )

        if maximering < 0:
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam} - Voorzieningen: Max verdubbeling punten bad en douche"
                ),
                punten=maximering,
            )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=Sanitair(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )
