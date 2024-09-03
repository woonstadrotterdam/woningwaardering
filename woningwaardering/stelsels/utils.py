from datetime import date, datetime, time
from decimal import ROUND_HALF_UP, Decimal
import warnings

import pandas as pd
from dateutil.relativedelta import relativedelta
from loguru import logger
from prettytable import PrettyTable
from SPARQLWrapper import SPARQLWrapper2

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Energieprestatiesoort,
    Energieprestatiestatus,
)


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

    for woningwaardering_groep in (
        woningwaardering_resultaat.groepen or []
        if isinstance(
            woningwaardering_resultaat,
            WoningwaarderingResultatenWoningwaarderingResultaat,
        )
        else [woningwaardering_resultaat]
    ):
        woningwaarderingen = woningwaardering_groep.woningwaarderingen or []
        aantal_waarderingen = len(woningwaarderingen)
        for index, woningwaardering in enumerate(woningwaarderingen):
            if (
                woningwaardering_groep.criterium_groep
                and woningwaardering_groep.criterium_groep.stelselgroep
                and woningwaardering.criterium
            ):
                table.add_row(
                    [
                        woningwaardering_groep.criterium_groep.stelselgroep.naam,
                        woningwaardering.criterium.naam,
                        woningwaardering.aantal or "",
                        woningwaardering.criterium.meeteenheid.naam
                        if woningwaardering.criterium.meeteenheid is not None
                        else "",
                        woningwaardering.punten
                        if woningwaardering.punten is not None
                        else "",
                        f"{woningwaardering.opslagpercentage:.0%}"
                        if woningwaardering.opslagpercentage is not None
                        else "",
                    ],
                    divider=index + 1 == aantal_waarderingen,
                )

        aantallen = [
            Decimal(woningwaardering.aantal)
            for woningwaardering in woningwaarderingen
            if woningwaardering.aantal is not None
        ]

        subtotaal = float(sum(aantallen)) if aantallen else None

        if (
            (subtotaal is not None or aantal_waarderingen > 1)
            and woningwaardering_groep.criterium_groep
            and woningwaardering_groep.criterium_groep.stelselgroep
        ):
            meeteenheid = ", ".join(
                list(
                    {
                        woningwaardering.criterium.meeteenheid.naam or ""
                        for woningwaardering in woningwaarderingen
                        if woningwaardering.criterium is not None
                        and woningwaardering.criterium.meeteenheid is not None
                    }
                )
            )

            table.add_row(
                [
                    woningwaardering_groep.criterium_groep.stelselgroep.naam,
                    "Subtotaal",
                    subtotaal or "",
                    meeteenheid,
                    woningwaardering_groep.punten or "",
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


def dataframe_met_een_rij(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check of de dataframe exact één rij bevat.

    Args:
        df (pd.DataFrame): Het DataFrame dat gecheckt moet worden.

    Returns:
        pd.DataFrame: Het DataFrame als het aan de voorwaarden voldoet.

    Raises:
        ValueError: Als het DataFrame leeg is.
        ValueError: Als het DataFrame meer dan één rij bevat.
    """
    if df.empty:
        raise ValueError("Dataframe is leeg")
    if len(df) > 1:
        raise ValueError("Dataframe heeft meer dan één rij")

    return df


def energieprestatie_met_geldig_label(
    peildatum: date,
    eenheid: EenhedenEenheid,
) -> EenhedenEnergieprestatie | None:
    """
    Returnt de eerste geldige energieprestatie met een energielabel van een eenheid.

    Args:
        peildatum (date): De peildatum waarop de energieprestatie geldig moet zijn.
        eenheid (EenhedenEenheid): De eenheid met mogelijke energieprestaties.

    Returns:
        EenhedenEnergieprestatie | None: De eerste geldige energieprestatie met een energielabel en None Wanneer er geen geldige energieprestatie met label is gevonden.
    """
    if eenheid.energieprestaties is not None:
        for idx, energieprestatie in enumerate(eenheid.energieprestaties):
            missing_attributes = []

            if not energieprestatie.registratiedatum:
                missing_attributes.append("'registratiedatum'")

            if not energieprestatie.soort:
                missing_attributes.append("'soort'")
            elif not energieprestatie.soort or not energieprestatie.soort.code:
                missing_attributes.append("'soort.code'")

            if not energieprestatie.status:
                missing_attributes.append("status")
            elif not energieprestatie.status or not energieprestatie.status.code:
                missing_attributes.append("'status.code'")

            if not energieprestatie.begindatum:
                missing_attributes.append("'begindatum'")
            if not energieprestatie.einddatum:
                missing_attributes.append("'einddatum'")

            if not energieprestatie.label:
                missing_attributes.append("'label'")
            elif not energieprestatie.label.code:
                missing_attributes.append("'label.code'")

            if missing_attributes:
                msg = f"Eenheid {eenheid.id} mist energieprestatie attributen:"
                for attribute in missing_attributes:
                    msg += f" {attribute}"
                    msg += ", " if attribute != missing_attributes[-1] else "."

                # Als de energieprestatie niet alle benodigde attributen heeft, ga dan door naar de volgende energieprestatie indien die er is.
                logger.debug(msg)
                if (idx + 1) == len(eenheid.energieprestaties):
                    logger.info(
                        f"Eenheid {eenheid.id}: De energieprestatie mist attributen om gevalideerd te worden. Geen geldige energieprestatie gevonden."
                    )
                    return None
                else:
                    logger.debug(
                        f"Eenheid {eenheid.id}: Missende atrributen op de energieprestatie gevonden. De volgende energieprestatie wordt gevalideerd."
                    )
                    continue

            log_messages_count = 0

            if (
                energieprestatie.soort
                and energieprestatie.soort.code
                and energieprestatie.soort.code
                not in [
                    Energieprestatiesoort.energie_index.code,
                    Energieprestatiesoort.primair_energieverbruik_woningbouw.code,
                    Energieprestatiesoort.voorlopig_energielabel.code,  # Een voorlopig energie_label kan ook als status definitief zijn, want dit is het soort energie label gemeten met de meetmethode van voor 2015.
                ]
            ):
                logger.debug(
                    f"Eenheid {eenheid.id}: Energieprestatie soort code '{energieprestatie.soort.code}' zit niet in ['{Energieprestatiesoort.energie_index.code}', '{Energieprestatiesoort.primair_energieverbruik_woningbouw.code}'. '{Energieprestatiesoort.voorlopig_energielabel.code}'."
                )
                log_messages_count += 1

            if not (
                energieprestatie.begindatum
                and energieprestatie.einddatum
                and energieprestatie.begindatum
                <= peildatum
                < energieprestatie.einddatum
            ):
                logger.debug(
                    f"Eenheid {eenheid.id}: De peildatum {peildatum} ligt niet tussen de begindatum ({energieprestatie.begindatum}) en einddatum ({energieprestatie.einddatum}) van de energieprestatie."
                )
                log_messages_count += 1

            if not (
                energieprestatie.status
                and energieprestatie.status.code
                == Energieprestatiestatus.definitief.code
            ):
                logger.debug(
                    f"Eenheid {eenheid.id}: Energieprestatie status is niet definitief."
                )
                log_messages_count += 1

            if not (
                # Check of de registratie niet ouder is dan 10 jaar
                energieprestatie.registratiedatum
                and energieprestatie.registratiedatum
                > (
                    datetime.combine(peildatum, time.min).astimezone()
                    - relativedelta(years=10)
                )
            ):
                logger.debug(
                    f"Eenheid {eenheid.id}: Registratie van de energieprestatie is langer dan 10 jaar geleden gedaan op peildatum {peildatum}."
                )
                log_messages_count += 1

            if log_messages_count > 0:
                # Wanneer de energieprestatie niet voldoet aan de condities, ga dan door naar de volgende energieprestatie indien die er is.
                if (idx + 1) == len(eenheid.energieprestaties):
                    logger.info(
                        f"Eenheid {eenheid.id}: De energieprestatie voldoet niet aan de condities van de geldigheid. Geen geldige energieprestatie gevonden"
                    )
                    return None
                else:
                    logger.debug(
                        f"Eenheid {eenheid.id}: De energieprestatie voldoet niet aan de condities van de geldigheid. De volgende energieprestatie wordt gevalideerd."
                    )
                    continue

        logger.info(f"Eenheid {eenheid.id}: Geldige energieprestatie gevonden")
        logger.debug(f"Energieprestatie: {energieprestatie}")
        return energieprestatie

    warnings.warn(f"Eenheid {eenheid.id}: 'Energieprestaties' is None", UserWarning)
    return None


def rond_af(
    getal: float | None | Decimal,
    decimalen: int,
) -> Decimal:
    """
    Rondt een getal af op een bepaald aantal decimalen volgens de standaard afrondingsregels (arithmetic).

    Args:
        getal (float | None | Decimal): Het getal om af te ronden.
        decimalen (int): Het aantal decimalen na de komma om op af te ronden.

    Returns:
        Decimal: Het afgeronde getal.

    Raises:
        ValueError: als de input None is.
    """
    if getal is None:
        raise ValueError("Kan None niet afronden")
    return Decimal(str(getal)).quantize(
        Decimal(f"1e{-decimalen}"), rounding=ROUND_HALF_UP
    )


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


endpoint_cultureelerfgoed = (
    "https://api.linkeddata.cultureelerfgoed.nl/datasets/rce/cho/sparql"
)
endpoint_kadaster = (
    "https://api.labs.kadaster.nl/datasets/dst/kkg/services/default/sparql"
)

rijksmonumenten_query_template = """
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


beschermd_gezicht_query_template = """
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

    rijksmonumenten_query = rijksmonumenten_query_template.format(
        verblijfsobject_identificatie=verblijfsobject_identificatie,
    )

    sparql = SPARQLWrapper2(endpoint_cultureelerfgoed)
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

    beschermd_gezicht_query = beschermd_gezicht_query_template.format(
        endpoint_kadaster=endpoint_kadaster,
        verblijfsobject_identificatie=verblijfsobject_identificatie,
    )

    sparql = SPARQLWrapper2(endpoint_cultureelerfgoed)
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
                f"Eenheid {eenheid.id} is {'een' if rijksmonument else 'geen'} rijksmonument volgens de api van cultureelerfgoed."
            )
            if rijksmonument:
                eenheid.monumenten.append(Eenheidmonument.rijksmonument.value)

        beschermd_gezicht = is_beschermd_gezicht(
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
        )

        if beschermd_gezicht is not None:
            logger.info(
                f"Eenheid {eenheid.id} {'behoort' if beschermd_gezicht else 'behoort niet'} tot een beschermd stads- of dorpsgezicht volgens de api van cultureelerfgoed."
            )
            if beschermd_gezicht:
                eenheid.monumenten.append(Eenheidmonument.beschermd_stadsgezicht.value)

    return eenheid
