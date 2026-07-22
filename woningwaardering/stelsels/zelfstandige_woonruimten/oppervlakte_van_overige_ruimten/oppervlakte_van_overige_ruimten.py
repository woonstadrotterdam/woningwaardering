from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import Stelselgroep
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica import (
    is_zolder_zonder_vaste_trap,
    maak_zolder_correctie_waardering,
    structureer_subtotaal_bij_correcties,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_adressen,
    rond_af,
    rond_af_op_kwart,
    som_punten_waarderingen,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


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
        waarderingsgroep_builder = WaarderingsgroepBuilder(
            self.stelsel, self.stelselgroep
        )

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not gedeeld_met_adressen(ruimte)
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

        alle_waarderingen: list[WaarderingBuilder] = []
        for ruimte in ruimten:
            waarderingen = waardeer_oppervlakte_van_overige_ruimte(
                ruimte, waarderingsgroep_builder=waarderingsgroep_builder
            )

            # 2.2.2.3 Zolderruimte zonder vaste trap
            # Als een zolderruimte geen vertrek is maar wel als overige ruimte kan worden aangemerkt en er is geen vaste trap naar de zolder,
            # dan worden er 5 punten afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend.
            # Maar: er kunnen nooit meer punten afgetrokken worden dan het totaal aantal punten dat de zolderruimte zelf waard is.
            # Met andere woorden: de waarde van de zolder kan door deze aftrek niet negatief worden.
            if is_zolder_zonder_vaste_trap(ruimte):
                waarderingen.append(
                    maak_zolder_correctie_waardering(
                        ruimte,
                        totaal_oppervlakte,
                        waarderingsgroep_builder=waarderingsgroep_builder,
                    )
                )

            alle_waarderingen.extend(waarderingen)

        structureer_subtotaal_bij_correcties(
            alle_waarderingen,
            waarderingsgroep_builder=waarderingsgroep_builder,
            factor=Decimal("0.75"),
        )

        woningwaardering_groep = waarderingsgroep_builder.bouw()
        groep_waarderingen = woningwaardering_groep.woningwaarderingen or []
        if any(w.punten is not None for w in groep_waarderingen):
            # de maximering is altijd in punten en daarom wordt de som van de punten hier gebruikt om de maximering toe te passsen
            woningwaardering_groep.punten = som_punten_waarderingen(groep_waarderingen)
        else:
            punten = rond_af_op_kwart(
                rond_af(
                    sum(
                        Decimal(str(w.aantal))
                        for w in groep_waarderingen
                        if w.aantal is not None
                    ),
                    decimalen=0,
                )
                * Decimal("0.75")
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
