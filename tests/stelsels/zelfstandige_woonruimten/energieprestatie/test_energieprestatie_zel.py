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
    Referentiedata,
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


def test_van_twee_energieprestaties_telt_alleen_de_geldige(
    energieprestatie, vergelijk_met_testreferentie
):
    """Van twee energieprestaties bepaalt alleen de geldige de punten.

    Bron: beleidsboek zelfstandige woonruimten, 2.4.2: "De woonruimte krijgt
    punten voor de energieprestatie als de woning een geldend energielabel of
    energie-index heeft."

    Het eerste energielabel is op twee gronden niet geldig: het is op de
    peildatum vervallen en het is afgegeven in 2019.

    Bron: beleidsboek zelfstandige woonruimten, 2.4.3: "Aan een vervallen
    energielabel of energie-index wordt geen waardering toegekend.", "Een
    energielabel dat is afgegeven in de periode van 1 januari 2015 tot 1 januari
    2021 krijgt geen punten in het woningwaarderingsstelsel."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3: "De
    peildatum moet vallen tussen begindatum en einddatum."

    Het geldige energielabel A geeft een meergezinswoning 37 punten.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "A 0,8 < EI ≤ 1,2 2002 en later 41 37".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1993,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2019, 3, 27),
                einddatum=date(2021, 3, 27),
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

    assert punten_per_naam(groep) == {Energielabel.a.naam: 37.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energie-index uit 2020 wordt gewaardeerd op de index, niet op het label dat erbij is meegegeven.

    Bron: beleidsboek zelfstandige woonruimten, 2.4.4: "Bij een energie-index
    wordt het puntenaantal bepaald door het relevante cijfer."

    Een energie-index van 1,48 geeft een eengezinswoning 22 punten; het
    meegegeven label A zou 41 punten geven.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "C 1,4 < EI ≤ 1,8 1992 t/m 1999 22 15", "A 0,8 < EI ≤ 1,2 2002 en later 41
    37".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
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

    assert punten_per_naam(groep) == {"A -> C (Energie-index)": 22.0}
    vergelijk_met_testreferentie(eenheid, groep)


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

    Elke index ligt op de bovengrens van zijn klasse, behalve 2,71. De
    energieprestaties hebben geen label, zodat alleen de index de punten
    bepaalt. De grenzen bij A++ en E staan er niet in: daar verschillen de
    bronnen.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "A+ 0,6 < EI ≤ 0,8 n.v.t. 47 43", "A 0,8 < EI ≤ 1,2 2002 en later 41 37",
    "B 1,2 < EI ≤ 1,4 2000 t/m 2001 34 30", "C 1,4 < EI ≤ 1,8 1992 t/m 1999 22
    15", "D 1,8 < EI ≤ 2,1 1984 t/m 1991 14 11", "F 2,4 < EI ≤ 2,7 1977 t/m
    1978 –9 –9" en "G EI > 2,7 1976 of ouder –15 –15".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
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


def test_woning_met_energielabel_uit_2018_wordt_op_het_bouwjaar_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energielabel uit 2018 telt niet mee: de woning wordt op het bouwjaar gewaardeerd.

    Bron: beleidsboek zelfstandige woonruimten, 2.4.3: "Een energielabel dat is
    afgegeven in de periode van 1 januari 2015 tot 1 januari 2021 krijgt geen
    punten in het woningwaarderingsstelsel."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3: "Een
    energieprestatie van een ander soort dan energie-index in de periode
    2015-2021, of een energie-index zonder bruikbare `waarde`, telt niet mee
    (2.4.3, punt 4); de waardering valt dan terug op het bouwjaar (2.4.5)."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 4.1: "Daar waar een
    geldig energielabel ontbreekt, wordt de waardering van de energieprestatie
    bepaald op basis van het bouwjaar van de woning."

    Een eengezinswoning met bouwjaar 1990 krijgt 14 punten.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "D 1,8 < EI ≤ 2,1 1984 t/m 1991 14 11".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.voorlopig_energielabel,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 1),
                einddatum=date(2028, 6, 1),
                label=Energielabel.a,
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Bouwjaar 1990": 14.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_zonder_waarde_wordt_met_waarschuwing_op_het_bouwjaar_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energie-index zonder waarde wordt met een waarschuwing op het bouwjaar gewaardeerd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3: "Een
    energieprestatie van een ander soort dan energie-index in de periode
    2015-2021, of een energie-index zonder bruikbare `waarde`, telt niet mee
    (2.4.3, punt 4); de waardering valt dan terug op het bouwjaar (2.4.5). Bij
    een energie-index zonder `waarde` gebeurt dit met een `UserWarning`
    (standaard een error)."

    Een eengezinswoning met bouwjaar 1990 krijgt 14 punten.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "D 1,8 < EI ≤ 2,1 1984 t/m 1991 14 11".
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1990,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
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

    assert punten_per_naam(groep) == {"Bouwjaar 1990": 14.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_energieprestatie_zonder_soort_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energieprestatie zonder soort telt niet mee: de woning wordt op het bouwjaar gewaardeerd.

    De package slaat een energieprestatie zonder soort over zonder te
    waarschuwen. De implementatietoelichting noemt die keuze niet; de test legt
    het huidige gedrag vast. Het label heeft hier alleen een naam, geen code.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 4.1: "Daar waar een
    geldig energielabel ontbreekt, wordt de waardering van de energieprestatie
    bepaald op basis van het bouwjaar van de woning."

    Een meergezinswoning met bouwjaar 1921 krijgt -15 punten.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "G EI > 2,7 1976 of ouder –15 –15".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        energieprestaties=[
            EenhedenEnergieprestatie(
                status=Energieprestatiestatus.definitief,
                begindatum=date(2017, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Referentiedata(naam="C"),
                waarde="1.48",
            )
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Bouwjaar 1921": -15.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Monumenten


def test_rijksmonument_krijgt_geen_minpunten(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een rijksmonument krijgt geen minpunten voor de energieprestatie.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.2: "Indien de woonruimte
    bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
    of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
    rubriek geen minpunten toegekend. Voor energielabel E, F en G en daaraan
    gelijkgestelde Energie-indexen en bouwjaren, geldt in afwijking van de
    bovenstaande tabellen in dat geval een toekenning van nul punten."

    De eenheid heeft geen energieprestaties. De package waarschuwt daarvoor en
    waardeert op het bouwjaar.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 4.1: "Daar waar een
    geldig energielabel ontbreekt, wordt de waardering van de energieprestatie
    bepaald op basis van het bouwjaar van de woning."

    Een meergezinswoning met bouwjaar 1921 krijgt -15 punten.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.1, tabel met de kolommen
    energielabel, energie-index, bouwjaar, eengezinswoning en meergezinswoning:
    "G EI > 2,7 1976 of ouder –15 –15".
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        energieprestaties=[],
    )

    with pytest.warns(
        UserWarning, match="'energieprestaties' is None"
    ) as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

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

    Bron: wettekst, Bijlage I onder A, onderdeel 4.2: "Indien de woonruimte
    bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
    of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
    rubriek geen minpunten toegekend."

    De punten komen hier uit de energieprestatievergoeding van een
    eengezinswoning.

    Bron: wettekst, Bijlage I onder A, onderdeel 4.3: "In de gevallen waarin een
    energieprestatievergoeding als bedoeld in artikel 237 van boek 7 van het
    Burgerlijk Wetboek is overeengekomen, wordt in afwijking van bovenstaande
    tabel het volgende aantal punten toegekend: Eengezinswoning
    Meergezinswoning/duplexwoning 32 28".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
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

    assert punten_per_naam(groep) == {
        "Energieprestatievergoeding Eengezinswoning": 32.0
    }
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

    Bron: wettekst, Bijlage I onder A, onderdeel 4.3: "In de gevallen waarin een
    energieprestatievergoeding als bedoeld in artikel 237 van boek 7 van het
    Burgerlijk Wetboek is overeengekomen, wordt in afwijking van bovenstaande
    tabel het volgende aantal punten toegekend: Eengezinswoning
    Meergezinswoning/duplexwoning 32 28".
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        panden=[EenhedenPand(soort=pandsoort)],
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
