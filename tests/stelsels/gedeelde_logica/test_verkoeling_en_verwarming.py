"""Maximering van verkoeling en verwarming is onafhankelijk van invoervolgorde.

Privé en gemeenschappelijk hebben elk hun eigen teller. De helper loopt elke
teller in rangorde (kleinste deler, daarna invoervolgorde) vóór de aanroeper
deelt.
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


def test_verwarmde_verkeersruimten_prive_en_gedeeld_levert_4_5():
    """3 privé + 3 gemeenschappelijk /2: beide tellers blijven onder de cap van
    4 ruimten, dus 3 + 3/2 → 4,5."""
    ruimten = [
        _verkeersruimte("GangGedeeld1", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld2", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld3", aantal_onzelfstandige=2),
        _verkeersruimte("GangPrive1"),
        _verkeersruimte("GangPrive2"),
        _verkeersruimte("GangPrive3"),
    ]
    assert _punten(ruimten) == 4.5


def test_verwarmde_verkeersruimten_punten_onafhankelijk_van_invoervolgorde():
    ruimten = [
        _verkeersruimte("GangPrive1"),
        _verkeersruimte("GangPrive2"),
        _verkeersruimte("GangPrive3"),
        _verkeersruimte("GangGedeeld1", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld2", aantal_onzelfstandige=2),
        _verkeersruimte("GangGedeeld3", aantal_onzelfstandige=2),
    ]
    assert _punten(ruimten) == _punten(list(reversed(ruimten))) == 4.5


def test_verkoelde_vertrekken_punten_onafhankelijk_van_invoervolgorde():
    """3 privé + 3 /2 verwarmd én verkoeld: verwarming 9 + verkoeling 3 = 12.

    Verkoeling maximeert per teller: privé 3 − 1 = 2 en gemeenschappelijk
    (3 − 1)/2 = 1.
    """
    ruimten = [
        _vertrek("SlaapkamerGedeeld1", aantal_onzelfstandige=2),
        _vertrek("SlaapkamerGedeeld2", aantal_onzelfstandige=2),
        _vertrek("SlaapkamerGedeeld3", aantal_onzelfstandige=2),
        _vertrek("SlaapkamerPrive1"),
        _vertrek("SlaapkamerPrive2"),
        _vertrek("SlaapkamerPrive3"),
    ]
    assert _punten(ruimten) == _punten(list(reversed(ruimten))) == 12.0


def test_restant_slot_gaat_naar_kleinste_deler():
    """Binnen de gemeenschappelijke teller vullen de /2-ruimten de 4 slots; de
    aftrek valt op /4, niet op /2."""
    ruimten = [
        _verkeersruimte("GangDeler4", aantal_onzelfstandige=4),
        _verkeersruimte("GangDeler2a", aantal_onzelfstandige=2),
        _verkeersruimte("GangDeler2b", aantal_onzelfstandige=2),
        _verkeersruimte("GangDeler2c", aantal_onzelfstandige=2),
        _verkeersruimte("GangDeler2d", aantal_onzelfstandige=2),
    ]
    assert _punten(ruimten) == 2.0


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
