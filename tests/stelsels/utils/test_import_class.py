import pytest

from woningwaardering.stelsels import Stelsel, Stelselgroep
from woningwaardering.stelsels.utils import import_class


@pytest.mark.parametrize(
    "module_path, class_naam, class_type",
    [
        (
            "woningwaardering.stelsels.zelfstandige_woonruimten",
            "ZelfstandigeWoonruimten",
            Stelsel,
        ),
        (
            "woningwaardering.stelsels.zelfstandige_woonruimten.oppervlakte_van_vertrekken",
            "OppervlakteVanVertrekken",
            Stelselgroep,
        ),
    ],
)
def test_import_class(module_path, class_naam, class_type):
    class_ = import_class(module_path, class_naam, class_type)
    assert class_.__name__ == class_naam
