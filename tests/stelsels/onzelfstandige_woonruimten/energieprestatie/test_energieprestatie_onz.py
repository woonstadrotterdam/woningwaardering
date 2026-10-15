"""Energieprestatie, onzelfstandige woonruimten (rubriek 4)."""

from datetime import date

import pytest

from tests.input import ruimte
from tests.utils import aantal_per_naam, assert_stelselgroep_output, punten_per_naam
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Energieprestatie,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenPrijscomponent,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Prijscomponentdetailsoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def energieprestatie(peildatum):
    return Energieprestatie(peildatum=peildatum)


def test_Energieprestatie_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Energieprestatie,
    )


# De oppervlakte waarover de punten gelden


def test_toe_te_rekenen_oppervlakte_telt_onafgerond_mee_voor_de_energieprestatie(
    energieprestatie, vergelijk_met_testreferentie
):
    """De oppervlakte die aan de huurder is toe te rekenen, telt voor de energieprestatie onafgerond mee.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        monumenten=[],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 1, 1),
                einddatum=date(2031, 1, 1),
                label=Energielabel.a,
            )
        ],
        # Het voorbeeld uit de implementatietoelichting: 10,40 m² privé en 40,40 m² gedeeld met drie andere huurders.
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=10.4),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=40.4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10,40 m² slaapkamer + 40,40 m² woonkamer gedeeld door 4
    assert aantal_per_naam(groep) == {Energielabel.a.naam: 20.5}
    # 20,50 m² x 0,65 punt = 13,325 punten, afgerond op 13,25
    assert punten_per_naam(groep) == {
        Energielabel.a.naam: 13.33,
        "Afronding op kwartpunten": -0.08,
    }
    assert groep.punten == 13.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijk_vertrek_telt_voor_de_energieprestatie_mee_met_de_toe_te_rekenen_oppervlakte(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een gemeenschappelijk vertrek telt voor de energieprestatie mee met de oppervlakte die aan de huurder is toe te rekenen.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder B, onderdeel 4.1; wettekst, Bijlage I onder B, onderdeel 1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        monumenten=[],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 1, 1),
                einddatum=date(2031, 1, 1),
                label=Energielabel.a,
                waarde="0.9",
            )
        ],
        # Zoals in het rekenvoorbeeld: de woonkamer gedeeld met drie andere huurders, de slaapkamer privé.
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=20,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=40,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 20 m² slaapkamer + 40 m² woonkamer gedeeld door 4
    assert aantal_per_naam(groep) == {Energielabel.a.naam: 30.0}
    # 30 m² x 0,65 punt
    assert punten_per_naam(groep) == {Energielabel.a.naam: 19.5}
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_gedeeld_met_meerdere_adressen_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een vertrek dat met meerdere adressen wordt gedeeld, telt niet mee in de m² voor de energieprestatie.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        monumenten=[],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 1, 1),
                einddatum=date(2031, 1, 1),
                label=Energielabel.a,
                waarde="0.9",
            )
        ],
        # Gedeeld met twee adressen, het kleinste aantal voor meerdere adressen; de slaapkamer is privé.
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=20,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=40,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # Alleen de slaapkamer van 20 m² telt mee
    assert aantal_per_naam(groep) == {Energielabel.a.naam: 20.0}
    # 20 m² x 0,65 punt
    assert punten_per_naam(groep) == {Energielabel.a.naam: 13.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_kast_telt_mee_in_de_oppervlakte_voor_de_energieprestatie(
    energieprestatie, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast die met een vertrek is verbonden, telt mee in de m² voor de energieprestatie.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        # Zonder energieprestaties bepaalt het bouwjaar de punten per m².
        bouwjaar=1970,
        monumenten=[],
        # Een kast is geen vertrek, maar telt mee omdat ze met de slaapkamer verbonden is.
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=20.0,
                verbonden_ruimten=[ruimte(Ruimtedetailsoort.kast, oppervlakte=2.0)],
            )
        ],
    )

    with pytest.warns(
        UserWarning, match="'energieprestaties' is None"
    ) as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    # 20 m² slaapkamer + 2 m² kast
    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 22.0}
    # 22 m² x -0,15 punt = -3,3 punten
    assert punten_per_naam(groep) == {
        "Bouwjaar 1970": -3.3,
        "Afronding op kwartpunten": 0.05,
    }
    assert groep.punten == -3.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Energielabel en energie-index


def test_alleen_de_geldige_energieprestatie_telt_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Alleen een geldige energieprestatie bepaalt de punten per m² van de vertrekken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1993,
        monumenten=[],
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
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Energielabel.a.naam: 10.0}
    # 10 m² x 0,65 punt
    assert punten_per_naam(groep) == {Energielabel.a.naam: 6.5}
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    ("label", "verwachte_punten"),
    [
        pytest.param(Energielabel.ap4, 10.0, id="label_a4plus"),
        pytest.param(Energielabel.ap3, 9.5, id="label_a3plus"),
        pytest.param(Energielabel.app, 8.5, id="label_a2plus"),
        pytest.param(Energielabel.ap, 7.5, id="label_aplus"),
        pytest.param(Energielabel.a, 6.5, id="label_a"),
        pytest.param(Energielabel.b, 5.0, id="label_b"),
        pytest.param(Energielabel.c, 3.5, id="label_c"),
        pytest.param(Energielabel.d, 2.0, id="label_d"),
        pytest.param(Energielabel.e, -0.5, id="label_e"),
        pytest.param(Energielabel.f, -1.0, id="label_f"),
        pytest.param(Energielabel.g, -1.5, id="label_g"),
    ],
)
def test_punten_per_m2_voor_een_energielabel_hangen_af_van_de_labelklasse(
    energieprestatie, vergelijk_met_testreferentie, label, verwachte_punten
):
    """De punten per m² van de vertrekken voor een energielabel hangen af van de labelklasse.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1993,
        monumenten=[],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2021, 3, 27),
                einddatum=date(2031, 3, 27),
                label=label,
            )
        ],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {label.naam: 10.0}
    # 10 m² x de punten per m² van het label
    assert punten_per_naam(groep) == {label.naam: verwachte_punten}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label(
    energieprestatie, vergelijk_met_testreferentie
):
    """Bij een energie-index bepaalt de index de punten per m², niet het label dat erbij is meegegeven.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
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
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"A -> C (Energie-index)": 10.0}
    # 10 m² x 0,35 punt
    assert punten_per_naam(groep) == {"A -> C (Energie-index)": 3.5}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_zonder_label_wordt_op_de_index_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energie-index zonder label bepaalt de punten per m².

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.2;
    implementatietoelichting onzelfstandige woonruimten, 2.4.4; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1970,
        monumenten=[],
        # De index is opgenomen in 2018, tussen 1 januari 2015 en 1 januari 2021.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 1),
                einddatum=date(2028, 6, 1),
                waarde="1.0",
            )
        ],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Energie-index": 10.0}
    # 10 m² x 0,65 punt
    assert punten_per_naam(groep) == {"Energie-index": 6.5}
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3.

    Zonder geldige energieprestatie bepaalt het bouwjaar de punten per m².

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1970,
        monumenten=[],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.voorlopig_energielabel,
                status=Energieprestatiestatus.definitief,
                begindatum=begindatum,
                einddatum=einddatum,
                label=Energielabel.a,
            )
        ],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 10.0}
    # 10 m² x -0,15 punt
    assert punten_per_naam(groep) == {"Bouwjaar 1970": -1.5}
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_zonder_waarde_wordt_met_waarschuwing_op_het_bouwjaar_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energie-index zonder waarde wordt met een waarschuwing op het bouwjaar gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3.
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1970,
        monumenten=[],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 1),
                einddatum=date(2028, 6, 1),
            )
        ],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    with pytest.warns(UserWarning, match="energie-index mist waarde") as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 10.0}
    # 10 m² x -0,15 punt
    assert punten_per_naam(groep) == {"Bouwjaar 1970": -1.5}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_energieprestatie_zonder_soort_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energieprestatie zonder soort telt niet mee.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3.

    Zonder geldige energieprestatie bepaalt het bouwjaar de punten per m².

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
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
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Bouwjaar 1921": 10.0}
    # 10 m² x -0,15 punt
    assert punten_per_naam(groep) == {"Bouwjaar 1921": -1.5}
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
    wettekst, Bijlage I onder B, onderdeel 4.2.
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1921,
        monumenten=[monument],
        # Zonder energieprestaties bepaalt het bouwjaar de punten.
        energieprestaties=[],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    with pytest.warns(
        UserWarning, match="'energieprestaties' is None"
    ) as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Bouwjaar 1921": 10.0}
    # De correctie heft de minpunten van 10 m² x -0,15 punt op
    assert punten_per_naam(groep) == {
        "Bouwjaar 1921": -1.5,
        "Correctie monument": 1.5,
    }
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_rijksmonument_met_pluspunten_krijgt_geen_correctie(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een rijksmonument met een positief aantal punten voor de energieprestatie houdt die punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
    wettekst, Bijlage I onder B, onderdeel 4.2.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
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
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"C (Energie-index)": 10.0}
    # 10 m² x 0,35 punt
    assert punten_per_naam(groep) == {"C (Energie-index)": 3.5}
    assert groep.punten == 3.5
    vergelijk_met_testreferentie(eenheid, groep)


# Energieprestatievergoeding


def test_energieprestatievergoeding_geeft_een_vast_aantal_punten_per_m2(
    energieprestatie, vergelijk_met_testreferentie
):
    """Bij een energieprestatievergoeding krijgt de woonruimte 0,50 punt per m² van de vertrekken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.3.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
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
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Energieprestatievergoeding": 10.0}
    # 10 m² x 0,50 punt
    assert punten_per_naam(groep) == {"Energieprestatievergoeding": 5.0}
    vergelijk_met_testreferentie(eenheid, groep)
