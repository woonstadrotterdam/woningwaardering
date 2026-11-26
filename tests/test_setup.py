import warnings

import pytest

from woningwaardering._setup import initialize

# `pytest.warns` zet zelf het filter "always". Deze tests vangen de warnings daarom
# op met `warnings.catch_warnings(record=True)`: die verandert de filters niet.


def _waarschuw_vanuit(module: str) -> None:
    warnings.warn_explicit(
        "Dit is een warning",
        UserWarning,
        filename=f"{module}.py",
        lineno=1,
        module=module,
        registry={},
    )


def test_userwarning_van_woningwaardering_is_een_error() -> None:
    """Een `UserWarning` van een module van woningwaardering wordt een error."""
    with warnings.catch_warnings():
        warnings.resetwarnings()
        initialize()
        with pytest.raises(UserWarning):
            _waarschuw_vanuit("woningwaardering.stelsels.utils")


def test_userwarning_van_een_andere_package_is_geen_error() -> None:
    """Een `UserWarning` van een andere package volgt de filters van de applicatie."""
    with warnings.catch_warnings():
        warnings.resetwarnings()
        initialize()
        with warnings.catch_warnings(record=True) as meldingen:
            _waarschuw_vanuit("woningwaardering_extra")
            _waarschuw_vanuit("andere_package")
    assert len(meldingen) == 2
