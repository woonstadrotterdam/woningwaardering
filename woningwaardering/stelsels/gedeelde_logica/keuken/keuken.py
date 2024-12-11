import warnings
from collections import Counter
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.utils import (
    gedeeld_met_onzelfstandige_woonruimten,
    rond_af,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Voorzieningsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen


def waardeer_keuken(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    if not _is_keuken(ruimte):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.keuken.naam}"
        )
        return

    yield from _waardeer_aanrecht(ruimte, stelsel)

    yield from _waardeer_extra_voorzieningen(ruimte)


def _is_keuken(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of de ruimte een keuken is op basis van het aanrecht.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren.

    Returns:
        bool: True als de ruimte een keuken is, anders False.
    """
    aanrecht_aantal = len(
        [
            aanrecht
            for aanrecht in get_bouwkundige_elementen(
                ruimte, Bouwkundigelementdetailsoort.aanrecht
            )
            if aanrecht.lengte and aanrecht.lengte >= 1000
        ]
    )

    if not ruimte.detail_soort:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort",
            UserWarning,
        )
        return False

    if ruimte.detail_soort in [
        Ruimtedetailsoort.keuken,
        Ruimtedetailsoort.woonkamer_en_of_keuken,
    ]:
        if aanrecht_aantal == 0:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor {Woningwaarderingstelselgroep.keuken.naam}.",
                UserWarning,
            )
            return False  # ruimte is een keuken maar heeft geen valide aanrecht en mag dus niet als keuken gewaardeerd worden
        return True  # ruimte is een keuken met een valide aanrecht
    if ruimte.detail_soort not in [
        Ruimtedetailsoort.woonkamer,
        Ruimtedetailsoort.woon_en_of_slaapkamer,
        Ruimtedetailsoort.slaapkamer,
    ]:
        return False  # ruimte is geen ruimte dat een keuken zou kunnen zijn met een aanrecht erin

    if aanrecht_aantal == 0:  # ruimte is geen keuken want heeft geen valide aanrecht
        return False

    return True  # ruimte is een impliciete keuken vanwege een valide aanrecht


def _waardeer_aanrecht(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    """
    Waardeert de aanrechten van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de aanrechten gewaardeerd worden.
        stelsel (WoningwaarderingstelselReferentiedata): Het stelsel waarvoor de aanrechten gewaardeerd worden.

    Yields:
        WoningwaarderingResultatenWoningwaardering: De gewaardeerde aanrechten.
    """
    for element in ruimte.bouwkundige_elementen or []:
        if not element.detail_soort:
            warnings.warn(
                f"Bouwkundig element {element.id} heeft geen detailsoort en kan daardoor niet gewaardeerd worden.",
                UserWarning,
            )
            continue
        if element.detail_soort == Bouwkundigelementdetailsoort.aanrecht:
            if not element.lengte:
                warnings.warn(
                    f"{Bouwkundigelementdetailsoort.aanrecht.naam} {element.id} heeft geen lengte en kan daardoor niet gewaardeerd worden.",
                    UserWarning,
                )
                continue
            if element.lengte < 1000:
                aanrecht_punten = 0
            elif (
                element.lengte >= 2000
                and (
                    (  # zelfstandige keuken met aanrecht boven 2000mm is 7 punten
                        not gedeeld_met_onzelfstandige_woonruimten(ruimte)
                    )
                    or (  # onzelfstandige keuken met aanrecht tussen 2000mm en 3000mm is 7 punten
                        gedeeld_met_onzelfstandige_woonruimten(ruimte)
                        and element.lengte <= 3000
                    )
                )
            ):
                aanrecht_punten = 7
            elif (
                element.lengte > 3000
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
            ):
                aanrecht_punten = 13
            elif (
                element.lengte > 3000
                and stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten
            ):
                aanrecht_punten = 10

            else:
                aanrecht_punten = 4
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): een aanrecht van {int(element.lengte)}mm telt mee voor {Woningwaarderingstelselgroep.keuken.naam}"
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam}: Lengte {element.naam.lower() if element.naam else 'aanrecht'}",
                    meeteenheid=Meeteenheid.millimeter,
                ),
                punten=aanrecht_punten,
                aantal=element.lengte,
            )


def _waardeer_extra_voorzieningen(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    """
    Waardeert de extra voorzieningen van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de extra voorzieningen gewaardeerd worden.

    Yields:
        WoningwaarderingResultatenWoningwaardering: De gewaardeerde extra voorzieningen.
    """
    totaal_lengte_aanrechten = sum(
        Decimal(str(element.lengte or "0"))
        for element in ruimte.bouwkundige_elementen or []
        if element.detail_soort == Bouwkundigelementdetailsoort.aanrecht
    )

    punten_per_installatie: dict[Referentiedata, float] = {
        Voorzieningsoort.inbouw_afzuiginstallatie: 0.75,
        Voorzieningsoort.inbouw_kookplaat_inductie: 1.75,
        Voorzieningsoort.inbouw_kookplaat_keramisch: 1.0,
        Voorzieningsoort.inbouw_kookplaat_gas: 0.5,
        Voorzieningsoort.inbouw_koelkast: 1.0,
        Voorzieningsoort.inbouw_vrieskast: 0.75,
        Voorzieningsoort.inbouw_oven_elektrisch: 1.0,
        Voorzieningsoort.inbouw_oven_gas: 0.5,
        Voorzieningsoort.inbouw_magnetron: 1.0,
        Voorzieningsoort.inbouw_vaatwasmachine: 1.5,
        Voorzieningsoort.extra_keukenkastruimte_boven_het_minimum: 0.75,
        Voorzieningsoort.eenhandsmengkraan: 0.25,
        Voorzieningsoort.thermostatische_mengkraan: 0.5,
        Voorzieningsoort.kokend_waterfunctie: 0.5,
    }

    voorziening_counts = Counter(
        voorziening
        for voorziening in ruimte.installaties or []
        if voorziening in punten_per_installatie
    )
    punten_voor_extra_voorzieningen = sum(
        Decimal(str(punten_per_installatie[voorziening])) * Decimal(str(count))
        for voorziening, count in voorziening_counts.items()
    )

    for voorziening, count in voorziening_counts.items():
        punten = rond_af(
            Decimal(str(punten_per_installatie[voorziening])) * Decimal(str(count)),
            decimalen=2,
        )
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {count}x een '{voorziening.naam}' voor {Woningwaarderingstelselgroep.keuken.naam}."
        )
        yield (
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{voorziening.naam} (in zelfde ruimte)"
                    if count > 1
                    else voorziening.naam,
                ),
                punten=float(punten),
                aantal=count,
            )
        )

    max_punten_voorzieningen = (
        Decimal("7") if totaal_lengte_aanrechten >= Decimal("2000") else Decimal("4")
    )
    if punten_voor_extra_voorzieningen > max_punten_voorzieningen:
        aftrek = max_punten_voorzieningen - punten_voor_extra_voorzieningen
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aftrek} punt(en) i.v.m. te veel punten ({punten_voor_extra_voorzieningen} > {max_punten_voorzieningen}) voor extra keuken voorzieningen"
        )
        yield (
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Max. {max_punten_voorzieningen} punten voor voorzieningen in een (open) keuken met een aanrechtlengte van {totaal_lengte_aanrechten}mm",
                ),
                punten=float(aftrek),
            )
        )
