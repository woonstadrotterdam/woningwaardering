from woningwaardering.stelsels.criterium_id import GedeeldMetSoort
from woningwaardering.stelsels.woningwaardering_groep import WoningwaarderingGroep
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _groep() -> WoningwaarderingGroep:
    return WoningwaarderingGroep(
        stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
        stelselgroep=Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )


def _gem_groep() -> WoningwaarderingGroep:
    return WoningwaarderingGroep(
        stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
        stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    )


def test_met_onderliggend_voegt_waarderingsrij_toe():
    groep = _groep()

    groep.met_onderliggend("woz_waarde", aantal=318000)

    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1
    rij = groep.woningwaarderingen[0]
    assert rij.criterium is not None
    assert rij.criterium.id == "punten_voor_de_woz_waarde__woz_waarde"
    assert rij.aantal == 318000


def test_geneste_keten_zet_bovenliggend_criterium():
    groep = _groep()

    onderdeel_I = groep.met_onderliggend("onderdeel_I", punten=20.74)
    onderdeel_I.met_onderliggend("factor_I", aantal=15329)

    assert groep.woningwaarderingen is not None
    ids = [w.criterium.id for w in groep.woningwaarderingen if w.criterium]
    assert ids == [
        "punten_voor_de_woz_waarde__onderdeel_I",
        "punten_voor_de_woz_waarde__onderdeel_I__factor_I",
    ]
    factor = groep.woningwaarderingen[1]
    assert factor.criterium is not None
    assert factor.criterium.bovenliggende_criterium is not None
    assert (
        factor.criterium.bovenliggende_criterium.id
        == "punten_voor_de_woz_waarde__onderdeel_I"
    )


def test_subclass_is_geldige_groep():
    groep = _groep()
    assert groep.criterium_groep is not None
    assert groep.criterium_groep.stelselgroep is not None
    assert groep.woningwaarderingen == []


def test_structureel_criterium_zonder_onderliggend_verschijnt_niet():
    groep = _gem_groep()

    groep.met_onderliggend("gedeeld_met_2_adressen", naam="Gedeeld met 2 adressen")

    assert groep.woningwaarderingen == []


def test_waardecriterium_verschijnt_direct():
    groep = _groep()

    groep.met_onderliggend("woz_waarde", aantal=100000)

    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1


def test_waardecriterium_materialiseert_bovenliggend_structureel_criterium():
    groep = _gem_groep()

    gedeeld_met = groep.met_gedeeld_met_criterium(
        2, GedeeldMetSoort.adressen, naam="Gedeeld met 2 adressen"
    )
    gedeeld_met.met_onderliggend("keuken", naam="Keuken").met_onderliggend(
        "Space_1", naam="Keuken", punten=1.0
    )

    assert groep.woningwaarderingen is not None
    ids = [w.criterium.id for w in groep.woningwaarderingen if w.criterium]
    assert ids == [
        "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen",
        "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__keuken",
        "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__keuken__Space_1",
    ]
    detail = groep.woningwaarderingen[2]
    assert detail.criterium is not None
    assert detail.criterium.bovenliggende_criterium is not None
    assert (
        detail.criterium.bovenliggende_criterium.id
        == "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__keuken"
    )


def test_met_gedeeld_met_criterium_pad_en_naam():
    groep = _gem_groep()

    gedeeld_met = groep.met_gedeeld_met_criterium(
        4, GedeeldMetSoort.adressen, naam="Gedeeld met 4 adressen"
    )
    gedeeld_met.met_onderliggend("keuken", naam="Keuken", punten=0.0)

    assert groep.woningwaarderingen is not None
    rij = groep.woningwaarderingen[0]
    assert rij.criterium is not None
    assert (
        rij.criterium.id
        == "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
    )
    assert rij.criterium.naam == "Gedeeld met 4 adressen"


def test_hergebruik_gedeeld_met_criterium_materialiseert_eenmaal():
    groep = _gem_groep()

    onz = groep.met_gedeeld_met_criterium(
        2,
        GedeeldMetSoort.onzelfstandige_woonruimten,
        naam="Gedeeld met 2 onzelfstandige woonruimten",
    )
    adr1 = onz.met_gedeeld_met_criterium(
        3, GedeeldMetSoort.adressen, naam="Gedeeld met 3 adressen"
    )
    adr1.met_onderliggend("keuken", naam="Keuken", punten=1.0)

    adr2 = onz.met_gedeeld_met_criterium(
        4, GedeeldMetSoort.adressen, naam="Gedeeld met 4 adressen"
    )
    adr2.met_onderliggend("sanitair", naam="Sanitair", punten=2.0)

    assert groep.woningwaarderingen is not None
    onz_ids = [
        w.criterium.id
        for w in groep.woningwaarderingen
        if w.criterium
        and w.criterium.id
        == "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_onzelfstandige_woonruimten"
    ]
    assert len(onz_ids) == 1
