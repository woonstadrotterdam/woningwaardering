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
    Referentiedata,
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
        # Zoals in het rekenvoorbeeld deelt de huurder de woonkamer met drie
        # andere huurders; de privéslaapkamer is niet gedeeld.
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
        # Twee adressen is de kleinste waarde waarmee het vertrek met meerdere
        # adressen wordt gedeeld; de slaapkamer is privé.
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
        # Een kast is geen vertrek; ze telt mee omdat ze met de slaapkamer
        # verbonden is.
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
        # Het eerste label is op de peildatum vervallen en afgegeven in 2019.
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
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {Energielabel.a.naam: 3.67}
    # 3,67 m² x 0,65 punt
    assert punten_per_naam(groep) == {
        Energielabel.a.naam: 2.38,
        "Afronding op kwartpunten": 0.12,
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_energielabel_f_geeft_minpunten_per_m2(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energielabel F geeft 0,10 minpunt per m² van de vertrekken.

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
                label=Energielabel.f,
                waarde="160.92",
            )
        ],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=20.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=30.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Energielabel.f.naam: 9.0}
    assert punten_per_naam(groep) == {
        Energielabel.f.naam: -0.9,
        "Afronding op kwartpunten": -0.1,
    }
    assert groep.punten == -1.0
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
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"A -> C (Energie-index)": 3.67}
    # 3,67 m² x 0,35 punt
    assert punten_per_naam(groep) == {
        "A -> C (Energie-index)": 1.28,
        "Afronding op kwartpunten": -0.03,
    }
    assert groep.punten == 1.25
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
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Energie-index": 3.67}
    # 3,67 m² x 0,65 punt
    assert punten_per_naam(groep) == {
        "Energie-index": 2.38,
        "Afronding op kwartpunten": 0.12,
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zonder geldige energieprestatie: het bouwjaar


def test_energielabel_afgegeven_van_2015_tot_2021_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energielabel dat is afgegeven van 1 januari 2015 tot 1 januari 2021 telt niet mee: het bouwjaar bepaalt de punten per m².

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3;
    implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1970,
        monumenten=[],
        # Het label is afgegeven in 2018, in de periode waarin labels niet meetellen.
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.voorlopig_energielabel,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 1),
                einddatum=date(2028, 6, 1),
                label=Energielabel.a,
            )
        ],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 3.67}
    # 3,67 m² x -0,15 punt
    assert punten_per_naam(groep) == {
        "Bouwjaar 1970": -0.55,
        "Afronding op kwartpunten": 0.05,
    }
    assert groep.punten == -0.5
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
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    with pytest.warns(UserWarning, match="energie-index mist waarde") as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 3.67}
    # 3,67 m² x -0,15 punt
    assert punten_per_naam(groep) == {
        "Bouwjaar 1970": -0.55,
        "Afronding op kwartpunten": 0.05,
    }
    assert groep.punten == -0.5
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_energieprestatie_zonder_soort_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energieprestatie zonder soort telt niet mee: het bouwjaar bepaalt de punten per m².

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3;
    implementatietoelichting onzelfstandige woonruimten, 2.4.5; wettekst,
    Bijlage I onder B, onderdeel 4.1.
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
        # De energieprestatie heeft geen soort; het label heeft alleen een naam.
        energieprestaties=[
            EenhedenEnergieprestatie(
                status=Energieprestatiestatus.definitief,
                begindatum=date(2017, 2, 23),
                einddatum=date(2027, 2, 23),
                label=Referentiedata(naam="C"),
                waarde="1.48",
            )
        ],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Bouwjaar 1921": 3.67}
    # 3,67 m² x -0,15 punt
    assert punten_per_naam(groep) == {
        "Bouwjaar 1921": -0.55,
        "Afronding op kwartpunten": 0.05,
    }
    assert groep.punten == -0.5
    vergelijk_met_testreferentie(eenheid, groep)


# Monumenten


def test_rijksmonument_krijgt_geen_minpunten(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een rijksmonument krijgt geen minpunten voor de energieprestatie.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
    wettekst, Bijlage I onder B, onderdeel 4.2.
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
        # Zonder energieprestaties bepaalt het bouwjaar de punten.
        energieprestaties=[],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    with pytest.warns(
        UserWarning, match="'energieprestaties' is None"
    ) as waarschuwingen:
        groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Bouwjaar 1921": 3.67}
    # De correctie heft de minpunten van 3,67 m² x -0,15 punt op
    assert punten_per_naam(groep) == {
        "Bouwjaar 1921": -0.55,
        "Correctie monument": 0.55,
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
        # De energieprestatievergoeding geeft pluspunten, ook al zou het bouwjaar
        # minpunten geven.
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
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Energieprestatievergoeding": 3.67}
    # 3,67 m² x 0,50 punt
    assert punten_per_naam(groep) == {
        "Energieprestatievergoeding": 1.83,
        "Afronding op kwartpunten": -0.08,
    }
    assert groep.punten == 1.75
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
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10.0,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ],
    )

    groep = energieprestatie.waardeer(eenheid)

    # 10 m² gedeeld door 5 + 10 m² gedeeld door 6
    assert aantal_per_naam(groep) == {"Energieprestatievergoeding": 3.67}
    # 3,67 m² x 0,50 punt
    assert punten_per_naam(groep) == {
        "Energieprestatievergoeding": 1.83,
        "Afronding op kwartpunten": -0.08,
    }
    assert groep.punten == 1.75
    vergelijk_met_testreferentie(eenheid, groep)
