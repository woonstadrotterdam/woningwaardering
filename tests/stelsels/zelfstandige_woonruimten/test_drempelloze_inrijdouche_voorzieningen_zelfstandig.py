"""Tests voor extra voorzieningen bij een drempelloze inrijdouche.

Bron: docs/implementatietoelichtingen/zelfstandige-woonruimten.md
- §2.6.1: douche = elke door verhuurder aangebrachte installatie voor stortbad (4 punten)
- §2.6.2: extra voorzieningen vereisen wastafel én douche of bad in bad-/doucheruimte
"""

import warnings
from datetime import date
from decimal import Decimal

from woningwaardering.stelsels.zelfstandige_woonruimten.sanitair import Sanitair
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


def _maak_badkamer_met_drempelloze_inrijdouche() -> EenhedenEenheid:
    return EenhedenEenheid(
        id="drempelloze_inrijdouche",
        ruimten=[
            EenhedenRuimte(
                id="badkamer",
                naam="Badkamer",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.badkamer,
                installaties=[
                    Installatiesoort.drempelloze_inrijdouche,
                    Installatiesoort.wastafel,
                    Installatiesoort.handdoekenradiator,
                    Installatiesoort.thermostatische_mengkraan,
                ],
            )
        ],
    )


def _criterium_ids(groep) -> list[str]:
    return [
        waardering.criterium.id
        for waardering in groep.woningwaarderingen or []
        if waardering.criterium and waardering.criterium.id
    ]


def _waardeer(eenheid: EenhedenEenheid):
    return Sanitair(peildatum=date(2026, 1, 1)).waardeer(eenheid)


def test_drempelloze_inrijdouche_telt_als_douche_voor_extra_voorzieningen():
    """§2.6.2 [ZEL]: drempelloze inrijdouche + wastafel → extra voorzieningen gewaardeerd."""
    eenheid = _maak_badkamer_met_drempelloze_inrijdouche()
    groep = _waardeer(eenheid)
    ids = _criterium_ids(groep)

    assert any(
        "drempelloze_inrijdouche" in criterium_id for criterium_id in ids
    ), "Drempelloze inrijdouche moet als basisdouche gewaardeerd worden (§2.6.1)"
    assert any(
        "extra_voorzieningen" in criterium_id for criterium_id in ids
    ), "Extra voorzieningen ontbreken terwijl douche (DRD) en wastafel aanwezig zijn (§2.6.2)"
    assert any("handdoekenradiator" in criterium_id for criterium_id in ids)
    assert any("thermostatische_mengkraan" in criterium_id for criterium_id in ids)


def test_totaal_punten_met_extra_voorzieningen():
    """Scenario: 1 + 4 + 0,75 + 0,50 = 6,25 punt."""
    eenheid = _maak_badkamer_met_drempelloze_inrijdouche()
    groep = _waardeer(eenheid)

    assert groep.punten is not None
    assert Decimal(str(groep.punten)) == Decimal("6.25")


def test_geen_warning_geen_bad_of_douche():
    """§2.6.2: drempelloze inrijdouche is douche; geen 'geen bad of douche'-warning."""
    eenheid = _maak_badkamer_met_drempelloze_inrijdouche()

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", UserWarning)
        _waardeer(eenheid)

    bad_of_douche_warnings = [
        w
        for w in caught
        if issubclass(w.category, UserWarning)
        and "geen bad of douche aanwezig" in str(w.message)
    ]
    assert (
        not bad_of_douche_warnings
    ), "Onterechte warning: drempelloze inrijdouche telt als douche (§2.6.1, §2.6.2)"
