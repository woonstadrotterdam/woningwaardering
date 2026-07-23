from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    naam_uit_subgroep_criterium_id,
)
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_keuken,
    waardeer_oppervlakte_van_overige_ruimte,
    waardeer_oppervlakte_van_vertrek,
    waardeer_sanitair,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
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
    Doelgroep,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen
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

        # Gemeenschappelijke ruimten en voorzieningen in een zorgwoning
        #
        # De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en
        # voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning
        # veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief
        # meetwerk te voorkomen waardeert de Huurcommissie in dat geval een waardering
        # van 3 punten per woning.
        if eenheid.doelgroep == Doelgroep.zorg:
            logger.info(
                f"Eenheid ({eenheid.id}) is een zorgwoning en wordt met 3 punten gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
            )
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Zorgwoning",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="zorgwoning",
                            )
                        ),
                    ),
                    punten=3.0,
                )
            )
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if utils.gedeeld_met_eenheden(ruimte)
            ]

            totaal_criteria: dict[str, CriteriumId] = {}

            def _oppervlakte_vertrek(
                ruimte: EenhedenRuimte,
            ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
                return waardeer_oppervlakte_van_vertrek(ruimte, self.stelselgroep)

            def _oppervlakte_overige(
                ruimte: EenhedenRuimte,
            ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
                return waardeer_oppervlakte_van_overige_ruimte(
                    ruimte, self.stelselgroep
                )

            oppervlakte_berekeningen = {
                Ruimtesoort.vertrek: _oppervlakte_vertrek,
                Ruimtesoort.overige_ruimten: _oppervlakte_overige,
            }

            for ruimte in gedeelde_ruimten:
                if ruimte.detail_soort is None:
                    continue

                ruimtesoort = classificeer_ruimte(ruimte)
                if ruimtesoort is None:
                    continue

                oppervlakte_berekening = oppervlakte_berekeningen.get(ruimtesoort, None)

                if oppervlakte_berekening is not None:
                    oppervlakte_waarderingen = list(oppervlakte_berekening(ruimte))
                else:
                    oppervlakte_waarderingen = []

                # Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:
                #
                # […]
                # * de oppervlakte, na deling door het aantal adressen, per woning minstens
                #   2m2 bedraagt.
                if ruimte.detail_soort in [
                    Ruimtedetailsoort.berging,
                    Ruimtedetailsoort.bergruimte,
                ]:
                    if ruimte.oppervlakte and ruimte.gedeeld_met_aantal_eenheden:
                        gedeelde_oppervlakte = (
                            ruimte.oppervlakte / ruimte.gedeeld_met_aantal_eenheden
                        )
                        if gedeelde_oppervlakte < Decimal("2.0"):
                            logger.info(
                                f"Eenheid ({eenheid.id}): {ruimte.naam} ({ruimte.id}) heeft, na deling door het aantal adressen, een oppervlakte van minder dan 2 m2 en wordt daarom niet gewaardeerd onder {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
                            )
                            oppervlakte_waarderingen = []

                # waarderingen voor de oppervlakten van gedeelde ruimten
                for oppervlakte_waardering in oppervlakte_waarderingen:
                    if oppervlakte_waardering.punten is None:
                        oppervlakte_waardering.punten = float(
                            Decimal(str(oppervlakte_waardering.aantal))
                            * (
                                Decimal("1.0")
                                if ruimtesoort == Ruimtesoort.vertrek
                                else Decimal("0.75")
                            )
                        )

                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, oppervlakte_waarderingen, totaal_criteria
                    )
                )

                # waarderingen voor de keuken van gedeelde ruimten
                keuken_waarderingen = list(
                    waardeer_keuken(ruimte, self.stelsel, self.stelselgroep)
                )
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, keuken_waarderingen, totaal_criteria
                    )
                )

                # waarderingen voor sanitair van gedeelde ruimten
                sanitair_waarderingen = list(
                    waardeer_sanitair(ruimte, self.stelselgroep, self.stelsel)
                )
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, sanitair_waarderingen, totaal_criteria
                    )
                )

            # waarderingen voor de verkoeling en verwarming van gedeelde ruimten
            verkoeling_en_verwarming_waarderingen = list(
                waardeer_verkoeling_en_verwarming(
                    gedeelde_ruimten, self.stelselgroep, self.stelsel
                )
            )

            for ruimte, waardering in verkoeling_en_verwarming_waarderingen:
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, [waardering], totaal_criteria
                    )
                )

            woningwaardering_groep.woningwaarderingen.extend(
                self._maak_adressen_totalen(woningwaardering_groep, totaal_criteria)
            )
            woningwaardering_groep.woningwaarderingen.extend(
                self._maak_verkoeling_subgroep_totalen(
                    woningwaardering_groep, set(totaal_criteria.keys())
                )
            )

        punten = utils.rond_af_op_kwart(
            Decimal(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in woningwaardering_groep.woningwaarderingen
                    or []
                    if woningwaardering.punten is not None
                    and woningwaardering.criterium is not None
                    and woningwaardering.criterium.bovenliggende_criterium is None
                )
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _adressen_totaal_id(
        self,
        ruimte: EenhedenRuimte,
        totaal_criteria: dict[str, CriteriumId],
    ) -> str:
        gedeeld_met = ruimte.gedeeld_met_aantal_eenheden or 1
        totaal_criterium_id = CriteriumId.totaal_deel(
            self.stelselgroep,
            gedeeld_met,
            GedeeldMetSoort.adressen,
            stelsel=self.stelsel,
        )
        totaal_id = str(totaal_criterium_id)
        totaal_criteria[totaal_id] = totaal_criterium_id
        return totaal_id

    def _deel_woningwaarderingen_door_aantal_eenheden(
        self,
        ruimte: EenhedenRuimte,
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
        totaal_criteria: dict[str, CriteriumId],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        for woningwaardering in woningwaarderingen or []:
            woningwaardering.punten = float(
                utils.rond_af(
                    float(
                        Decimal(str(woningwaardering.punten))
                        / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
                    ),
                    decimalen=2,
                )
            )

            if woningwaardering.criterium is not None and (
                woningwaardering.criterium.bovenliggende_criterium is None
            ):
                totaal_id = self._adressen_totaal_id(ruimte, totaal_criteria)
                woningwaardering.criterium.bovenliggende_criterium = (
                    WoningwaarderingCriteriumSleutels(id=totaal_id)
                )

            yield woningwaardering

    def _maak_adressen_totalen(
        self,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
        totaal_criteria: dict[str, CriteriumId],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        for totaal_id, totaal_criterium in totaal_criteria.items():
            punten = sum(
                woningwaardering.punten
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium.id == totaal_id
                and isinstance(woningwaardering.punten, float)
            )
            gedeeld_met = totaal_criterium.gedeeld_met_aantal or 1
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Totaal (gedeeld met {gedeeld_met} eenheden)",
                    id=totaal_id,
                ),
                punten=float(utils.rond_af(punten, decimalen=2)),
            )

    def _maak_verkoeling_subgroep_totalen(
        self,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
        adressen_totaal_ids: set[str],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        criteriumsleutelpunten: dict[str, float] = defaultdict(float)
        for woningwaardering in woningwaardering_groep.woningwaarderingen or []:
            parent_id = (
                woningwaardering.criterium.bovenliggende_criterium.id
                if woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium
                else None
            )
            if (
                parent_id
                and parent_id not in adressen_totaal_ids
                and isinstance(woningwaardering.punten, float)
            ):
                criteriumsleutelpunten[parent_id] += woningwaardering.punten

        for subgroep_id, punten in criteriumsleutelpunten.items():
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=naam_uit_subgroep_criterium_id(subgroep_id),
                    id=subgroep_id,
                ),
                punten=float(utils.rond_af(punten, decimalen=2)),
            )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
