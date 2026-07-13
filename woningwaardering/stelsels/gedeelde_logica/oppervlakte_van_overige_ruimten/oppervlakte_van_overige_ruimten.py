from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    rond_af_op_kwart,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
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
    *,
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> WaarderingBouwer:
    zolder_oppervlakte = rond_af(ruimte.oppervlakte, decimalen=2)
    return waarderingsgroep_bouwer.maak_onderliggende(
        id=f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
        naam="Correctie: zolder zonder vaste trap",
        punten=float(bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)),
    )


def waardeer_oppervlakte_van_overige_ruimte(
    ruimte: EenhedenRuimte,
    *,
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> list[WaarderingBouwer]:
    if classificeer_ruimte(ruimte) != Ruimtesoort.overige_ruimten:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )
        return []

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
    )

    return [
        waarderingsgroep_bouwer.maak_onderliggende(
            id=ruimte.id,
            naam=criterium_naam,
            meeteenheid=Meeteenheid.vierkante_meter_m2,
            aantal=float(rond_af(ruimte.oppervlakte, decimalen=2)),
        )
    ]


def _is_ruimteregel_met_aantal(
    waardering: WaarderingBouwer,
    *,
    onder_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> bool:
    if waardering.aantal is None or waardering.punten is not None:
        return False
    return waardering.bovenliggende is onder_bouwer


def structureer_subtotaal_bij_correcties(
    waarderingen: list[WaarderingBouwer],
    *,
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
    factor: Decimal,
    deler: int = 1,
) -> list[WaarderingBouwer]:
    """Voeg een Subtotaal-waardering toe wanneer er een punten-correctie voor een zolderruimte plaatsvindt.

    Oppervlakte van overige ruimten berekent punten op basis van de afgeronde som van de oppervlakte van de ruimten.
    Bij zoldercorrecties moet er een subtotaalregel worden toegevoegd zodat de som van detailpunten gelijk is aan de som van de punten van destelselgroep.

    De ruimteregels worden onder het Subtotaal opgebouwd, zodat ``subtotaal`` net als
    elke andere tussenlaag in het id-pad van de onderliggende waarderingen voorkomt.
    """
    heeft_ruimte_aantal = any(
        _is_ruimteregel_met_aantal(w, onder_bouwer=waarderingsgroep_bouwer)
        for w in waarderingen
    )
    heeft_puntenregel = any(w.punten is not None for w in waarderingen)
    if not (heeft_ruimte_aantal and heeft_puntenregel):
        return waarderingen

    ruimteregels = [
        w
        for w in waarderingen
        if _is_ruimteregel_met_aantal(w, onder_bouwer=waarderingsgroep_bouwer)
    ]
    overige = [w for w in waarderingen if w not in ruimteregels]

    totaal_oppervlakte = sum(
        (Decimal(str(w.aantal)) for w in ruimteregels),
        start=Decimal("0"),
    )
    punten_uit_m2 = bereken_oppervlakte_punten(totaal_oppervlakte, factor)
    if deler > 1:
        punten_uit_m2 /= Decimal(str(deler))
    subtotaal = waarderingsgroep_bouwer.maak_onderliggende(
        id="subtotaal",
        naam="Subtotaal",
        meeteenheid=Meeteenheid.vierkante_meter_m2,
        aantal=float(rond_af(totaal_oppervlakte, decimalen=2)),
        punten=float(rond_af_op_kwart(punten_uit_m2)),
    )

    # Verplaats de ruimteregels onder het Subtotaal, zodat hun id-pad net als elke
    # andere tussenlaag het ``subtotaal``-segment bevat.
    for waardering in ruimteregels:
        waardering.verplaats_naar(subtotaal)

    # Zet de correctie-waarderingen ná het Subtotaal, consistent met de
    # gemeenschappelijke oppervlakte-waarderingen. Ze blijven directe kinderen van
    # dezelfde bovenliggende; alleen de volgorde in de output verandert.
    for waardering in overige:
        if waardering.bovenliggende is waarderingsgroep_bouwer:
            waardering.verplaats_naar(waarderingsgroep_bouwer)

    return [subtotaal, *ruimteregels, *overige]
