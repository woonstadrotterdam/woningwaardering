from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.utils import gedeeld_met_adressen
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Installatiesoort,
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import aantal_bouwkundige_elementen


def waardeer_bijzondere_voorzieningen(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroepen_zonder_opslag: list[WoningwaarderingstelselgroepReferentiedata],
    stelsel: WoningwaarderingstelselReferentiedata,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat | None
    ) = None,
) -> list[WaarderingBuilder]:
    """Genereert de woningwaarderingen voor bijzondere voorzieningen.

    Args:
        peildatum (date): De peildatum.
        eenheid (EenhedenEenheid): De eenheid.
        stelselgroepen_zonder_opslag (list[WoningwaarderingstelselgroepReferentiedata]): De stelselgroepen die niet moeten worden opgehoogd met zorgwoning opslag.
        stelsel (WoningwaarderingstelselReferentiedata): Het woningwaarderingsstelsel.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Het woningwaardering resultaat.

    Returns:
        list[WaarderingBuilder]: De aangemaakte woningwaarderingen.
    """
    woningwaarderingen = [
        _opslag_zorgwoning(
            peildatum,
            eenheid,
            stelselgroepen_zonder_opslag,
            stelsel,
            waarderingsgroep_builder,
            woningwaardering_resultaat,
        ),
        _aanbelfunctie_met_video_en_audioverbinding(eenheid, waarderingsgroep_builder),
        _prive_laadpaal(eenheid, waarderingsgroep_builder),
    ]

    return [waardering for waardering in woningwaarderingen if waardering is not None]


def _opslag_zorgwoning(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroepen_zonder_opslag: list[WoningwaarderingstelselgroepReferentiedata],
    stelsel: WoningwaarderingstelselReferentiedata,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat | None
    ) = None,
) -> WaarderingBuilder | None:
    """Als sprake is van een zorgwoning, dan volgt er een opslag van 35% op het puntentotaal van
    de rubrieken 1 tot en met 11 (of 1 tot en met 10 voor onzelfstandige woonruimten) van het
    woningwaarderingsstelsel. Deze opslag wordt gedaan in de rubriek Bijzondere voorzieningen.

    Args:
        peildatum (date): De peildatum voor de berekening.
        eenheid (EenhedenEenheid): De eenheid die wordt gewaardeerd.
        stelselgroepen_zonder_opslag (list[WoningwaarderingstelselgroepReferentiedata]): Lijst van stelselgroepen die niet worden meegenomen in de opslag.
        stelsel (WoningwaarderingstelselReferentiedata): Het type woningwaarderingsstelsel.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Het bestaande waarderingsresultaat, indien aanwezig.

    Returns:
        WaarderingBuilder | None: De woningwaardering met 35% opslag als het een zorgwoning betreft, anders None.

    Raises:
        ValueError: Als het stelsel niet gelijk is aan zelfstandige woonruimten of onzelfstandige woonruimten.
    """
    if eenheid.doelgroep is None or (
        eenheid.doelgroep and eenheid.doelgroep != Doelgroep.zorg
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
            ).waardeer(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen,
            )

        elif stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten:
            from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
                OnzelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = OnzelfstandigeWoonruimten(
                peildatum=peildatum
            ).waardeer(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen,
            )
        else:
            raise ValueError(
                f"Invalid stelsel {stelsel}. Bijzondere voorzieningen zijn alleen gedefinieerd voor {Woningwaarderingstelsel.zelfstandige_woonruimten.naam} en {Woningwaarderingstelsel.onzelfstandige_woonruimten.naam}"
            )

    puntentotaal = sum(
        Decimal(str(groep.punten or "0")) or Decimal()
        for groep in woningwaardering_resultaat.groepen or []
        if (
            groep.punten
            and groep.criterium_groep
            and groep.criterium_groep.stelselgroep not in stelselgroepen_zonder_opslag
        )
    )

    logger.info(
        f"Eenheid ({eenheid.id}): Puntentotaal van de rubrieken 1 tot en met 11 van het woningwaarderingsstelsel is {puntentotaal}"
    )

    verhoging = utils.rond_af_op_kwart(puntentotaal * Decimal("0.35"))

    logger.info(
        f"Eenheid ({eenheid.id}) is een zorgwoning: {verhoging} punten voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return waarderingsgroep_builder.maak_onderliggende(
        id="zorgwoning_puntenverhoging",
        naam="Zorgwoning 35% puntenverhoging",
        punten=float(verhoging),
    )


def _aanbelfunctie_met_video_en_audioverbinding(
    eenheid: EenhedenEenheid,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> WaarderingBuilder | None:
    """Een aanbelfunctie met video- en audioverbinding waarbij de voordeur
    automatisch kan worden geopend vanuit de woning wordt gewaardeerd
    met 0,25 punt.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de opslag berekend wordt.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.

    Returns:
        WaarderingBuilder | None: De woningwaardering met 0,25 punt
        als de eenheid een aanbelfunctie met video en audio heeft, anders None.
    """
    if not any(
        installatie == Installatiesoort.aanbelfunctie_met_video_en_audioverbinding
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

    return waarderingsgroep_builder.maak_onderliggende(
        id="aanbelfunctie_met_video_en_audioverbinding",
        naam="Aanbelfunctie met video- en audioverbinding",
        punten=0.25,
    )


def _prive_laadpaal(
    eenheid: EenhedenEenheid,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> WaarderingBuilder | None:
    """Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik
    door de bewoners wordt gewaardeerd met 2 punten.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de waardering berekend wordt.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.
    Returns:
        WaarderingBuilder | None: De woningwaardering met 2 punten
        als de eenheid een laadpaal heeft, anders None.
    """
    aantal_laadpalen = sum(
        aantal_bouwkundige_elementen(ruimte, Bouwkundigelementdetailsoort.laadpaal)
        for ruimte in eenheid.ruimten or []
        if not gedeeld_met_adressen(ruimte)
    )

    if aantal_laadpalen == 0:
        logger.debug(f"Eenheid ({eenheid.id}) heeft geen privé laadpaal")
        return None

    punten_laadpalen = aantal_laadpalen * 2

    logger.info(
        f"Eenheid ({eenheid.id}) heeft {aantal_laadpalen} {'laadpaal' if aantal_laadpalen == 1 else 'laadpalen'}: {punten_laadpalen} punten voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return waarderingsgroep_builder.maak_onderliggende(
        id="laadpalen",
        naam="Laadpalen",
        meeteenheid=Meeteenheid.stuks,
        aantal=aantal_laadpalen,
        punten=punten_laadpalen,
    )
