import warnings

import pytest
from loguru import logger

from woningwaardering.stelsels.utils import _userwarning_setting, waarschuw_gebruiker

ERROR_TEKST = "geef eenheid.wozEenheden mee"
LOG_TEKST = "het minimum wordt toegepast"


def test_userwarning_setting_error():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        assert _userwarning_setting() == "error"


def test_userwarning_setting_default():
    with warnings.catch_warnings():
        warnings.simplefilter("default", UserWarning)
        assert _userwarning_setting() == "default"


def test_userwarning_setting_ignore():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        assert _userwarning_setting() == "ignore"


def test_waarschuw_gebruiker_error_gebruikt_error_tekst():
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        with pytest.raises(UserWarning, match=ERROR_TEKST):
            waarschuw_gebruiker(error=ERROR_TEKST, log=LOG_TEKST)


def test_waarschuw_gebruiker_default_gebruikt_log_tekst():
    with warnings.catch_warnings():
        warnings.simplefilter("default", UserWarning)
        with pytest.warns(UserWarning, match=LOG_TEKST) as recorded:
            waarschuw_gebruiker(error=ERROR_TEKST, log=LOG_TEKST)
        assert not any(ERROR_TEKST in str(w.message) for w in recorded)


def test_waarschuw_gebruiker_ignore_is_stil():
    berichten: list[str] = []
    logger.enable("woningwaardering")
    handler_id = logger.add(lambda message: berichten.append(str(message)))
    try:
        with warnings.catch_warnings(record=True) as recorded:
            warnings.simplefilter("ignore", UserWarning)
            waarschuw_gebruiker(error=ERROR_TEKST, log=LOG_TEKST)
        assert not any(issubclass(w.category, UserWarning) for w in recorded)
        assert not any(LOG_TEKST in bericht for bericht in berichten)
        assert not any(ERROR_TEKST in bericht for bericht in berichten)
    finally:
        logger.remove(handler_id)
