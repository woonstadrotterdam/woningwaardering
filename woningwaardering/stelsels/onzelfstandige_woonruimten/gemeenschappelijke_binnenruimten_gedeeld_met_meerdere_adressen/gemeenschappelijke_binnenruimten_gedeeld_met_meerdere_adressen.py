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
    maximeer_wastafels,
    waardeer_keuken,
    waardeer_oppervlakte_van_overige_ruimte,
    waardeer_oppervlakte_van_vertrek,
    waardeer_sanitair,
    waardeer_verkoeling_en_verwarming,
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

            # waarderingen voor de oppervlakten van gedeelde ruimten
            self._oppervlakte_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)
            # waarderingen voor de verkoeling en verwarming van gedeelde ruimten
            self._verkoeling_en_verwarming_waarderingen(
                waarderingsgroep_bouwer, gedeelde_ruimten
            )
            # waarderingen voor de keuken van gedeelde ruimten
            self._keuken_waarderingen(waarderingsgroep_bouwer, gedeelde_ruimten)
            # waarderingen voor sanitair van gedeelde ruimten
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

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met(
                aantal_adressen=sleutel.aantal_eenheden,
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
            categorie = gedeeld_met_laag.categorie(
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
                # 2.2.2.3 Zolderruimte zonder vaste trap
                # Als een zolderruimte geen vertrek is maar wel als overige ruimte kan worden
                # aangemerkt en er is geen vaste trap naar de zolder, dan worden er 5 punten
                # afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend. Maar:
                # er kunnen nooit meer punten afgetrokken worden dan het totaal aantal punten
                # dat de zolderruimte zelf waard is. Met andere woorden: de waarde van de
                # zolder kan door deze aftrek niet negatief worden.
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
        # met hoeveel adressen/onzelfstandige woonruimten ze gedeeld worden. De helper
        # wordt daarom eenmalig aangeroepen; elk resultaat wordt daarna onder de juiste
        # adressengroep gehangen, waar de punten door het aantal adressen en
        # onzelfstandige woonruimten worden gedeeld.
        def subgroep(
            ruimte: EenhedenRuimte, subgroep_id: str, subgroep_naam: str
        ) -> WaarderingBouwer:
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met(
                aantal_adressen=aantal_eenheden,
                aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
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
            ruimten, subgroep=subgroep
        ):
            if waardering.punten is None:
                continue
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            deler = Decimal(str(aantal_eenheden)) * Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )
            waardering.punten = Decimal(str(waardering.punten)) / deler

    def _sanitair_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        ruimte_waarderingen: list[
            tuple[EenhedenRuimte, WaarderingBouwer, list[WaarderingBouwer]]
        ] = []

        for ruimte in ruimten:
            if ruimte.soort is None:
                warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                continue
            if ruimte.detail_soort is None:
                continue

            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met(
                aantal_adressen=aantal_eenheden,
                aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
            )

            sanitair_categorie = gedeeld_met_laag.categorie(
                id="sanitair",
                naam="Sanitair",
            )
            waarderingen = waardeer_sanitair(
                ruimte,
                self.stelsel,
                waarderingsgroep_bouwer=sanitair_categorie,
                deler=1,
            )
            if not waarderingen:
                continue

            ruimte_criterium = waarderingen[0]
            ruimte_waarderingen.append((ruimte, ruimte_criterium, waarderingen))

        maximeer_wastafels(ruimte_waarderingen)

        for ruimte, ruimte_criterium, waarderingen in ruimte_waarderingen:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            deler = Decimal(str(aantal_eenheden)) * Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )

            for waardering in waarderingen[1:]:
                if waardering.punten is not None:
                    waardering.punten = float(Decimal(str(waardering.punten)) / deler)

    def _keuken_waarderingen(
        self,
        waarderingsgroep_bouwer: WaarderingsgroepBouwer,
        ruimten: list[EenhedenRuimte],
    ) -> None:
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            deler = Decimal(str(aantal_eenheden)) * Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )

            gedeeld_met_laag = waarderingsgroep_bouwer.gedeeld_met(
                aantal_adressen=aantal_eenheden,
                aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
            )

            keuken_categorie = gedeeld_met_laag.categorie(
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
                continue

            for waardering in ruimte_waarderingen:
                if waardering.punten is not None:
                    waardering.punten = float(Decimal(str(waardering.punten)) / deler)


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
