from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica import (
    bereken_oppervlakte_punten,
    bereken_zolder_correctie,
    is_zolder_zonder_vaste_trap,
    waardeer_oppervlakte_van_overige_ruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
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
        woningwaardering_groep = WoningwaarderingGroep(
            stelsel=self.stelsel,
            stelselgroep=self.stelselgroep,
        )

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        totaal_oppervlakte = sum(
            (
                utils.rond_af(ruimte.oppervlakte, decimalen=2)
                for ruimte in ruimten
                if ruimte.oppervlakte is not None
                and utils.classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
            ),
            start=Decimal("0"),
        )

        details = _verzamel_oppervlakte_details(ruimten, self.stelselgroep.name)
        heeft_correcties = any(
            is_zolder_zonder_vaste_trap(ruimte) for ruimte in ruimten
        )

        if heeft_correcties:
            if details:
                punten = utils.rond_af_op_kwart(
                    bereken_oppervlakte_punten(totaal_oppervlakte, Decimal("0.75"))
                )
                subtotaal = woningwaardering_groep.met_onderliggend(
                    "subtotaal",
                    naam="Subtotaal",
                    aantal=float(utils.rond_af(totaal_oppervlakte, decimalen=2)),
                    punten=float(punten),
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                )
                for ruimte_id, naam, meeteenheid, aantal in details:
                    subtotaal.met_onderliggend(
                        ruimte_id,
                        naam=naam,
                        meeteenheid=meeteenheid,
                        aantal=aantal,
                    )

            # 2.2.2.3 Zolderruimte zonder vaste trap
            # Als een zolderruimte geen vertrek is maar wel als overige ruimte kan worden aangemerkt en er is geen vaste trap naar de zolder,
            # dan worden er 5 punten afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend.
            # Maar: er kunnen nooit meer punten afgetrokken worden dan het totaal aantal punten dat de zolderruimte zelf waard is.
            # Met andere woorden: de waarde van de zolder kan door deze aftrek niet negatief worden.
            for ruimte in ruimten:
                if not is_zolder_zonder_vaste_trap(ruimte):
                    continue
                zolder_oppervlakte = utils.rond_af(ruimte.oppervlakte, decimalen=2)
                woningwaardering_groep.met_onderliggend(
                    f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
                    naam="Correctie: zolder zonder vaste trap",
                    punten=float(
                        bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)
                    ),
                )
        elif details:
            for ruimte_id, naam, meeteenheid, aantal in details:
                woningwaardering_groep.met_onderliggend(
                    ruimte_id,
                    naam=naam,
                    meeteenheid=meeteenheid,
                    aantal=aantal,
                )

        waarderingen = woningwaardering_groep.woningwaarderingen or []
        if any(w.punten is not None for w in waarderingen):
            woningwaardering_groep.punten = utils.som_punten_waarderingen(waarderingen)
        else:
            punten = utils.rond_af_op_kwart(
                utils.rond_af(
                    sum(
                        Decimal(str(w.aantal))
                        for w in waarderingen
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

        if woningwaardering_groep.woningwaarderingen is not None:
            woningwaardering_groep.woningwaarderingen = (
                utils.herordenen_fluent_waarderingen(
                    woningwaardering_groep.woningwaarderingen
                )
            )

        return woningwaardering_groep


def _verzamel_oppervlakte_details(
    ruimten: list[EenhedenRuimte],
    stelselgroep_naam_key: str,
) -> list[tuple[str, str, Referentiedata | None, float | None]]:
    details: list[tuple[str, str, Referentiedata | None, float | None]] = []
    for ruimte in ruimten:
        bron = next(iter(waardeer_oppervlakte_van_overige_ruimte(ruimte)), None)
        if bron is None or bron.criterium is None or bron.criterium.naam is None:
            continue
        ruimte_id = utils.criteriumid_onder_stelselgroep(
            bron.criterium.id, stelselgroep_naam_key
        )
        if ruimte_id is None:
            if bron.criterium.id == stelselgroep_naam_key:
                ruimte_id = ruimte.id or "ruimte"
            else:
                continue
        elif ruimte_id == "":
            ruimte_id = ruimte.id or "ruimte"
        details.append(
            (
                ruimte_id,
                bron.criterium.naam or "",
                bron.criterium.meeteenheid,
                bron.aantal,
            )
        )
    return details


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OppervlakteVanOverigeRuimten(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
