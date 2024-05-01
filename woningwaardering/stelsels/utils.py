from decimal import Decimal
import importlib
import os
import pandas as pd
from datetime import date
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


def geef_dataframe_waarde(df: pd.DataFrame, target_col: str, col_mapping: dict) -> str:
    # TODO: kijk naar 'import operator' en 'get_truth' zodat je eventueel een mapping met operator kan meegeven
    for column, value in col_mapping.items():
        df = df[df[column] == value]

    # Check op het resultaat
    if df.empty:
        raise ValueError(
            f"Geen resultaat rij gevonden voor target_col {target_col} en col_mapping."
        )
    elif len(df) > 1:
        raise ValueError(
            f"Meerdere rijen gevonden voor gegeven {col_mapping}. Hoeveelheid gevonden rijen {len(df)}."
        )

    return df[target_col].values[0]


def lees_csv_als_dataframe(file_path) -> pd.DataFrame:
    return pd.read_csv(file_path, sep=",", encoding="utf-8")


# def lees_csv_als_records(file_path) -> list[dict]:
#     """
#     Read a CSV file and return its contents as a list of dictionaries.

#     Parameters:
#     - file_path (str): The path to the CSV file to read.

#     Returns:
#     - list[dict]: A list of dictionaries where each dictionary represents a row in the CSV file,
#       and the keys are the column headers.
#     """
#     data_list = []

#     with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             data_list.append(row)

#     return data_list
