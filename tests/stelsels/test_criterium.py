from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

STELSEL = Woningwaarderingstelsel.onzelfstandige_woonruimten
STELSELGROEP = Woningwaarderingstelselgroep.sanitair


def _builder() -> WaarderingsgroepBuilder:
    return WaarderingsgroepBuilder(STELSEL, STELSELGROEP)


def test_met_onderliggend_onder_groep_gebruikt_stelselgroep_als_prefix() -> None:
    waardering = _builder().met_onderliggend(
        id="Space_1",
        naam="Badkamer",
    )
    assert waardering.criterium_id == f"{STELSELGROEP.name}__Space_1"
    assert waardering.bovenliggende_id is None
    assert waardering.punten is None


def test_met_onderliggend_nest_onder_waardering() -> None:
    ruimte = _builder().met_onderliggend(id="Space_1", naam="Badkamer")
    detail = ruimte.met_onderliggend(
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
    criterium = _builder().gedeeld_met()
    assert criterium.criterium_id == f"{STELSELGROEP.name}__prive"
    assert criterium.naam == "Privé"


def test_gedeeld_met_gebruikt_enkele_underscores() -> None:
    criterium = _builder().gedeeld_met(aantal_onzelfstandige_woonruimten=3)
    assert (
        criterium.criterium_id
        == f"{STELSELGROEP.name}__gedeeld_met_3_onzelfstandige_woonruimten"
    )
    assert criterium.naam == "Gedeeld met 3 onzelfstandige woonruimten"


def test_builder_dedupliceert_gedeelde_criteria_en_sommeert_punten() -> None:
    waarderingsgroep_builder = _builder()

    eerste = waarderingsgroep_builder.gedeeld_met(aantal_onzelfstandige_woonruimten=3)
    tweede = waarderingsgroep_builder.gedeeld_met(aantal_onzelfstandige_woonruimten=3)
    assert eerste is tweede

    eerste.met_onderliggend(id="Space_1", naam="Badkamer")
    eerste.met_onderliggend(id="Space_1__bad", naam="Bad", punten=2)

    groep = waarderingsgroep_builder.build()

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
