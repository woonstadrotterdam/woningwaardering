import warnings
from datetime import date, datetime, time
from decimal import ROUND_HALF_UP, Decimal
from functools import wraps
from importlib.resources import files
from typing import Callable, Counter, Iterator, List, Tuple

import pandas as pd
import requests
from dateutil.relativedelta import relativedelta
from loguru import logger
from prettytable import PrettyTable
from SPARQLWrapper import SPARQLWrapper2

from woningwaardering.stelsels import utils
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenRuimte,
    EenhedenWoonplaats,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Eenheidmonument,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Ruimtedetailsoort,
    Ruimtesoort,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element

index: int = 0  # nodig voor mypy voor de global index voor de tabel


def is_geldig(
    begindatum: date = date.min,
    einddatum: date = date.max,
    peildatum: date = date.today(),
) -> bool:
    """
    Controleert of de peildatum valt tussen de begindatum en einddatum.

    Parameters:
        begindatum (date): De begindatum.
        einddatum (date): De einddatum.
        peildatum (date): De peildatum.

    Returns:
        bool: True als de peildatum tussen de begindatum en einddatum valt, anders False.
    """
    return begindatum <= peildatum <= einddatum


def _voeg_onderliggende_woningwaarderingen_toe(
    table: PrettyTable,
    stelselgroep_naam: str,
    woningwaardering: WoningwaarderingResultatenWoningwaardering,
    woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
    aantal_waarderingen: int,
    indent: int = 0,
) -> None:
    """
    Voeg de onderliggende woningwaarderingen toe aan de tabel.
    """

    global index

    if not woningwaardering.criterium or not woningwaardering.criterium.id:
        return

    onderliggende_woningwaarderingen = [
        onderliggende_woningwaardering
        for onderliggende_woningwaardering in woningwaarderingen
        if onderliggende_woningwaardering.criterium is not None
        and onderliggende_woningwaardering.criterium.bovenliggende_criterium is not None
        and onderliggende_woningwaardering.criterium.bovenliggende_criterium.id
        == woningwaardering.criterium.id
    ]

    for onderliggende_woningwaardering in onderliggende_woningwaarderingen:
        if onderliggende_woningwaardering.criterium is not None:
            index += 1
            table.add_row(
                [
                    stelselgroep_naam,
                    f"{' '*indent} - {onderliggende_woningwaardering.criterium.naam}",
                    f"{'['*indent}{onderliggende_woningwaardering.aantal}{']'*indent}"
                    if onderliggende_woningwaardering.aantal is not None
                    else "",
                    onderliggende_woningwaardering.criterium.meeteenheid.naam
                    if onderliggende_woningwaardering.criterium.meeteenheid is not None
                    else "",
                    f"{'['*indent}{rond_af(onderliggende_woningwaardering.punten, decimalen=2)}{']'*indent}"
                    if onderliggende_woningwaardering.punten is not None
                    else "",
                    f"{onderliggende_woningwaardering.opslagpercentage:.0%}"
                    if onderliggende_woningwaardering.opslagpercentage is not None
                    else "",
                ],
                divider=index == aantal_waarderingen,
            )

        _voeg_onderliggende_woningwaarderingen_toe(
            table,
            stelselgroep_naam,
            onderliggende_woningwaardering,
            woningwaarderingen,
            aantal_waarderingen=aantal_waarderingen,
            indent=indent + 1,
        )


def naar_tabel(
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat
        | WoningwaarderingResultatenWoningwaarderingGroep
    ),
) -> PrettyTable:
    """
    Genereer een tabel met de details van een woningwaarderingresultaat.

    Parameters:
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | WoningwaarderingResultatenWoningwaarderingGroep): Het object om de gegevens uit te halen

    Returns:
        PrettyTable: Een tabel met de gegevens van het woningwaarderingresultaat
    """
    table = PrettyTable()
    table.field_names = [
        "Groep",
        "Naam",
        "Aantal",
        "Meeteenheid",
        "Punten",
        "Opslag",
    ]
    table.align["Groep"] = "l"
    table.align["Naam"] = "l"
    table.align["Aantal"] = "r"
    table.align["Meeteenheid"] = "l"
    table.align["Punten"] = "r"
    table.align["Opslag"] = "r"
    table.float_format = ".2"

    table._min_width = {
        "Groep": 33,
        "Naam": 75,
        "Aantal": 12,
        "Meeteenheid": 19,
        "Punten": 8,
        "Opslag": 7,
    }

    table._max_width = table._min_width

    for woningwaardering_groep in (
        woningwaardering_resultaat.groepen or []
        if isinstance(
            woningwaardering_resultaat,
            WoningwaarderingResultatenWoningwaarderingResultaat,
        )
        else [woningwaardering_resultaat]
    ):
        stelselgroep_naam = (
            woningwaardering_groep.criterium_groep
            and woningwaardering_groep.criterium_groep.stelselgroep
            and woningwaardering_groep.criterium_groep.stelselgroep.naam
            or ""
        )
        stelselgroep_naam = (
            (stelselgroep_naam[:30] + "...")
            if len(stelselgroep_naam) > 33
            else stelselgroep_naam
        )
        woningwaarderingen = woningwaardering_groep.woningwaarderingen or []
        aantal_waarderingen = len(woningwaarderingen)
        global index
        index = 0

        for woningwaardering in [
            woningwaardering
            for woningwaardering in woningwaarderingen
            if woningwaardering.criterium is not None
            and woningwaardering.criterium.bovenliggende_criterium is None
        ]:
            if (
                woningwaardering_groep.criterium_groep
                and woningwaardering_groep.criterium_groep.stelselgroep
                and woningwaardering.criterium
            ):
                index += 1
                table.add_row(
                    [
                        stelselgroep_naam,
                        woningwaardering.criterium.naam,
                        woningwaardering.aantal or "",
                        woningwaardering.criterium.meeteenheid.naam
                        if woningwaardering.criterium.meeteenheid is not None
                        else "",
                        rond_af(woningwaardering.punten, decimalen=2)
                        if woningwaardering.punten is not None
                        else "",
                        f"{woningwaardering.opslagpercentage:.0%}"
                        if woningwaardering.opslagpercentage is not None
                        else "",
                    ],
                    divider=index == aantal_waarderingen,
                )

                _voeg_onderliggende_woningwaarderingen_toe(
                    table,
                    stelselgroep_naam,
                    woningwaardering,
                    woningwaarderingen,
                    indent=1,
                    aantal_waarderingen=aantal_waarderingen,
                )

        aantallen = [
            Decimal(woningwaardering.aantal)
            for woningwaardering in woningwaarderingen
            if woningwaardering.aantal is not None
            and woningwaardering.criterium is not None
            and woningwaardering.criterium.bovenliggende_criterium is None
        ]

        subtotaal = rond_af(sum(aantallen), 2) if aantallen else None

        if (
            (subtotaal is not None or aantal_waarderingen > 1)
            and woningwaardering_groep.criterium_groep
            and woningwaardering_groep.criterium_groep.stelselgroep
        ):
            # stukje hieronder is om subtotaal en meeteenheid te bepalen.
            # indien er meerdere meeteenheden zijn, dan wordt het subtotaal en de meeteenheid leeg bij subtotalen
            meeteenheden_zonder_nones = [
                woningwaardering.criterium.meeteenheid.naam or ""
                for woningwaardering in woningwaarderingen
                if woningwaardering.criterium is not None
                and woningwaardering.criterium.meeteenheid is not None
            ]
            critera = [
                woningwaardering.criterium or ""
                for woningwaardering in woningwaarderingen
                if woningwaardering.criterium is not None
            ]
            verschillende_meeteenheden = len(set(meeteenheden_zonder_nones)) > 1 or len(
                critera
            ) != len(meeteenheden_zonder_nones)

            if verschillende_meeteenheden:
                meeteenheid = ""
            else:
                meeteenheid = meeteenheden_zonder_nones[0]

            table.add_row(
                [
                    woningwaardering_groep.criterium_groep.stelselgroep.naam,
                    "Totaal",
                    (subtotaal or "") if not verschillende_meeteenheden else "",
                    meeteenheid if not verschillende_meeteenheden else "",
                    rond_af(woningwaardering_groep.punten, decimalen=2) or "",
                    f"{woningwaardering_groep.opslagpercentage:.0%}"
                    if woningwaardering_groep.opslagpercentage is not None
                    else "",
                ],
                divider=True,
            )
    if (
        isinstance(
            woningwaardering_resultaat,
            WoningwaarderingResultatenWoningwaarderingResultaat,
        )
        and woningwaardering_resultaat.stelsel
    ):
        table.add_row(
            [
                woningwaardering_resultaat.stelsel.naam,
                "Afgerond totaal",
                "",
                "",
                woningwaardering_resultaat.punten,
                f"{woningwaardering_resultaat.opslagpercentage:.0%}"
                if woningwaardering_resultaat.opslagpercentage is not None
                else "",
            ],
            divider=True,
        )

        if woningwaardering_resultaat.maximale_huur is None:
            return table

        table.add_row(
            [
                "",
                "Maximale huur",
                woningwaardering_resultaat.maximale_huur,
                "EUR",
                "",
                "",
            ],
        )
        if woningwaardering_resultaat.opslagpercentage is not None:
            table.add_row(
                [
                    "",
                    f"Huurprijsopslag {woningwaardering_resultaat.opslagpercentage:.0%}",
                    woningwaardering_resultaat.huurprijsopslag,
                    "EUR",
                    "",
                    "",
                ],
                divider=True,
            )
            table.add_row(
                [
                    "",
                    "Maximale huur inclusief opslag",
                    woningwaardering_resultaat.maximale_huur_inclusief_opslag,
                    "EUR",
                    "",
                    "",
                ],
            )

    return table


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
        ("registratiedatum", lambda ep: ep.registratiedatum is not None),
        ("soort", lambda ep: ep.soort is not None and ep.soort.code is not None),
        ("status", lambda ep: ep.status is not None and ep.status.code is not None),
        ("begindatum", lambda ep: ep.begindatum is not None),
        ("einddatum", lambda ep: ep.einddatum is not None),
        ("label", lambda ep: ep.label is not None and ep.label.code is not None),
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

        # vanwege het gebruik van mypy wordt in de code hieronder de check op attributen nogmaals uitgevoerd, maar deze kunnen op dit moment niet meer None zijn
        if (
            energieprestatie.soort and energieprestatie.soort.code
        ) and energieprestatie.soort.code not in {
            Energieprestatiesoort.energie_index.code,
            Energieprestatiesoort.primair_energieverbruik_woningbouw.code,
            Energieprestatiesoort.voorlopig_energielabel.code,
        }:
            logger.debug(
                f"Eenheid ({eenheid.id}): ongeldige energieprestatie.soort.code '{energieprestatie.soort.code}'."
            )
            continue

        if (energieprestatie.begindatum and energieprestatie.einddatum) and not (
            energieprestatie.begindatum <= peildatum < energieprestatie.einddatum
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): peildatum {peildatum} valt buiten geldigheidsperiode van de energieprestatie."
            )
            continue

        if (energieprestatie.status and energieprestatie.status.code) and (
            energieprestatie.status.code != Energieprestatiestatus.definitief.code
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): energieprestatie status is niet definitief."
            )
            continue

        if energieprestatie.registratiedatum and (
            energieprestatie.registratiedatum
            <= (
                datetime.combine(peildatum, time.min).astimezone()
                - relativedelta(years=10)
            )
        ):
            logger.debug(
                f"Eenheid ({eenheid.id}): registratie van de energieprestatie is ouder dan 10 jaar op peildatum {peildatum}."
            )
            continue

        logger.info(f"Eenheid ({eenheid.id}): geldige energieprestatie gevonden.")
        logger.debug(
            f"Energieprestatie: id={energieprestatie.id} soort={energieprestatie.soort.naam if energieprestatie.soort else None}"
            f" status={energieprestatie.status.naam if energieprestatie.status else None}"
            f" label={energieprestatie.label.naam if energieprestatie.label else None}"
            f" waarde={energieprestatie.waarde} begindatum={energieprestatie.begindatum}"
            f" einddatum={energieprestatie.einddatum} registratiedatum={energieprestatie.registratiedatum.date() if energieprestatie.registratiedatum else None}"
        )
        return energieprestatie

    logger.info(f"Eenheid ({eenheid.id}): geen geldige energieprestatie gevonden.")
    return None


def rond_af(
    getal: float | None | Decimal, decimalen: int, rounding: str | None = ROUND_HALF_UP
) -> Decimal:
    """
    Rondt een getal af op een bepaald aantal decimalen volgens de standaard afrondingsregels (arithmetic).

    Args:
        getal (float | None | Decimal): Het getal om af te ronden.
        decimalen (int): Het aantal decimalen na de komma om op af te ronden.
        rounding (str | None, optional): Het type afrondingsregel. Default is ROUND_HALF_UP.

    Returns:
        Decimal: Het afgeronde getal.

    Raises:
        ValueError: als de input None is.
    """
    if getal is None:
        raise ValueError("Kan None niet afronden")
    return Decimal(str(getal)).quantize(Decimal(f"1e{-decimalen}"), rounding=rounding)


def rond_af_op_kwart(getal: float | None | Decimal) -> Decimal:
    """
    Rond een getal af op een kwart.

    Args:
        getal (float | None | Decimal): Het getal om af te ronden.

    Returns:
        Decimal: Het afgeronde getal.

    Raises:
        ValueError: als de input None is.
    """
    if getal is None:
        raise ValueError("Kan None niet afronden")
    kwart = Decimal("0.25")
    return (Decimal(getal) / kwart).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    ) * kwart


CULTUREELERFGOED_SPARQL_ENDPOINT = (
    "https://api.linkeddata.cultureelerfgoed.nl/datasets/rce/cho/sparql"
)
KADASTER_SPARQL_ENDPOINT = "https://api.labs.kadaster.nl/datasets/kadaster/kkg/sparql"

RIJKSMONUMENTEN_QUERY_TEMPLATE = """
PREFIX ceo:<https://linkeddata.cultureelerfgoed.nl/def/ceo#>
PREFIX bag:<http://bag.basisregistraties.overheid.nl/bag/id/>

ASK
WHERE {{
    ?monument a ceo:Rijksmonument .
    ?monument ceo:heeftBasisregistratieRelatie ?basisregistratieRelatie .
    ?basisregistratieRelatie ceo:heeftBAGRelatie ?bagRelatie .
    ?bagRelatie ceo:verblijfsobjectIdentificatie "{verblijfsobject_identificatie}" .
}}
"""

BESCHERMD_GEZICHT_QUERY_TEMPLATE = """
PREFIX sor: <https://data.kkg.kadaster.nl/sor/model/def/>
PREFIX nen3610: <https://data.kkg.kadaster.nl/nen3610/model/def/>
PREFIX ceo:<https://linkeddata.cultureelerfgoed.nl/def/ceo#>
PREFIX rn:<https://data.cultureelerfgoed.nl/term/id/rn/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof:<http://www.opengis.net/def/function/geosparql/>
ASK
WHERE {{
  SERVICE <{endpoint_kadaster}> {{
      ?verblijfsobject sor:geregistreerdMet/nen3610:identificatie "{verblijfsobject_identificatie}".
      ?verblijfsobject geo:hasGeometry/geo:asWKT ?verblijfsobjectWkt.
  }}
  ?gezicht a ceo:Gezicht ;
      ceo:heeftGeometrie ?gezichtGeometrie ;
      ceo:heeftGezichtsstatus rn:fd968529-bf70-4afa-8564-7c6c2fcfcc54;
      ceo:heeftNaam/ceo:naam ?naam.
  ?gezichtGeometrie geo:asWKT ?gezichtWkt.
  filter(geof:sfWithin(?verblijfsobjectWkt, ?gezichtWkt))
}}
"""


def is_rijksmonument(verblijfsobject_identificatie: str) -> bool | None:
    """
    Controleert of een verblijfsobject een rijksmonument is.

    Args:
        verblijfsobject_identificatie (str): De identificatie van het verblijfsobject.

    Returns:
        bool | None: True als het verblijfsobject een rijksmonument is, False anders, of None bij een fout.

    Raises:
        ValueError: Als verblijfsobject_identificatie niet numeriek is.
    """
    if not verblijfsobject_identificatie.isnumeric():
        raise ValueError("verblijfsobject_identificatie moet numeriek zijn")

    rijksmonumenten_query = RIJKSMONUMENTEN_QUERY_TEMPLATE.format(
        verblijfsobject_identificatie=verblijfsobject_identificatie,
    )

    sparql = SPARQLWrapper2(CULTUREELERFGOED_SPARQL_ENDPOINT)
    sparql.setQuery(rijksmonumenten_query)
    result = sparql.queryAndConvert()

    if isinstance(result, dict):
        rijksmonument = result.get("boolean")
        if isinstance(rijksmonument, bool):
            return rijksmonument

    logger.warning(
        f"Onverwacht resultaat bij ophalen rijksmonument voor verblijfsobject identificatie {verblijfsobject_identificatie}"
    )
    return None


def is_beschermd_gezicht(verblijfsobject_identificatie: str) -> bool | None:
    """
    Controleert of een verblijfsobject tot een beschermd gezicht behoort.

    Args:
        verblijfsobject_identificatie (str): De identificatie van het verblijfsobject.

    Returns:
        bool | None: True als het verblijfsobject tot een beschermd gezicht behoort, False anders, of None bij een fout.

    Raises:
        ValueError: Als verblijfsobject_identificatie niet numeriek is.
    """
    if not verblijfsobject_identificatie.isnumeric():
        raise ValueError("verblijfsobject_identificatie moet numeriek zijn")

    beschermd_gezicht_query = BESCHERMD_GEZICHT_QUERY_TEMPLATE.format(
        endpoint_kadaster=KADASTER_SPARQL_ENDPOINT,
        verblijfsobject_identificatie=verblijfsobject_identificatie,
    )

    sparql = SPARQLWrapper2(CULTUREELERFGOED_SPARQL_ENDPOINT)
    sparql.setQuery(beschermd_gezicht_query)
    result = sparql.queryAndConvert()

    if isinstance(result, dict):
        rijksmonument = result.get("boolean")
        if isinstance(rijksmonument, bool):
            return rijksmonument

    logger.warning(
        f"Onverwacht resultaat bij ophalen beschermd gezicht voor verblijfsobject identificatie {verblijfsobject_identificatie}"
    )
    return None


def update_eenheid_monumenten(eenheid: EenhedenEenheid) -> EenhedenEenheid:
    eenheid.monumenten = eenheid.monumenten or []

    if (
        eenheid.adresseerbaar_object_basisregistratie is not None
        and eenheid.adresseerbaar_object_basisregistratie.bag_identificatie is not None
    ):
        rijksmonument = is_rijksmonument(
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
        )

        if rijksmonument is not None:
            logger.info(
                f"Eenheid ({eenheid.id}) is {'een' if rijksmonument else 'geen'} rijksmonument volgens de api van cultureelerfgoed."
            )
            if rijksmonument:
                eenheid.monumenten.append(Eenheidmonument.rijksmonument.value)

        beschermd_gezicht = is_beschermd_gezicht(
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
        )

        if beschermd_gezicht is not None:
            logger.info(
                f"Eenheid ({eenheid.id}) {'behoort' if beschermd_gezicht else 'behoort niet'} tot een beschermd stads- of dorpsgezicht volgens de api van cultureelerfgoed."
            )
            if beschermd_gezicht:
                eenheid.monumenten.append(Eenheidmonument.beschermd_stadsgezicht.value)

    return eenheid


def normaliseer_ruimte_namen(eenheid: EenhedenEenheid) -> None:
    for ruimte in eenheid.ruimten or []:
        if not ruimte.naam:
            ruimte.naam = getattr(ruimte.detail_soort, "naam", ruimte.id)

    naam_counter = Counter(
        ruimte.naam for ruimte in eenheid.ruimten or [] if ruimte.naam
    )
    nummering_counter: Counter[str] = Counter()

    for ruimte in eenheid.ruimten or []:
        if ruimte.naam is not None and naam_counter[ruimte.naam] > 1:
            nummering_counter[ruimte.naam] += 1
            ruimte.naam = f"{ruimte.naam} {nummering_counter[ruimte.naam]}"


def _classificeer_ruimte_dec(
    func: Callable[[EenhedenRuimte], Ruimtesoort | None],
) -> Callable[[EenhedenRuimte], Ruimtesoort | None]:
    """Logt de classificatie van de ruimte volgens het Woningwaarderingstelsel"""

    @wraps(func)
    def wrapper(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
        ruimtesoort = func(ruimte)
        if ruimtesoort is not None:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is geclassificeerd als een {ruimtesoort.naam if ruimtesoort.naam else ruimtesoort.code}"
            )
        else:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) kan niet worden geclassificeerd als een ruimtesoort."
            )
        return ruimtesoort

    return wrapper


# @_classificeer_ruimte_dec
def classificeer_ruimte(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
    """
    Classificeert de ruimte volgens het Woningwaarderingstelsel

    Args:
        ruimte (EenhedenRuimte): De ruimte die geclassificeerd moet worden.

    Returns:
        Ruimtesoort | None: De classificatie van de ruimte volgens het Woningwaarderingstelsel.
            Geeft `None` terug als de ruimte niet kan worden gewaardeerd.
    """

    if ruimte.oppervlakte is None:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte"
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.soort is None:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen soort"
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.detail_soort is None:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort"
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.soort.code == Ruimtesoort.verkeersruimte.code:
        return Ruimtesoort.verkeersruimte

    if ruimte.detail_soort.code in [
        # onderstaande parkeergelegenden worden binnenkort vervangen: https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/110#issuecomment-2190641829
        Ruimtedetailsoort.gemeenschappelijke_parkeerruimte_niet_specifieke_plek.code,
        Ruimtedetailsoort.gemeenschappelijke_parkeerruimte_specifieke_plek.code,
        Ruimtedetailsoort.open_parkeergarage_niet_specifieke_plek.code,
        Ruimtedetailsoort.open_parkeergarage_specifieke_plek.code,
        Ruimtedetailsoort.parkeergarage_niet_specifieke_plek.code,
        Ruimtedetailsoort.parkeergarage_specifieke_plek.code,
    ]:
        warning_msg = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft als ruimtedetailsoort {ruimte.detail_soort.naam} ({ruimte.detail_soort.code}) en kan daardoor niet geclassificeerd worden. Gebruik voor parkeerplaatsen: {Ruimtedetailsoort.carport.naam} ({Ruimtedetailsoort.carport.code}), {Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.naam} ({Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code}) of {Ruimtedetailsoort.parkeervak_auto_binnen.naam} ({Ruimtedetailsoort.parkeervak_auto_binnen.code})"
        warnings.warn(warning_msg, UserWarning)
        return None

    if (
        ruimte.detail_soort.code
        in [  # deze ruimten zijn sowieso buitenruimten
            Ruimtedetailsoort.atrium_en_of_patio.code,
            Ruimtedetailsoort.gemeenschappelijk_dakterras.code,
            Ruimtedetailsoort.achtertuin.code,
            Ruimtedetailsoort.balkon.code,
            Ruimtedetailsoort.zijtuin.code,
            Ruimtedetailsoort.voortuin.code,
            Ruimtedetailsoort.dakterras.code,
            Ruimtedetailsoort.gemeenschappelijke_tuin.code,
            Ruimtedetailsoort.terras.code,
            Ruimtedetailsoort.tuin.code,
            Ruimtedetailsoort.tuin_rondom.code,
            Ruimtedetailsoort.loggia.code,
        ]
        or (  # privé parkeerplaatsen buiten zijn privé buitenruimten
            ruimte.detail_soort.code
            in [
                Ruimtedetailsoort.carport.code,
                Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code,
            ]
            and not gedeeld_met_eenheden(ruimte)
        )
        or (
            ruimte.detail_soort.code == Ruimtedetailsoort.parkeerplaats.code
            and ruimte.soort.code == Ruimtesoort.buitenruimte.code
            and not gedeeld_met_eenheden(ruimte)
        )
    ):
        return Ruimtesoort.buitenruimte

    # Keuken, badkamer en doucheruimte worden altijd gewaardeerd als vertrek
    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.keuken.code,
        Ruimtedetailsoort.badkamer.code,
        Ruimtedetailsoort.doucheruimte.code,
    ]:
        return Ruimtesoort.vertrek

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.woonkamer.code,
        Ruimtedetailsoort.woon_en_of_slaapkamer.code,
        Ruimtedetailsoort.woonkamer_en_of_keuken.code,
        Ruimtedetailsoort.slaapkamer.code,
        Ruimtedetailsoort.badkamer_met_toilet.code,
        Ruimtedetailsoort.overig_vertrek.code,
        Ruimtedetailsoort.bijkeuken.code,
        Ruimtedetailsoort.berging.code,
        Ruimtedetailsoort.wasruimte.code,
        Ruimtedetailsoort.kelder.code,
        # Ruimtedetailsoort.schuur.code,
    ] or (
        Ruimtedetailsoort.schuur.naam == ruimte.detail_soort.naam
    ):  # Schacht en schuur hebben dezelfde code
        if (
            ruimte.detail_soort.code == Ruimtedetailsoort.berging.code
            and Ruimtesoort.overige_ruimten
        ):
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1
            if (
                Decimal(str(ruimte.oppervlakte)) / Decimal(str(aantal_eenheden))
            ) >= Decimal("2"):
                return Ruimtesoort.overige_ruimten
            else:
                return None

        if ruimte.soort.code == Ruimtesoort.vertrek.code:
            if ruimte.oppervlakte >= 4:
                return Ruimtesoort.vertrek
            if ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimten

        if ruimte.soort.code == Ruimtesoort.overige_ruimten.code:
            if ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimten

    if ruimte.detail_soort.code == Ruimtedetailsoort.toiletruimte.code:
        # mag alleen als overige ruimte gewaardeerd worden
        if ruimte.oppervlakte >= 2:
            return Ruimtesoort.overige_ruimten

    if (
        ruimte.detail_soort.code
        in [
            Ruimtedetailsoort.garage_inpandig.code,
            Ruimtedetailsoort.garage_uitpandig.code,
            Ruimtedetailsoort.garagebox.code,
            Ruimtedetailsoort.parkeervak_auto_binnen.code,
        ]
        and not gedeeld_met_eenheden(
            ruimte
        )  # garages moeten privé zijn om gecategoriseerd te worden als overige ruimte
        or (
            ruimte.detail_soort.code == Ruimtedetailsoort.parkeerplaats.code
            and ruimte.soort.code == Ruimtesoort.overige_ruimten.code
            and not gedeeld_met_eenheden(ruimte)
        )
    ):
        if ruimte.oppervlakte >= 2.0:
            return Ruimtesoort.overige_ruimten

    if ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
        if ruimte.soort.code == Ruimtesoort.vertrek.code:
            if (
                heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)
                and ruimte.oppervlakte >= 4
            ):
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een vaste trap: Ruimte wordt gewaardeerd als {Ruimtesoort.vertrek.naam}."
                )
                return Ruimtesoort.vertrek

            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen vaste trap gevonden: Ruimte wordt niet gewaardeerd als {ruimte.soort.naam}."
                )

        if ruimte.soort.code == Ruimtesoort.overige_ruimten.code:
            if (
                heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)
                or heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.vlizotrap
                )
            ) and ruimte.oppervlakte >= 2:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een trap: Ruimte wordt gewaardeerd als {Ruimtesoort.overige_ruimten.naam}."
                )
                return Ruimtesoort.overige_ruimten

            else:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen trap: Ruimte wordt niet gewaardeerd als {Ruimtesoort.overige_ruimten.naam}."
                )

    return None


def voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte: EenhedenRuimte) -> str:
    """
    Deze functie voegt de oppervlakte van kasten toe aan een ruimte en retourneert de naam van de ruimte inclusief het aantal kasten.

    Args:
        ruimte (EenhedenRuimte): De ruimte waar kasten aan toegevoegd moeten worden.

    Returns:
        str: De naam van de ruimte inclusief het aantal toegevoegde kasten.
    """

    criterium_naam = ruimte.naam or "Naamloze ruimte"

    if ruimte.detail_soort is None or ruimte.detail_soort.code is None:
        message = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort"
        warnings.warn(message, UserWarning)
        return criterium_naam

    if ruimte.oppervlakte is None:
        message = f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte"
        warnings.warn(message, UserWarning)
        return criterium_naam

    # Van vaste kasten wordt de netto oppervlakte bepaald
    # en bij de oppervlakte van de betreffende ruimte opgeteld.
    # Een kast waarvan de deur uitkomt op een
    # verkeersruimte, wordt niet gewaardeerd
    if ruimte.detail_soort.code not in [
        Ruimtedetailsoort.hal.code,
        Ruimtedetailsoort.overloop.code,
        Ruimtedetailsoort.entree.code,
        Ruimtedetailsoort.gang.code,
    ]:
        ruimte_kasten = [
            verbonden_ruimte
            for verbonden_ruimte in ruimte.verbonden_ruimten or []
            if verbonden_ruimte.detail_soort is not None
            and verbonden_ruimte.detail_soort.code == Ruimtedetailsoort.kast.code
        ]

        aantal_ruimte_kasten = len(ruimte_kasten)

        if aantal_ruimte_kasten > 0:
            ruimte.oppervlakte += sum(
                [
                    ruimte_kast.oppervlakte
                    for ruimte_kast in ruimte_kasten
                    if ruimte_kast.oppervlakte is not None
                ]
            )

            if ruimte.inhoud is not None:
                ruimte.inhoud += sum(
                    [
                        ruimte_kast.inhoud
                        for ruimte_kast in ruimte_kasten
                        if ruimte_kast.inhoud is not None
                    ]
                )

            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): de netto oppervlakte van {aantal_ruimte_kasten} verbonden {'kast' if aantal_ruimte_kasten == 1 else 'kasten'} is erbij opgeteld."
            )

            criterium_naam = f"{ruimte.naam} (+{aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'})"
    return criterium_naam


def deel_punten_door_aantal_onzelfstandige_woonruimten(
    ruimte: EenhedenRuimte,
    woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering]
    | Iterator[WoningwaarderingResultatenWoningwaardering],
    update_criterium_naam: bool = True,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    """
    Deelt punten door het aantal onzelfstandige woonruimten.

    Deze functie verdeelt de punten voor woningwaarderingen over het aantal onzelfstandige woonruimten dat een ruimte deelt.

    Args:
        ruimte (EenhedenRuimte): De ruimte waarvoor de punten verdeeld moeten worden.
        woningwaarderingen (list[WoningwaarderingResultatenWoningwaardering] | Iterator[WoningwaarderingResultatenWoningwaardering]):
            Een lijst of iterator van woningwaarderingen waarvan de punten verdeeld moeten worden.
        update_criterium_naam (bool, optional): Een boolean die aangeeft of de naam van het criterium moet worden aangepast. Default is True.

    Yields:
        WoningwaarderingResultatenWoningwaardering: Woningwaarderingen met verdeelde punten.
    """
    gedeelde_ruimte = gedeeld_met_onzelfstandige_woonruimten(ruimte)
    for woningwaardering in woningwaarderingen:
        if (
            gedeelde_ruimte
            and woningwaardering.criterium
            and woningwaardering.punten
            and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten  # nodig voor mypy
        ):
            woningwaardering.criterium.naam = f"{woningwaardering.criterium.naam}"
            if update_criterium_naam:
                woningwaardering.criterium.naam += f" (gedeeld met {ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten})"

            woningwaardering.punten = float(
                utils.rond_af(
                    utils.rond_af(woningwaardering.punten, decimalen=2)
                    / ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                    decimalen=2,
                )
            )
        yield woningwaardering


def gedeeld_met_eenheden(ruimte: EenhedenRuimte) -> bool:
    """Geeft True terug als de ruimte gedeeld is met andere eenheden"""
    return (
        ruimte.gedeeld_met_aantal_eenheden is not None
        and ruimte.gedeeld_met_aantal_eenheden >= 2
    )


def gedeeld_met_onzelfstandige_woonruimten(
    ruimte: EenhedenRuimte,
) -> bool:
    """Geeft True terug als de ruimte gedeeld is met andere onzelfstandige woonruimten"""
    return (
        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
        and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 2
    )


WOONPLAATS_QUERY_TEMPLATE = """
prefix sor: <https://data.kkg.kadaster.nl/sor/model/def/>
prefix nen3610: <https://data.kkg.kadaster.nl/nen3610/model/def/>
prefix skos: <http://www.w3.org/2004/02/skos/core#>

select ?identificatie ?naam
where {{
  values ?postcode {{ "{postcode}" }}
  values ?huisnummer {{ {huisnummer} }}
  values ?huisnummertoevoeging {{ "{huisnummertoevoeging}" }}
  values ?huisletter {{ "{huisletter}" }}

  ?adres a sor:Nummeraanduiding;
         sor:postcode ?postcode;
         sor:ligtAan/sor:ligtIn ?woonplaats;
         sor:huisnummer ?adresHuisnummer.

  ?woonplaats sor:geregistreerdMet/nen3610:identificatie ?identificatie;
              skos:prefLabel ?naam.

  optional
  {{
    ?adres sor:huisnummer ?adresHuisnummer.
  }}
  optional
  {{
    ?adres sor:huisnummertoevoeging ?adresHuisnummertoevoeging.
  }}
  optional
  {{
    ?adres sor:huisletter ?adresHuisletter.
  }}
  FILTER(
    (!BOUND(?adresHuisnummer) && ?huisnummer = "") ||
    (?adresHuisnummer = ?huisnummer)
  )
  FILTER(
    (!BOUND(?adresHuisletter) && ?huisletter = "") ||
    (lcase(?adresHuisletter) = lcase(?huisletter))
  )
  FILTER(
    (!BOUND(?adresHuisnummertoevoeging) && ?huisnummertoevoeging = "") ||
    (lcase(?adresHuisnummertoevoeging) = lcase(?huisnummertoevoeging))
  )
}}
"""


def get_woonplaats(adres: EenhedenEenheidadres) -> EenhedenWoonplaats | None:
    """
    Haalt de woonplaats op voor een gegeven adres.

    Args:
        adres (EenhedenEenheidadres): Adres met woonplaats met woonplaatscode of postcode, huisnummer en optioneel huisletter en huisnummertoevoeging.

    Returns:
        EenhedenWoonplaats | None: de woonplaats,
                               of None als de gegevens niet gevonden kunnen worden.
    """
    if (
        adres.woonplaats is not None
        and adres.woonplaats.code is not None
        and adres.woonplaats.naam is not None
    ):
        return adres.woonplaats

    if not adres.postcode or not adres.huisnummer:
        return None

    logger.info(
        f"Adres {adres} bevat geen woonplaats met woonplaatscode. Woonplaats wordt opgehaald via het Kadaster"
    )

    if not adres.huisnummer.isnumeric():
        warnings.warn(
            f'Huisnummer "{adres.huisnummer}" moet numeriek zijn. Maak gebruik van de attributen huisnummer, huisnummerToevoeging en huisletter voor de nummeraanduiding.'
        )

    query = WOONPLAATS_QUERY_TEMPLATE.format(
        postcode=adres.postcode.replace(" ", ""),
        huisnummer=int(adres.huisnummer),
        huisletter=adres.huisletter or "",
        huisnummertoevoeging=adres.huisnummer_toevoeging or "",
    )
    request_data = {"query": query, "format": "json"}

    try:
        response = requests.post(KADASTER_SPARQL_ENDPOINT, data=request_data, timeout=5)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and len(result) == 1:
            adres.woonplaats = EenhedenWoonplaats(
                code=result[0]["identificatie"], naam=result[0]["naam"]
            )
            return adres.woonplaats
        return None
    except requests.RequestException as e:
        warnings.warn(f"Fout bij het ophalen van woonplaatsdata: {e}, UserWarning")
        return None


def get_corop_voor_woonplaats(woonplaats_code: str) -> dict[str, str] | None:
    """
    Haalt het COROP-gebied op voor een gegeven woonplaatscode.

    Args:
        woonplaats_code (str): De code van de woonplaats.

    Returns:
        dict[str, str] | None: Een dictionary met 'code' en 'naam' van het COROP-gebied,
                               of None als de gegevens niet gevonden kunnen worden.
    """
    data = pd.read_csv(
        files("woningwaardering").joinpath("data/corop/corop.generated.csv"),
        dtype={"Woonplaatscode": str, "Gemeentecode": str, "COROP-gebiedcode": str},
    )

    woonplaats_dataframe = data[data["Woonplaatscode"] == woonplaats_code.lstrip("WP")]

    if woonplaats_dataframe.empty:
        return None

    resultaat = woonplaats_dataframe.iloc[0]

    return {"code": resultaat["COROP-gebiedcode"], "naam": resultaat["COROP-gebied"]}
