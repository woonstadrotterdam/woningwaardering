import warnings
from datetime import date

import pytest

from woningwaardering.stelsels.onzelfstandige_woonruimten.punten_voor_de_woz_waarde.punten_voor_de_woz_waarde import (
    PuntenVoorDeWozWaarde,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenWozEenheid,
)

PEILDATUM = date(2026, 7, 1)


def _eenheid_zonder_woz() -> EenhedenEenheid:
    return EenhedenEenheid(id="test")


def _eenheid_onbruikbare_woz() -> EenhedenEenheid:
    return EenhedenEenheid(
        id="test",
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1),
                vastgestelde_waarde=300_000,
            )
        ],
    )


def test_geen_woz_error_geeft_instructie_met_woz_eenheden():
    """Zonder WOZ-waarde en simplefilter("error") stopt de run.

    De UserWarning vraagt om wozEenheden met de waardepeildatums T-1/T-2.
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=PEILDATUM)
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        with pytest.raises(UserWarning, match="wozEenheden"):
            stelselgroep.waardeer(_eenheid_zonder_woz())


def test_geen_woz_default_geeft_minimum_van_10_punten():
    """Zonder WOZ-waarde en simplefilter("default") gaat de berekening door.

    De UserWarning noemt de 10 fallback-punten, niet de instructie om
    wozEenheden mee te geven.
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=PEILDATUM)
    with warnings.catch_warnings():
        warnings.simplefilter("default", UserWarning)
        with pytest.warns(
            UserWarning, match="het minimum van 10 punten wordt toegepast"
        ) as recorded:
            stelselgroep.waardeer(_eenheid_zonder_woz())
    assert not any("wozEenheden" in str(w.message) for w in recorded)


def test_onbruikbare_woz_error_geeft_waardepeildatums_en_woz_eenheden():
    """Een WOZ-beschikking buiten T-1/T-2 telt niet; error vraagt om invoer.

    De UserWarning noemt wozEenheden en de waardepeildatums
    01-01-2025 of 01-01-2024.
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=PEILDATUM)
    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        with pytest.raises(UserWarning, match="wozEenheden") as excinfo:
            stelselgroep.waardeer(_eenheid_onbruikbare_woz())
    assert "01-01-2025 of 01-01-2024" in str(excinfo.value)


def test_onbruikbare_woz_default_geeft_minimum_van_10_punten():
    """Een WOZ-beschikking buiten T-1/T-2; default past 10 punten toe.

    De UserWarning noemt die 10 punten, niet de instructie om
    wozEenheden mee te geven.
    """
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=PEILDATUM)
    with warnings.catch_warnings():
        warnings.simplefilter("default", UserWarning)
        with pytest.warns(
            UserWarning, match="het minimum van 10 punten wordt toegepast"
        ) as recorded:
            stelselgroep.waardeer(_eenheid_onbruikbare_woz())
    assert not any("wozEenheden" in str(w.message) for w in recorded)
