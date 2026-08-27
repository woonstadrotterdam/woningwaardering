import warnings
from collections import Counter
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica.aanrecht import (
    AANRECHT_MINIMALE_LENGTE_MM,
    heeft_valide_aanrecht,
    telt_aanrecht_mee,
)
from woningwaardering.stelsels.utils import rond_af
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

# Vertrek-detailsoorten die de keuken al in de naam hebben en daardoor voor
# rubriek 3 altijd een open keuken zijn, ook zonder aanrecht in de invoer.
# `keuken` zelf hoort hier niet bij: dat is een apart vertrek, geen open keuken.
OPEN_KEUKEN_DETAIL_SOORTEN = frozenset(
    {
        Ruimtedetailsoort.woonkamer_en_of_keuken,
        Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken,
    }
)


def waardeer_keuken(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    deler: int = 1,
) -> list[WaarderingBuilder]:
    if not _is_keuken(ruimte):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.keuken.naam}"
        )
        return []

    ruimte_criterium = waarderingsgroep_builder.met_subgroep(
        id=ruimte.id,
        naam=ruimte.naam
        or ruimte.id
        or (ruimte.detail_soort.naam if ruimte.detail_soort else ""),
    )

    aanrecht_waarderingen = _waardeer_aanrecht(ruimte, stelsel, ruimte_criterium)
    extra_waarderingen = list(_waardeer_extra_voorzieningen(ruimte, ruimte_criterium))
    detail_waarderingen = [*aanrecht_waarderingen, *extra_waarderingen]
    if not detail_waarderingen:
        return []

    punten_voor_extra_voorzieningen = sum(
        Decimal(str(waardering.punten))
        for waardering in extra_waarderingen
        if waardering.punten is not None
    )
    # 2.5.3 Punten voor extra voorzieningen keuken
    # Het aantal punten voor de extra voorzieningen kan niet meer zijn dan het
    # aantal punten voor de basisvoorzieningen (de aanrechtlengte).
    max_punten_voorzieningen = sum(
        Decimal(str(waardering.punten))
        for waardering in aanrecht_waarderingen
        if waardering.punten is not None
    )

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
        extra_voorzieningen_criterium = ruimte_criterium.met_subgroep(
            id="extra_voorzieningen",
            naam="Extra voorzieningen",
        )
        detail_waarderingen.append(
            extra_voorzieningen_criterium.met_onderliggend(
                id="maximering_extra_voorzieningen",
                naam="Maximaal evenveel punten als aanrecht",
                punten=aftrek,
            )
        )

    return [ruimte_criterium, *detail_waarderingen]


def _is_keuken(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of de ruimte een keuken is op basis van het aanrecht.

    Wettekst Bijlage I A rubriek 5 stelt eisen aan de keuken zelf, niet aan de
    ruimte waarin die ligt. Elke ruimte waarin een aanrecht meetelt
    (zie :func:`telt_aanrecht_mee`) is daarom een keuken zodra er een aanrecht
    vanaf 1 meter aanwezig is.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren.

    Returns:
        bool: True als de ruimte een keuken is, anders False.
    """
    valide_aanrecht = heeft_valide_aanrecht(ruimte)

    if not ruimte.detail_soort:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort",
            UserWarning,
        )
        return False

    if not telt_aanrecht_mee(ruimte):
        return (
            False  # buitenruimte of parkeervoorziening: een aanrecht telt hier niet mee
        )

    if ruimte.detail_soort in {
        Ruimtedetailsoort.keuken,
        *OPEN_KEUKEN_DETAIL_SOORTEN,
    }:
        if not valide_aanrecht:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >={AANRECHT_MINIMALE_LENGTE_MM}mm) en mag daardoor niet gewaardeerd worden voor {Woningwaarderingstelselgroep.keuken.naam}.",
                UserWarning,
            )
            return False  # ruimte is een keuken maar heeft geen valide aanrecht en mag dus niet als keuken gewaardeerd worden
        return True  # ruimte is een keuken met een valide aanrecht

    # elke andere ruimte is een keuken zodra er een valide aanrecht in staat
    return valide_aanrecht


def _waardeer_aanrecht(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> list[WaarderingBuilder]:
    """
    Waardeert de aanrechten van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de aanrechten gewaardeerd worden.
        stelsel (WoningwaarderingstelselReferentiedata): Het stelsel waarvoor de aanrechten gewaardeerd worden.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.

    Returns:
        list[WaarderingBuilder]: De puntdragende aanrechtwaardering, of een lege
        lijst als er geen geldig aanrecht is. Bij één aanrecht is dat de
        lengteregel zelf. Bij meerdere aanrechten is dat alleen de
        subtotaalregel; de lengtedetails hangen daaronder in de boom zonder
        punten.
    """
    aanrechten_met_lengte = []
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
            aanrechten_met_lengte.append(element)

    if not aanrechten_met_lengte:
        return []

    totaal_lengte_aanrechten = sum(
        (Decimal(str(element.lengte)) for element in aanrechten_met_lengte),
        start=Decimal("0"),
    )
    aanrecht_punten = _punten_voor_aanrechtlengte(
        totaal_lengte_aanrechten,
        ruimte,
        stelsel,
    )

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}): {len(aanrechten_met_lengte)} "
        f"aanrecht(en) van samen {int(totaal_lengte_aanrechten)}mm tellen mee voor "
        f"{Woningwaarderingstelselgroep.keuken.naam}"
    )

    details = [
        waarderingsgroep_builder.met_onderliggend(
            id=f"lengte_aanrecht_{element.id}",
            naam=f"Lengte {element.naam.lower() if element.naam else 'aanrecht'}",
            meeteenheid=Meeteenheid.millimeter,
            aantal=element.lengte,
        )
        for element in aanrechten_met_lengte
    ]

    if len(details) == 1:
        details[0].punten = aanrecht_punten
        return details

    subtotaal = waarderingsgroep_builder.met_onderliggend(
        id="subtotaal",
        naam="Totale aanrechtlengte",
        meeteenheid=Meeteenheid.millimeter,
        aantal=totaal_lengte_aanrechten,
        punten=aanrecht_punten,
    )
    for detail in details:
        detail.verplaats_naar(subtotaal)
    return [subtotaal]


def _punten_voor_aanrechtlengte(
    lengte: Decimal,
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
) -> Decimal:
    # 2.5.2 Punten voor basisvoorzieningen keuken
    # Zelfstandig: Tussen 1 en 2 meter → 4; Langer dan 2 meter → 7
    # Onzelfstandig: Tussen 1 en 2 meter → 4; Tussen 2 en 3 meter → 7;
    # Meer dan 3 meter → 10; Meer dan 5 meter* → 13
    # * Er worden 13 punten toegekend mits er minimaal 8 onzelfstandige
    # wooneenheden toegang en gebruiksrecht hebben tot de keuken.
    if lengte < AANRECHT_MINIMALE_LENGTE_MM:
        return Decimal("0")
    if stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten:
        if (
            lengte > 5000
            and (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 0) >= 8
        ):
            return Decimal("13")
        if lengte > 3000:
            return Decimal("10")
        if lengte >= 2000:
            return Decimal("7")
        return Decimal("4")
    if lengte >= 2000:
        return Decimal("7")
    return Decimal("4")


def _waardeer_extra_voorzieningen(
    ruimte: EenhedenRuimte,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> Iterator[WaarderingBuilder]:
    """
    Waardeert de extra voorzieningen van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de extra voorzieningen gewaardeerd worden.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.

    Yields:
        WaarderingBuilder: De gewaardeerde extra voorzieningen.
    """
    punten_per_installatie: dict[Referentiedata, float] = {
        Installatiesoort.inbouw_afzuiginstallatie: 0.75,
        Installatiesoort.inbouw_kookplaat_inductie: 1.75,
        Installatiesoort.inbouw_kookplaat_keramisch: 1.0,
        Installatiesoort.inbouw_kookplaat_gas: 0.5,
        Installatiesoort.inbouw_koelkast: 1.0,
        Installatiesoort.inbouw_vrieskast: 0.75,
        Installatiesoort.inbouw_koelvriescombinatie: 1.75,
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
    extra_voorzieningen_criterium = waarderingsgroep_builder.met_subgroep(
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
        yield extra_voorzieningen_criterium.met_onderliggend(
            id=f"extra_voorziening_{installatiesoort.name}",
            naam=installatiesoort.naam,
            meeteenheid=Meeteenheid.stuks,
            punten=punten,
            aantal=count,
        )
