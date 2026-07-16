import warnings
from collections import Counter
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.bouwers import (
    WaarderingBouwer,
    WaarderingsgroepBouwer,
)
from woningwaardering.stelsels.utils import (
    gedeeld_met_onzelfstandige_woonruimten,
    rond_af,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen


def waardeer_keuken(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
    *,
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
    deler: int = 1,
) -> list[WaarderingBouwer]:
    if not _is_keuken(ruimte):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.keuken.naam}"
        )
        return []

    ruimte_criterium = waarderingsgroep_bouwer.categorie(
        id=ruimte.id,
        naam=ruimte.naam
        or ruimte.id
        or (ruimte.detail_soort.naam if ruimte.detail_soort else ""),
    )

    aanrecht_waarderingen = list(_waardeer_aanrecht(ruimte, stelsel, ruimte_criterium))
    extra_waarderingen = list(_waardeer_extra_voorzieningen(ruimte, ruimte_criterium))
    detail_waarderingen = [*aanrecht_waarderingen, *extra_waarderingen]
    if not detail_waarderingen:
        return []

    punten_voor_extra_voorzieningen = sum(
        Decimal(str(waardering.punten))
        for waardering in extra_waarderingen
        if waardering.punten is not None
    )
    max_punten_voorzieningen = _max_punten_voorzieningen(ruimte)

    # De punten van een gedeelde ruimte worden gedeeld door het aantal woonruimten
    # waarmee de ruimte gedeeld wordt.
    if deler > 1:
        for waardering in detail_waarderingen:
            if waardering.punten is not None:
                waardering.punten = float(
                    rond_af(
                        Decimal(str(waardering.punten)) / Decimal(deler),
                        decimalen=2,
                    )
                )

    if punten_voor_extra_voorzieningen > max_punten_voorzieningen:
        # Maximum tot het aantal punten dat voor de aanrechtlengte is bepaald.
        aftrek_ongedeeld = max_punten_voorzieningen - punten_voor_extra_voorzieningen
        aftrek = rond_af(aftrek_ongedeeld / Decimal(deler), decimalen=2)
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aftrek_ongedeeld} punt(en) i.v.m. te veel punten ({punten_voor_extra_voorzieningen} > {max_punten_voorzieningen}) voor extra keuken voorzieningen"
        )
        extra_voorzieningen_criterium = ruimte_criterium.categorie(
            id="extra_voorzieningen",
            naam="Extra voorzieningen",
        )
        detail_waarderingen.append(
            extra_voorzieningen_criterium.maak_onderliggende(
                id="maximering_extra_voorzieningen",
                naam="Maximaal evenveel punten als aanrecht",
                punten=aftrek,
            )
        )

    return [ruimte_criterium, *detail_waarderingen]


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
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> Iterator[WaarderingBouwer]:
    """
    Waardeert de aanrechten van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de aanrechten gewaardeerd worden.
        stelsel (WoningwaarderingstelselReferentiedata): Het stelsel waarvoor de aanrechten gewaardeerd worden.
        waarderingsgroep_bouwer (WaarderingsgroepBouwer | WaarderingBouwer): waarderingsgroep of bestaande waardering in de hiërarchie.

    Yields:
        WaarderingBouwer: De gewaardeerde aanrechten.
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
            yield waarderingsgroep_bouwer.maak_onderliggende(
                id=f"lengte_aanrecht_{element.id}",
                naam=f"Lengte {element.naam.lower() if element.naam else 'aanrecht'}",
                meeteenheid=Meeteenheid.millimeter,
                punten=aanrecht_punten,
                aantal=element.lengte,
            )


def _max_punten_voorzieningen(ruimte: EenhedenRuimte) -> Decimal:
    totaal_lengte_aanrechten = sum(
        Decimal(str(element.lengte or "0"))
        for element in ruimte.bouwkundige_elementen or []
        if element.detail_soort == Bouwkundigelementdetailsoort.aanrecht
    )
    return Decimal("7") if totaal_lengte_aanrechten >= Decimal("2000") else Decimal("4")


def _waardeer_extra_voorzieningen(
    ruimte: EenhedenRuimte,
    waarderingsgroep_bouwer: WaarderingsgroepBouwer | WaarderingBouwer,
) -> Iterator[WaarderingBouwer]:
    """
    Waardeert de extra voorzieningen van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de extra voorzieningen gewaardeerd worden.
        waarderingsgroep_bouwer (WaarderingsgroepBouwer | WaarderingBouwer): waarderingsgroep of bestaande waardering in de hiërarchie.

    Yields:
        WaarderingBouwer: De gewaardeerde extra voorzieningen.
    """
    punten_per_installatie: dict[Referentiedata, float] = {
        Installatiesoort.inbouw_afzuiginstallatie: 0.75,
        Installatiesoort.inbouw_kookplaat_inductie: 1.75,
        Installatiesoort.inbouw_kookplaat_keramisch: 1.0,
        Installatiesoort.inbouw_kookplaat_gas: 0.5,
        Installatiesoort.inbouw_koelkast: 1.0,
        Installatiesoort.inbouw_vrieskast: 0.75,
        Installatiesoort.inbouw_oven_elektrisch: 1.0,
        Installatiesoort.inbouw_oven_gas: 0.5,
        Installatiesoort.inbouw_magnetron: 1.0,
        Installatiesoort.inbouw_combi_magnetron_en_of_oven: 2,
        Installatiesoort.inbouw_vaatwasmachine: 1.5,
        Installatiesoort.extra_keukenkastruimte_boven_het_minimum: 0.75,
        Installatiesoort.eenhandsmengkraan: 0.25,
        Installatiesoort.thermostatische_mengkraan: 0.5,
        Installatiesoort.kokend_waterfunctie: 0.5,
    }

    installaties = Counter(ruimte.installaties or [])
    extra_voorzieningen_criterium = waarderingsgroep_bouwer.categorie(
        id="extra_voorzieningen",
        naam="Extra voorzieningen",
    )

    for installatiesoort in punten_per_installatie:
        count = installaties[installatiesoort]
        if count == 0:
            continue

        punten = rond_af(
            Decimal(str(punten_per_installatie[installatiesoort]))
            * Decimal(str(count)),
            decimalen=2,
        )
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {count}x een '{installatiesoort.naam}' voor {Woningwaarderingstelselgroep.keuken.naam}."
        )
        yield extra_voorzieningen_criterium.maak_onderliggende(
            id=f"extra_voorziening_{installatiesoort.name}",
            naam=installatiesoort.naam,
            meeteenheid=Meeteenheid.stuks,
            punten=punten,
            aantal=count,
        )
