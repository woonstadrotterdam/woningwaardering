from woningwaardering.stelsels.bouwers import WaarderingsgroepBouwer
from woningwaardering.stelsels.criterium import GedeeldMetSoort
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

STELSEL = Woningwaarderingstelsel.onzelfstandige_woonruimten
STELSELGROEP = Woningwaarderingstelselgroep.sanitair


def _bouwer() -> WaarderingsgroepBouwer:
    return WaarderingsgroepBouwer(STELSEL, STELSELGROEP)


def test_maak_onderliggende_onder_groep_gebruikt_stelselgroep_als_prefix() -> None:
    waardering = _bouwer().maak_onderliggende(
        id="Space_1",
        naam="Badkamer",
    )
    assert waardering.criterium_id == f"{STELSELGROEP.name}__Space_1"
    assert waardering.bovenliggende_id is None
    assert waardering.punten is None


def test_maak_onderliggende_nest_onder_waardering() -> None:
    ruimte = _bouwer().maak_onderliggende(id="Space_1", naam="Badkamer")
    detail = ruimte.maak_onderliggende(
        id="bad",
        naam="Bad",
        punten=6,
        aantal=1,
        meeteenheid=Meeteenheid.stuks,
    )
    assert detail.criterium_id == f"{STELSELGROEP.name}__Space_1__bad"
    assert detail.bovenliggende_id == f"{STELSELGROEP.name}__Space_1"
    assert detail.punten == 6
    assert detail.aantal == 1


def test_gedeeld_met_prive_bij_aantal_een() -> None:
    criterium = _bouwer().gedeeld_met(
        aantal=1, soort=GedeeldMetSoort.onzelfstandige_woonruimten
    )
    assert criterium.criterium_id == f"{STELSELGROEP.name}__prive"
    assert criterium.naam == "Privé"


def test_gedeeld_met_gebruikt_enkele_underscores() -> None:
    criterium = _bouwer().gedeeld_met(
        aantal=3, soort=GedeeldMetSoort.onzelfstandige_woonruimten
    )
    assert (
        criterium.criterium_id
        == f"{STELSELGROEP.name}__gedeeld_met_3_onzelfstandige_woonruimten"
    )
    assert criterium.naam == "Gedeeld met 3 onzelfstandige woonruimten"


def test_bouwer_dedupliceert_gedeelde_criteria_en_sommeert_punten() -> None:
    waarderingsgroep_bouwer = _bouwer()

    eerste = waarderingsgroep_bouwer.gedeeld_met(
        aantal=3, soort=GedeeldMetSoort.onzelfstandige_woonruimten
    )
    tweede = waarderingsgroep_bouwer.gedeeld_met(
        aantal=3, soort=GedeeldMetSoort.onzelfstandige_woonruimten
    )
    assert eerste is tweede

    eerste.maak_onderliggende(id="Space_1", naam="Badkamer")
    eerste.maak_onderliggende(id="Space_1__bad", naam="Bad", punten=2)

    groep = waarderingsgroep_bouwer.bouw()

    assert groep.punten == 2.0
    assert groep.woningwaarderingen is not None
    assert (
        sum(
            1
            for w in groep.woningwaarderingen
            if w.criterium
            and w.criterium.id
            == f"{STELSELGROEP.name}__gedeeld_met_3_onzelfstandige_woonruimten"
        )
        == 1
    )
