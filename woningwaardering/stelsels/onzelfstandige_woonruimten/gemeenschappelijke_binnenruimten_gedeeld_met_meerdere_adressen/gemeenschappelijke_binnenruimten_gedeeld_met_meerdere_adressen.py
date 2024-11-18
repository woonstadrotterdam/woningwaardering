import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Sanitair as OnzelfstandigeWoonruimtenSanitair,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    Keuken as ZelfstandigeWoonruimtenKeuken,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanOverigeRuimten as ZelfstandigeWoonruimtenOppervlakteVanOverigeRuimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanVertrekken as ZelfstandigeWoonruimtenOppervlakteVanVertrekken,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.verkoeling_en_verwarming.verkoeling_en_verwarming import (
    VerkoelingEnVerwarming as ZelfstandigeWoonruimtenVerkoelingEnVerwarming,
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid


class GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def _maak_woningwaardering(
        self,
        punten: Decimal | None,
        criterium: str,
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
            punten=punten,
        )
        if bovenliggende_criterium_id and woningwaardering.criterium:
            woningwaardering.criterium.bovenliggende_criterium = (
                WoningwaarderingCriteriumSleutels(id=bovenliggende_criterium_id)
            )
        return woningwaardering

    def _maak_oppervlakte_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: dict[int, dict[int, Decimal]],
    ) -> tuple[
        dict[int, dict[int, Decimal]], list[WoningwaarderingResultatenWoningwaardering]
    ]:
        waarderigen = []
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )

            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            oppervlakte_vertrekken = list(
                ZelfstandigeWoonruimtenOppervlakteVanVertrekken.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep
                )
            )

            oppervlakte_van_overige_ruimten = list(
                ZelfstandigeWoonruimtenOppervlakteVanOverigeRuimten.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep
                )
            )

            if (
                oppervlakte_vertrekken is not None
                or oppervlakte_van_overige_ruimten is not None
            ):
                if oppervlakte_vertrekken:
                    oppervlakte_resultaat = oppervlakte_vertrekken[0]
                    punten_per_m2 = Decimal("1.0")
                else:
                    oppervlakte_resultaat = oppervlakte_van_overige_ruimten[0]
                    punten_per_m2 = Decimal("0.75")

                if gedeeld_met_punten.get(aantal_onzelfstandige_woonruimten) is None:
                    gedeeld_met_punten[aantal_onzelfstandige_woonruimten] = {
                        aantal_eenheden: Decimal("0")
                    }

                if (
                    gedeeld_met_punten[aantal_onzelfstandige_woonruimten].get(
                        aantal_eenheden
                    )
                    is None
                ):
                    gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                        aantal_eenheden
                    ] = Decimal("0")

                punten = (
                    Decimal(str(oppervlakte_resultaat.aantal))
                    * punten_per_m2
                    / Decimal(str(aantal_eenheden))
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                )
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] += punten

                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue
                if oppervlakte_resultaat.criterium is None:
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue

                criterium_naam = (
                    f"{oppervlakte_resultaat.criterium.naam}: {ruimte.soort.naam}"
                )
                aantal = oppervlakte_resultaat.aantal
                meeteenheid = Meeteenheid.vierkante_meter_m2.value
                bovenliggende_criterium_id = f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_eenheden}_adressen"

                waarderigen.append(
                    self._maak_woningwaardering(
                        punten,
                        criterium_naam,
                        bovenliggende_criterium_id,
                        aantal,
                        meeteenheid,
                    )
                )

        return gedeeld_met_punten, waarderigen

    def _maak_verkoeling_en_verwarming_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: dict[int, dict[int, Decimal]],
    ) -> tuple[
        dict[int, dict[int, Decimal]], list[WoningwaarderingResultatenWoningwaardering]
    ]:
        waarderingen = []

        resultaten = list(
            ZelfstandigeWoonruimtenVerkoelingEnVerwarming.genereer_woningwaarderingen(
                ruimten, self.stelselgroep
            )
        )
        for ruimte, resultaat in resultaten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            if gedeeld_met_punten.get(aantal_onzelfstandige_woonruimten) is None:
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten] = {
                    aantal_eenheden: Decimal("0")
                }

            if (
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten].get(
                    aantal_eenheden
                )
                is None
            ):
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] = Decimal("0")

            punten = (
                Decimal(str(resultaat.punten))
                / Decimal(str(aantal_eenheden))
                / Decimal(str(aantal_onzelfstandige_woonruimten))
            )

            gedeeld_met_punten[aantal_onzelfstandige_woonruimten][aantal_eenheden] += (
                punten
            )

            if ruimte.soort is None:
                warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                continue
            if resultaat.criterium is None:
                warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                continue

            if "Max" not in (resultaat.criterium.naam or ""):
                criterium_naam = f"{resultaat.criterium.naam}: {resultaat.criterium.bovenliggende_criterium.id.capitalize().replace('_', ' ') if resultaat.criterium.bovenliggende_criterium and resultaat.criterium.bovenliggende_criterium.id else ''}"
            else:
                criterium_naam = f"{resultaat.criterium.naam}"
            bovenliggende_criterium_id = f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_eenheden}_adressen"
            waarderingen.append(
                self._maak_woningwaardering(
                    punten, criterium_naam, bovenliggende_criterium_id, None, None
                )
            )

        return gedeeld_met_punten, waarderingen

    def _maak_sanitair_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: dict[int, dict[int, Decimal]],
    ) -> tuple[
        dict[int, dict[int, Decimal]], list[WoningwaarderingResultatenWoningwaardering]
    ]:
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        woningwaarderingen_met_ruimten = list(
            OnzelfstandigeWoonruimtenSanitair.genereer_woningwaarderingen(
                ruimten, self.stelselgroep
            )
        )

        if not woningwaarderingen_met_ruimten:
            return gedeeld_met_punten, woningwaarderingen

        for ruimte, woningwaardering in woningwaarderingen_met_ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            if ruimte.soort is None:
                warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                continue
            if woningwaardering.criterium is None:
                warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                continue

            if gedeeld_met_punten.get(aantal_onzelfstandige_woonruimten) is None:
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten] = {
                    aantal_eenheden: Decimal("0")
                }

            if (
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten].get(
                    aantal_eenheden
                )
                is None
            ):
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] = Decimal("0")

            punten = Decimal(str(woningwaardering.punten)) / Decimal(
                str(aantal_onzelfstandige_woonruimten)
            )

            gedeeld_met_punten[aantal_onzelfstandige_woonruimten][aantal_eenheden] += (
                punten
            )

            criterium_naam = (
                f"{woningwaardering.criterium.naam.replace(':', '').replace(' -', ':')}"
            )
            bovenliggende_criterium_id = f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_eenheden}_adressen"
            woningwaarderingen.append(
                self._maak_woningwaardering(
                    punten, criterium_naam, bovenliggende_criterium_id, None, None
                )
            )

        return gedeeld_met_punten, woningwaarderingen

    def _maak_keuken_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: dict[int, dict[int, Decimal]],
    ) -> tuple[
        dict[int, dict[int, Decimal]], list[WoningwaarderingResultatenWoningwaardering]
    ]:
        woningwaarderingen = []
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            waarderingen = list(
                ZelfstandigeWoonruimtenKeuken.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep, self.stelsel
                )
            )
            for waardering in waarderingen:
                if waardering.criterium is None:
                    logger.warning(
                        f"Geen criterium gevonden in waardring voor ruimte {ruimte.id}"
                    )
                    continue
                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )

                if gedeeld_met_punten.get(aantal_onzelfstandige_woonruimten) is None:
                    gedeeld_met_punten[aantal_onzelfstandige_woonruimten] = {
                        aantal_eenheden: Decimal("0")
                    }

                if (
                    gedeeld_met_punten[aantal_onzelfstandige_woonruimten].get(
                        aantal_eenheden
                    )
                    is None
                ):
                    gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                        aantal_eenheden
                    ] = Decimal("0")

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
                bovenliggende_criterium_id = f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_eenheden}_adressen"
                woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten,
                        criterium,
                        bovenliggende_criterium_id,
                        waardering.aantal,
                        waardering.criterium.meeteenheid,
                    )
                )
        return gedeeld_met_punten, woningwaarderingen

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.value,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        gedeelde_ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is not None
            and ruimte.gedeeld_met_aantal_eenheden > 1
        ]

        gedeeld_met_punten: dict[
            int, dict[int, Decimal]
        ] = {}  # {onzelfstandige_woonruimten: (aantal_adressen, punten)}

        # maak oppervlakte waarderingen
        gedeeld_met_punten, oppervlakte_waarderingen = (
            self._maak_oppervlakte_waarderingen(gedeelde_ruimten, gedeeld_met_punten)
        )
        woningwaardering_groep.woningwaarderingen.extend(list(oppervlakte_waarderingen))

        # maak verkoeling en verwarming waarderingen
        gedeeld_met_punten, verkoeling_en_verwarming_waarderingen = (
            self._maak_verkoeling_en_verwarming_waarderingen(
                gedeelde_ruimten, gedeeld_met_punten
            )
        )
        woningwaardering_groep.woningwaarderingen.extend(
            list(verkoeling_en_verwarming_waarderingen)
        )

        # maak keuken waarderingen
        gedeeld_met_punten, keuken_waarderingen = self._maak_keuken_waarderingen(
            gedeelde_ruimten, gedeeld_met_punten
        )
        woningwaardering_groep.woningwaarderingen.extend(list(keuken_waarderingen))

        # maak sanitair waarderingen
        gedeeld_met_punten, sanitair_waarderingen = self._maak_sanitair_waarderingen(
            gedeelde_ruimten, gedeeld_met_punten
        )
        woningwaardering_groep.woningwaarderingen.extend(list(sanitair_waarderingen))

        # maak (sub)totaal waarderingen
        for (
            aantal_onzelfstandifge_woonruimten,
            punten_per_aantal_adressen,
        ) in gedeeld_met_punten.items():
            onz_punten = Decimal("0")
            for aantal_adressen, punten in punten_per_aantal_adressen.items():
                onz_punten += punten
                woningwaardering_groep.woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        id=f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_adressen}_adressen",
                        criterium=f"Totaal (gedeeld met {aantal_adressen} adressen)",
                        bovenliggende_criterium_id=f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_onzelfstandifge_woonruimten}_onzelfstandige_woonruimten",
                    )
                )
            woningwaardering_groep.woningwaarderingen.append(
                self._maak_woningwaardering(
                    punten=onz_punten,
                    id=f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_onzelfstandifge_woonruimten}_onzelfstandige_woonruimten",
                    criterium=f"Totaal (gedeeld met {aantal_onzelfstandifge_woonruimten} onzelfstandige {'woonruimten' if aantal_onzelfstandifge_woonruimten > 1 else 'woonruimte'})",
                )
            )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen()
    with open(
        "tests/data/onzelfstandige_woonruimten/input/15004000185.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
