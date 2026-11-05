"""Print het rapport van één model op stelselniveau, zoals de testreferentie het vastlegt.

Gebruik: `task toon-rapport -- tests/stelsels/modellen/zelfstandige_woonruimten/<naam>.json`

Dit is hetzelfde rapport als in de testreferentie, zonder de pytest-fixtures. Gebruik
het om input te zoeken: je ziet direct welke rubriek welke punten krijgt.
"""

import sys
import warnings
from pathlib import Path

from loguru import logger

from woningwaardering.rapport import naar_rapport
from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
    OnzelfstandigeWoonruimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Gebruik: toon_rapport.py <model.json>", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    # Inline: tests is pas importeerbaar na de sys.path-aanpassing hierboven.
    from tests.peildatum import REFERENTIE_PEILDATUM  # noqa: PLC0415

    pad = Path(argv[1])
    eenheid = EenhedenEenheid.model_validate_json(pad.read_text())

    stelsels = {
        Woningwaarderingstelsel.zelfstandige_woonruimten.code: ZelfstandigeWoonruimten,
        Woningwaarderingstelsel.onzelfstandige_woonruimten.code: OnzelfstandigeWoonruimten,
    }
    if eenheid.woningwaarderingstelsel is None:
        print(f"{pad.name}: geen woningwaarderingstelsel in het model", file=sys.stderr)
        return 2
    stelsel_klasse = stelsels[eenheid.woningwaarderingstelsel.code]

    warnings.filterwarnings("ignore", category=UserWarning)
    logger.remove()
    resultaat = stelsel_klasse(peildatum=REFERENTIE_PEILDATUM).waardeer(eenheid)
    print(naar_rapport(resultaat, eenheid_id=eenheid.id).get_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
