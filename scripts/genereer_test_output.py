import sys
from datetime import date, datetime
from pathlib import Path

from loguru import logger
from pydantic import ValidationError

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)

logger.enable("woningwaardering")

# zet logger level to INFO
logger.remove()
stdout_id = logger.add(sys.stdout, level="INFO")

jaar = datetime.now().year
PEILDATUM = date(year=jaar, month=1, day=1)

INPUT_DIR = Path("tests/data/input")
OUTPUT_DIR = Path("tests/data/output")

input_file_paths = (INPUT_DIR / "zelfstandige_woonruimten").rglob("*.json")


output_file_paths = list((OUTPUT_DIR / "zelfstandige_woonruimten").rglob("*.json"))

for input_file_path in input_file_paths:
    if input_file_path.name not in [x.name for x in output_file_paths]:
        output_file_path = (
            OUTPUT_DIR
            / "zelfstandige_woonruimten/peildatum"
            / datetime.strftime(PEILDATUM, "%Y-%m-%d")
            / input_file_path.name
        )
        unverified_path = output_file_path.with_suffix(
            ".unverified" + output_file_path.suffix
        )

        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        # get input model
        with open(input_file_path, "r+") as f:
            try:
                eenheid_input = EenhedenEenheid.model_validate_json(f.read())
            except ValidationError as e:
                logger.error(f"Error in inputmodel van {input_file_path.name}: {e}")
                continue

            handler_id = logger.add(
                unverified_path.with_suffix(".log"), level="TRACE", mode="w"
            )
            # zet logger naar ERROR voor de stdout om niet alle logging in de terminal te zien van de berekeningen
            logger.remove(stdout_id)
            zelfstandige_woonruimten = ZelfstandigeWoonruimten(peildatum=PEILDATUM)
            woningwaardering_resultaat = zelfstandige_woonruimten.bereken(eenheid_input)
            stdout_id = logger.add(sys.stdout, level="INFO")
            logger.remove(handler_id)
            # write output model
            with open(
                unverified_path,
                "w+",
            ) as f:
                logger.info(
                    f"Resultaat voor {input_file_path.name} is opgenomen in {unverified_path}, inclusief logs in {unverified_path.with_suffix('.log')}"
                )
                f.write(
                    woningwaardering_resultaat.model_dump_json(
                        by_alias=True, indent=2, exclude_none=True
                    )
                )
                f.write("\n")
