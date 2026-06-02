import argparse
import string
import sys
import warnings
from datetime import date
from importlib import import_module
from pathlib import Path

from loguru import logger
from pydantic import ValidationError

from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genereer expected outputs onder tests/data/**/output/."
    )
    parser.add_argument(
        "--force",
        "--overwrite",
        dest="force",
        action="store_true",
        help="Overschrijf bestaande output-bestanden.",
    )
    parser.add_argument(
        "--stelsel",
        choices=["zelfstandige_woonruimten", "onzelfstandige_woonruimten"],
        action="append",
        help="Beperk tot één of meer stelsels (kan meerdere keren).",
    )
    parser.add_argument(
        "--scope",
        choices=["stelselgroepen", "units", "all"],
        default="all",
        help="Welke outputs te genereren.",
    )
    parser.add_argument(
        "--only-stelselgroep",
        action="append",
        help="Alleen deze stelselgroep(en) onder tests/data/<stelsel>/stelselgroepen/ (kan meerdere keren).",
    )
    return parser.parse_args()


def _is_stelselgroep_input(input_file_path: Path) -> bool:
    return input_file_path.parent.parent.parent.name == "stelselgroepen"


def _output_path_for_input(input_file_path: Path) -> Path:
    return Path(str(input_file_path).replace("/input/", "/output/"))


def _skip_by_scope(scope: str, input_file_path: Path) -> bool:
    if scope == "all":
        return False
    if scope == "stelselgroepen":
        return not _is_stelselgroep_input(input_file_path)
    # scope == "units"
    return _is_stelselgroep_input(input_file_path)


def _skip_by_only_stelselgroep(
    only_stelselgroepen: list[str] | None, input_file_path: Path
) -> bool:
    if not only_stelselgroepen:
        return False
    if not _is_stelselgroep_input(input_file_path):
        return True
    return input_file_path.parent.parent.name not in set(only_stelselgroepen)


def main() -> int:
    args = _parse_args()

    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

    # Set logger level to INFO
    logger.remove()
    stdout_id = logger.add(sys.stdout, level="INFO")

    peildatum = date(2026, 1, 1)
    data_dir = Path("tests/data")
    stelsels = args.stelsel or [
        "zelfstandige_woonruimten",
        "onzelfstandige_woonruimten",
    ]

    updated = 0
    skipped_existing = 0
    skipped_filtered = 0
    errors = 0

    for stelsel_naam in stelsels:
        input_file_paths = (data_dir / stelsel_naam).rglob("**/input/*.json")
        for input_file_path in input_file_paths:
            if _skip_by_scope(
                args.scope, input_file_path
            ) or _skip_by_only_stelselgroep(args.only_stelselgroep, input_file_path):
                skipped_filtered += 1
                continue

            output_file_path = _output_path_for_input(input_file_path)
            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            if output_file_path.exists() and not args.force:
                skipped_existing += 1
                continue

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

            with open(output_file_path, "w+") as f:
                logger.info(
                    f"Resultaat voor {input_file_path.name} is opgenomen in {output_file_path}, inclusief logs in {output_file_path.with_suffix('.log')}"
                )
                f.write(
                    woningwaardering_resultaat.model_dump_json(
                        by_alias=True, indent=2, exclude_none=True
                    )
                )
                f.write("\n")

            if not _is_stelselgroep_input(input_file_path):
                txt_path = output_file_path.with_suffix(".txt")
                txt_path.write_text(
                    naar_tabel(woningwaardering_resultaat).get_string() + "\n"
                )

            updated += 1

    logger.info(
        "Samenvatting: "
        f"updated={updated}, "
        f"skipped_existing={skipped_existing}, "
        f"skipped_filtered={skipped_filtered}, "
        f"errors={errors}"
    )

    if args.force and updated == 0 and errors == 0:
        logger.error("Niets bijgewerkt (force=True). Check filters/scope.")
        return 2
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
