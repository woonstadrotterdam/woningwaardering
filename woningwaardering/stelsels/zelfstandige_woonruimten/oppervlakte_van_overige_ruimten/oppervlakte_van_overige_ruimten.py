from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import Stelselgroep
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_eenheden,
    rond_af,
    rond_af_op_kwart,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


class OppervlakteVanOverigeRuimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten

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
            ),
        )

        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not gedeeld_met_eenheden(ruimte)
        ]

        totaal_oppervlakte = sum(
            (
                rond_af(ruimte.oppervlakte, decimalen=2)
                for ruimte in ruimten
                if ruimte.oppervlakte is not None
                and classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ),
            start=Decimal("0"),
        )

        for ruimte in ruimten:
            woningwaarderingen = list(waardeer_oppervlakte_van_overige_ruimte(ruimte))

            # 2.2.2.3 Zolderruimte zonder vaste trap
            # Als een zolderruimte geen vertrek is maar wel als overige ruimte kan worden aangemerkt en er is geen vaste trap naar de zolder, 
            # dan worden er 5 punten afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend.
            # Maar: er kunnen nooit meer punten afgetrokken worden dan het totaal aantal punten dat de zolderruimte zelf waard is. 
            # Met andere woorden: de waarde van de zolder kan door deze aftrek niet negatief worden.
            if (
                ruimte.detail_soort == Ruimtedetailsoort.zolder
                and heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.vlizotrap
                )
                and classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ):
                zolder_opp = rond_af(ruimte.oppervlakte, decimalen=2)
                correctie = min(
                    Decimal("5"),
                    (
                        rond_af(totaal_oppervlakte, decimalen=0)
                        - rond_af(totaal_oppervlakte - zolder_opp, decimalen=0)
                    )
                    * Decimal("0.75"),
                )
                for woningwaardering in woningwaarderingen:
                    if (
                        woningwaardering.criterium is not None
                        and woningwaardering.criterium.id is not None
                        and woningwaardering.criterium.id.endswith(
                            "__correctie_zolder_zonder_vaste_trap"
                        )
                    ):
                        woningwaardering.punten = float(correctie * Decimal("-1"))
                        break

            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        punten = rond_af_op_kwart(
            (
                rond_af(
                    sum(
                        Decimal(str(woningwaardering.aantal))
                        for woningwaardering in woningwaardering_groep.woningwaarderingen
                        or []
                        if woningwaardering.aantal is not None
                    ),
                    decimalen=0,
                )
                * Decimal("0.75")
            )
            # de maximering is altijd in punten en daarom wordt de som van de punten hier gebruikt om de maximering toe te passsen
            + sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanOverigeRuimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
