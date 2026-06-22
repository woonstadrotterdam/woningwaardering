from collections import defaultdict, namedtuple
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import bouw_sanitair, waardeer_sanitair
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    SanitairVoorRuimten,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
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


def _criterium_id_eindigt_op(criterium_id: str | None, installatie: str) -> bool:
    """Controleert of de laatste ``criteriumid_toevoeging`` gelijk is aan ``installatie``.

    Sanitair-totalen groeperen op installatiesoort; de laatste toevoeging na ``__``
    identificeert douche, bad, etc. zonder het volledige pad te parsen.

    Args:
        criterium_id (str | None): Te controleren criteriumid.
        installatie (str): Verwachte ``criteriumid_toevoeging``.

    Returns:
        bool: Of de laatste toevoeging overeenkomt.

    Example:
        >>> _criterium_id_eindigt_op("sanitair__Space_1__douche", "douche")
        True
    """
    if not criterium_id:
        return False
    return criterium_id.split("__")[-1] == installatie


def _sanitair_voor_ruimten(
    items: list[
        tuple[EenhedenRuimte, list[WoningwaarderingResultatenWoningwaardering]]
    ],
) -> SanitairVoorRuimten:
    item_map = {
        ruimte.id: waarderingen
        for ruimte, waarderingen in items
        if ruimte.id is not None
    }

    def sanitair_voor_ruimten(
        ruimten_batch: list[EenhedenRuimte],
    ) -> Iterator[
        tuple[EenhedenRuimte, list[WoningwaarderingResultatenWoningwaardering]]
    ]:
        for ruimte in ruimten_batch:
            if ruimte.id in item_map:
                yield ruimte, item_map[ruimte.id]

    return sanitair_voor_ruimten


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
        woningwaardering_groep = WoningwaarderingGroep(
            stelsel=self.stelsel,
            stelselgroep=self.stelselgroep,
        )

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        waarderingen_met_ruimten = list(
            Sanitair.genereer_woningwaarderingen(ruimten, self.stelselgroep)
        )

        groepen: dict[
            int,
            list[
                tuple[
                    EenhedenRuimte,
                    list[WoningwaarderingResultatenWoningwaardering],
                ]
            ],
        ] = defaultdict(list)
        for ruimte, waarderingen in waarderingen_met_ruimten:
            onz_aantal = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            groepen[onz_aantal].append((ruimte, waarderingen))

        # bereken de som van de woningwaarderingen per het aantal gedeelde onzelfstandige woonruimten
        for onz_aantal, items in groepen.items():
            if onz_aantal > 1:
                gedeeld_met_handle = woningwaardering_groep.met_gedeeld_met_criterium(
                    onz_aantal,
                    GedeeldMetSoort.onzelfstandige_woonruimten,
                    naam=utils.naam_gedeeld_met_groep(
                        onz_aantal,
                        soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                    ),
                )
            else:
                gedeeld_met_handle = woningwaardering_groep.met_gedeeld_met_criterium(
                    1, naam=utils.naam_gedeeld_met_groep(1)
                )

            groep_ruimten = [ruimte for ruimte, _ in items]

            bouw_sanitair(
                groep_ruimten,
                _sanitair_voor_ruimten(items),
                gedeeld_met_handle,
                Decimal(str(onz_aantal)),
            )

        # er is hier al op kwart afgerond
        woningwaardering_groep.punten = utils.som_punten_waarderingen(
            woningwaardering_groep.woningwaarderingen
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimten: list[EenhedenRuimte],
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    ) -> Iterator[
        tuple[EenhedenRuimte, list[WoningwaarderingResultatenWoningwaardering]]
    ]:
        woningwaarderingen_voor_gedeeld = []
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
                waardeer_sanitair(
                    ruimte,
                    stelselgroep,
                    Woningwaarderingstelsel.onzelfstandige_woonruimten,
                )
            )
            if ruimte.detail_soort not in [
                Ruimtedetailsoort.badkamer,
                Ruimtedetailsoort.badkamer_met_toilet,
                Ruimtedetailsoort.doucheruimte,
            ]:
                # zoek het maximum aantal wastafels in een ruimte m.u.v. badkamer
                wastafel_deel = utils.installatie_id_deel(Installatiesoort.wastafel)
                meerpersoons_deel = utils.installatie_id_deel(
                    Installatiesoort.meerpersoonswastafel
                )
                aantal_wastafels = sum(
                    woningwaardering.aantal or 0
                    for woningwaardering in woningwaarderingen
                    if (
                        woningwaardering.criterium
                        and _criterium_id_eindigt_op(
                            woningwaardering.criterium.id, wastafel_deel
                        )
                        and woningwaardering.aantal is not None
                    )
                )
                if aantal_wastafels > max_wastafels.aantal_wastafels:
                    max_wastafels = MaxCount(aantal_wastafels, ruimte)

                aantal_meerpersoonswastafels = sum(
                    woningwaardering.aantal or 0
                    for woningwaardering in woningwaarderingen
                    if (
                        woningwaardering.criterium
                        and _criterium_id_eindigt_op(
                            woningwaardering.criterium.id, meerpersoons_deel
                        )
                    )
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
        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld:
            if (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
                and max_wastafels.ruimte != ruimte
            ):
                for index, woningwaardering in enumerate(woningwaarderingen):
                    if (
                        woningwaardering.criterium
                        and _criterium_id_eindigt_op(
                            woningwaardering.criterium.id,
                            utils.installatie_id_deel(Installatiesoort.wastafel),
                        )
                        and woningwaardering.aantal is not None
                        and woningwaardering.aantal > 1
                    ):
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {woningwaardering.aantal} wastafels. Maximaal 1 punt voor wastafels."
                        )
                        woningwaarderingen.insert(
                            index + 1,
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"Max 1 punt voor {Installatiesoort.wastafel.naam}",
                                    id=str(
                                        CriteriumId.voor_stelselgroep(stelselgroep)
                                        .met_onderliggend(ruimte.id)
                                        .met_onderliggend(
                                            f"max_punten_{utils.installatie_id_deel(Installatiesoort.wastafel)}"
                                        )
                                    ),
                                ),
                                punten=float(
                                    utils.rond_af(
                                        1 - woningwaardering.aantal * 1,
                                        decimalen=2,
                                    )
                                ),
                            ),
                        )
            if (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
                and max_meerpersoonswastafels.ruimte != ruimte
            ):
                for index, woningwaardering in enumerate(woningwaarderingen):
                    if (
                        woningwaardering.criterium
                        and _criterium_id_eindigt_op(
                            woningwaardering.criterium.id,
                            utils.installatie_id_deel(
                                Installatiesoort.meerpersoonswastafel
                            ),
                        )
                        and woningwaardering.aantal is not None
                        and woningwaardering.aantal > 1
                    ):
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {woningwaardering.aantal} meerpersoonswastafels. Maximaal 1.5 punt voor meerpersoonswastafels."
                        )
                        woningwaarderingen.insert(
                            index + 1,
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"Max 1.5 punt voor {Installatiesoort.meerpersoonswastafel.naam}",
                                    id=str(
                                        CriteriumId.voor_stelselgroep(stelselgroep)
                                        .met_onderliggend(ruimte.id)
                                        .met_onderliggend(
                                            f"max_punten_{utils.installatie_id_deel(Installatiesoort.meerpersoonswastafel)}"
                                        )
                                    ),
                                ),
                                punten=float(
                                    utils.rond_af(
                                        Decimal("1.5")
                                        - (
                                            Decimal(str(woningwaardering.aantal))
                                            * Decimal("1.5")
                                        ),
                                        decimalen=2,
                                    )
                                ),
                            ),
                        )
            yield (ruimte, woningwaarderingen)


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Sanitair(peildatum=date(2026, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
