from collections import namedtuple
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.criterium import (
    GedeeldMetSoort,
)
from woningwaardering.stelsels.gedeelde_logica import waardeer_sanitair
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Installatiesoort,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
)

# De ruimte met de meeste (meerpersoons)wastafels, m.u.v. de badkamer, behoudt
# bij >= 8 onzelfstandige woonruimten de waardering zonder maximering.
MaxCount = namedtuple("MaxCount", ["aantal_wastafels", "ruimte"])


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        # Waardeer elke ruimte onder het bijbehorende gedeeld-met-criterium en houd
        # het maximum aantal (meerpersoons)wastafels per ruimte bij (m.u.v. badkamer).
        ruimte_waarderingen: list[
            tuple[
                EenhedenRuimte,
                WaarderingBouwer,
                list[WaarderingBouwer],
            ]
        ] = []
        max_wastafels = MaxCount(0, None)
        max_meerpersoonswastafels = MaxCount(0, None)

        for ruimte in ruimten:
            aantal_gedeeld = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
            if aantal_gedeeld is not None and aantal_gedeeld > 1:
                deler = aantal_gedeeld
            else:
                deler = 1
            gedeeld_met = waarderingsgroep_bouwer.gedeeld_met(
                aantal=deler,
                soort=GedeeldMetSoort.onzelfstandige_woonruimten,
            )

            waarderingen = waardeer_sanitair(
                ruimte,
                self.stelsel,
                waarderingsgroep_bouwer=gedeeld_met,
                deler=deler,
            )
            if not waarderingen:
                if gedeeld_met.is_leeg:
                    gedeeld_met.verwijder()
                continue

            ruimte_criterium = waarderingen[0]
            ruimte_waarderingen.append((ruimte, ruimte_criterium, waarderingen))

            # * tot een maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer.
            if ruimte.detail_soort not in [
                Ruimtedetailsoort.badkamer,
                Ruimtedetailsoort.badkamer_met_toilet,
                Ruimtedetailsoort.doucheruimte,
            ]:
                aantal_wastafels = self._aantal_wastafels(
                    waarderingen, ruimte_criterium, Installatiesoort.wastafel
                )
                if aantal_wastafels > max_wastafels.aantal_wastafels:
                    max_wastafels = MaxCount(aantal_wastafels, ruimte)

                aantal_meerpersoonswastafels = self._aantal_wastafels(
                    waarderingen,
                    ruimte_criterium,
                    Installatiesoort.meerpersoonswastafel,
                )
                if (
                    aantal_meerpersoonswastafels
                    > max_meerpersoonswastafels.aantal_wastafels
                ):
                    max_meerpersoonswastafels = MaxCount(
                        aantal_meerpersoonswastafels, ruimte
                    )

        # Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt
        # het maximum van 1 punt voor (meerpersoons)wastafels niet voor maximaal
        # één ruimte, namelijk de ruimte met de meeste (meerpersoons)wastafels.
        for ruimte, ruimte_criterium, waarderingen in ruimte_waarderingen:
            aantal_onzelfstandige = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            self._pas_wastafel_maximering_toe(
                ruimte,
                ruimte_criterium,
                waarderingen,
                aantal_onzelfstandige=aantal_onzelfstandige,
                deler=aantal_onzelfstandige,
                soort=Installatiesoort.wastafel,
                max_count=max_wastafels,
                maximum=Decimal("1"),
            )
            self._pas_wastafel_maximering_toe(
                ruimte,
                ruimte_criterium,
                waarderingen,
                aantal_onzelfstandige=aantal_onzelfstandige,
                deler=aantal_onzelfstandige,
                soort=Installatiesoort.meerpersoonswastafel,
                max_count=max_meerpersoonswastafels,
                maximum=Decimal("1.5"),
            )

        woningwaardering_groep = waarderingsgroep_bouwer.bouw()

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimten: list[EenhedenRuimte],
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    ) -> Iterator[tuple[EenhedenRuimte, list[WaarderingBouwer]]]:
        """Genereer sanitair-waarderingen per ruimte voor hergebruik in GBA.

        De waarderingen worden opgebouwd onder een losse ``WaarderingsgroepBouwer``
        met ``stelselgroep`` ``sanitair`` (niet onder de aanroepende stelselgroep);
        de aanroeper herparent ze in de GBA-hierarchie. Wastafel-maximering bij
        >= 8 onzelfstandige woonruimten wordt hier toegepast zonder punten te delen
        (deling gebeurt in de GBA-wrapper).
        """
        del stelselgroep  # behouden voor API-compatibiliteit met GBA

        waarderingsgroep_bouwer = WaarderingsgroepBouwer(
            Woningwaarderingstelsel.onzelfstandige_woonruimten,
            Woningwaarderingstelselgroep.sanitair,
        )
        woningwaarderingen_voor_gedeeld: list[
            tuple[EenhedenRuimte, list[WaarderingBouwer]]
        ] = []
        max_wastafels = MaxCount(0, None)
        max_meerpersoonswastafels = MaxCount(0, None)

        for ruimte in ruimten:
            waarderingen = waardeer_sanitair(
                ruimte,
                Woningwaarderingstelsel.onzelfstandige_woonruimten,
                waarderingsgroep_bouwer=waarderingsgroep_bouwer,
                deler=1,
            )
            if not waarderingen:
                continue

            ruimte_criterium = waarderingen[0]
            if ruimte.detail_soort not in [
                Ruimtedetailsoort.badkamer,
                Ruimtedetailsoort.badkamer_met_toilet,
                Ruimtedetailsoort.doucheruimte,
            ]:
                aantal_wastafels = Sanitair._aantal_wastafels(
                    waarderingen, ruimte_criterium, Installatiesoort.wastafel
                )
                if aantal_wastafels > max_wastafels.aantal_wastafels:
                    max_wastafels = MaxCount(aantal_wastafels, ruimte)

                aantal_meerpersoonswastafels = Sanitair._aantal_wastafels(
                    waarderingen,
                    ruimte_criterium,
                    Installatiesoort.meerpersoonswastafel,
                )
                if (
                    aantal_meerpersoonswastafels
                    > max_meerpersoonswastafels.aantal_wastafels
                ):
                    max_meerpersoonswastafels = MaxCount(
                        aantal_meerpersoonswastafels, ruimte
                    )

            woningwaarderingen_voor_gedeeld.append((ruimte, waarderingen))

        for ruimte, waarderingen in woningwaarderingen_voor_gedeeld:
            ruimte_criterium = waarderingen[0]
            aantal_onzelfstandige = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            Sanitair._pas_wastafel_maximering_toe(
                ruimte,
                ruimte_criterium,
                waarderingen,
                aantal_onzelfstandige=aantal_onzelfstandige,
                deler=1,
                soort=Installatiesoort.wastafel,
                max_count=max_wastafels,
                maximum=Decimal("1"),
            )
            Sanitair._pas_wastafel_maximering_toe(
                ruimte,
                ruimte_criterium,
                waarderingen,
                aantal_onzelfstandige=aantal_onzelfstandige,
                deler=1,
                soort=Installatiesoort.meerpersoonswastafel,
                max_count=max_meerpersoonswastafels,
                maximum=Decimal("1.5"),
            )
            yield (ruimte, waarderingen)

    @staticmethod
    def _aantal_wastafels(
        waarderingen: list[WaarderingBouwer],
        ruimte_criterium: WaarderingBouwer,
        soort: Referentiedata,
    ) -> int:
        criterium_id = f"{ruimte_criterium.criterium_id}__{soort.name}"
        return int(
            sum(
                int(woningwaardering.aantal or 0)
                for woningwaardering in waarderingen
                if (
                    woningwaardering.criterium_id == criterium_id
                    and woningwaardering.aantal is not None
                )
            )
        )

    @staticmethod
    def _pas_wastafel_maximering_toe(
        ruimte: EenhedenRuimte,
        ruimte_criterium: WaarderingBouwer,
        waarderingen: list[WaarderingBouwer],
        *,
        aantal_onzelfstandige: int,
        deler: int = 1,
        soort: Referentiedata,
        max_count: "MaxCount",
        maximum: Decimal,
    ) -> None:
        if not (aantal_onzelfstandige >= 8 and max_count.ruimte != ruimte):
            return
        criterium_id = f"{ruimte_criterium.criterium_id}__{soort.name}"
        for index, woningwaardering in enumerate(list(waarderingen)):
            if (
                woningwaardering.criterium_id == criterium_id
                and woningwaardering.aantal is not None
                and woningwaardering.aantal > 1
            ):
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {woningwaardering.aantal} {soort.naam}. Maximaal {maximum} punt voor {soort.naam}."
                )
                correctie = utils.rond_af(
                    maximum - Decimal(str(woningwaardering.aantal)) * maximum,
                    decimalen=2,
                )
                correctie_gedeeld = utils.rond_af(
                    correctie / Decimal(deler), decimalen=2
                )
                waarderingen.insert(
                    index + 1,
                    ruimte_criterium.maak_onderliggende(
                        id=f"max_punten_{soort.name}",
                        naam=f"Max {maximum} punt voor {soort.naam}",
                        punten=float(correctie_gedeeld),
                    ),
                )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Sanitair(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
