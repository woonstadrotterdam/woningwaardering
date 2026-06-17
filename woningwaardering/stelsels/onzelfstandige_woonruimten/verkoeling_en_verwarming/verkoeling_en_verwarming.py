from collections import defaultdict
from datetime import date
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    laatste_criteriumid_toevoeging,
    weergavenaam_voor,
)
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    deel_punten_door_aantal_onzelfstandige_woonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
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


class VerkoelingEnVerwarming(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.verkoeling_en_verwarming  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        woningwaarderingen = list(waardeer_verkoeling_en_verwarming(ruimten))
        woningwaarderingen_totaal: list[
            tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]
        ] = []
        for ruimte, woningwaardering in woningwaarderingen:
            waardering_gedeeld = list(
                deel_punten_door_aantal_onzelfstandige_woonruimten(
                    ruimte, [woningwaardering], update_criterium_naam=False
                )
            )[0]  # er is altijd maar een woningwaardering
            self._nest_onder_gedeeld_met(ruimte, waardering_gedeeld)
            woningwaarderingen_totaal.append((ruimte, waardering_gedeeld))
            woningwaardering_groep.woningwaarderingen.append(waardering_gedeeld)

        woningwaardering_groep.woningwaarderingen.extend(
            list(self._maak_totalen(woningwaarderingen_totaal))
        )

        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _nest_onder_gedeeld_met(
        self,
        ruimte: EenhedenRuimte,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> None:
        """Verplaatst een waardering onder het gedeeld-met-criterium van de ruimte (in-place).

        Mechanisme om criterium-paden te verlengen; geen synoniem voor geneste
        stelselgroep. Onzelfstandige gedeelde ruimten krijgen ids onder
        ``{stelselgroep}__gedeeld_met_N_onzelfstandige_woonruimten__...``.

        Args:
            ruimte (EenhedenRuimte): Ruimte met gedeeld-met-aantallen.
            woningwaardering (WoningwaarderingResultatenWoningwaardering): Te verplaatsen waardering.

        Example:
            ``verkoeling_en_verwarming__verwarmde_vertrekken__...`` →
            ``verkoeling_en_verwarming__gedeeld_met_3_onzelfstandige_woonruimten__verwarmde_vertrekken__...``.
        """
        if woningwaardering.criterium is None or not woningwaardering.criterium.id:
            return

        onz_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
        gedeeld_met_groep = CriteriumId.voor_stelselgroep(
            self.stelselgroep
        ).gedeeld_met_criterium(onz_aantal, GedeeldMetSoort.onzelfstandige_woonruimten)

        criterium_id = woningwaardering.criterium.id
        suffix = criterium_id.split("__", 1)[1]
        woningwaardering.criterium.id = str(gedeeld_met_groep.met_onderliggend(suffix))

        if (
            woningwaardering.criterium.bovenliggende_criterium
            and woningwaardering.criterium.bovenliggende_criterium.id
        ):
            bovenliggend_id = woningwaardering.criterium.bovenliggende_criterium.id
            if "__" in bovenliggend_id:
                groepering_suffix = bovenliggend_id.split("__", 1)[1]
                nieuwe_bovenliggend_id = str(
                    gedeeld_met_groep.met_onderliggend(groepering_suffix)
                )
            else:
                nieuwe_bovenliggend_id = str(gedeeld_met_groep)
            woningwaardering.criterium.bovenliggende_criterium = (
                WoningwaarderingCriteriumSleutels(id=nieuwe_bovenliggend_id)
            )

    def _maak_totalen(
        self,
        waarderingen: list[
            tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]
        ],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        gedeeld_met_criterium_ids: defaultdict[int, dict[str, None]] = defaultdict(dict)

        # {bovenliggend_criterium: {onzelfstandige_woonruimten: punten}}
        for ruimte, woningwaardering in waarderingen:
            gedeeld_met_onz = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            groeperings_id: str | None = None
            if woningwaardering.criterium and woningwaardering.criterium.id:
                if (
                    woningwaardering.criterium.bovenliggende_criterium
                    and woningwaardering.criterium.bovenliggende_criterium.id
                    and "__" in woningwaardering.criterium.bovenliggende_criterium.id
                ):
                    groeperings_id = (
                        woningwaardering.criterium.bovenliggende_criterium.id
                    )
                elif "__" in woningwaardering.criterium.id:
                    groeperings_id = woningwaardering.criterium.id
            if groeperings_id is not None:
                gedeeld_met_criterium_ids[gedeeld_met_onz][groeperings_id] = None

        for aantal_onz, bovenliggend_criterium_ids in gedeeld_met_criterium_ids.items():
            gedeeld_met_groep = CriteriumId.voor_stelselgroep(
                self.stelselgroep
            ).gedeeld_met_criterium(
                aantal_onz, GedeeldMetSoort.onzelfstandige_woonruimten
            )
            gedeeld_met_groep_id = str(gedeeld_met_groep)
            for criterium_id in bovenliggend_criterium_ids:
                if criterium_id == gedeeld_met_groep_id:
                    continue
                if criterium_id.startswith(f"{gedeeld_met_groep_id}__"):
                    groepering_id = criterium_id
                elif "__" not in criterium_id:
                    continue
                else:
                    suffix = criterium_id.split("__", 1)[1]
                    groepering_id = str(gedeeld_met_groep.met_onderliggend(suffix))
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=groepering_id,
                        naam=weergavenaam_voor(
                            laatste_criteriumid_toevoeging(criterium_id)
                        ),
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=gedeeld_met_groep_id
                        ),
                    ),
                )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    id=gedeeld_met_groep_id,
                    naam=utils.naam_gedeeld_met_groep(
                        aantal_onz,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                ),
            )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/vertrek_verkoeld_en_verwarmd_onz.json"
        )
