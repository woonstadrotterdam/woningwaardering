from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.gedeelde_logica.gemeenschappelijke_ruimten import (
    waardeer_gemeenschappelijke_ruimten,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.sanitair import (
    Sanitair as OnzelfstandigeWoonruimtenSanitair,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen
        super().__init__(
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if zorgwoning := self._zorgwoning(eenheid):
            woningwaardering_groep.woningwaarderingen.append(zorgwoning)
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if ruimte.gedeeld_met_aantal_eenheden is not None
                and ruimte.gedeeld_met_aantal_eenheden > 1
            ]

            woningwaardering_groep.woningwaarderingen.extend(
                waardeer_gemeenschappelijke_ruimten(
                    stelselgroep=self.stelselgroep,
                    stelsel=self.stelsel,
                    ruimten=gedeelde_ruimten,
                    sanitair_voor_ruimten=lambda ruimten: (
                        OnzelfstandigeWoonruimtenSanitair.genereer_woningwaarderingen(
                            ruimten, self.stelselgroep
                        )
                    ),
                )
            )

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid {eenheid.id} krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _zorgwoning(
        self, eenheid: EenhedenEenheid
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        """
        Beleidsboek: De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en
        voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning
        veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief
        meetwerk te voorkomen waardeert de Huurcommissie in dat geval een waardering
        van 3 punten per woning.

        Args:
            eenheid (EenhedenEenheid): Eenheid

        Returns:
            WoningwaarderingResultatenWoningwaardering | None: Woningwaardering van 3 punten voor een zorgwoning of None als de eenheid geen zorgwoning is
        """
        if eenheid.doelgroep == Doelgroep.zorg:
            logger.info(
                f"Eenheid {eenheid.id} is een zorgwoning en krijgt 3 punten voor {self.stelselgroep.naam}"
            )
            return WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Zorgwoning",
                    id=str(
                        CriteriumId.voor_stelselgroep(
                            self.stelselgroep
                        ).met_onderliggend("zorgwoning")
                    ),
                ),
                punten=3.0,
            )
        logger.debug(
            f"Eenheid {eenheid.id} is geen zorgwoning en krijgt daarvoor geen punten voor {self.stelselgroep.naam}"
        )
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/input/voorbeeld_beleidsboek.json"
        )
