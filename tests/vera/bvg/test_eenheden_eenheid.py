import warnings

import pytest

from woningwaardering.vera.bvg.generated import EenhedenEenheid

_DECIMAAL_PUNT_MSG = "Gebruik een punt als decimaalscheidingsteken"


def test_EenhedenEenheid_komma_in_genest_veld_benoemt_de_komma() -> None:
    with pytest.warns(UserWarning, match=_DECIMAAL_PUNT_MSG):
        eenheid = EenhedenEenheid.model_validate(
            {
                "ruimten": [
                    {"naam": "Woonkamer", "oppervlakte": "12,5"},
                    {"naam": "Keuken", "oppervlakte": 8.0},
                ]
            }
        )
    assert eenheid.ruimten is not None
    # De foutieve waarde valt weg; de rest van de input blijft overeind.
    assert eenheid.ruimten[0].oppervlakte is None
    assert eenheid.ruimten[1].oppervlakte == 8.0


def test_EenhedenEenheid_komma_in_eigen_veld_benoemt_de_komma() -> None:
    with pytest.warns(UserWarning, match=_DECIMAAL_PUNT_MSG):
        eenheid = EenhedenEenheid.model_validate({"totaalInhoud": "250,5"})
    assert eenheid.totaal_inhoud is None


def test_EenhedenEenheid_validatiefout_op_eigen_veld_laat_de_waarde_wegvallen() -> None:
    with pytest.warns(UserWarning, match="Validatiefout in attribuut 'bouwjaar'"):
        eenheid = EenhedenEenheid.model_validate({"bouwjaar": "onbekend"})
    assert eenheid.bouwjaar is None


def test_EenhedenEenheid_validatiefout_zonder_komma_noemt_de_komma_niet() -> None:
    with pytest.warns(UserWarning) as records:
        EenhedenEenheid.model_validate({"ruimten": [{"oppervlakte": "12.5 m2"}]})
    assert not any(_DECIMAAL_PUNT_MSG in str(record.message) for record in records)


def test_EenhedenEenheid_punt_als_decimaalscheidingsteken_wordt_geaccepteerd() -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        eenheid = EenhedenEenheid.model_validate(
            {"totaalInhoud": "250.5", "ruimten": [{"oppervlakte": "12.5"}]}
        )
    assert eenheid.totaal_inhoud == 250.5
    assert eenheid.ruimten is not None
    assert eenheid.ruimten[0].oppervlakte == 12.5
