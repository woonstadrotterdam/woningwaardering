import sys
import warnings
from datetime import date
from pathlib import Path

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)


def _write_text_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text() == content:
        return False

    path.write_text(content)
    return True


def _genereer_docs_outputs(peildatum: date) -> int:
    # Inline: tests is pas importeerbaar nadat main() de repo-root aan sys.path toevoegt.
    from tests.docs._examples import (  # noqa: PLC0415
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
    """Schrijf de verwachte output van de docs-voorbeelden.

    De testreferenties schrijft `pytest --update-testreferenties`; samen vormen ze
    `task genereer-test-output`.
    """
    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    # Inline: tests is pas importeerbaar na de sys.path-aanpassing hierboven.
    from tests.peildatum import REFERENTIE_PEILDATUM  # noqa: PLC0415

    warnings.filterwarnings("ignore", category=UserWarning)

    updated = _genereer_docs_outputs(REFERENTIE_PEILDATUM)
    logger.info(f"Samenvatting: updated={updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
