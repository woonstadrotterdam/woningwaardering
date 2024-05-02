from decimal import Decimal
import importlib
import os
import pandas as pd
from datetime import date, datetime
from typing import Type, TypeVar

from loguru import logger
from prettytable import PrettyTable

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
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
        ModuleNotFoundError: Als de module niet gevonden kan worden.
        AttributeError: Als de klasse van het opgegeven type niet gevonden kan worden in de module.
    """
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
    logger.debug(f"Zoek naar YAML-bestanden in: {directory}")

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
    table.field_names = ["Groep", "Naam", "Aantal", "Meeteenheid", "Punten"]
    table.align["Groep"] = "l"
    table.align["Naam"] = "l"
    table.align["Aantal"] = "r"
    table.align["Meeteenheid"] = "l"
    table.align["Punten"] = "r"

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
                        woningwaardering.punten or "",
                    ],
                    divider=index + 1 == aantal_waarderingen,
                )
        if (
            woningwaardering_groep.criterium_groep
            and woningwaardering_groep.criterium_groep.stelselgroep
        ):
            table.add_row(
                [
                    woningwaardering_groep.criterium_groep.stelselgroep.naam,
                    "Subtotaal",
                    float(
                        sum(
                            [
                                Decimal(woningwaardering.aantal)
                                for woningwaardering in woningwaarderingen
                                if woningwaardering.aantal is not None
                            ]
                        )
                    )
                    or "",
                    ", ".join(
                        list(
                            {
                                woningwaardering.criterium.meeteenheid.naam or ""
                                for woningwaardering in woningwaarderingen
                                if woningwaardering.criterium is not None
                                and woningwaardering.criterium.meeteenheid is not None
                            }
                        )
                    ),
                    woningwaardering_groep.punten,
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
            ],
            divider=True,
        )

    return table


def lees_csv_als_dataframe(file_path: str) -> pd.DataFrame:
    """
    Leest a CSV bestand en returnt een pandas DataFrame.

    Parameters:
        file_path (str): het pad naar het csv bestand

    Returns:
        pd.DataFrame: The contents of the CSV file as a DataFrame.
    Raises:
        ValueError: Als de file_path extentie niet CSV is.
    """
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path, sep=",", encoding="utf-8")
    else:
        raise ValueError(f"Bestandstype '{file_path.split('.')[-1]}' niet ondersteund.")


def filter_dataframe_op_peildatum(df: pd.DataFrame, peildatum: date) -> pd.DataFrame:
    """
    Filtert een DataFrame op basis van een peildatum.
    Het dataframe moet de kolommen 'Begindatum' en 'Einddatum' bevatten.

    Args:
        df (pd.DataFrame): Het DataFrame dat gefilterd moet worden.
        peildatum (date): De peildatum waarop gefilterd moet worden.

    Returns:
        pd.DataFrame: Het gefilterde DataFrame.

    Raises:
        ValueError: Als de DataFrame geen 'Begindatum' en 'Einddatum' kolommen bevat.
        ValueError: Als de filtering op peildatum geen records oplevert.
    """
    peildatum_datetime = datetime.combine(peildatum, datetime.min.time())

    if "Begindatum" not in df.columns or "Einddatum" not in df.columns:
        # TODO: loggen of error raisen? of allebei?
        error_message = (
            "The DataFrame must contain 'Begindatum' and 'Einddatum' columns."
        )
        logger.error(error_message)
        raise ValueError(error_message)

    df["Begindatum"] = pd.to_datetime(df["Begindatum"])
    df["Einddatum"] = pd.to_datetime(df["Einddatum"])

    mask = (df["Begindatum"] <= peildatum_datetime) & (
        (df["Einddatum"] >= peildatum_datetime) | df["Einddatum"].isnull()
    )
    resultaat_df = df[mask]

    if resultaat_df.empty:
        error_message = "Peildatum levert geen records op."
        logger.error(error_message)
        raise ValueError(error_message)

    return df[mask]


def dataframe_heeft_een_rij(df: pd.DataFrame) -> None | bool:
    # TODO: nagaan of we error willen raisen of loggen.
    if df.empty:
        logger.error("Geen resultaat gevonden in de bouwjaar_punten lookup tabel.")
        raise ValueError
    if len(df) > 1:
        logger.error("Meerdere resultaten gevonden in de bouwjaar_punten lookup tabel.")
        raise ValueError

    return True
