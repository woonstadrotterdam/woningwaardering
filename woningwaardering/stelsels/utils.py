import importlib
import os
from datetime import date
from typing import Type, TypeVar

from loguru import logger

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
        class_: type = getattr(module, class_naam)
        if not issubclass(class_, class_type):
            raise TypeError(
                f"Class '{class_.__qualname__}' in '{class_.__module__}' is niet van het type '{class_type.__qualname__}'."
            )

    except ModuleNotFoundError as e:
        logger.error(f"Module {module_path} niet gevonden.", e)
        raise

    except AttributeError as e:
        logger.error(f"Class {class_naam} niet gevonden in: {module_path}.", e)
        raise

    return class_


def is_geldig(begindatum: date, einddatum: date, peildatum: date) -> bool:
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
