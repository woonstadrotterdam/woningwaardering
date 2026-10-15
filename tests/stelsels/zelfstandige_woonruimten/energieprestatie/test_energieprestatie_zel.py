"""Energieprestatie, zelfstandige woonruimten (rubriek 4)."""

from datetime import date

import pytest

from tests.utils import assert_stelselgroep_output, punten_per_naam
from woningwaardering.stelsels.zelfstandige_woonruimten.energieprestatie import (
    Energieprestatie,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenPrijscomponent,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Pandsoort,
    Prijscomponentdetailsoort,
)


@pytest.fixture()
def energieprestatie(peildatum):
    return Energieprestatie(peildatum=peildatum)


def test_Energieprestatie_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Energieprestatie,
    )


# Energielabel en energie-index


def test_alleen_de_geldige_energieprestatie_telt_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Alleen een geldige energieprestatie bepaalt de punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3; wettekst,
    Bijlage I onder A, toelichting rubriek 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1993,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        # Het eerste label is op de peildatum vervallen.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2014, 3, 27),
                einddatum=date(2024, 3, 27),
                label=Energielabel.f,
                waarde="160",
            ),
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 3, 27),
                einddatum=date(2031, 3, 27),
                label=Energielabel.a,
                waarde="170",
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # Label A geeft een meergezinswoning 37 punten.
    assert punten_per_naam(groep) == {Energielabel.a.naam: 37.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energie-index wordt gewaardeerd op de index, niet op het label dat erbij is meegegeven.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder A, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        # Index 1,48 hoort bij klasse C, het meegegeven label A bij klasse A.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2020, 8, 1),
                einddatum=date(2030, 8, 1),
                label=Energielabel.a,
                waarde="1.48",
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # Index 1,4 tot 1,8 geeft een eengezinswoning 22 punten; label A zou 41
    # punten geven.
    assert punten_per_naam(groep) == {"A -> C (Energie-index)": 22.0}
    vergelijk_met_testreferentie(eenheid, groep)


# E ontbreekt omdat de bronnen verschillen.
@pytest.mark.parametrize(
    ("label", "verwachte_punten"),
    [
        pytest.param(Energielabel.ap4, 62.0, id="label_a4plus"),
        pytest.param(Energielabel.ap3, 57.0, id="label_a3plus"),
        pytest.param(Energielabel.app, 52.0, id="label_a2plus"),
        pytest.param(Energielabel.ap, 47.0, id="label_aplus"),
        pytest.param(Energielabel.a, 41.0, id="label_a"),
        pytest.param(Energielabel.b, 34.0, id="label_b"),
        pytest.param(Energielabel.c, 22.0, id="label_c"),
        pytest.param(Energielabel.d, 14.0, id="label_d"),
        pytest.param(Energielabel.f, -9.0, id="label_f"),
        pytest.param(Energielabel.g, -15.0, id="label_g"),
    ],
)
def test_punten_voor_een_energielabel_hangen_af_van_de_labelklasse(
    energieprestatie, vergelijk_met_testreferentie, label, verwachte_punten
):
    """De punten voor een energielabel hangen af van de labelklasse.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder A, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 3, 27),
                einddatum=date(2031, 3, 27),
                label=label,
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert punten_per_naam(groep) == {label.naam: verwachte_punten}
    vergelijk_met_testreferentie(eenheid, groep)


# Elke index op de bovengrens van zijn klasse, behalve 2,71; A++ en E ontbreken omdat de bronnen verschillen.
@pytest.mark.parametrize(
    ("energie_index", "verwachte_punten"),
    [
        pytest.param("0.8", 47.0, id="index_0_8"),
        pytest.param("1.2", 41.0, id="index_1_2"),
        pytest.param("1.4", 34.0, id="index_1_4"),
        pytest.param("1.8", 22.0, id="index_1_8"),
        pytest.param("2.1", 14.0, id="index_2_1"),
        pytest.param("2.7", -9.0, id="index_2_7"),
        pytest.param("2.71", -15.0, id="index_2_71"),
    ],
)
def test_punten_voor_een_energie_index_hangen_af_van_de_klasse(
    energieprestatie, vergelijk_met_testreferentie, energie_index, verwachte_punten
):
    """De punten voor een energie-index hangen af van de klasse waarin de index valt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder A, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        # Zonder label bepaalt alleen de index de punten.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2020, 8, 1),
                einddatum=date(2030, 8, 1),
                waarde=energie_index,
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Energie-index": verwachte_punten}
    vergelijk_met_testreferentie(eenheid, groep)


# Zonder geldige energieprestatie: het bouwjaar


# Beide einddata liggen na de peildatum, zodat alleen de afgiftedatum het label tegenhoudt.
@pytest.mark.parametrize(
    ("begindatum", "einddatum"),
    [
        pytest.param(
            date(2015, 1, 1),
            date(2027, 1, 1),
            id="afgegeven_op_1_januari_2015",
        ),
        pytest.param(
            date(2020, 12, 31),
            date(2030, 12, 31),
            id="afgegeven_op_31_december_2020",
        ),
    ],
)
def test_energielabel_afgegeven_van_2015_tot_2021_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie, begindatum, einddatum
):
    """Een energielabel dat is afgegeven van 1 januari 2015 tot 1 januari 2021, telt niet mee.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3.

    Zonder geldige energieprestatie bepaalt het bouwjaar de punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.5; wettekst,
    Bijlage I onder A, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.voorlopig_energielabel,
                status=Energieprestatiestatus.definitief,
                begindatum=begindatum,
                einddatum=einddatum,
                label=Energielabel.a,
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # Bouwjaar 1984 t/m 1991 geeft een eengezinswoning 14 punten.
    assert punten_per_naam(groep) == {"Bouwjaar 1990": 14.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_zonder_waarde_wordt_met_waarschuwing_op_het_bouwjaar_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energie-index zonder waarde wordt met een waarschuwing op het bouwjaar gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3.
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1990,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        # De energie-index heeft geen waarde; het label A telt niet mee.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 1),
                einddatum=date(2028, 6, 1),
                label=Energielabel.a,
            )
        ],
    )

    with pytest.warns(UserWarning, match="energie-index mist waarde") as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    # Bouwjaar 1984 t/m 1991 geeft een eengezinswoning 14 punten.
    assert punten_per_naam(groep) == {"Bouwjaar 1990": 14.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_energieprestatie_zonder_soort_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energieprestatie zonder soort telt niet mee.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3.

    Zonder geldige energieprestatie bepaalt het bouwjaar de punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.5; wettekst,
    Bijlage I onder A, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        # De energieprestatie heeft geen soort.
        energieprestaties=[
            EenhedenEnergieprestatie(
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 2, 23),
                einddatum=date(2031, 2, 23),
                label=Energielabel.c,
                waarde="1.48",
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # Bouwjaar 1976 of ouder geeft een meergezinswoning -15 punten.
    assert punten_per_naam(groep) == {"Bouwjaar 1921": -15.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Monumenten


@pytest.mark.parametrize(
    "monument",
    [
        pytest.param(Eenheidmonument.rijksmonument, id="rijksmonument"),
        pytest.param(Eenheidmonument.provinciaal_monument, id="provinciaal_monument"),
        pytest.param(Eenheidmonument.gemeentelijk_monument, id="gemeentelijk_monument"),
    ],
)
def test_monument_krijgt_geen_minpunten(
    energieprestatie, vergelijk_met_testreferentie, monument
):
    """Een rijks-, provinciaal of gemeentelijk monument krijgt geen minpunten voor de energieprestatie.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.6.1; wettekst,
    Bijlage I onder A, onderdeel 4.2.
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1921,
        monumenten=[monument],
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        # Zonder energieprestaties bepaalt het bouwjaar de punten.
        energieprestaties=[],
    )

    with pytest.warns(
        UserWarning, match="'energieprestaties' is None"
    ) as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    # Bouwjaar 1976 of ouder geeft een meergezinswoning -15 punten.
    assert punten_per_naam(groep) == {
        "Bouwjaar 1921": -15.0,
        "Correctie monument": 15.0,
    }
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_rijksmonument_met_pluspunten_krijgt_geen_correctie(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een rijksmonument met een positief aantal punten voor de energieprestatie houdt die punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.6.1; wettekst,
    Bijlage I onder A, onderdeel 4.2.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        # Een geldige energie-index C geeft pluspunten.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2017, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Energielabel.c,
                waarde="1.48",
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert punten_per_naam(groep) == {"C (Energie-index)": 22.0}
    assert groep.punten == 22.0
    vergelijk_met_testreferentie(eenheid, groep)


# Energieprestatievergoeding


@pytest.mark.parametrize(
    ("pandsoort", "verwachte_punten"),
    [
        pytest.param(
            Pandsoort.eengezinswoning,
            {"Energieprestatievergoeding Eengezinswoning": 32.0},
            id="eengezinswoning",
        ),
        pytest.param(
            Pandsoort.meergezinswoning,
            {"Energieprestatievergoeding Meergezinswoning": 28.0},
            id="meergezinswoning",
        ),
    ],
)
def test_energieprestatievergoeding_geeft_een_vast_aantal_punten(
    energieprestatie, vergelijk_met_testreferentie, pandsoort, verwachte_punten
):
    """Bij een energieprestatievergoeding krijgt een eengezinswoning 32 punten en een meergezinswoning 28 punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.6.3; wettekst,
    Bijlage I onder A, onderdeel 4.3.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=pandsoort)],
        # Een geldige energie-index, zodat de vergoeding voorgaat op de tabel.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2017, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Energielabel.c,
                waarde="1.48",
            )
        ],
        prijscomponenten=[
            EenhedenPrijscomponent(
                detail_soort=Prijscomponentdetailsoort.energieprestatievergoeding
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert punten_per_naam(groep) == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)
