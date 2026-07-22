from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica import (
    GedeeldeRuimtegroepsleutel,
    GedeeldMet,
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
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Meeteenheid,
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
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

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
            waarderingsgroep_builder.met_onderliggend(
                id="zorgwoning",
                naam="Zorgwoning",
                punten=3.0,
            )
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if utils.gedeeld_met_adressen(ruimte)
            ]

            # waarderingen voor de oppervlakten van gedeelde ruimten
            self._oppervlakte_waarderingen(waarderingsgroep_builder, gedeelde_ruimten)
            # waarderingen voor de verkoeling en verwarming van gedeelde ruimten
            self._verkoeling_en_verwarming_waarderingen(
                waarderingsgroep_builder, gedeelde_ruimten
            )
            # waarderingen voor de keuken van gedeelde ruimten
            self._keuken_waarderingen(waarderingsgroep_builder, gedeelde_ruimten)
            # waarderingen voor sanitair van gedeelde ruimten
            self._sanitair_waarderingen(waarderingsgroep_builder, gedeelde_ruimten)

        woningwaardering_groep = waarderingsgroep_builder.bouw()

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
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        gedeelde_ruimten: list[EenhedenRuimte],
    ) -> None:
        # 2.9.7 Rekenmethode gemeenschappelijke ruimten: oppervlaktepunten volgens
        # paragraaf 2.2. Ruimten worden gegroepeerd per combinatie van aantal adressen
        # en ruimtesoort; per oppervlaktegroep wordt op hele m² afgerond (op het totaal)
        # en daarna door het aantal adressen gedeeld.
        oppervlaktegroepen: defaultdict[
            GedeeldeRuimtegroepsleutel, list[EenhedenRuimte]
        ] = defaultdict(list)

        for ruimte in gedeelde_ruimten:
            if (
                ruimte.detail_soort is None
                or ruimte.gedeeld_met_aantal_adressen is None
            ):
                continue

            ruimtesoort = classificeer_ruimte(ruimte)
            if ruimtesoort not in (Ruimtesoort.vertrek, Ruimtesoort.overige_ruimten):
                continue

            if ruimte.detail_soort in [
                Ruimtedetailsoort.berging,
                Ruimtedetailsoort.bergruimte,
            ]:
                # Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:
                #
                # […]
                # * de oppervlakte, na deling door het aantal adressen, per woning minstens
                #   2m2 bedraagt.
                if ruimte.oppervlakte and ruimte.gedeeld_met_aantal_adressen:
                    gedeelde_oppervlakte = (
                        ruimte.oppervlakte / ruimte.gedeeld_met_aantal_adressen
                    )
                    if gedeelde_oppervlakte < Decimal("2.0"):
                        logger.info(
                            f"Ruimte ({ruimte.id}) heeft, na deling door het aantal adressen, een oppervlakte van minder dan 2 m2 en wordt daarom niet gewaardeerd onder {self.stelselgroep.naam}"
                        )
                        continue

            oppervlaktegroepen[
                (
                    GedeeldMet(
                        ruimte.gedeeld_met_aantal_adressen or 1,
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1,
                    ),
                    ruimtesoort,
                )
            ].append(ruimte)

        def sorteer_oppervlaktegroepen(
            oppervlaktegroep: tuple[GedeeldeRuimtegroepsleutel, list[EenhedenRuimte]],
        ) -> int:
            (gedeeld_met, _ruimtesoort), _ruimten = oppervlaktegroep
            return gedeeld_met.aantal_adressen

        for (gedeeld_met, ruimtesoort), ruimten in sorted(
            oppervlaktegroepen.items(),
            key=sorteer_oppervlaktegroepen,
        ):
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
            deler = Decimal(
                gedeeld_met.aantal_adressen
                * gedeeld_met.aantal_onzelfstandige_woonruimten
            )
            oppervlaktepunten = (
                bereken_oppervlakte_punten(totaal_oppervlakte, punten_per_m2) / deler
            )

            gedeeld_met_laag = waarderingsgroep_builder.gedeeld_met(
                aantal_adressen=gedeeld_met.aantal_adressen,
                aantal_onzelfstandige_woonruimten=gedeeld_met.aantal_onzelfstandige_woonruimten,
            )
            if ruimtesoort == Ruimtesoort.vertrek:
                categorie_lokaal_id = (
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.name
                )
                categorie_naam = "Oppervlakte van vertrekken"
            else:
                categorie_lokaal_id = (
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.name
                )
                categorie_naam = "Oppervlakte van overige ruimten"
            categorie = gedeeld_met_laag.categorie(
                id=categorie_lokaal_id,
                naam=categorie_naam,
            )

            heeft_zolder_zonder_trap = (
                ruimtesoort == Ruimtesoort.overige_ruimten
                and any(is_zolder_zonder_vaste_trap(ruimte) for ruimte in ruimten)
            )
            if heeft_zolder_zonder_trap:
                detail_bovenliggende = categorie.met_onderliggend(
                    id="subtotaal",
                    naam="Subtotaal",
                    punten=oppervlaktepunten,
                    aantal=float(totaal_oppervlakte),
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                )
            else:
                detail_bovenliggende = categorie

            for ruimte in ruimten:
                if ruimtesoort == Ruimtesoort.vertrek:
                    waardeer_oppervlakte_van_vertrek(
                        ruimte,
                        waarderingsgroep_builder=detail_bovenliggende,
                    )
                else:
                    waardeer_oppervlakte_van_overige_ruimte(
                        ruimte,
                        waarderingsgroep_builder=detail_bovenliggende,
                    )

            if ruimtesoort == Ruimtesoort.overige_ruimten:
                for ruimte in ruimten:
                    if not is_zolder_zonder_vaste_trap(ruimte):
                        continue
                    zolder_oppervlakte = rond_af(ruimte.oppervlakte, decimalen=2)
                    correctie_punten = (
                        bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)
                        / deler
                    )
                    categorie.met_onderliggend(
                        id=f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
                        naam="Correctie: zolder zonder vaste trap",
                        punten=correctie_punten,
                    )

            # In het zoldergeval draagt de Subtotaal-waardering de oppervlaktepunten; anders
            # krijgt de categorie-waardering zelf de punten.
            if not heeft_zolder_zonder_trap:
                categorie.punten = oppervlaktepunten

    def _verkoeling_en_verwarming_waarderingen(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        gedeelde_ruimten: list[EenhedenRuimte],
    ) -> None:
        def subgroep(
            ruimte: EenhedenRuimte, subgroep_id: str, subgroep_naam: str
        ) -> WaarderingBuilder:
            gedeeld_met_laag = waarderingsgroep_builder.gedeeld_met(
                aantal_adressen=ruimte.gedeeld_met_aantal_adressen or 1,
                aantal_onzelfstandige_woonruimten=(
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                ),
            )
            verkoeling_categorie = gedeeld_met_laag.categorie(
                id=Woningwaarderingstelselgroep.verkoeling_en_verwarming.name,
                naam="Verkoeling en verwarming",
            )
            return verkoeling_categorie.categorie(
                id=subgroep_id,
                naam=subgroep_naam,
            )

        for ruimte, waardering in waardeer_verkoeling_en_verwarming(
            gedeelde_ruimten, subgroep=subgroep
        ):
            if waardering.punten is None:
                continue
            aantal_adressen = ruimte.gedeeld_met_aantal_adressen or 1
            waardering.punten = float(
                rond_af(
                    Decimal(str(waardering.punten)) / Decimal(str(aantal_adressen)),
                    decimalen=2,
                )
            )

    def _keuken_waarderingen(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                continue
            aantal_adressen = ruimte.gedeeld_met_aantal_adressen or 1
            gedeeld_met_laag = waarderingsgroep_builder.gedeeld_met(
                aantal_adressen=aantal_adressen,
            )
            keuken_categorie = gedeeld_met_laag.categorie(
                id="keuken",
                naam="Keuken",
            )
            ruimte_waarderingen = waardeer_keuken(
                ruimte,
                self.stelsel,
                waarderingsgroep_builder=keuken_categorie,
                deler=aantal_adressen,
            )
            if not ruimte_waarderingen:
                continue

    def _sanitair_waarderingen(
        self,
        waarderingsgroep_builder: WaarderingsgroepBuilder,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                continue
            aantal_adressen = ruimte.gedeeld_met_aantal_adressen or 1
            gedeeld_met_laag = waarderingsgroep_builder.gedeeld_met(
                aantal_adressen=aantal_adressen,
            )
            sanitair_categorie = gedeeld_met_laag.categorie(
                id="sanitair",
                naam="Sanitair",
            )
            waarderingen = waardeer_sanitair(
                ruimte,
                self.stelsel,
                waarderingsgroep_builder=sanitair_categorie,
                deler=aantal_adressen,
            )
            if not waarderingen:
                continue


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
