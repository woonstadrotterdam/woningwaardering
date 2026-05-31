from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


def oppervlaktepunten_overige_ruimte_per_ruimte(oppervlakte: Decimal) -> Decimal:
    # 2.2.2.1 Afronding op hele m²
    return rond_af(oppervlakte, decimalen=0) * Decimal("0.75")


def bereken_zolder_correctie_zonder_vaste_trap(
    zolder_oppervlakte: Decimal,
    *,
    totaal_oppervlakte_groep: Decimal | None = None,
) -> Decimal:
    # 2.2.2.3 Zolderruimte zonder vaste trap
    # Als een zolderruimte geen vertrek is maar wel als overige ruimte kan worden
    # aangemerkt en er is geen vaste trap naar de zolder, dan worden er 5 punten
    # afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend.
    # Maar: er kunnen nooit meer punten afgetrokken worden dan het totaal aantal
    # punten dat de zolderruimte zelf waard is.
    zolder_opp = rond_af(zolder_oppervlakte, decimalen=2)
    if totaal_oppervlakte_groep is not None:
        totaal = totaal_oppervlakte_groep
        toegekende_punten = (
            rond_af(totaal, decimalen=0) - rond_af(totaal - zolder_opp, decimalen=0)
        ) * Decimal("0.75")
    else:
        toegekende_punten = oppervlaktepunten_overige_ruimte_per_ruimte(zolder_opp)
    return -min(Decimal("5"), toegekende_punten)


def waardeer_oppervlakte_van_overige_ruimte(
    ruimte: EenhedenRuimte,
    *,
    totaal_oppervlakte_groep: Decimal | None = None,
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

    if ruimte.detail_soort == Ruimtedetailsoort.zolder:
        # Corrigeer met -5 punten als de zolder niet bereikbaar is met een vaste trap
        # Note: Op dit moment kan de zolder alleen een
        # Bouwkundigelementdetailsoort.trap (vast) of Bouwkundigelementdetailsoort.vlizotrap (niet vast)
        # hebben vanwege classificeer_ruimte in utils.py.
        if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.vlizotrap):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): maximaal correctie van -5 punten: zolder is niet bereikbaar via een vaste trap."
            )
            woningwaardering_correctie = WoningwaarderingResultatenWoningwaardering()
            woningwaardering_correctie.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Correctie: zolder zonder vaste trap",
                id=str(
                    CriteriumId(
                        stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
                        ruimte_id=ruimte.id,
                        criterium="correctie_zolder_zonder_vaste_trap",
                    )
                ),
            )

            woningwaardering_correctie.punten = float(
                bereken_zolder_correctie_zonder_vaste_trap(
                    rond_af(ruimte.oppervlakte, decimalen=2),
                    totaal_oppervlakte_groep=totaal_oppervlakte_groep,
                )
            )
            yield woningwaardering_correctie
