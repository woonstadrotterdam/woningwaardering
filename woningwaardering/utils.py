import importlib
import os
from datetime import datetime
from typing import Any

from loguru import logger


def import_class(module_path: str, class_naam: str) -> Any:
    """
    Importeert een klasse uit een module.

    Parameters:
        module_path (str): Het pad naar de module waarin de klasse zich bevindt.
        class_naam (str): De naam van de klasse die geïmporteerd moet worden.

    Returns:
        Any: De geïmporteerde klasse.

    Raises:
        ModuleNotFoundError: Als de module niet gevonden kan worden.
        AttributeError: Als de klasse niet gevonden kan worden in de module.
    """
    logger.debug(f"Importeer class '{class_naam}' uit '{module_path}'")
    try:
        module = importlib.import_module(module_path)
        class_ = getattr(module, class_naam)
        return class_
    except ModuleNotFoundError:
        logger.error(f"Module {module_path} niet gevonden.")
        raise
    except AttributeError:
        logger.error(f"Class {class_naam} niet gevonden in: {module_path}.")
        raise


def is_geldig(begindatum: str, einddatum: str, peildatum: str) -> bool:
    """
    Controleert of de peildatum valt tussen de begindatum en einddatum.

    Parameters:
        begindatum (str): De begindatum in het formaat "dd-mm-jjjj".
        einddatum (str): De einddatum in het formaat "dd-mm-jjjj".
        peildatum (str): De peildatum in het formaat "dd-mm-jjjj".

    Returns:
        bool: True als de peildatum tussen de begindatum en einddatum valt, anders False.
    """
    return (
        datetime.strptime(begindatum, "%d-%m-%Y").date()
        <= datetime.strptime(peildatum, "%d-%m-%Y").date()
        <= datetime.strptime(einddatum, "%d-%m-%Y").date()
    )


def vind_yaml_bestanden(directory: str) -> list[str]:
    """
    Zoekt alle YAML-bestanden in de opgegeven directory en de subdirectories.

    Parameters:
        directory (str): De hoofddirectory waarin naar YAML-bestanden wordt gezocht.

    Returns:
        list: Een lijst met paden naar de gevonden YAML-bestanden.
    """
    logger.debug(f"Zoek naar YAML-bestanden in: {directory}")
    yaml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                yaml_files.append(os.path.join(root, file))
    if len(yaml_files) == 0:
        logger.error(f"Geen YAML-bestanden gevonden in: {directory}")
    return yaml_files
