import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal

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
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.sanitair import (
    Sanitair as OnzelfstandigeWoonruimtenSanitair,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
    Ruimtesoort,
    RuimtesoortReferentiedata,
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

            gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]] = (
                defaultdict(lambda: defaultdict(Decimal))
            )  # {onzelfstandige_woonruimten: (aantal_adressen, punten)}

            # oppervlakte waarderingen
            gedeeld_met_punten, oppervlakte_waarderingen = (
                self._oppervlakte_waarderingen(gedeelde_ruimten, gedeeld_met_punten)
            )
            woningwaardering_groep.woningwaarderingen.extend(
                list(oppervlakte_waarderingen)
            )

            # verkoeling en verwarming waarderingen
            gedeeld_met_punten, verkoeling_en_verwarming_waarderingen = (
                self._verkoeling_en_verwarming_waarderingen(
                    gedeelde_ruimten, gedeeld_met_punten
                )
            )
            woningwaardering_groep.woningwaarderingen.extend(
                list(verkoeling_en_verwarming_waarderingen)
            )

            # keuken waarderingen
            gedeeld_met_punten, keuken_waarderingen = self._keuken_waarderingen(
                gedeelde_ruimten, gedeeld_met_punten
            )
            woningwaardering_groep.woningwaarderingen.extend(list(keuken_waarderingen))

            # sanitair waarderingen
            gedeeld_met_punten, sanitair_waarderingen = self._sanitair_waarderingen(
                gedeelde_ruimten, gedeeld_met_punten
            )
            woningwaardering_groep.woningwaarderingen.extend(
                list(sanitair_waarderingen)
            )

            # (sub)totaal waarderingen
            for (
                aantal_onzelfstandige_woonruimten,
                punten_per_aantal_adressen,
            ) in gedeeld_met_punten.items():
                bovenliggende_criterium_id = (
                    str(
                        CriteriumId.voor_stelselgroep(
                            self.stelselgroep
                        ).gedeeld_met_criterium(
                            aantal_onzelfstandige_woonruimten,
                            GedeeldMetSoort.onzelfstandige_woonruimten,
                        )
                    )
                    if aantal_onzelfstandige_woonruimten > 1
                    else None
                )

                for aantal_adressen in punten_per_aantal_adressen:
                    if aantal_adressen <= 1:
                        continue
                    woningwaardering_groep.woningwaarderingen.append(
                        self._maak_woningwaardering(
                            id=str(
                                CriteriumId.voor_stelselgroep(
                                    self.stelselgroep
                                ).gedeeld_met_criterium(
                                    aantal_adressen, GedeeldMetSoort.adressen
                                )
                            ),
                            criterium=utils.naam_gedeeld_met_groep(
                                aantal_adressen,
                                soort=GedeeldMetSoort.adressen,
                            ),
                            bovenliggende_criterium_id=bovenliggende_criterium_id,
                        )
                    )

                if aantal_onzelfstandige_woonruimten > 1:
                    woningwaardering_groep.woningwaarderingen.append(
                        self._maak_woningwaardering(
                            id=bovenliggende_criterium_id,
                            criterium=utils.naam_gedeeld_met_groep(
                                aantal_onzelfstandige_woonruimten,
                                soort=GedeeldMetSoort.onzelfstandige_woonruimten,
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
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        # 2.9.7 -> 2.2: ruimten worden gegroepeerd per combinatie van aantal adressen,
        # aantal onzelfstandige woonruimten en ruimtesoort. Per oppervlaktegroep wordt op
        # hele m² afgerond (op het totaal) en daarna door beide aantallen gedeeld.
        oppervlaktegroepen: defaultdict[
            tuple[int, int, RuimtesoortReferentiedata], list[EenhedenRuimte]
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
                (
                    ruimte.gedeeld_met_aantal_eenheden,
                    aantal_onzelfstandige_woonruimten,
                    ruimtesoort,
                )
            ].append(ruimte)

        waarderingen: list[WoningwaarderingResultatenWoningwaardering] = []

        def sorteer_oppervlaktegroepen(
            oppervlaktegroep: tuple[
                tuple[int, int, RuimtesoortReferentiedata], list[EenhedenRuimte]
            ],
        ) -> tuple[int, int, str]:
            (
                (
                    aantal_eenheden,
                    aantal_onzelfstandige_woonruimten,
                    ruimtesoort,
                ),
                _,
            ) = oppervlaktegroep
            return aantal_eenheden, aantal_onzelfstandige_woonruimten, str(ruimtesoort)

        for groepssleutel, groep_ruimten in sorted(
            oppervlaktegroepen.items(), key=sorteer_oppervlaktegroepen
        ):
            aantal_eenheden, aantal_onzelfstandige_woonruimten, ruimtesoort = (
                groepssleutel
            )
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
                if ruimtesoort == Ruimtesoort.vertrek
                else Decimal("0.75")
            )
            oppervlaktepunten = (
                bereken_oppervlakte_punten(totaal_oppervlakte, punten_per_m2)
                / Decimal(str(aantal_eenheden))
                / Decimal(str(aantal_onzelfstandige_woonruimten))
            )

            bovenliggende_criterium_id = str(
                CriteriumId.voor_stelselgroep(self.stelselgroep).gedeeld_met_criterium(
                    aantal_eenheden, GedeeldMetSoort.adressen
                )
            )
            oppervlaktegroep_id = str(
                CriteriumId.voor_stelselgroep(self.stelselgroep)
                .gedeeld_met_criterium(aantal_eenheden, GedeeldMetSoort.adressen)
                .met_onderliggend(
                    "vertrekken"
                    if ruimtesoort == Ruimtesoort.vertrek
                    else "overige_ruimten"
                )
            )
            groep_naam = (
                "Vertrekken"
                if ruimtesoort == Ruimtesoort.vertrek
                else "Overige ruimten"
            )

            for ruimte in groep_ruimten:
                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue

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
                ):
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue

                waarderingen.append(
                    self._maak_woningwaardering(
                        criterium=oppervlakte_resultaat.criterium.naam,
                        bovenliggende_criterium_id=oppervlaktegroep_id,
                        aantal=oppervlakte_resultaat.aantal,
                        meeteenheid=Meeteenheid.vierkante_meter_m2,
                        id=str(
                            CriteriumId.voor_stelselgroep(
                                self.stelselgroep
                            ).met_onderliggend(ruimte.id)
                        ),
                    )
                )

            correctie_totaal = Decimal("0")
            if ruimtesoort == Ruimtesoort.overige_ruimten:
                for ruimte in groep_ruimten:
                    if not is_zolder_zonder_vaste_trap(ruimte):
                        continue
                    zolder_oppervlakte = utils.rond_af(ruimte.oppervlakte, decimalen=2)
                    correctie_punten = (
                        bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)
                        / Decimal(str(aantal_eenheden))
                        / Decimal(str(aantal_onzelfstandige_woonruimten))
                    )
                    correctie_totaal += correctie_punten
                    waarderingen.append(
                        self._maak_woningwaardering(
                            punten=correctie_punten,
                            criterium="Correctie: zolder zonder vaste trap",
                            bovenliggende_criterium_id=bovenliggende_criterium_id,
                            id=str(
                                CriteriumId.voor_stelselgroep(self.stelselgroep)
                                .met_onderliggend(ruimte.id)
                                .met_onderliggend("correctie_zolder_zonder_vaste_trap")
                            ),
                        )
                    )

            gedeeld_met_punten[aantal_onzelfstandige_woonruimten][aantal_eenheden] += (
                oppervlaktepunten + correctie_totaal
            )

            waarderingen.append(
                self._maak_woningwaardering(
                    punten=oppervlaktepunten,
                    criterium=groep_naam,
                    bovenliggende_criterium_id=bovenliggende_criterium_id,
                    id=oppervlaktegroep_id,
                )
            )

        return gedeeld_met_punten, waarderingen

    def _verkoeling_en_verwarming_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        waarderingen = []

        resultaten = list(waardeer_verkoeling_en_verwarming(ruimten))
        for ruimte, resultaat in resultaten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            punten = (
                Decimal(str(resultaat.punten))
                / Decimal(str(aantal_eenheden))
                / Decimal(str(aantal_onzelfstandige_woonruimten))
            )

            gedeeld_met_punten[aantal_onzelfstandige_woonruimten][aantal_eenheden] += (
                punten
            )
            criterium = resultaat.criterium
            if ruimte.soort is None:
                warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                continue
            if criterium is None:
                warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                continue

            if resultaat.punten and resultaat.punten < 0:
                criterium_naam = f"{criterium.naam.rstrip(':') if criterium.naam else ''} voor {criterium.bovenliggende_criterium.id.split('__')[-1].lower().replace('_', ' ') if criterium.bovenliggende_criterium and criterium.bovenliggende_criterium.id else ''}"
            else:
                criterium_naam = f"{criterium.naam}: {criterium.bovenliggende_criterium.id.split('__')[-1].capitalize().replace('_', ' ') if criterium.bovenliggende_criterium and criterium.bovenliggende_criterium.id else ''}"

            waarderingen.append(
                self._maak_woningwaardering(
                    punten=punten,
                    criterium=criterium_naam,
                    bovenliggende_criterium_id=str(
                        CriteriumId.voor_stelselgroep(
                            self.stelselgroep
                        ).gedeeld_met_criterium(
                            aantal_eenheden, GedeeldMetSoort.adressen
                        )
                    ),
                    aantal=resultaat.aantal,
                    meeteenheid=resultaat.criterium.meeteenheid
                    if resultaat.criterium
                    else None,
                    id=str(
                        CriteriumId.voor_stelselgroep(
                            self.stelselgroep
                        ).met_onderliggend(ruimte.id)
                    ),
                )
            )

        return gedeeld_met_punten, waarderingen

    def _sanitair_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        woningwaarderingen_met_ruimten = list(
            OnzelfstandigeWoonruimtenSanitair.genereer_woningwaarderingen(
                ruimten, self.stelselgroep
            )
        )

        if not woningwaarderingen_met_ruimten:
            return gedeeld_met_punten, woningwaarderingen

        for ruimte, waarderingen in woningwaarderingen_met_ruimten:
            for waardering in waarderingen:
                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )
                aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue
                if waardering.criterium is None or waardering.criterium.naam is None:
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue

                punten = (
                    Decimal(str(waardering.punten))
                    / Decimal(aantal_eenheden)
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                )

                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] += punten

                woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=f"{waardering.criterium.naam.replace(':', '').replace(' -', ':')}",
                        bovenliggende_criterium_id=str(
                            CriteriumId.voor_stelselgroep(
                                self.stelselgroep
                            ).gedeeld_met_criterium(
                                aantal_eenheden, GedeeldMetSoort.adressen
                            )
                        ),
                        aantal=None,
                        meeteenheid=None,
                        id=str(
                            CriteriumId.voor_stelselgroep(
                                self.stelselgroep
                            ).met_onderliggend(ruimte.id)
                        ),
                    )
                )

        return gedeeld_met_punten, woningwaarderingen

    def _keuken_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        woningwaarderingen = []
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            waarderingen = list(waardeer_keuken(ruimte, self.stelsel))
            for waardering in waarderingen:
                if waardering.criterium is None:
                    logger.warning(
                        f"Geen criterium gevonden in waardring voor ruimte {ruimte.id}"
                    )
                    continue
                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )

                if not waardering.punten:
                    continue

                punten = (
                    Decimal(str(waardering.punten))
                    / Decimal(str(aantal_eenheden))
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                    if waardering.punten
                    else Decimal("0")
                )
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] += punten

                if waardering.criterium.naam is None:
                    criterium = f"{ruimte.naam}"
                else:
                    criterium = f"{ruimte.naam + ': ' if ruimte.naam is not None and ruimte.naam not in waardering.criterium.naam else ''}{waardering.criterium.naam}"

                woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=criterium,
                        bovenliggende_criterium_id=str(
                            CriteriumId.voor_stelselgroep(
                                self.stelselgroep
                            ).gedeeld_met_criterium(
                                aantal_eenheden, GedeeldMetSoort.adressen
                            )
                        ),
                        aantal=waardering.aantal,
                        meeteenheid=waardering.criterium.meeteenheid,
                        id=str(
                            CriteriumId.voor_stelselgroep(
                                self.stelselgroep
                            ).met_onderliggend(ruimte.id)
                        ),
                    )
                )
        return gedeeld_met_punten, woningwaarderingen


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
