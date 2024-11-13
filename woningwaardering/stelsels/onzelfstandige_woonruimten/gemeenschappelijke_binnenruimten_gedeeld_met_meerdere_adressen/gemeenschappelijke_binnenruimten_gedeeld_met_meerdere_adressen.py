import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
        punten: Decimal,
        criterium: str,
        bovenliggende_criterium_id: str | None = None,
        aantal: float | None = None,
        meeteenheid: Referentiedata | None = None,
    ) -> WoningwaarderingResultatenWoningwaardering:
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                meeteenheid=meeteenheid,
                naam=criterium,
                bovenliggendeCriterium=WoningwaarderingCriteriumSleutels(
                    id=bovenliggende_criterium_id,
                ),
            ),
            aantal=aantal,
            punten=punten,
        )

    def _maak_oppervlakte_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_onzelfstandig_en_adressen: dict[int, Decimal],
    ) -> tuple[dict[int, Decimal], list[WoningwaarderingResultatenWoningwaardering]]:
        waarderigen = []
        for ruimte in ruimten:
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

                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )

                if (
                    gedeeld_met_onzelfstandig_en_adressen.get(
                        aantal_onzelfstandige_woonruimten
                    )
                    is None
                ):
                    gedeeld_met_onzelfstandig_en_adressen[
                        aantal_onzelfstandige_woonruimten
                    ] = Decimal("0")

                punten = (
                    Decimal(str(oppervlakte_resultaat.aantal))
                    * punten_per_m2
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                )
                gedeeld_met_onzelfstandig_en_adressen[
                    aantal_onzelfstandige_woonruimten
                ] += punten

                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue
                if oppervlakte_resultaat.criterium is None:
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue

                criterium_naam = (
                    f"{oppervlakte_resultaat.criterium.naam}: {ruimte.soort.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden} adressen)"
                    # if oppervlakte_resultaat.criterium
                    # else f"{ruimte.soort.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden} adressen)"
                )
                aantal = oppervlakte_resultaat.aantal
                meeteenheid = Meeteenheid.vierkante_meter_m2.value
                bovenliggende_criterium_id = f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_onzelfstandige_woonruimten}"

                waarderigen.append(
                    self._maak_woningwaardering(
                        punten,
                        criterium_naam,
                        bovenliggende_criterium_id,
                        aantal,
                        meeteenheid,
                    )
                )

        return gedeeld_met_onzelfstandig_en_adressen, waarderigen

    def _maak_verkoeling_en_verwarming_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_onzelfstandig_en_adressen: dict[int, Decimal],
    ) -> tuple[dict[int, Decimal], list[WoningwaarderingResultatenWoningwaardering]]:
        verkoeling_en_verwarming_resultaten = []
        waarderingen = []
        for ruimte in ruimten:
            resultaten = list(
                ZelfstandigeWoonruimtenVerkoelingEnVerwarming.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep
                )
            )
            verkoeling_en_verwarming_resultaten.extend(resultaten)

            for resultaat in resultaten:
                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )

                if (
                    gedeeld_met_onzelfstandig_en_adressen.get(
                        aantal_onzelfstandige_woonruimten
                    )
                    is None
                ):
                    gedeeld_met_onzelfstandig_en_adressen[
                        aantal_onzelfstandige_woonruimten
                    ] = Decimal("0")

                punten = (
                    Decimal(str(resultaat.punten))
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                )

                gedeeld_met_onzelfstandig_en_adressen[
                    aantal_onzelfstandige_woonruimten
                ] += punten

                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue
                if resultaat.criterium is None:
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue
                criterium_naam = f"{resultaat.criterium.naam}: {resultaat.criterium.bovenliggende_criterium.id.capitalize().replace('_', ' ') if resultaat.criterium.bovenliggende_criterium and resultaat.criterium.bovenliggende_criterium.id else ''} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden} adressen)"
                bovenliggende_criterium_id = f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_onzelfstandige_woonruimten}"
                waarderingen.append(
                    self._maak_woningwaardering(
                        punten, criterium_naam, bovenliggende_criterium_id, None, None
                    )
                )

        # TODO: maximering
        # maximering = list(
        #     ZelfstandigeWoonruimtenVerkoelingEnVerwarming.maximering(
        #         verkoeling_en_verwarming_resultaten
        #     )
        # )

        return gedeeld_met_onzelfstandig_en_adressen, waarderingen

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
            int, Decimal
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

        for (
            aantal_onzelfstandige_woonruimten,
            punten,
        ) in gedeeld_met_punten.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Totaal (gedeeld met {aantal_onzelfstandige_woonruimten} onzelfstandige {'woonruimten' if aantal_onzelfstandige_woonruimten > 1 else 'woonruimte'})",
                    id=f"gemeenschappelijke_binnenruimten_gedeeld_met_{aantal_onzelfstandige_woonruimten}",
                ),
                punten=punten,
            )

            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

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
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/input/voorbeeld_beleidsboek.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
