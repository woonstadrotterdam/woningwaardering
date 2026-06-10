from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    bereken_oppervlakte_punten,
    bereken_zolder_correctie,
    is_zolder_zonder_vaste_trap,
    waardeer_keuken,
    waardeer_oppervlakte_van_overige_ruimte,
    waardeer_oppervlakte_van_vertrek,
    waardeer_sanitair,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
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
    RuimtesoortReferentiedata,
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

            woningwaardering_groep.woningwaarderingen.extend(
                self._oppervlakte_waarderingen(gedeelde_ruimten)
            )

            for ruimte in gedeelde_ruimten:
                if ruimte.detail_soort is None:
                    continue

                # waarderingen voor de keuken van gedeelde ruimten
                keuken_waarderingen = list(waardeer_keuken(ruimte, self.stelsel))
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, keuken_waarderingen
                    )
                )

                # waarderingen voor sanitair van gedeelde ruimten
                sanitair_waarderingen = list(
                    waardeer_sanitair(ruimte, self.stelselgroep, self.stelsel)
                )
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, sanitair_waarderingen
                    )
                )

            # waarderingen voor de verkoeling en verwarming van gedeelde ruimten
            verkoeling_en_verwarming_waarderingen = list(
                waardeer_verkoeling_en_verwarming(gedeelde_ruimten)
            )

            for ruimte, waardering in verkoeling_en_verwarming_waarderingen:
                # Hier zetten we de bovenliggende criterium op None omdat deze
                # anders niet in de tabel wordt getoond doordat het bovenliggende
                # criterium zelf niet in de waarderingen voorkomt.
                if waardering.criterium:
                    waardering.criterium.bovenliggende_criterium = None
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, [waardering]
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
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _oppervlakte_waarderingen(
        self, gedeelde_ruimten: list[EenhedenRuimte]
    ) -> list[WoningwaarderingResultatenWoningwaardering]:
        # 2.9.7 Rekenmethode gemeenschappelijke ruimten: oppervlaktepunten volgens
        # paragraaf 2.2. Ruimten worden gegroepeerd per combinatie van aantal adressen
        # en ruimtesoort; per oppervlaktegroep wordt op hele m² afgerond (op het totaal)
        # en daarna door het aantal adressen gedeeld.
        oppervlaktegroepen: defaultdict[
            tuple[int, RuimtesoortReferentiedata], list[EenhedenRuimte]
        ] = defaultdict(list)

        for ruimte in gedeelde_ruimten:
            if (
                ruimte.detail_soort is None
                or ruimte.gedeeld_met_aantal_eenheden is None
            ):
                continue

            ruimtesoort = classificeer_ruimte(ruimte)
            if ruimtesoort not in (Ruimtesoort.vertrek, Ruimtesoort.overige_ruimten):
                continue

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
                            f"Ruimte ({ruimte.id}) heeft, na deling door het aantal adressen, een oppervlakte van minder dan 2 m2 en wordt daarom niet gewaardeerd onder {self.stelselgroep.naam}"
                        )
                        continue

            oppervlaktegroepen[
                (ruimte.gedeeld_met_aantal_eenheden, ruimtesoort)
            ].append(ruimte)

        waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []

        def sorteer_oppervlaktegroepen(
            oppervlaktegroep: tuple[
                tuple[int, RuimtesoortReferentiedata], list[EenhedenRuimte]
            ],
        ) -> tuple[int, str]:
            (aantal_eenheden, ruimtesoort), _ = oppervlaktegroep
            return aantal_eenheden, str(ruimtesoort)

        for groepssleutel, ruimten in sorted(
            oppervlaktegroepen.items(), key=sorteer_oppervlaktegroepen
        ):
            aantal_eenheden, ruimtesoort = groepssleutel
            totaal_oppervlakte = sum(
                (
                    rond_af(ruimte.oppervlakte, decimalen=2)
                    for ruimte in ruimten
                    if ruimte.oppervlakte is not None
                ),
                start=Decimal("0"),
            )
            punten_per_m2 = (
                Decimal("1.0")
                if ruimtesoort == Ruimtesoort.vertrek
                else Decimal("0.75")
            )
            oppervlaktepunten = bereken_oppervlakte_punten(
                totaal_oppervlakte, punten_per_m2
            ) / Decimal(str(aantal_eenheden))

            groep_criterium_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                    criterium=(
                        "vertrekken"
                        if ruimtesoort == Ruimtesoort.vertrek
                        else "overige_ruimten"
                    ),
                )
            )
            groep_criterium_sleutel = WoningwaarderingCriteriumSleutels(
                id=groep_criterium_id
            )

            for ruimte in ruimten:
                if ruimtesoort == Ruimtesoort.vertrek:
                    oppervlakte_waardering = next(
                        waardeer_oppervlakte_van_vertrek(ruimte)
                    )
                else:
                    oppervlakte_waardering = next(
                        waardeer_oppervlakte_van_overige_ruimte(ruimte)
                    )
                if oppervlakte_waardering.criterium is not None:
                    oppervlakte_waardering.criterium.bovenliggende_criterium = (
                        groep_criterium_sleutel
                    )
                    if oppervlakte_waardering.criterium.naam is not None:
                        oppervlakte_waardering.criterium.naam = f"{oppervlakte_waardering.criterium.naam} (gedeeld met {aantal_eenheden})"
                oppervlakte_waardering.punten = None
                waarderingen.append(oppervlakte_waardering)

            if ruimtesoort == Ruimtesoort.overige_ruimten:
                for ruimte in ruimten:
                    if not is_zolder_zonder_vaste_trap(ruimte):
                        continue
                    zolder_oppervlakte = rond_af(ruimte.oppervlakte, decimalen=2)
                    correctie_punten = bereken_zolder_correctie(
                        totaal_oppervlakte, zolder_oppervlakte
                    ) / Decimal(str(aantal_eenheden))
                    waarderingen.append(
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam="Correctie: zolder zonder vaste trap",
                                id=str(
                                    CriteriumId(
                                        stelselgroep=self.stelselgroep,
                                        ruimte_id=ruimte.id,
                                        criterium="correctie_zolder_zonder_vaste_trap",
                                    )
                                ),
                            ),
                            punten=float(correctie_punten),
                        )
                    )

            groep_naam = (
                f"Vertrekken (gedeeld met {aantal_eenheden})"
                if ruimtesoort == Ruimtesoort.vertrek
                else f"Overige ruimten (gedeeld met {aantal_eenheden})"
            )
            waarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=groep_criterium_id,
                        naam=groep_naam,
                    ),
                    punten=float(oppervlaktepunten),
                )
            )

        return waarderingen

    def _deel_woningwaarderingen_door_aantal_eenheden(
        self,
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
    with DevelopmentContext(
        instance=GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
