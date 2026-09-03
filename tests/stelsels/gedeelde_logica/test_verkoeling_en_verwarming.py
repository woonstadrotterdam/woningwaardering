"""Maximering van verkoeling en verwarming is onafhankelijk van invoervolgorde.

Privé en gemeenschappelijk delen tot #293 één teller. De helper loopt die teller
in rangorde (kleinste deler, daarna invoervolgorde) vóór de aanroeper deelt.
"""

from tests.peildatum import REFERENTIE_PEILDATUM
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    VerkoelingEnVerwarming,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Ruimtedetailsoort,
    Ruimtesoort,
)


def _verkeersruimte(
    ruimte_id: str,
    *,
    aantal_onzelfstandige: int | None = None,
) -> EenhedenRuimte:
    return EenhedenRuimte(
        id=ruimte_id,
        naam=ruimte_id,
        soort=Ruimtesoort.verkeersruimte,
        detail_soort=Ruimtedetailsoort.gang,
        oppervlakte=5,
        verwarmd=True,
        gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_onzelfstandige,
    )


def _vertrek(
    ruimte_id: str,
    *,
    aantal_onzelfstandige: int | None = None,
    verkoeld: bool = True,
) -> EenhedenRuimte:
    return EenhedenRuimte(
        id=ruimte_id,
        naam=ruimte_id,
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        oppervlakte=12,
        verwarmd=True,
        verkoeld=verkoeld,
        gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_onzelfstandige,
    )


def _punten(ruimten: list[EenhedenRuimte]) -> float:
    eenheid = EenhedenEenheid(id="test", ruimten=ruimten)
    groep = VerkoelingEnVerwarming(peildatum=REFERENTIE_PEILDATUM).waardeer(eenheid)
    assert groep.punten is not None
    return float(groep.punten)


def test_verwarmde_verkeersruimten_prive_en_gedeeld_levert_3_5():
    """3 privé + 3 gemeenschappelijk /2: cap 4 ruimten, privé eerst → 3,5."""
    ruimten = [
        _verkeersruimte("GangGedeeld1", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld2", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld3", aantal_onzelfstandige=2),
        _verkeersruimte("GangPrive1"),
        _verkeersruimte("GangPrive2"),
        _verkeersruimte("GangPrive3"),
    ]
    assert _punten(ruimten) == 3.5


def test_verwarmde_verkeersruimten_punten_onafhankelijk_van_invoervolgorde():
    ruimten = [
        _verkeersruimte("GangPrive1"),
        _verkeersruimte("GangPrive2"),
        _verkeersruimte("GangPrive3"),
        _verkeersruimte("GangGedeeld1", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld2", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld3", aantal_onzelfstandige=2),
    ]
    assert _punten(ruimten) == _punten(list(reversed(ruimten))) == 3.5


def test_verkoelde_vertrekken_punten_onafhankelijk_van_invoervolgorde():
    """3 privé + 3 /2 verwarmd én verkoeld: verwarming 9 + verkoeling 2 = 11."""
    ruimten = [
        _vertrek("SlaapkamerGedeeld1", aantal_onzelfstandige=2),
        _vertrek("SlaapkamerGedeeld2", aantal_onzelfstandige=2),
        _vertrek("SlaapkamerGedeeld3", aantal_onzelfstandige=2),
        _vertrek("SlaapkamerPrive1"),
        _vertrek("SlaapkamerPrive2"),
        _vertrek("SlaapkamerPrive3"),
    ]
    assert _punten(ruimten) == _punten(list(reversed(ruimten))) == 11.0


def test_restant_slot_gaat_naar_kleinste_deler():
    """3 privé vullen 3 van 4 slots; het restant gaat naar /2, niet naar /4."""
    ruimten = [
        _verkeersruimte("GangDeler4", aantal_onzelfstandige=4),
        _verkeersruimte("GangDeler2", aantal_onzelfstandige=2),
        _verkeersruimte("GangPrive1"),
        _verkeersruimte("GangPrive2"),
        _verkeersruimte("GangPrive3"),
    ]
    assert _punten(ruimten) == 3.5


def test_homogene_gedeelde_overige_ruimten_blijven_2_0():
    ruimten = [
        EenhedenRuimte(
            id=f"Berging{i}",
            naam=f"Berging{i}",
            soort=Ruimtesoort.overige_ruimten,
            detail_soort=Ruimtedetailsoort.berging,
            oppervlakte=2,
            verwarmd=True,
            gedeeld_met_aantal_onzelfstandige_woonruimten=2,
        )
        for i in range(1, 6)
    ]
    assert _punten(ruimten) == 2.0


def test_sorteer_muteert_invoerlijst_niet():
    ruimten = [
        _verkeersruimte("GangGedeeld1", aantal_onzelfstandige=2),
        _verkeersruimte("GangPrive1"),
    ]
    ids_voor = [ruimte.id for ruimte in ruimten]
    _punten(ruimten)
    assert [ruimte.id for ruimte in ruimten] == ids_voor
