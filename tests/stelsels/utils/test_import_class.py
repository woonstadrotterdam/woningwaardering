import pytest

from woningwaardering.stelsels.utils import import_class


@pytest.mark.parametrize(
    "module_path, class_naam",
    [
        ("woningwaardering.stelsels.zelfstandig.zelfstandig", "Zelfstandig"),
        (
            "woningwaardering.stelsels.zelfstandig.oppervlakte_van_vertrekken",
            "OppervlakteVanVertrekken",
        ),
    ],
)
def test_import_class(module_path, class_naam):
    class_ = import_class(module_path, class_naam)
    assert class_.__name__ == class_naam
