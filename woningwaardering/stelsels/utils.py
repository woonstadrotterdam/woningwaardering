import importlib
import keyword
import os
from datetime import date, datetime, time
from decimal import ROUND_HALF_UP, Decimal
from typing import Type, TypeVar

import pandas as pd
from dateutil.relativedelta import relativedelta
from loguru import logger
from prettytable import PrettyTable

from rdflib import Graph, Literal, Namespace
from rdflib.plugins.sparql import prepareQuery

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

T = TypeVar("T")


def import_class(module_path: str, class_naam: str, class_type: Type[T]) -> Type[T]:
    """
    Importeert een klasse uit een module.

    Parameters:
        module_path (str): Het pad naar de module waarin de klasse zich bevindt.
        class_naam (str): De naam van de klasse die geïmporteerd moet worden.
        class_type (Type[T]): Het verwachtte type van de klasse.

    Returns:
        Type[T]: De geïmporteerde klasse.

    Raises:
        ValueError: Als de class naam of module path ongeldige tekens of een keyword bevat.
        ModuleNotFoundError: Als de module niet gevonden kan worden.
        AttributeError: Als de klasse van het opgegeven type niet gevonden kan worden in de module.
    """
    if not class_naam.isidentifier() or keyword.iskeyword(class_naam):
        raise ValueError("Class naam bevat ongeldige tekens of is een keyword.")

    module_path_parts = module_path.split(".")

    if any(
        not part.isidentifier() or keyword.iskeyword(part) for part in module_path_parts
    ):
        raise ValueError("Module path bevat ongeldige tekens of keywords.")

    logger.debug(f"Importeer class '{class_naam}' uit '{module_path}'")

    try:
        module = importlib.import_module(module_path)
        class_: Type[T] = getattr(module, class_naam)
        if not issubclass(class_, class_type):
            raise TypeError(
                f"class '{class_.__qualname__}' in '{class_.__module__}' is niet van het type '{class_type.__qualname__}'"
            )

    except ModuleNotFoundError as e:
        logger.error(f"Module {module_path} niet gevonden.", e)
        raise

    except AttributeError as e:
        logger.error(f"Class {class_naam} niet gevonden in: {module_path}.", e)
        raise

    return class_


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


def vind_yaml_bestanden(directory: str) -> list[str]:
    """
    Zoekt alle YAML-bestanden in de opgegeven directory en de subdirectories.

    Parameters:
        directory (str): De hoofddirectory waarin naar YAML-bestanden wordt gezocht.

    Returns:
        list[str]: Een lijst met paden naar de gevonden YAML-bestanden.
    """
    logger.info(f"Zoek naar YAML-bestanden in: {directory}")

    yaml_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(directory)
        for file in files
        if file.endswith((".yaml", ".yml"))
    ]

    if not yaml_files:
        logger.error(f"Geen YAML-bestanden gevonden in: {directory}")
    return yaml_files


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


def filter_dataframe_op_datum(df: pd.DataFrame, datum_filter: date) -> pd.DataFrame:
    """
    Filtert een DataFrame op basis van een datum.
    Het dataframe moet de kolommen 'Begindatum' en 'Einddatum' bevatten.

    Args:
        df (pd.DataFrame): Het DataFrame dat gefilterd moet worden.
        datum_filter (date): De datum waarop gefilterd moet worden.

    Returns:
        pd.DataFrame: Het gefilterde DataFrame.

    Raises:
        ValueError: Als de DataFrame geen 'Begindatum' en 'Einddatum' kolommen bevat.
        ValueError: Als de filtering op datum geen records oplevert.
    """
    datum_filter_datetime = datetime.combine(datum_filter, datetime.min.time())

    if "Begindatum" not in df.columns or "Einddatum" not in df.columns:
        error_message = (
            "De DataFrame moet de kolommen 'Begindatum' en 'Einddatum' bevatten."
        )
        logger.error(error_message)
        raise ValueError(error_message)

    df["Begindatum"] = pd.to_datetime(df["Begindatum"])
    df["Einddatum"] = pd.to_datetime(df["Einddatum"])

    mask = (df["Begindatum"] <= datum_filter_datetime) & (
        (df["Einddatum"] >= datum_filter_datetime) | df["Einddatum"].isnull()
    )
    resultaat_df = df[mask]

    if resultaat_df.empty:
        raise ValueError("Datum filter levert geen records op")

    return df[mask]


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


CEO = Namespace("https://linkeddata.cultureelerfgoed.nl/def/ceo#")
BAG = Namespace("http://bag.basisregistraties.overheid.nl/bag/id/")

endpoint = "https://api.linkeddata.cultureelerfgoed.nl/datasets/rce/cho/sparql"


query_template = """
ASK
WHERE {{
    SERVICE <{endpoint}> {{
        ?monument a ceo:Rijksmonument .
        ?monument ceo:heeftBasisregistratieRelatie ?basisregistratieRelatie .
        ?basisregistratieRelatie ceo:heeftBAGRelatie ?bagRelatie .
        ?bagRelatie ceo:verblijfsobjectIdentificatie ?verblijfsobjectIdentificatie .
    }}
}}
"""

rijksmonumenten_query = prepareQuery(
    query_template.format(endpoint=endpoint), initNs={"ceo": CEO, "bag": BAG}
)


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
        for energieprestatie in eenheid.energieprestaties:
            if (
                energieprestatie.registratiedatum
                and energieprestatie.soort
                and energieprestatie.soort.code
                and energieprestatie.status
                and energieprestatie.status.code
                and energieprestatie.begindatum
                and energieprestatie.einddatum
                and energieprestatie.label
                and (
                    energieprestatie.soort.code
                    in [
                        Energieprestatiesoort.energie_index.code,
                        Energieprestatiesoort.primair_energieverbruik_woningbouw.code,
                        Energieprestatiesoort.voorlopig_energielabel.code,  # Een voorlopig energie_label kan ook als status definitief zijn, want dit is het soort energie label gemeten met de meetmethode van voor 2015.
                    ]
                )
                and (
                    energieprestatie.begindatum < peildatum < energieprestatie.einddatum
                    and energieprestatie.status.code
                    == Energieprestatiestatus.definitief.code
                )
                and (
                    # Check of de registratie niet ouder is dan 10 jaar
                    energieprestatie.registratiedatum
                    > (
                        datetime.combine(peildatum, time.min).astimezone()
                        - relativedelta(years=10)
                    )
                )
            ):
                logger.info("Energieprestatie met geldig label gevonden")
                logger.debug(f"Energieprestatie: {energieprestatie}")
                return energieprestatie

    logger.info("Geen geldige energieprestatie met label gevonden")
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


def is_rijksmonument(verblijfsobjectIdentificatie: str) -> bool:
    if not str.isnumeric(verblijfsobjectIdentificatie):
        raise ValueError("VerblijfsobjectIdentificatie moet numeriek zijn")

    graph = Graph()

    result = graph.query(
        rijksmonumenten_query,
        initBindings={
            "verblijfsobjectIdentificatie": Literal(verblijfsobjectIdentificatie),
        },
    )

    if result is None or result.askAnswer is None:
        return False
    else:
        return result.askAnswer


def update_eenheid_monumenten(eenheid: EenhedenEenheid) -> EenhedenEenheid:
    eenheid.monumenten = eenheid.monumenten or []

    if (
        eenheid.adresseerbaar_object_basisregistratie is not None
        and eenheid.adresseerbaar_object_basisregistratie.bag_identificatie is not None
    ):
        is_rijksmonument(
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
        )
        rijksmonument = is_rijksmonument(
            eenheid.adresseerbaar_object_basisregistratie.bag_identificatie
        )
        logger.info(
            f"Eenheid {eenheid.id} met verblijfsobjectIdentificatie {eenheid.adresseerbaar_object_basisregistratie.bag_identificatie} is {'een' if rijksmonument else 'geen'} rijksmonument volgens de api van cultureelerfgoed."
        )
        if rijksmonument:
            eenheid.monumenten.append(Eenheidmonument.rijksmonument.value)

    return eenheid
