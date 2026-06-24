from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import NamedTuple

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
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


class Oppervlaktegroepsleutel(NamedTuple):
    aantal_eenheden: int
    ruimtesoort: RuimtesoortReferentiedata


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
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
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
            waarderingsgroep_bouwer.maak_onderliggende(
                id="zorgwoning",
                naam="Zorgwoning",
                punten=3.0,
            )
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if utils.gedeeld_met_eenheden(ruimte)
            ]

            self._oppervlakte_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)
            self._verkoeling_en_verwarming_waarderingen(
                waarderingsgroep_bouwer, gedeelde_ruimten
            )
            self._keuken_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)
            self._sanitair_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

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
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        gedeelde_ruimten: list[EenhedenRuimte],
    ) -> None:
        # 2.9.7 Rekenmethode gemeenschappelijke ruimten: oppervlaktepunten volgens
        # paragraaf 2.2. Ruimten worden gegroepeerd per combinatie van aantal adressen
        # en ruimtesoort; per oppervlaktegroep wordt op hele m² afgerond (op het totaal)
        # en daarna door het aantal adressen gedeeld.
        oppervlaktegroepen: defaultdict[
            Oppervlaktegroepsleutel, list[EenhedenRuimte]
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
                Oppervlaktegroepsleutel(
                    ruimte.gedeeld_met_aantal_eenheden,
                    ruimtesoort,
                )
            ].append(ruimte)

        def sorteer_oppervlaktegroepen(
            oppervlaktegroep: tuple[Oppervlaktegroepsleutel, list[EenhedenRuimte]],
        ) -> int:
            sleutel, _ruimten = oppervlaktegroep
            return sleutel.aantal_eenheden

        for groepssleutel, ruimten in sorted(
            oppervlaktegroepen.items(),
            key=sorteer_oppervlaktegroepen,
        ):
            aantal_eenheden = groepssleutel.aantal_eenheden
            ruimtesoort = groepssleutel.ruimtesoort
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

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
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
            categorie = gedeeld_met_laag.maak_onderliggende(
                id=categorie_lokaal_id,
                naam=categorie_naam,
            )

            heeft_zolder_zonder_trap = (
                ruimtesoort == Ruimtesoort.overige_ruimten
                and any(is_zolder_zonder_vaste_trap(ruimte) for ruimte in ruimten)
            )
            if heeft_zolder_zonder_trap:
                detail_bovenliggende = categorie.maak_onderliggende(
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
                        waarderingsgroep_bouwer=detail_bovenliggende,
                    )
                else:
                    waardeer_oppervlakte_van_overige_ruimte(
                        ruimte,
                        waarderingsgroep_bouwer=detail_bovenliggende,
                    )

            if ruimtesoort == Ruimtesoort.overige_ruimten:
                for ruimte in ruimten:
                    if not is_zolder_zonder_vaste_trap(ruimte):
                        continue
                    zolder_oppervlakte = rond_af(ruimte.oppervlakte, decimalen=2)
                    correctie_punten = bereken_zolder_correctie(
                        totaal_oppervlakte, zolder_oppervlakte
                    ) / Decimal(str(aantal_eenheden))
                    categorie.maak_onderliggende(
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
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        gedeelde_ruimten: list[EenhedenRuimte],
    ) -> None:
        ruimten_per_groep: defaultdict[int, list[EenhedenRuimte]] = defaultdict(list)
        for ruimte in gedeelde_ruimten:
            ruimten_per_groep[ruimte.gedeeld_met_aantal_eenheden or 1].append(ruimte)

        for aantal_eenheden, groep_ruimten in sorted(ruimten_per_groep.items()):
            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
            )
            verkoeling_categorie = gedeeld_met_laag.maak_onderliggende(
                id=Woningwaarderingstelselgroep.verkoeling_en_verwarming.name,
                naam="Verkoeling en verwarming",
            )

            # De helper bouwt subgroepen en detailwaarderingen rechtstreeks onder de
            # verkoeling-categorie; voor gemeenschappelijke ruimten worden de punten
            # vervolgens door het aantal adressen gedeeld.
            for _ruimte, resultaat in waardeer_verkoeling_en_verwarming(
                groep_ruimten,
                waarderingsgroep_bouwer=verkoeling_categorie,
            ):
                if resultaat.punten is None:
                    continue
                resultaat.punten = float(
                    utils.rond_af(
                        Decimal(str(resultaat.punten)) / Decimal(str(aantal_eenheden)),
                        decimalen=2,
                    )
                )

            if verkoeling_categorie.is_leeg:
                verkoeling_categorie.verwijder()

    def _keuken_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        keuken_categorieen: dict[str, WaarderingBouwer] = {}

        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                continue
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
            )
            laag_id = gedeeld_met_laag.criterium_id
            keuken_categorie = keuken_categorieen.get(laag_id)
            categorie_is_nieuw = keuken_categorie is None
            if keuken_categorie is None:
                keuken_categorie = gedeeld_met_laag.maak_onderliggende(
                    id="keuken",
                    naam="Keuken",
                )

            ruimte_waarderingen = waardeer_keuken(
                ruimte,
                self.stelsel,
                waarderingsgroep_bouwer=keuken_categorie,
                deler=aantal_eenheden,
            )
            if not ruimte_waarderingen:
                if categorie_is_nieuw and keuken_categorie.is_leeg:
                    keuken_categorie.verwijder()
                continue
            keuken_categorieen[laag_id] = keuken_categorie

    def _sanitair_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        sanitair_categorieen: dict[str, WaarderingBouwer] = {}

        for ruimte in ruimten:
            if ruimte.detail_soort is None:
                continue
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
            )
            laag_id = gedeeld_met_laag.criterium_id
            sanitair_categorie = sanitair_categorieen.get(laag_id)
            categorie_is_nieuw = sanitair_categorie is None
            if sanitair_categorie is None:
                sanitair_categorie = gedeeld_met_laag.maak_onderliggende(
                    id="sanitair",
                    naam="Sanitair",
                )

            ruimte_waarderingen = waardeer_sanitair(
                ruimte,
                self.stelsel,
                waarderingsgroep_bouwer=sanitair_categorie,
                deler=aantal_eenheden,
            )
            if not ruimte_waarderingen:
                if categorie_is_nieuw and sanitair_categorie.is_leeg:
                    sanitair_categorie.verwijder()
                continue
            sanitair_categorieen[laag_id] = sanitair_categorie


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,
        log_level="DEBUG",
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer("tests/data/generiek/input/37101000032.json")
