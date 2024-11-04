import warnings
from collections import defaultdict, namedtuple
from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.sanitair.sanitair import (
    Sanitair as ZelfstandigeWoonruimtenSanitair,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.voorzieningsoort import Voorzieningsoort


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.sanitair.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []
        woningwaarderingen_voor_gedeeld = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden < 2
        ]
        # * tot een maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer.
        # Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt dit maximum niet voor maximaal één ruimte.
        # Dat betekent dat er voor adressen met acht of meer onzelfstandige woonruimten maximaal één ruimte mag zijn,
        # naast de badkamer, met meer dan één wastafel die voor waardering in aanmerking kom
        MaxCount = namedtuple("MaxCount", ["aantal_wastafels", "ruimte"])

        # Initialize with zero counts and no rooms
        max_wastafels = MaxCount(0, None)
        max_meerpersoonswastafels = MaxCount(0, None)

        for ruimte in ruimten:
            woningwaarderingen = list(
                ZelfstandigeWoonruimtenSanitair.genereer_woningwaarderingen(
                    ruimte, self.stelselgroep
                )
            )
            # zoek het maximum aantal wastafels in een ruimte m.u.v. badkamer
            if ruimte.detail_soort not in [
                Ruimtedetailsoort.badkamer.value,
                Ruimtedetailsoort.badkamer_met_toilet.value,
                Ruimtedetailsoort.doucheruimte.value,
            ]:
                aantal_wastafels = sum(
                    [
                        woningwaardering.aantal or 0
                        for woningwaardering in woningwaarderingen
                        if (
                            woningwaardering.criterium
                            and woningwaardering.criterium.naam
                            and isinstance(woningwaardering.criterium.naam, str)
                            and f"{ruimte.naam} - {Voorzieningsoort.wastafel.naam}"
                            in woningwaardering.criterium.naam
                            and woningwaardering.aantal is not None
                            and isinstance(
                                Voorzieningsoort.meerpersoonswastafel.naam, str
                            )
                            and Voorzieningsoort.meerpersoonswastafel.naam
                            not in woningwaardering.criterium.naam
                        )
                    ]
                )
                if aantal_wastafels > max_wastafels.aantal_wastafels:
                    max_wastafels = MaxCount(aantal_wastafels, ruimte)

                aantal_meerpersoonswastafels = sum(
                    [
                        woningwaardering.aantal or 0
                        for woningwaardering in woningwaarderingen
                        if (
                            woningwaardering.criterium
                            and woningwaardering.criterium.naam
                            and isinstance(woningwaardering.criterium.naam, str)
                            and f"{ruimte.naam} - {Voorzieningsoort.meerpersoonswastafel.naam}"
                            in woningwaardering.criterium.naam
                        )
                    ]
                )
                if (
                    aantal_meerpersoonswastafels
                    > max_meerpersoonswastafels.aantal_wastafels
                ):
                    max_meerpersoonswastafels = MaxCount(
                        aantal_meerpersoonswastafels, ruimte
                    )
            woningwaarderingen_voor_gedeeld.append((ruimte, woningwaarderingen))

        # pas maximering toe voor wastafels en meerpersoonswastafels m.u.v. één ruimte,
        # de ruimte met de meeste wastafels/meerpersoonswastafels.
        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld[:]:
            if max_wastafels.ruimte != ruimte:
                for woningwaardering in woningwaarderingen:
                    if (
                        woningwaardering.criterium
                        and woningwaardering.criterium.naam
                        and isinstance(woningwaardering.criterium.naam, str)
                        and isinstance(Voorzieningsoort.wastafel.naam, str)
                        and isinstance(Voorzieningsoort.meerpersoonswastafel.naam, str)
                        and f"{ruimte.naam} - {Voorzieningsoort.wastafel.naam}"
                        in woningwaardering.criterium.naam
                        and Voorzieningsoort.meerpersoonswastafel.naam
                        not in woningwaardering.criterium.naam
                        and woningwaardering.aantal is not None
                        and woningwaardering.aantal > 1
                    ):
                        logger.info(
                            f"Ruimte {ruimte.naam} ({ruimte.id}) heeft {woningwaardering.aantal} wastafels. Maximaal 1 punt voor wastafels."
                        )
                        woningwaarderingen_voor_gedeeld.append(
                            (
                                ruimte,
                                [
                                    WoningwaarderingResultatenWoningwaardering(
                                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                            naam=f"{ruimte.naam} - Max 1 punt voor {Voorzieningsoort.wastafel.naam}",
                                        ),
                                        punten=utils.rond_af(
                                            1 - woningwaardering.aantal * 1,
                                            decimalen=2,
                                        ),
                                    )
                                ],
                            )
                        )
            if max_meerpersoonswastafels.ruimte != ruimte:
                for woningwaardering in woningwaarderingen:
                    if (
                        woningwaardering.criterium
                        and woningwaardering.criterium.naam
                        and isinstance(woningwaardering.criterium.naam, str)
                        and isinstance(Voorzieningsoort.meerpersoonswastafel.naam, str)
                        and f"{ruimte.naam} - {Voorzieningsoort.meerpersoonswastafel.naam}"
                        in woningwaardering.criterium.naam
                        and woningwaardering.aantal is not None
                        and woningwaardering.aantal > 1
                    ):
                        logger.info(
                            f"Ruimte {ruimte.naam} ({ruimte.id}) heeft {woningwaardering.aantal} meerpersoonswastafels. Maximaal 1,5 punt voor meerpersoonswastafels."
                        )
                        woningwaarderingen_voor_gedeeld.append(
                            (
                                ruimte,
                                [
                                    WoningwaarderingResultatenWoningwaardering(
                                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                            naam=f"{ruimte.naam} - Max 1,5 punt voor {Voorzieningsoort.meerpersoonswastafel.naam}",
                                        ),
                                        punten=utils.rond_af(
                                            1.5 - woningwaardering.aantal * 1.5,
                                            decimalen=2,
                                        ),
                                    )
                                ],
                            )
                        )

        gedeeld_met_counter: defaultdict[int, float] = defaultdict(float)
        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld:
            for woningwaardering in woningwaarderingen:
                if ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None:
                    if woningwaardering.criterium:
                        woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=f"{self.stelselgroep.name}_gedeeld_met_{ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten}_onzelfstandige_woonruimten"
                        )
                    gedeeld_met_counter[
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                    ] += woningwaardering.punten or 0
                else:
                    if woningwaardering.criterium:
                        woningwaardering.criterium.bovenliggende_criterium = (
                            WoningwaarderingCriteriumSleutels(
                                id=f"{self.stelselgroep.name}_prive"
                            )
                        )
                    gedeeld_met_counter[1] += woningwaardering.punten or 0
            woningwaardering_groep.woningwaarderingen.extend(woningwaarderingen)

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for aantal, punten in gedeeld_met_counter.items():
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"Totaal (gedeeld met {aantal})"
                if aantal > 1
                else "Totaal (privé)",
                id=f"{self.stelselgroep.name}_gedeeld_met_{aantal}_onzelfstandige_woonruimten"
                if aantal > 1
                else f"{self.stelselgroep.name}_prive",
            )
            woningwaardering.punten = float(utils.rond_af_op_kwart(punten / aantal))
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = sum(
            woningwaardering.punten
            for woningwaardering in woningwaardering_groep.woningwaarderingen or []
            if woningwaardering.punten is not None
            and woningwaardering.criterium is not None
            and woningwaardering.criterium.bovenliggende_criterium is None
        )

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.sanitair.naam}"
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    sanitair = Sanitair()
    with open(
        "tests/data/onzelfstandige_woonruimten/stelselgroepen/sanitair/input/maximering_wastafels.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[sanitair.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
