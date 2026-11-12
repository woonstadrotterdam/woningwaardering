import sys
import warnings
from types import SimpleNamespace
from typing import Any

import pytest

from woningwaardering.stelsels.utils import update_eenheid_monumenten
from woningwaardering.vera.bvg.generated import (
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
)

BAG_ID = "0599010000000001"
ONBEPAALD = "kon de monumentstatus niet bepalen"


class _ClientMetAntwoord:
    """Geeft voor elke aanroep hetzelfde antwoord, zoals `process_from_list(..., to_vera=True)`."""

    antwoord: dict[str, Any] = {}

    async def __aenter__(self) -> "_ClientMetAntwoord":
        return self

    async def __aexit__(self, *args: object) -> None:
        return None

    async def process_from_list(self, ids: list[str], to_vera: bool) -> dict[str, Any]:
        return self.antwoord


class _ClientZonderAntwoord(_ClientMetAntwoord):
    """Geeft een `RuntimeError`, zoals de `BronFoutError` van de package monumenten."""

    async def __aenter__(self) -> "_ClientZonderAntwoord":
        raise RuntimeError("bron gaf geen antwoord")


def _vervang_monumenten(
    monkeypatch: pytest.MonkeyPatch,
    client: type[_ClientMetAntwoord],
    antwoord: dict[str, Any] | None = None,
) -> None:
    """Vervangt de package monumenten, zodat de test de API niet aanroept."""
    client.antwoord = antwoord or {}
    monkeypatch.setitem(
        sys.modules, "monumenten", SimpleNamespace(MonumentenClient=client)
    )


def _eenheid() -> EenhedenEenheid:
    return EenhedenEenheid(
        id="eenheid",
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie=BAG_ID
        ),
    )


def test_onbepaalde_monumentstatus_geeft_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een monumentstatus die de package monumenten niet kan bepalen, geeft een waarschuwing."""
    # De package monumenten geeft `None` als een bron geen antwoord gaf.
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with pytest.warns(UserWarning, match=ONBEPAALD):
        update_eenheid_monumenten(_eenheid())


def test_eenheid_met_onbepaalde_monumentstatus_heeft_geen_monumenten(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een eenheid met een monumentstatus die de package monumenten niet kan bepalen, heeft geen monumenten."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with pytest.warns(UserWarning, match=ONBEPAALD):
        eenheid = update_eenheid_monumenten(_eenheid())

    assert eenheid.monumenten == []


def test_onbepaalde_monumentstatus_is_een_error_met_de_standaardfilter(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Met de standaardfilter is een onbepaalde monumentstatus een error met alleen de eigen melding."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        with pytest.raises(UserWarning) as error:
            update_eenheid_monumenten(_eenheid())

    assert ONBEPAALD in str(error.value)
    assert "konden niet worden opgehaald" not in str(error.value)


def test_mislukte_aanroep_geeft_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een aanroep van de package monumenten die mislukt, geeft een waarschuwing."""
    _vervang_monumenten(monkeypatch, _ClientZonderAntwoord)

    with pytest.warns(UserWarning, match="konden niet worden opgehaald"):
        update_eenheid_monumenten(_eenheid())


def test_eenheid_na_mislukte_aanroep_heeft_geen_monumenten(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een eenheid waarvoor de aanroep van de package monumenten mislukt, heeft geen monumenten."""
    _vervang_monumenten(monkeypatch, _ClientZonderAntwoord)

    with pytest.warns(UserWarning, match="konden niet worden opgehaald"):
        eenheid = update_eenheid_monumenten(_eenheid())

    assert eenheid.monumenten == []


def test_rijksmonument_telt_alleen_met_de_rce_als_bron(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een rijksmonument telt alleen als het in het Rijksmonumentenregister van de RCE staat.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.13.4
    - implementatietoelichting onzelfstandige woonruimten, 2.14.4
    """
    _vervang_monumenten(
        monkeypatch,
        _ClientMetAntwoord,
        {
            BAG_ID: [
                # Alleen het Kadaster noemt dit rijksmonument. De package
                # monumenten geeft `bron` als string, bijvoorbeeld "RCE, Kadaster".
                {"code": "RIJ", "naam": "Rijksmonument", "bron": "Kadaster"},
                {"code": "GEM", "naam": "Gemeentelijk monument"},
            ]
        },
    )

    eenheid = update_eenheid_monumenten(_eenheid())

    assert [monument.code for monument in eenheid.monumenten or []] == ["GEM"]
