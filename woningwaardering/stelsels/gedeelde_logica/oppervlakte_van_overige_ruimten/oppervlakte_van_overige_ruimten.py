from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.utils import (
    ZOLDER_DETAIL_SOORTEN,
    classificeer_ruimte,
    heeft_vaste_trap,
    oppervlakte_inclusief_verbonden_kasten,
    rond_af,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)


def bereken_oppervlakte_punten(
    totaal_oppervlakte: Decimal, punten_per_m2: Decimal
) -> Decimal:
    # 2.2.2.1 / 2.1.1.1: waardering op hele m² (afronden op het totaal), daarna
    # vermenigvuldigen met het aantal punten per m².
    return rond_af(totaal_oppervlakte, decimalen=0) * punten_per_m2


def bereken_zolder_correctie(
    totaal_oppervlakte: Decimal,
    zolder_oppervlakte: Decimal,
    *,
    max_aftrek: Decimal = Decimal("5"),
) -> Decimal:
    # 2.2.2.3 Zolderruimte zonder vaste trap
    # Maximaal 5 punten aftrek, maar niet meer dan de oppervlaktepunten die de zolder
    # zelf aan het totaal toevoegt. De correctie is negatief en wordt niet op een kwart
    # afgerond; die afronding gebeurt pas op het rubriektotaal.
    correctie = min(
        max_aftrek,
        (
            rond_af(totaal_oppervlakte, decimalen=0)
            - rond_af(totaal_oppervlakte - zolder_oppervlakte, decimalen=0)
        )
        * Decimal("0.75"),
    )
    return correctie * Decimal("-1")


def is_zolder_zonder_vaste_trap(ruimte: EenhedenRuimte) -> bool:
    return (
        ruimte.detail_soort in ZOLDER_DETAIL_SOORTEN
        and ruimte.oppervlakte is not None
        and not heeft_vaste_trap(ruimte)
        and classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
    )


def maak_zolder_correctie_waardering(
    ruimte: EenhedenRuimte,
    totaal_oppervlakte: Decimal,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> WaarderingBuilder:
    zolder_oppervlakte = rond_af(
        oppervlakte_inclusief_verbonden_kasten(ruimte), decimalen=2
    )
    return waarderingsgroep_builder.met_onderliggend(
        id=f"{ruimte.id}__correctie_zolder_zonder_vaste_trap",
        naam="Correctie: zolder zonder vaste trap",
        punten=float(bereken_zolder_correctie(totaal_oppervlakte, zolder_oppervlakte)),
    )


def waardeer_oppervlakte_van_overige_ruimte(
    ruimte: EenhedenRuimte,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> list[WaarderingBuilder]:
    if classificeer_ruimte(ruimte) != Ruimtesoort.overige_ruimten:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
        )
        return []

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)
    oppervlakte_met_kasten = oppervlakte_inclusief_verbonden_kasten(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {oppervlakte_met_kasten:.2f}m2 "
        f"telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
    )

    return [
        waarderingsgroep_builder.met_onderliggend(
            id=ruimte.id,
            naam=criterium_naam,
            meeteenheid=Meeteenheid.vierkante_meter_m2,
            aantal=float(rond_af(oppervlakte_met_kasten, decimalen=2)),
        )
    ]
