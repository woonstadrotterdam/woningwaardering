import warnings
from datetime import date
from decimal import Decimal
from typing import Callable, List, Tuple

from loguru import logger

from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenPrijscomponent,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Prijscomponentdetailsoort,
    Woningwaarderingstelselgroep,
)

# 2.4.3.4 Energielabel afgegeven in de periode 1 januari 2015 tot 1 januari 2021
# Een energielabel dat is afgegeven in de periode van 1 januari 2015 tot 1 januari
# 2021 krijgt geen punten in het woningwaarderingsstelsel. Dit zijn namelijk de
# zogenaamde 'vereenvoudigde energielabels'. Alleen energie-indexen die in de
# genoemde periode zijn afgegeven komen in aanmerking voor waardering.
VEREENVOUDIGD_LABEL_PERIODE_START = date(2015, 1, 1)
VEREENVOUDIGD_LABEL_PERIODE_EINDE = date(2021, 1, 1)


def in_vereenvoudigd_label_periode(begindatum: date) -> bool:
    """
    Of ``begindatum`` valt in de periode van de 'vereenvoudigde energielabels' (2.4.3.4).

    In deze periode (1 januari 2015 tot 1 januari 2021) telt alleen een energie-index
    mee voor de woningwaardering; een energielabel uit die periode krijgt geen punten.

    Args:
        begindatum (date): Begindatum van de energieprestatie.

    Returns:
        bool: True als ``begindatum`` in de periode valt, anders False.
    """
    return (
        VEREENVOUDIGD_LABEL_PERIODE_START
        <= begindatum
        < VEREENVOUDIGD_LABEL_PERIODE_EINDE
    )


def monument_correctie(
    eenheid: EenhedenEenheid,
    woningwaardering: WaarderingBuilder,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> WaarderingBuilder | None:
    """
    Berekent de correctie voor monumenten.
    Voor rijks-, provinciale en gemeentelijke monumenten geldt dat de waardering voor energieprestatie minimaal 0 punten is.

    Args:
        eenheid (EenhedenEenheid): Eenheid
        woningwaardering (WaarderingBuilder): De waardering voor Energieprestatie tot zover.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.

    Returns:
        WaarderingBuilder | None: De correctiewaardering indien van toepassing, anders None
    """

    is_rijks_provinciaal_of_gemeentelijk_monument = eenheid.monumenten and any(
        monument
        in [
            Eenheidmonument.rijksmonument,
            Eenheidmonument.gemeentelijk_monument,
            Eenheidmonument.provinciaal_monument,
        ]
        for monument in eenheid.monumenten or []
    )
    if not is_rijks_provinciaal_of_gemeentelijk_monument:
        return None

    punten = woningwaardering.punten
    minimum_punten = Decimal("0.0")

    if punten is None or punten >= minimum_punten:
        return None

    correctie_punten = minimum_punten - Decimal(str(punten))

    logger.info(
        f"Eenheid ({eenheid.id}) is een monument: waardering voor {Woningwaarderingstelselgroep.energieprestatie.naam} is minimaal {minimum_punten} punten."
    )
    return waarderingsgroep_builder.met_onderliggend(
        id="correctie_monument",
        naam="Correctie monument",
        punten=correctie_punten,
    )


def get_energieprestatievergoeding(
    peildatum: date,
    eenheid: EenhedenEenheid,
) -> EenhedenPrijscomponent | None:
    """
    Geeft de eerst gevonden geldige energieprestatievergoeding voor de eenheid.

    Args:
        peildatum (date): Peildatum
        eenheid (EenhedenEenheid): Eenheid

    Returns:
        EenhedenPrijscomponent | None: Energieprestatievergoeding of None indien niet gevonden.
    """
    return next(
        (
            prijscomponent
            for prijscomponent in eenheid.prijscomponenten or []
            if prijscomponent.detail_soort
            == Prijscomponentdetailsoort.energieprestatievergoeding
            and (
                prijscomponent.begindatum is None
                or prijscomponent.begindatum <= peildatum
            )
            and (
                prijscomponent.einddatum is None or prijscomponent.einddatum > peildatum
            )
        ),
        None,
    )


def energieprestatie_met_geldig_label(
    peildatum: date, eenheid: EenhedenEenheid
) -> EenhedenEnergieprestatie | None:
    """
    Returnt de eerste geldige energieprestatie met een energielabel van een eenheid.

    Args:
        peildatum (date): De peildatum waarop de energieprestatie geldig moet zijn.
        eenheid (EenhedenEenheid): De eenheid met mogelijke energieprestaties.

    Returns:
        EenhedenEnergieprestatie | None: De eerst geldige energieprestatie en None wanneer er geen geldige energieprestatie met label is gevonden.
    """
    aantal_energieprestaties = len(eenheid.energieprestaties or [])
    if aantal_energieprestaties == 0:
        warnings.warn(
            f"Eenheid ({eenheid.id}): 'energieprestaties' is None", UserWarning
        )
        return None

    vereiste_attributen: List[
        Tuple[str, Callable[[EenhedenEnergieprestatie], bool]]
    ] = [
        ("soort", lambda ep: ep.soort is not None),
        ("status", lambda ep: ep.status is not None),
        ("begindatum", lambda ep: ep.begindatum is not None),
        ("einddatum", lambda ep: ep.einddatum is not None),
    ]

    for idx, energieprestatie in enumerate(eenheid.energieprestaties or []):
        logger.debug(
            f"Eenheid ({eenheid.id}): energieprestatie {idx + 1} van {aantal_energieprestaties} wordt gevalideerd."
        )
        ontbrekende_attributen = [
            naam for naam, check in vereiste_attributen if not check(energieprestatie)
        ]
        if ontbrekende_attributen:
            logger.debug(
                f"Eenheid ({eenheid.id}) mist energieprestatie attributen: {', '.join(ontbrekende_attributen)}."
            )
            continue

        if energieprestatie.soort not in (
            Energieprestatiesoort.energie_index,
            Energieprestatiesoort.energielabel_conform_nta8800,
            Energieprestatiesoort.primair_energieverbruik_woningbouw,
            Energieprestatiesoort.voorlopig_energielabel,
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): ongeldige energieprestatiesoort '{energieprestatie.soort}'."
            )
            continue

        # 2.4.3 Geldigheid energieprestatie op peildatum (beleidsboek).
        # Wij berekenen de 10-jaarsgeldigheid niet zelf; wij gaan uit van de geldigheid van het energielabel.
        # In EP-online is dat de 'Geldig tot'-datum; in VERA is dat einddatum. Peildatum moet vóór einddatum liggen.
        begindatum = energieprestatie.begindatum
        einddatum = energieprestatie.einddatum
        if begindatum is None or einddatum is None:
            continue
        if not (begindatum <= peildatum < einddatum):
            logger.debug(
                f"Eenheid ({eenheid.id}): peildatum {peildatum} valt buiten geldigheidsperiode van de energieprestatie."
            )
            continue

        if energieprestatie.status != Energieprestatiestatus.definitief:
            logger.debug(
                f"Eenheid ({eenheid.id}): energieprestatie status is niet definitief."
            )
            continue

        if (
            in_vereenvoudigd_label_periode(begindatum)
            and energieprestatie.soort != Energieprestatiesoort.energie_index
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): energielabel in periode 2015-2021 is geen geldige energieprestatie voor de woningwaardering."
            )
            continue

        if (
            energieprestatie.soort != Energieprestatiesoort.energie_index
            and energieprestatie.label is None
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): energieprestatie zonder label is onbruikbaar voor labelwaardering."
            )
            continue

        logger.info(f"Eenheid ({eenheid.id}): geldige energieprestatie gevonden.")
        logger.debug(
            f"Energieprestatie: id={energieprestatie.id} soort={energieprestatie.soort.naam if energieprestatie.soort else None}"
            f" status={energieprestatie.status.naam if energieprestatie.status else None}"
            f" label={energieprestatie.label.naam if energieprestatie.label else None}"
            f" waarde={energieprestatie.waarde} begindatum={energieprestatie.begindatum}"
            f" einddatum={energieprestatie.einddatum}"
        )
        return energieprestatie

    logger.info(f"Eenheid ({eenheid.id}): geen geldige energieprestatie gevonden.")
    return None
