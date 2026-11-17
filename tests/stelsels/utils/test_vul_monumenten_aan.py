import sys
import warnings
from types import SimpleNamespace
from typing import Any

import pytest

from woningwaardering.stelsels.utils import vul_monumenten_aan
from woningwaardering.vera.bvg.generated import (
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import Eenheidmonument

BAG_ID = "0599010000000001"
NIET_GESPECIFICEERD = "'monumenten' is niet gespecificeerd"
ONBEPAALD = "kon de monumentstatus niet bepalen"
AANROEP_MISLUKT = "de aanroep mislukte"


class _ClientMetAntwoord:
    """Geeft voor elke aanroep hetzelfde antwoord, zoals `process_from_list(..., to_vera=True)`."""

    antwoord: dict[str, Any] = {}
    aanroepen = 0

    async def __aenter__(self) -> "_ClientMetAntwoord":
        return self

    async def __aexit__(self, *args: object) -> None:
        return None

    async def process_from_list(self, ids: list[str], to_vera: bool) -> dict[str, Any]:
        type(self).aanroepen += 1
        return self.antwoord


class _ClientMetWaarschuwing(_ClientMetAntwoord):
    """Geeft `None` en een `UserWarning`, zoals de package monumenten bij een bron zonder antwoord."""

    async def process_from_list(self, ids: list[str], to_vera: bool) -> dict[str, Any]:
        warnings.warn("De RCE gaf geen antwoord", UserWarning)
        return await super().process_from_list(ids, to_vera)


class _ClientZonderAntwoord(_ClientMetAntwoord):
    """Geeft een `RuntimeError`, zoals de `BronFoutError` van de package monumenten."""

    async def __aenter__(self) -> "_ClientZonderAntwoord":
        type(self).aanroepen += 1
        raise RuntimeError("bron gaf geen antwoord")


def _vervang_monumenten(
    monkeypatch: pytest.MonkeyPatch,
    client: type[_ClientMetAntwoord],
    antwoord: dict[str, Any] | None = None,
) -> None:
    """Vervangt de package monumenten, zodat de test de API niet aanroept."""
    monkeypatch.setattr(client, "antwoord", antwoord or {})
    monkeypatch.setattr(client, "aanroepen", 0)
    monkeypatch.setitem(
        sys.modules, "monumenten", SimpleNamespace(MonumentenClient=client)
    )


def _eenheid(**velden: Any) -> EenhedenEenheid:
    return EenhedenEenheid(
        id="eenheid",
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie=BAG_ID
        ),
        **velden,
    )


# Monumenten opgegeven


def test_opgegeven_monumenten_roepen_de_package_monumenten_niet_aan(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Staat `monumenten` in de input, dan roept woningwaardering de package monumenten niet aan."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        eenheid = vul_monumenten_aan(_eenheid(monumenten=[]))

    assert eenheid.monumenten == []
    assert _ClientMetAntwoord.aanroepen == 0


# Package monumenten niet geïnstalleerd


def test_zonder_package_monumenten_volgt_een_waarschuwing() -> None:
    """Zonder `monumenten` in de input en zonder de package monumenten volgt een waarschuwing."""
    # De fixture `monumenten_niet_geinstalleerd` blokkeert de import.
    with pytest.warns(UserWarning, match=NIET_GESPECIFICEERD) as waarschuwingen:
        vul_monumenten_aan(_eenheid())

    assert len(waarschuwingen) == 1
    assert "woningwaardering[monumenten]" in str(waarschuwingen[0].message)


def test_eenheid_zonder_package_monumenten_heeft_geen_monumenten() -> None:
    """Een eenheid zonder `monumenten` in de input en zonder de package monumenten heeft geen monumenten."""
    with pytest.warns(UserWarning, match=NIET_GESPECIFICEERD):
        eenheid = vul_monumenten_aan(_eenheid())

    assert eenheid.monumenten == []


# Geen BAG-identificatie


def test_zonder_bag_identificatie_volgt_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Zonder BAG-identificatie kan de package de monumentstatus niet ophalen en volgt een waarschuwing."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord)

    with pytest.warns(UserWarning, match="geen BAG-identificatie") as waarschuwingen:
        eenheid = vul_monumenten_aan(EenhedenEenheid(id="eenheid"))

    assert len(waarschuwingen) == 1
    assert eenheid.monumenten == []
    assert _ClientMetAntwoord.aanroepen == 0


def test_lege_bag_identificatie_geeft_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een lege BAG-identificatie telt als geen BAG-identificatie."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord)
    eenheid = EenhedenEenheid(
        id="eenheid",
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie=""
        ),
    )

    with pytest.warns(UserWarning, match="geen BAG-identificatie"):
        vul_monumenten_aan(eenheid)

    assert _ClientMetAntwoord.aanroepen == 0


# Monumentstatus opgehaald


def test_opgehaalde_monumentstatus_geeft_geen_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een monumentstatus die de package monumenten ophaalt, geeft geen waarschuwing."""
    _vervang_monumenten(
        monkeypatch,
        _ClientMetAntwoord,
        {BAG_ID: [{"code": "GEM", "naam": "Gemeentelijk monument"}]},
    )

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        eenheid = vul_monumenten_aan(_eenheid())

    assert [monument.code for monument in eenheid.monumenten or []] == [
        Eenheidmonument.gemeentelijk_monument.code
    ]


def test_de_package_monumenten_wordt_een_keer_per_eenheid_aangeroepen(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Woningwaardering roept de package monumenten één keer per eenheid aan, ook als de status onbepaald blijft."""
    # Prijsopslag monumenten en Energieprestatie vragen allebei de monumentstatus.
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})
    eenheid = _eenheid()

    with pytest.warns(UserWarning, match=ONBEPAALD):
        vul_monumenten_aan(eenheid)
        vul_monumenten_aan(eenheid)

    assert _ClientMetAntwoord.aanroepen == 1


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

    eenheid = vul_monumenten_aan(_eenheid())

    assert [monument.code for monument in eenheid.monumenten or []] == ["GEM"]


# Monumentstatus onbepaald


def test_onbepaalde_monumentstatus_geeft_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een monumentstatus die de package monumenten niet kan bepalen, geeft een waarschuwing."""
    # De package monumenten geeft `None` als een bron geen antwoord gaf.
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with pytest.warns(UserWarning, match=ONBEPAALD) as waarschuwingen:
        vul_monumenten_aan(_eenheid())

    assert len(waarschuwingen) == 1


def test_eenheid_met_onbepaalde_monumentstatus_heeft_geen_monumenten(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een eenheid met een monumentstatus die de package monumenten niet kan bepalen, heeft geen monumenten."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with pytest.warns(UserWarning, match=ONBEPAALD):
        eenheid = vul_monumenten_aan(_eenheid())

    assert eenheid.monumenten == []


def test_onbepaalde_monumentstatus_is_een_error_met_de_standaardfilter(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Met de standaardfilter is een onbepaalde monumentstatus een error met alleen de eigen melding."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {BAG_ID: None})

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        with pytest.raises(UserWarning) as error:
            vul_monumenten_aan(_eenheid())

    assert ONBEPAALD in str(error.value)
    assert AANROEP_MISLUKT not in str(error.value)


def test_warning_van_de_package_monumenten_staat_in_de_eigen_warning(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Met de standaardfilter volgt één error, met de tekst van de warning van de package monumenten."""
    _vervang_monumenten(monkeypatch, _ClientMetWaarschuwing, {BAG_ID: None})

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        with pytest.raises(UserWarning) as error:
            vul_monumenten_aan(_eenheid())

    assert ONBEPAALD in str(error.value)
    assert "De RCE gaf geen antwoord" in str(error.value)
    assert AANROEP_MISLUKT not in str(error.value)


def test_ontbrekende_bag_identificatie_in_het_antwoord_geeft_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Geeft de package monumenten geen antwoord voor de BAG-identificatie, dan volgt een waarschuwing."""
    _vervang_monumenten(monkeypatch, _ClientMetAntwoord, {})

    with pytest.warns(UserWarning, match=ONBEPAALD) as waarschuwingen:
        eenheid = vul_monumenten_aan(_eenheid())

    assert len(waarschuwingen) == 1
    assert eenheid.monumenten == []


# Aanroep mislukt


def test_mislukte_aanroep_geeft_een_waarschuwing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een mislukte aanroep van de package monumenten geeft een waarschuwing met de reden."""
    _vervang_monumenten(monkeypatch, _ClientZonderAntwoord)

    with pytest.warns(UserWarning, match=AANROEP_MISLUKT) as waarschuwingen:
        vul_monumenten_aan(_eenheid())

    assert len(waarschuwingen) == 1
    assert ONBEPAALD in str(waarschuwingen[0].message)


def test_eenheid_na_mislukte_aanroep_heeft_geen_monumenten(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Een eenheid waarvoor de aanroep van de package monumenten mislukt, heeft geen monumenten."""
    _vervang_monumenten(monkeypatch, _ClientZonderAntwoord)

    with pytest.warns(UserWarning, match=AANROEP_MISLUKT):
        eenheid = vul_monumenten_aan(_eenheid())

    assert eenheid.monumenten == []
