import warnings
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
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.sanitair import (
    Sanitair as OnzelfstandigeWoonruimtenSanitair,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Meeteenheid,
    Ruimtesoort,
    RuimtesoortReferentiedata,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Oppervlaktegroepsleutel(NamedTuple):
    aantal_eenheden: int
    aantal_onzelfstandige_woonruimten: int
    ruimtesoort: RuimtesoortReferentiedata


def _lokaal_segment(volledige_id: str, bovenliggende_id: str) -> str:
    prefix = f"{bovenliggende_id}__"
    if volledige_id.startswith(prefix):
        return volledige_id[len(prefix) :]
    return volledige_id.split("__")[-1]


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
        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            self.stelsel, self.stelselgroep
        )

        if not self._zorgwoning(waarderingsgroep_bouwer, eenheid):
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if ruimte.gedeeld_met_aantal_eenheden is not None
                and ruimte.gedeeld_met_aantal_eenheden > 1
            ]

            self._oppervlakte_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)
            self._verkoeling_en_verwarming_waarderingen(
                waarderingsgroep_bouwer, gedeelde_ruimten
            )
            self._keuken_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)
            self._sanitair_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid {eenheid.id} krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _zorgwoning(
        self, waarderingsgroep_bouwer: WaarderingsgroepBouwer, eenheid: EenhedenEenheid
    ) -> WaarderingBouwer | None:
        """
        Beleidsboek: De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en
        voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning
        veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief
        meetwerk te voorkomen waardeert de Huurcommissie in dat geval een waardering
        van 3 punten per woning.

        Args:
            waarderingsgroep_bouwer (WaarderingsgroepBouwer): Bouwer voor deze stelselgroep
            eenheid (EenhedenEenheid): Eenheid

        Returns:
            WaarderingBouwer | None: Woningwaardering van 3 punten voor een zorgwoning of None als de eenheid geen zorgwoning is
        """
        if eenheid.doelgroep == Doelgroep.zorg:
            logger.info(
                f"Eenheid {eenheid.id} is een zorgwoning en krijgt 3 punten voor {self.stelselgroep.naam}"
            )
            return waarderingsgroep_bouwer.maak_onderliggende(
                id="zorgwoning",
                naam="Zorgwoning",
                punten=3.0,
            )
        logger.debug(
            f"Eenheid {eenheid.id} is geen zorgwoning en krijgt daarvoor geen punten voor {self.stelselgroep.naam}"
        )
        return None

    def _oppervlakte_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        # 2.9.7 -> 2.2: ruimten worden gegroepeerd per combinatie van aantal adressen,
        # aantal onzelfstandige woonruimten en ruimtesoort. Per oppervlaktegroep wordt op
        # hele m² afgerond (op het totaal) en daarna door beide aantallen gedeeld.
        oppervlaktegroepen: defaultdict[
            Oppervlaktegroepsleutel, list[EenhedenRuimte]
        ] = defaultdict(list)

        for ruimte in ruimten:
            if ruimte.gedeeld_met_aantal_eenheden is None:
                continue
            ruimtesoort = utils.classificeer_ruimte(ruimte)
            if ruimtesoort not in (Ruimtesoort.vertrek, Ruimtesoort.overige_ruimten):
                continue
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            oppervlaktegroepen[
                Oppervlaktegroepsleutel(
                    ruimte.gedeeld_met_aantal_eenheden,
                    aantal_onzelfstandige_woonruimten,
                    ruimtesoort,
                )
            ].append(ruimte)

        def sorteer_oppervlaktegroepen(
            oppervlaktegroep: tuple[Oppervlaktegroepsleutel, list[EenhedenRuimte]],
        ) -> tuple[int, int]:
            sleutel, _ruimten = oppervlaktegroep
            return sleutel.aantal_eenheden, sleutel.aantal_onzelfstandige_woonruimten

        for sleutel, groep_ruimten in sorted(
            oppervlaktegroepen.items(), key=sorteer_oppervlaktegroepen
        ):
            totaal_oppervlakte = sum(
                (
                    utils.rond_af(ruimte.oppervlakte, decimalen=2)
                    for ruimte in groep_ruimten
                    if ruimte.oppervlakte is not None
                ),
                start=Decimal("0"),
            )
            punten_per_m2 = (
                Decimal("1.0")
                if sleutel.ruimtesoort == Ruimtesoort.vertrek
                else Decimal("0.75")
            )
            oppervlaktepunten = (
                bereken_oppervlakte_punten(totaal_oppervlakte, punten_per_m2)
                / Decimal(str(sleutel.aantal_eenheden))
                / Decimal(str(sleutel.aantal_onzelfstandige_woonruimten))
            )

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=sleutel.aantal_eenheden,
                aantal_onzelfstandige_woonruimten=sleutel.aantal_onzelfstandige_woonruimten,
            )
            if sleutel.ruimtesoort == Ruimtesoort.vertrek:
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
                sleutel.ruimtesoort == Ruimtesoort.overige_ruimten
                and any(is_zolder_zonder_vaste_trap(ruimte) for ruimte in groep_ruimten)
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

            for ruimte in groep_ruimten:
                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue

                if sleutel.ruimtesoort == Ruimtesoort.vertrek:
                    waardeer_oppervlakte_van_vertrek(
                        ruimte,
                        waarderingsgroep_bouwer=detail_bovenliggende,
                    )
                else:
                    waardeer_oppervlakte_van_overige_ruimte(
                        ruimte,
                        waarderingsgroep_bouwer=detail_bovenliggende,
                    )

            if sleutel.ruimtesoort == Ruimtesoort.overige_ruimten:
                for ruimte in groep_ruimten:
                    if not is_zolder_zonder_vaste_trap(ruimte):
                        continue
                    zolder_oppervlakte = utils.rond_af(ruimte.oppervlakte, decimalen=2)
                    correctie_punten = (
                        bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)
                        / Decimal(str(sleutel.aantal_eenheden))
                        / Decimal(str(sleutel.aantal_onzelfstandige_woonruimten))
                    )
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
        ruimten: list[EenhedenRuimte],
    ) -> None:
        # De maximering op verwarmde overige ruimten (max. 4 punten) en op verkoelde
        # vertrekken (max. 2 punten) telt over álle gedeelde ruimten samen, ongeacht
        # met hoeveel adressen/onzelfstandige woonruimten ze gedeeld worden. We roepen
        # de helper daarom eenmalig aan op een tijdelijke waarderingsgroep_bouwer (zodat de teller
        # globaal is) en routeren elk resultaat daarna naar de juiste adressengroep,
        # waar de punten door het aantal adressen en onzelfstandige woonruimten worden
        # gedeeld.
        tijdelijk = WaarderingsgroepBouwer(self.stelsel, self.stelselgroep)

        verkoeling_per_laag: dict[str, WaarderingBouwer] = {}
        subgroep_per_id: dict[str, WaarderingBouwer] = {}

        for ruimte, resultaat in waardeer_verkoeling_en_verwarming(
            ruimten,
            waarderingsgroep_bouwer=tijdelijk,
        ):
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            deler = Decimal(str(aantal_eenheden)) * Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
                aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
            )
            laag_id = gedeeld_met_laag.criterium_id

            verkoeling_categorie = verkoeling_per_laag.get(laag_id)
            if verkoeling_categorie is None:
                verkoeling_categorie = gedeeld_met_laag.maak_onderliggende(
                    id=Woningwaarderingstelselgroep.verkoeling_en_verwarming.name,
                    naam="Verkoeling en verwarming",
                )
                verkoeling_per_laag[laag_id] = verkoeling_categorie

            subgroep_segment = (resultaat.bovenliggende_id or "").split("__")[-1]
            subgroep_id = f"{verkoeling_categorie.criterium_id}__{subgroep_segment}"
            subgroep = subgroep_per_id.get(subgroep_id)
            if subgroep is None:
                subgroep = verkoeling_categorie.maak_onderliggende(
                    id=subgroep_segment,
                    naam=subgroep_segment.capitalize().replace("_", " "),
                )
                subgroep_per_id[subgroep_id] = subgroep

            punten = (
                None
                if resultaat.punten is None
                else Decimal(str(resultaat.punten)) / deler
            )
            subgroep.maak_onderliggende(
                id=resultaat.criterium_id.split("__")[-1],
                naam=resultaat.naam,
                punten=punten,
                aantal=resultaat.aantal,
                meeteenheid=resultaat.meeteenheid,
            )

    def _sanitair_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        sanitair_categorieen: dict[str, WaarderingBouwer] = {}
        woningwaarderingen_met_ruimten = list(
            OnzelfstandigeWoonruimtenSanitair.genereer_woningwaarderingen(
                ruimten, self.stelselgroep
            )
        )

        for ruimte, waarderingen in woningwaarderingen_met_ruimten:
            if ruimte.soort is None:
                warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                continue

            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            deler = Decimal(str(aantal_eenheden)) * Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
                aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
            )
            laag_id = gedeeld_met_laag.criterium_id
            sanitair_categorie = sanitair_categorieen.get(laag_id)
            if sanitair_categorie is None:
                sanitair_categorie = gedeeld_met_laag.maak_onderliggende(
                    id="sanitair",
                    naam="Sanitair",
                )
                sanitair_categorieen[laag_id] = sanitair_categorie

            ruimte_criterium = waarderingen[0]
            reparented_ruimte = sanitair_categorie.maak_onderliggende(
                id=_lokaal_segment(
                    ruimte_criterium.criterium_id,
                    Woningwaarderingstelselgroep.sanitair.name,
                ),
                naam=ruimte_criterium.naam,
            )

            for waardering in waarderingen[1:]:
                if waardering.punten is None:
                    continue

                punten = Decimal(str(waardering.punten)) / deler
                reparented_ruimte.maak_onderliggende(
                    id=_lokaal_segment(
                        waardering.criterium_id, ruimte_criterium.criterium_id
                    ),
                    naam=waardering.naam,
                    punten=punten,
                    aantal=waardering.aantal,
                    meeteenheid=waardering.meeteenheid,
                )

    def _keuken_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        keuken_categorieen: dict[str, WaarderingBouwer] = {}
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            deler = Decimal(str(aantal_eenheden)) * Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met_laag(
                aantal_eenheden=aantal_eenheden,
                aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
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
                deler=1,
            )
            if not ruimte_waarderingen:
                if categorie_is_nieuw and keuken_categorie.is_leeg:
                    keuken_categorie.verwijder()
                continue

            for waardering in ruimte_waarderingen:
                if waardering.punten is not None:
                    waardering.punten = float(Decimal(str(waardering.punten)) / deler)
            keuken_categorieen[laag_id] = keuken_categorie


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(
            peildatum=date(2026, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as waarderingsgroep_bouwer:
        waarderingsgroep_bouwer.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/input/voorbeeld_beleidsboek.json"
        )
