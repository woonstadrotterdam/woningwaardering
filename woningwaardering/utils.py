import importlib

from woningwaardering.stelsels.stelselgroep import Stelselgroep


def import_stelselgroep_versie(module_path: str, class_naam: str) -> Stelselgroep:
    try:
        module = importlib.import_module(module_path)
        class_: Stelselgroep = getattr(module, class_naam)
        return class_
    except ModuleNotFoundError:
        print(f"Module {module_path} not found.")
        raise
    except AttributeError:
        print(f"Class {class_naam} not found in module {module_path}.")
        raise
