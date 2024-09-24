from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.keuken import Keuken
from woningwaardering.stelsels.zelfstandige_woonruimten.oppervlakte_van_overige_ruimten import (
    OppervlakteVanOverigeRuimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.sanitair import Sanitair
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import (
    classificeer_ruimte,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.verkoeling_en_verwarming import (
    VerkoelingEnVerwarming,
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
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

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
                stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.value,
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
        if (
            eenheid.doelgroep is not None
            and eenheid.doelgroep.code == Doelgroep.zorg.code
        ):
            logger.info(
                f"Eenheid {eenheid.id} is een zorgwoning en wordt met 3 punten gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
            )
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Zorgwoning",
                    ),
                    punten=3.0,
                )
            )
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if ruimte.gedeeld_met_aantal_eenheden is not None
                and ruimte.gedeeld_met_aantal_eenheden > 1
            ]

            oppervlakte_berekeningen = {
                Ruimtesoort.vertrek: OppervlakteVanVertrekken.genereer_woningwaarderingen,
                Ruimtesoort.overige_ruimten: OppervlakteVanOverigeRuimten.genereer_woningwaarderingen,
            }

            for ruimte in gedeelde_ruimten:
                if ruimte.detail_soort is None:
                    continue

                ruimtesoort = classificeer_ruimte(ruimte)
                if ruimtesoort is None:
                    continue

                oppervlakte_berekening = oppervlakte_berekeningen.get(ruimtesoort, None)

                if oppervlakte_berekening is not None:
                    oppervlakte_waarderingen = list(
                        oppervlakte_berekening(ruimte, self.stelselgroep)
                    )
                # Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:
                #
                # […]
                # * de oppervlakte, na deling door het aantal adressen, per woning minstens
                #   2m2 bedraagt.
                if ruimte.detail_soort.code == Ruimtedetailsoort.berging.code:
                    if ruimte.oppervlakte and ruimte.gedeeld_met_aantal_eenheden:
                        gedeelde_oppervlakte = (
                            ruimte.oppervlakte / ruimte.gedeeld_met_aantal_eenheden
                        )
                        if gedeelde_oppervlakte < Decimal("2.0"):
                            logger.info(
                                f"Eenheid {eenheid.id}: {Ruimtedetailsoort.berging.naam} ({ruimte.id}) heeft, na deling door het aantal adressen, een oppervlakte van minder dan 2 m2 en wordt daarom niet gewaardeerd onder {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
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
                    self.deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, oppervlakte_waarderingen
                    )
                )

                # waarderingen voor de verkoeling en verwarming van gedeelde ruimten
                verkoeling_en_verwarming_waarderingen = list(
                    VerkoelingEnVerwarming.genereer_woningwaarderingen(
                        ruimte, self.stelselgroep
                    )
                )

                woningwaardering_groep.woningwaarderingen.extend(
                    self.deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, verkoeling_en_verwarming_waarderingen
                    )
                )

                # waarderingen voor de keuken van gedeelde ruimten
                keuken_waarderingen = list(
                    Keuken.genereer_woningwaarderingen(ruimte, self.stelselgroep)
                )
                woningwaardering_groep.woningwaarderingen.extend(
                    self.deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, keuken_waarderingen
                    )
                )

                # waarderingen voor sanitair van gedeelde ruimten
                sanitair_waarderingen = list(
                    Sanitair.genereer_woningwaarderingen(ruimte, self.stelselgroep)
                )
                woningwaardering_groep.woningwaarderingen.extend(
                    self.deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, sanitair_waarderingen
                    )
                )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
        )
        return woningwaardering_groep

    @staticmethod
    def deel_woningwaarderingen_door_aantal_eenheden(
        ruimte: EenhedenRuimte,
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
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

            if (
                woningwaardering.criterium is not None
                and woningwaardering.criterium.naam is not None
            ):
                woningwaardering.criterium.naam = f"{woningwaardering.criterium.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden})"
            yield woningwaardering


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen = (
        GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date.fromisoformat("2024-07-01")
        )
    )

    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen/input/verwarmde_vertrekken.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[
            gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.bereken(
                eenheid
            )
        ]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
