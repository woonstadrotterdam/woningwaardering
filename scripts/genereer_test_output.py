import string
import sys
import warnings
from datetime import date
from importlib import import_module
from pathlib import Path

from loguru import logger
from pydantic import ValidationError

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

STELSELS = ("zelfstandige_woonruimten", "onzelfstandige_woonruimten")


def _write_text_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text() == content:
        return False

    path.write_text(content)
    return True


def _is_stelselgroep_input(input_file_path: Path) -> bool:
    return input_file_path.parent.parent.parent.name == "stelselgroepen"


def _output_path_for_input(input_file_path: Path) -> Path:
    return Path(str(input_file_path).replace("/input/", "/output/"))


def _genereer_docs_outputs(peildatum: date) -> int:
    from tests.docs._examples import (
        voorbeeld1_json_input_path,
        voorbeeld2_python_eenheid,
    )

    wws = Woningwaardering(peildatum=peildatum)
    json_output = Path("tests/docs/output_json_json_voorbeeld.json")
    eenheid = EenhedenEenheid.model_validate_json(
        voorbeeld1_json_input_path().read_text()
    )
    updated = 0

    json_content = (
        wws.waardeer(eenheid).model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
        + "\n"
    )
    if _write_text_if_changed(json_output, json_content):
        updated += 1

    python_output = Path("tests/docs/output_json_python_voorbeeld.json")
    python_content = (
        wws.waardeer(voorbeeld2_python_eenheid()).model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
        + "\n"
    )
    if _write_text_if_changed(python_output, python_content):
        updated += 1

    return updated


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    from tests.peildatum import REFERENTIE_PEILDATUM

    peildatum = REFERENTIE_PEILDATUM

    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

    logger.remove()
    stdout_id = logger.add(sys.stdout, level="INFO")

    data_dir = Path("tests/data")

    updated = 0
    errors = 0

    for stelsel_naam in STELSELS:
        input_file_paths = (data_dir / stelsel_naam).rglob("**/input/*.json")
        for input_file_path in input_file_paths:
            output_file_path = _output_path_for_input(input_file_path)
            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(input_file_path, "r+") as f:
                try:
                    eenheid_input = EenhedenEenheid.model_validate_json(f.read())
                except ValidationError as e:
                    logger.error(f"Error in inputmodel van {input_file_path.name}: {e}")
                    errors += 1
                    continue

            handler_id = logger.add(
                output_file_path.with_suffix(".log"), level="TRACE", mode="w"
            )
            logger.remove(stdout_id)

            try:
                if _is_stelselgroep_input(input_file_path):
                    stelselgroep_naam = input_file_path.parent.parent.name
                    stelselgroep_class = import_module(
                        f"woningwaardering.stelsels.{stelsel_naam}." + stelselgroep_naam
                    )
                    stelselgroep: Stelselgroep = getattr(
                        stelselgroep_class,
                        string.capwords(stelselgroep_naam.replace("_", " ")).replace(
                            " ", ""
                        ),
                    )(peildatum=peildatum)
                    woningwaardering_resultaat = (
                        WoningwaarderingResultatenWoningwaarderingResultaat(
                            groepen=[stelselgroep.waardeer(eenheid_input)]
                        )
                    )
                else:
                    stelsel_class = import_module(
                        f"woningwaardering.stelsels.{stelsel_naam}.{stelsel_naam}"
                    )
                    stelsel = getattr(
                        stelsel_class,
                        string.capwords(stelsel_naam.replace("_", " ")).replace(
                            " ", ""
                        ),
                    )(peildatum=peildatum)
                    woningwaardering_resultaat = stelsel.waardeer(eenheid_input)
            except Exception:
                logger.exception(f"Fout bij waarderen van {input_file_path}")
                errors += 1
                continue
            finally:
                stdout_id = logger.add(sys.stdout, level="INFO")
                logger.remove(handler_id)

            logger.info(
                f"Resultaat voor {input_file_path.name} is opgenomen in {output_file_path}, inclusief logs in {output_file_path.with_suffix('.log')}"
            )
            output_content = (
                woningwaardering_resultaat.model_dump_json(
                    by_alias=True, indent=2, exclude_none=True
                )
                + "\n"
            )
            input_updated = _write_text_if_changed(output_file_path, output_content)

            txt_path = output_file_path.with_suffix(".txt")
            txt_content = (
                naar_tabel(
                    woningwaardering_resultaat, eenheid_id=eenheid_input.id
                ).get_string()
                + "\n"
            )
            # Altijd synchroniseren: JSON kan ongewijzigd zijn terwijl .txt verouderd is
            # (bijv. na handmatige restore of oude PrettyTable-fixtures).
            if _write_text_if_changed(txt_path, txt_content):
                input_updated = True

            if input_updated:
                updated += 1

    updated += _genereer_docs_outputs(peildatum)

    logger.info(f"Samenvatting: updated={updated}, errors={errors}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
