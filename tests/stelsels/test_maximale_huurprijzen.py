from decimal import Decimal
from importlib.resources import files
from statistics import median

import pandas as pd
import pytest

from woningwaardering.vera.referentiedata import Woningwaarderingstelsel

# Maximale afwijking van een stap t.o.v. de mediaan van de omliggende stappen.
# De stappen in de huurprijstabellen variëren door afronding van de indexatie
# enkele centen; een tikfout in de euro's of tientallen valt hierbuiten.
MAXIMALE_AFWIJKING_STAP = Decimal("0.50")

# Aantal stappen aan weerszijden waarover de mediaan wordt bepaald. Een venster
# van vijf stappen laat een enkele knik in de tabel toe (zoals bij onzelfstandige
# woonruimten tussen 60 en 61 punten), maar vangt een uitschieter op één punt.
VENSTER = 2


@pytest.fixture(
    params=[
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
    ],
    ids=lambda stelsel: stelsel.name,
)
def maximale_huurprijzen(request: pytest.FixtureRequest) -> pd.DataFrame:
    return pd.read_csv(
        str(
            files("woningwaardering").joinpath(
                f"stelsels/{request.param.name}/maximale_huurprijzen.csv"
            )
        ),
        dtype={"Bedrag": str},
    )


def test_maximale_huurprijzen_punten_aaneengesloten(
    maximale_huurprijzen: pd.DataFrame,
) -> None:
    punten = maximale_huurprijzen["Punten"].tolist()
    assert punten == list(range(punten[0], punten[0] + len(punten)))
    assert punten[-1] == 250


def test_maximale_huurprijzen_stappen(maximale_huurprijzen: pd.DataFrame) -> None:
    punten = maximale_huurprijzen["Punten"].tolist()
    bedragen = [Decimal(bedrag) for bedrag in maximale_huurprijzen["Bedrag"]]
    stappen = [b - a for a, b in zip(bedragen, bedragen[1:])]

    for i, stap in enumerate(stappen):
        assert stap > 0, (
            f"Bedrag bij {punten[i + 1]} punten ({bedragen[i + 1]}) is niet hoger "
            f"dan bij {punten[i]} punten ({bedragen[i]})"
        )
        omliggend = stappen[max(0, i - VENSTER) : i + VENSTER + 1]
        afwijking = abs(stap - median(omliggend))
        assert afwijking <= MAXIMALE_AFWIJKING_STAP, (
            f"Stap van {punten[i]} naar {punten[i + 1]} punten ({stap}) wijkt "
            f"{afwijking} af van de omliggende stappen; mogelijk een tikfout"
        )
