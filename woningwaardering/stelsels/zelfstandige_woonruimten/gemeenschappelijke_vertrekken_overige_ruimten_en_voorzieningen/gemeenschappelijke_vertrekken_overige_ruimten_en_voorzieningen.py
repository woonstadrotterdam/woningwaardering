from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import (
    CriteriumId,
    GedeeldMetSoort,
    nest_onder,
)
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
    Referentiedata,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Meeteenheid,
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
            gedeeld_met_eenheden: set[int] = set()

            woningwaardering_groep.woningwaarderingen.extend(
                self._oppervlakte_waarderingen(gedeelde_ruimten, gedeeld_met_eenheden)
            )
            woningwaardering_groep.woningwaarderingen.extend(
                self._verkoeling_en_verwarming_waarderingen(
                    gedeelde_ruimten, gedeeld_met_eenheden
                )
            )
            woningwaardering_groep.woningwaarderingen.extend(
                self._keuken_waarderingen(gedeelde_ruimten, gedeeld_met_eenheden)
            )
            woningwaardering_groep.woningwaarderingen.extend(
                self._sanitair_waarderingen(gedeelde_ruimten, gedeeld_met_eenheden)
            )

            for aantal_eenheden in sorted(gedeeld_met_eenheden):
                adressen_id = str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        gedeeld_met_aantal=aantal_eenheden,
                        gedeeld_met_soort=GedeeldMetSoort.adressen,
                    )
                )
                woningwaardering_groep.woningwaarderingen.append(
                    self._maak_woningwaardering(
                        id=adressen_id,
                        criterium=utils.naam_gedeeld_met_groep(
                            aantal_eenheden,
                            soort=GedeeldMetSoort.adressen,
                        ),
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

    def _maak_woningwaardering(
        self,
        criterium: str,
        *,
        punten: Decimal | float | None = None,
        bovenliggende_criterium_id: str | None = None,
        aantal: float | None = None,
        meeteenheid: Referentiedata | None = None,
        id: str | None = None,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering = WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                id=id,
                meeteenheid=meeteenheid,
                naam=criterium,
            ),
            aantal=aantal,
            punten=float(punten) if punten is not None else None,
        )
        if bovenliggende_criterium_id and woningwaardering.criterium:
            woningwaardering.criterium.bovenliggende_criterium = (
                WoningwaarderingCriteriumSleutels(id=bovenliggende_criterium_id)
            )
        return woningwaardering

    def _oppervlakte_waarderingen(
        self,
        gedeelde_ruimten: list[EenhedenRuimte],
        gedeeld_met_eenheden: set[int],
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

        for (aantal_eenheden, ruimtesoort), ruimten in sorted(
            oppervlaktegroepen.items(),
            key=lambda item: (item[0][0], str(item[0][1])),
        ):
            gedeeld_met_eenheden.add(aantal_eenheden)
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

            adressen_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                )
            )
            if ruimtesoort == Ruimtesoort.vertrek:
                categorie_id = nest_onder(
                    adressen_id,
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name,
                )
                categorie_naam = "Oppervlakte van vertrekken"
            else:
                categorie_id = nest_onder(
                    adressen_id,
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name,
                )
                categorie_naam = "Oppervlakte van overige ruimten"

            heeft_zolder_zonder_trap = (
                ruimtesoort == Ruimtesoort.overige_ruimten
                and any(is_zolder_zonder_vaste_trap(ruimte) for ruimte in ruimten)
            )
            detail_bovenliggende_id = (
                nest_onder(categorie_id, "subtotaal")
                if heeft_zolder_zonder_trap
                else categorie_id
            )
            detail_waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []

            for ruimte in ruimten:
                if ruimtesoort == Ruimtesoort.vertrek:
                    oppervlakte_resultaat = next(
                        waardeer_oppervlakte_van_vertrek(ruimte)
                    )
                else:
                    oppervlakte_resultaat = next(
                        waardeer_oppervlakte_van_overige_ruimte(ruimte)
                    )
                if (
                    oppervlakte_resultaat.criterium is None
                    or oppervlakte_resultaat.criterium.naam is None
                    or oppervlakte_resultaat.criterium.id is None
                ):
                    continue

                detail_waarderingen.append(
                    self._maak_woningwaardering(
                        criterium=oppervlakte_resultaat.criterium.naam,
                        bovenliggende_criterium_id=detail_bovenliggende_id,
                        aantal=oppervlakte_resultaat.aantal,
                        meeteenheid=Meeteenheid.vierkante_meter_m2,
                        id=nest_onder(
                            detail_bovenliggende_id, oppervlakte_resultaat.criterium.id
                        ),
                    )
                )

            correctie_waarderingen: list[
                WoningwaarderingResultatenWoningwaardering
            ] = []
            if ruimtesoort == Ruimtesoort.overige_ruimten:
                for ruimte in ruimten:
                    if not is_zolder_zonder_vaste_trap(ruimte):
                        continue
                    zolder_oppervlakte = rond_af(ruimte.oppervlakte, decimalen=2)
                    correctie_punten = bereken_zolder_correctie(
                        totaal_oppervlakte, zolder_oppervlakte
                    ) / Decimal(str(aantal_eenheden))
                    correctie_waarderingen.append(
                        self._maak_woningwaardering(
                            punten=correctie_punten,
                            criterium="Correctie: zolder zonder vaste trap",
                            bovenliggende_criterium_id=categorie_id,
                            id=nest_onder(
                                categorie_id,
                                str(
                                    CriteriumId(
                                        stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
                                        ruimte_id=ruimte.id,
                                        criterium="correctie_zolder_zonder_vaste_trap",
                                    )
                                ),
                            ),
                        )
                    )

            if heeft_zolder_zonder_trap:
                waarderingen.append(
                    self._maak_woningwaardering(
                        punten=oppervlaktepunten,
                        criterium="Subtotaal",
                        bovenliggende_criterium_id=categorie_id,
                        aantal=float(totaal_oppervlakte),
                        meeteenheid=Meeteenheid.vierkante_meter_m2,
                        id=detail_bovenliggende_id,
                    )
                )
                waarderingen.extend(detail_waarderingen)
                waarderingen.extend(correctie_waarderingen)
                waarderingen.append(
                    self._maak_woningwaardering(
                        criterium=categorie_naam,
                        bovenliggende_criterium_id=adressen_id,
                        id=categorie_id,
                    )
                )
            else:
                waarderingen.extend(detail_waarderingen)
                waarderingen.append(
                    self._maak_woningwaardering(
                        punten=oppervlaktepunten,
                        criterium=categorie_naam,
                        bovenliggende_criterium_id=adressen_id,
                        id=categorie_id,
                    )
                )

        return waarderingen

    def _verkoeling_en_verwarming_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_eenheden: set[int],
    ) -> list[WoningwaarderingResultatenWoningwaardering]:
        waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        verkoeling_subgroepen: dict[str, tuple[str, str]] = {}
        verkoeling_categorieen: dict[str, str] = {}

        for ruimte, resultaat in waardeer_verkoeling_en_verwarming(ruimten):
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            gedeeld_met_eenheden.add(aantal_eenheden)

            if resultaat.punten is None:
                continue
            criterium = resultaat.criterium
            if (
                criterium is None
                or criterium.id is None
                or criterium.bovenliggende_criterium is None
                or criterium.bovenliggende_criterium.id is None
            ):
                continue

            punten = float(
                utils.rond_af(
                    Decimal(str(resultaat.punten)) / Decimal(str(aantal_eenheden)),
                    decimalen=2,
                )
            )
            adressen_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                )
            )
            verkoeling_categorie_id = nest_onder(
                adressen_id, Woningwaarderingstelselgroep.verkoeling_en_verwarming.name
            )
            verkoeling_categorieen[verkoeling_categorie_id] = adressen_id

            subgroep_id = nest_onder(
                verkoeling_categorie_id, criterium.bovenliggende_criterium.id
            )
            subgroep_naam = (
                criterium.bovenliggende_criterium.id.split("__")[-1]
                .capitalize()
                .replace("_", " ")
            )
            verkoeling_subgroepen[subgroep_id] = (
                subgroep_naam,
                verkoeling_categorie_id,
            )

            criterium_naam = (
                criterium.naam or "Maximaal aantal punten"
                if resultaat.punten < 0
                else ruimte.naam or criterium.naam or ""
            )
            if resultaat.punten < 0:
                detail_id = nest_onder(subgroep_id, "max_aantal_punten")
            else:
                detail_id = nest_onder(subgroep_id, criterium.id)

            waarderingen.append(
                self._maak_woningwaardering(
                    punten=punten,
                    criterium=criterium_naam,
                    bovenliggende_criterium_id=subgroep_id,
                    aantal=resultaat.aantal,
                    meeteenheid=criterium.meeteenheid,
                    id=detail_id,
                )
            )

        for subgroep_id, (subgroep_naam, verkoeling_categorie_id) in sorted(
            verkoeling_subgroepen.items()
        ):
            waarderingen.append(
                self._maak_woningwaardering(
                    criterium=subgroep_naam,
                    bovenliggende_criterium_id=verkoeling_categorie_id,
                    id=subgroep_id,
                )
            )

        for verkoeling_categorie_id, adressen_id in sorted(
            verkoeling_categorieen.items()
        ):
            waarderingen.append(
                self._maak_woningwaardering(
                    criterium="Verkoeling en verwarming",
                    bovenliggende_criterium_id=adressen_id,
                    id=verkoeling_categorie_id,
                )
            )

        return waarderingen

    def _keuken_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_eenheden: set[int],
    ) -> list[WoningwaarderingResultatenWoningwaardering]:
        waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        keuken_categorieen: dict[str, str] = {}

        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                continue
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            gedeeld_met_eenheden.add(aantal_eenheden)
            adressen_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                )
            )
            keuken_categorie_id = nest_onder(adressen_id, "keuken")

            for waardering in waardeer_keuken(ruimte, self.stelsel):
                if (
                    waardering.criterium is None
                    or waardering.criterium.id is None
                    or not waardering.punten
                ):
                    continue

                keuken_categorieen[keuken_categorie_id] = adressen_id
                punten = Decimal(str(waardering.punten)) / Decimal(str(aantal_eenheden))
                waarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=waardering.criterium.naam or ruimte.naam or "",
                        bovenliggende_criterium_id=keuken_categorie_id,
                        aantal=waardering.aantal,
                        meeteenheid=waardering.criterium.meeteenheid,
                        id=nest_onder(keuken_categorie_id, waardering.criterium.id),
                    )
                )

        for keuken_categorie_id, adressen_id in sorted(keuken_categorieen.items()):
            waarderingen.append(
                self._maak_woningwaardering(
                    criterium="Keuken",
                    bovenliggende_criterium_id=adressen_id,
                    id=keuken_categorie_id,
                )
            )

        return waarderingen

    def _sanitair_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_eenheden: set[int],
    ) -> list[WoningwaarderingResultatenWoningwaardering]:
        waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        sanitair_categorieen: dict[str, str] = {}

        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                continue
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            gedeeld_met_eenheden.add(aantal_eenheden)
            adressen_id = str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    gedeeld_met_aantal=aantal_eenheden,
                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                )
            )
            sanitair_categorie_id = nest_onder(adressen_id, "sanitair")

            for waardering in waardeer_sanitair(
                ruimte, self.stelselgroep, self.stelsel
            ):
                if (
                    waardering.criterium is None
                    or waardering.criterium.id is None
                    or waardering.criterium.naam is None
                    or waardering.punten is None
                ):
                    continue

                sanitair_categorieen[sanitair_categorie_id] = adressen_id
                punten = float(
                    utils.rond_af(
                        Decimal(str(waardering.punten)) / Decimal(str(aantal_eenheden)),
                        decimalen=2,
                    )
                )
                waarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=waardering.criterium.naam,
                        bovenliggende_criterium_id=sanitair_categorie_id,
                        aantal=waardering.aantal,
                        meeteenheid=waardering.criterium.meeteenheid,
                        id=nest_onder(sanitair_categorie_id, waardering.criterium.id),
                    )
                )

        for sanitair_categorie_id, adressen_id in sorted(sanitair_categorieen.items()):
            waarderingen.append(
                self._maak_woningwaardering(
                    criterium="Sanitair",
                    bovenliggende_criterium_id=adressen_id,
                    id=sanitair_categorie_id,
                )
            )

        return waarderingen


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,
        log_level="DEBUG",
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
