from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    rond_af_op_kwart,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


def bereken_oppervlakte_punten(
    totaal_oppervlakte: Decimal, punten_per_m2: Decimal
) -> Decimal:
    # 2.2.2.1 / 2.1.1.1: waardering op hele m² (afronden op het totaal), daarna
    # vermenigvuldigen met het aantal punten per m².
    return rond_af(totaal_oppervlakte, decimalen=0) * punten_per_m2


def bereken_zolder_correctie(
    totaal_oppervlakte: Decimal, zolder_oppervlakte: Decimal
) -> Decimal:
    # 2.2.2.3 Zolderruimte zonder vaste trap
    # Maximaal 5 punten aftrek, maar niet meer dan de oppervlaktepunten die de zolder
    # zelf aan het totaal toevoegt. De correctie is negatief en wordt niet op een kwart
    # afgerond; die afronding gebeurt pas op het rubriektotaal.
    correctie = min(
        Decimal("5"),
        (
            rond_af(totaal_oppervlakte, decimalen=0)
            - rond_af(totaal_oppervlakte - zolder_oppervlakte, decimalen=0)
        )
        * Decimal("0.75"),
    )
    return correctie * Decimal("-1")


def is_zolder_zonder_vaste_trap(ruimte: EenhedenRuimte) -> bool:
    return (
        ruimte.detail_soort == Ruimtedetailsoort.zolder
        and ruimte.oppervlakte is not None
        and heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.vlizotrap)
        and classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
    )


def maak_zolder_correctie_waardering(
    ruimte: EenhedenRuimte,
    totaal_oppervlakte: Decimal,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
) -> WoningwaarderingResultatenWoningwaardering:
    zolder_oppervlakte = rond_af(ruimte.oppervlakte, decimalen=2)
    return WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Correctie: zolder zonder vaste trap",
            id=str(
                CriteriumId(
                    stelselgroep=stelselgroep,
                    ruimte_id=ruimte.id,
                    criterium="correctie_zolder_zonder_vaste_trap",
                )
            ),
        ),
        punten=float(bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)),
    )


def waardeer_oppervlakte_van_overige_ruimte(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    if classificeer_ruimte(ruimte) != Ruimtesoort.overige_ruimten:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )
        return

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
    )

    woningwaardering = WoningwaarderingResultatenWoningwaardering()
    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        meeteenheid=Meeteenheid.vierkante_meter_m2,
        naam=criterium_naam,
        id=str(
            CriteriumId(
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
                ruimte_id=ruimte.id,
            )
        ),
    )

    woningwaardering.aantal = float(rond_af(ruimte.oppervlakte, decimalen=2))

    yield woningwaardering


def _is_top_level_ruimteregel_met_aantal(
    waardering: WoningwaarderingResultatenWoningwaardering,
) -> bool:
    if waardering.aantal is None or waardering.punten is not None:
        return False
    if waardering.criterium is None:
        return False
    return waardering.criterium.bovenliggende_criterium is None


def structureer_subtotaal_bij_correcties(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering],
    *,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    factor: Decimal,
) -> list[WoningwaarderingResultatenWoningwaardering]:
    """Voeg een Subtotaal-waardering toe wanneer er een punten-correctie voor een zolderruimte plaatsvindt.

    Oppervlakte van overige ruimten berekent punten op basis van de afgeronde som van de oppervlakte van de ruimten.
    Bij zoldercorrecties moet er een subtotaalregel worden toegevoegd zodat de som van detailpunten gelijk is aan de som van de punten van destelselgroep.
    """
    heeft_ruimte_aantal = any(
        _is_top_level_ruimteregel_met_aantal(w) for w in waarderingen
    )
    heeft_puntenregel = any(w.punten is not None for w in waarderingen)
    if not (heeft_ruimte_aantal and heeft_puntenregel):
        return waarderingen

    ruimteregels = [w for w in waarderingen if _is_top_level_ruimteregel_met_aantal(w)]
    overige = [w for w in waarderingen if w not in ruimteregels]

    totaal_oppervlakte = sum(
        (Decimal(str(w.aantal)) for w in ruimteregels),
        start=Decimal("0"),
    )
    subtotaal_id = str(CriteriumId(stelselgroep=stelselgroep, criterium="subtotaal"))
    subtotaal = WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Subtotaal",
            id=subtotaal_id,
            meeteenheid=Meeteenheid.vierkante_meter_m2,
        ),
        aantal=float(rond_af(totaal_oppervlakte, decimalen=0)),
        punten=float(
            rond_af_op_kwart(bereken_oppervlakte_punten(totaal_oppervlakte, factor))
        ),
    )

    for waardering in ruimteregels:
        if waardering.criterium is None:
            continue
        waardering.criterium.bovenliggende_criterium = (
            WoningwaarderingCriteriumSleutels(id=subtotaal_id)
        )

    return [subtotaal, *ruimteregels, *overige]
