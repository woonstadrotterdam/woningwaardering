from datetime import date
from decimal import Decimal
from typing import Iterator

from woningwaardering._logging import logger
from woningwaardering.stelsels.utils import gedeeld_met_eenheden, rond_af
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.doelgroep import Doelgroep
from woningwaardering.vera.referentiedata.voorzieningsoort import Voorzieningsoort
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import aantal_bouwkundige_elementen


def waardeer(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroepen_zonder_opslag: list[Woningwaarderingstelselgroep],
    stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat | None
    ) = None,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    """Genereert de woningwaarderingen voor bijzondere voorzieningen.

    Args:
        peildatum (date): De peildatum.
        eenheid (EenhedenEenheid): De eenheid.
        stelselgroepen_zonder_opslag (list[Woningwaarderingstelselgroep]): De stelselgroepen die niet moeten worden opgehoogd met zorgwoning opslag.
        stelsel (Woningwaarderingstelsel): Het woningwaarderingsstelsel.
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Het woningwaardering resultaat.

    Yields:
        WoningwaarderingResultatenWoningwaardering: De woningwaarderingen.
    """
    woningwaarderingen = [
        opslag_zorgwoning(
            peildatum,
            eenheid,
            stelselgroepen_zonder_opslag,
            stelsel,
            woningwaardering_resultaat,
        ),
        aanbelfunctie_met_video_en_audioverbinding(eenheid),
        prive_laadpaal(eenheid),
    ]

    for waardering in woningwaarderingen:
        if waardering is not None:
            yield waardering


def opslag_zorgwoning(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroepen_zonder_opslag: list[Woningwaarderingstelselgroep],
    stelsel: Woningwaarderingstelsel,
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat | None
    ) = None,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Als sprake is van een zorgwoning, dan volgt er een opslag van 35% op het puntentotaal van
    de rubrieken 1 tot en met 11 (of 1 tot en met 10 voor onzelfstandige woonruimten) van het
    woningwaarderingsstelsel. Deze opslag wordt gedaan in de rubriek Bijzondere voorzieningen.

    Args:
        peildatum (date): De peildatum voor de berekening.
        eenheid (EenhedenEenheid): De eenheid die wordt gewaardeerd.
        stelselgroepen_zonder_opslag (list[Woningwaarderingstelselgroep]): Lijst van stelselgroepen die niet worden meegenomen in de opslag.
        stelsel (Woningwaarderingstelsel): Het type woningwaarderingsstelsel.
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Het bestaande waarderingsresultaat, indien aanwezig.

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De woningwaardering met 35% opslag als het een zorgwoning betreft, anders None.

    Raises:
        ValueError: Als het stelsel niet gelijk is aan zelfstandige woonruimten of onzelfstandige woonruimten.
    """
    if eenheid.doelgroep is None or (
        eenheid.doelgroep and eenheid.doelgroep.code != Doelgroep.zorg.code
    ):
        logger.debug(
            f"Eenheid ({eenheid.id}) is geen zorgwoning en krijgt dus geen zorgwoningopslag"
        )
        return None

    if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
        logger.warning(
            "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
        )
        if stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten:
            from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                ZelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = ZelfstandigeWoonruimten(
                peildatum=peildatum
            ).bereken(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen,
            )

        elif stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten:
            from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
                OnzelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = OnzelfstandigeWoonruimten(
                peildatum=peildatum
            ).bereken(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen,
            )
        else:
            raise ValueError(
                f"Invalid stelsel {stelsel}. Bijzondere voorzieningen zijn alleen gedefinieerd voor {Woningwaarderingstelsel.zelfstandige_woonruimten.naam} en {Woningwaarderingstelsel.onzelfstandige_woonruimten.naam}"
            )

    puntentotaal = rond_af(
        sum(
            Decimal(str(groep.punten or "0")) or Decimal()
            for groep in woningwaardering_resultaat.groepen or []
            if (
                groep.punten
                and groep.criterium_groep
                and groep.criterium_groep.stelselgroep
                and groep.criterium_groep.stelselgroep.code
                not in [
                    stelselgroep.code for stelselgroep in stelselgroepen_zonder_opslag
                ]
            )
        ),
        0,
    )

    logger.info(
        f"Eenheid ({eenheid.id}): Puntentotaal van de rubrieken 1 tot en met 11 van het woningwaarderingsstelsel is {puntentotaal}"
    )

    verhoging = puntentotaal * Decimal("0.35")

    logger.info(
        f"Eenheid ({eenheid.id}) is een zorgwoning: {verhoging} punten voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Zorgwoning 35% puntenverhoging",
        ),
        punten=float(verhoging),
    )


def aanbelfunctie_met_video_en_audioverbinding(
    eenheid: EenhedenEenheid,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Een aanbelfunctie met video- en audioverbinding waarbij de voordeur
    automatisch kan worden geopend vanuit de woning wordt gewaardeerd
    met 0,25 punt.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de opslag berekend wordt.

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De woningwaardering met 0,25 punt
        als de eenheid een aanbelfunctie met video en audio heeft, anders None.
    """
    if not any(
        installatie.code
        == Voorzieningsoort.aanbelfunctie_met_video_en_audioverbinding.code
        for ruimte in (eenheid.ruimten or [])
        for installatie in (ruimte.installaties or [])
    ):
        logger.debug(
            f"Eenheid ({eenheid.id}) heeft geen aanbelfunctie met video en audioverbinding"
        )
        return None

    logger.info(
        f"Eenheid ({eenheid.id}) heeft een aanbelfunctie met video en audioverbinding: 0.25 punt voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Aanbelfunctie met video- en audioverbinding",
        ),
        punten=0.25,
    )


def prive_laadpaal(
    eenheid: EenhedenEenheid,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik
    door de bewoners wordt gewaardeerd met 2 punten.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de waardering berekend wordt.
    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De woningwaardering met 2 punten
        als de eenheid een laadpaal heeft, anders None.
    """
    aantal_laadpalen = sum(
        aantal_bouwkundige_elementen(ruimte, Bouwkundigelementdetailsoort.laadpaal)
        for ruimte in eenheid.ruimten or []
        if not gedeeld_met_eenheden(ruimte)
    )

    if aantal_laadpalen == 0:
        logger.debug(f"Eenheid ({eenheid.id}) heeft geen privé laadpaal")
        return None

    punten_laadpalen = aantal_laadpalen * 2

    logger.info(
        f"Eenheid ({eenheid.id}) heeft {aantal_laadpalen} {'laadpaal' if aantal_laadpalen == 1 else 'laadpalen'}: {punten_laadpalen} punten voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Laadpalen",
        ),
        aantal=aantal_laadpalen,
        punten=punten_laadpalen,
    )
