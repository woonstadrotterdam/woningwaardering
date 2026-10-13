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


def test_rekenvoorbeeld_met_gemeenschappelijke_woonkamer_uit_het_beleidsboek(
    energieprestatie, vergelijk_met_testreferentie
):
    """Het rekenvoorbeeld uit het beleidsboek: een privéslaapkamer van 20 m² en een woonkamer van 40 m² die vier onzelfstandige woonruimten delen, geven bij energielabel A 19,50 punten.

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "Huurder heeft een
    privé slaapkamer van 20 m² in een pand met energielabel A. Naast de privé
    slaapkamer heeft huurder toegang tot een gemeenschappelijke woonkamer van
    40 m².", "Huurder deelt de woonkamer met drie andere huurders van
    onzelfstandige woonruimten op het adres. Het aantal m2 gemeenschappelijk
    vertrek dat aan de huurder is toe te rekenen is dus 40 m²/4 = 10 m².", "Het
    puntenaantal voor de energieprestatie wordt dan als volgt berekend:" en
    "(20 + 10) x 0,65 = 19,50 punten."

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
    1,2 2002 en later 0,65 punt".

    De privéslaapkamer heeft in de input
    `gedeeld_met_aantal_onzelfstandige_woonruimten` 1 en is daarmee niet
    gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4: "Indien
    deze property leeg is of kleiner is dan 2, tellen we de ruimte mee als
    zijnde niet gedeeld."
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

    assert aantal_per_naam(groep) == {Energielabel.a.naam: 30.0}
    assert punten_per_naam(groep) == {Energielabel.a.naam: 19.5}
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_gedeeld_met_meerdere_adressen_telt_niet_mee(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een vertrek dat met meerdere adressen wordt gedeeld, telt niet mee in de m² voor de energieprestatie.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4:
    "Gemeenschappelijke vertrekken die met meerdere adressen worden gedeeld
    (`gedeeldMetAantalAdressen` ≥ 2) tellen niet mee voor de oppervlakte in
    §2.4.4." en "Rubriek 1 dekt alleen privévertrekken en gemeenschappelijke
    vertrekken op hetzelfde adres; ruimten gedeeld met meerdere adressen
    vallen onder rubriek 9".

    De privéslaapkamer heeft in de input
    `gedeeld_met_aantal_onzelfstandige_woonruimten` 1 en is daarmee niet
    gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4: "Indien
    deze property leeg is of kleiner is dan 2, tellen we de ruimte mee als
    zijnde niet gedeeld."

    Alleen de privéslaapkamer van 20 m² telt mee. Label A geeft 0,65 punt per
    m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
    1,2 2002 en later 0,65 punt".
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

    assert aantal_per_naam(groep) == {Energielabel.a.naam: 20.0}
    assert punten_per_naam(groep) == {Energielabel.a.naam: 13.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_kast_telt_mee_in_de_oppervlakte_voor_de_energieprestatie(
    energieprestatie, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast die met een vertrek is verbonden, telt mee in de m² voor de energieprestatie.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Meting van de
    oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van
    1,50 meter boven de vloer, inclusief de oppervlakte van alle tot de woning
    behorende losse en vaste kasten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."

    De eenheid heeft geen energieprestaties. De package waarschuwt daarvoor en
    waardeert op het bouwjaar.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bouwjaar 1970 geeft -0,15 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "Indien geen
    energielabel of EI beschikbaar is, wordt gewaardeerd met het bouwjaar" en
    "G EI > 2,7 1976 of ouder – 0,15 punt".
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1970,
        monumenten=[],
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

    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 22.0}
    assert punten_per_naam(groep) == {
        "Bouwjaar 1970": -3.3,
        "Afronding op kwartpunten": 0.05,
    }
    assert groep.punten == -3.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Energielabel en energie-index


def test_van_twee_energieprestaties_telt_alleen_de_geldige(
    energieprestatie, vergelijk_met_testreferentie
):
    """Van twee energieprestaties bepaalt alleen de geldige de punten per m² van de vertrekken.

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.2: "De woonruimte krijgt
    punten voor de energieprestatie als de woning een geldend energielabel of
    energie-index heeft."

    Het eerste energielabel is op twee gronden niet geldig: het is op de
    peildatum vervallen en het is afgegeven in 2019.

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.3: "Aan een vervallen
    energielabel of energie-index wordt geen waardering toegekend.", "Een
    energielabel dat is afgegeven in de periode van 1 januari 2015 tot 1 januari
    2021 krijgt geen punten in het woningwaarderingsstelsel."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3: "De
    peildatum moet vallen tussen begindatum en einddatum."

    Het geldige energielabel A geeft 0,65 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
    1,2 2002 en later 0,65 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1993,
        monumenten=[],
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

    assert aantal_per_naam(groep) == {Energielabel.a.naam: 3.67}
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

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "De labelklasse
    (A++++ t/m G) bepaalt het aantal punten voor de energieprestatie."

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "F 2,4 < EI ≤
    2,7 1977 t/m 1978 – 0,10 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".
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
    """Bij een energie-index uit 2020 bepaalt de index de punten per m², niet het label dat erbij is meegegeven.

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "Bij een energie-index
    wordt het puntenaantal bepaald door het relevante cijfer."

    Een energie-index van 1,48 geeft 0,35 punt per m²; het meegegeven label A
    zou 0,65 punt per m² geven.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "C 1,4 < EI ≤
    1,8 1992 t/m 1999 0,35 punt", "A 0,8 < EI ≤ 1,2 2002 en later 0,65 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
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

    assert aantal_per_naam(groep) == {"A -> C (Energie-index)": 3.67}
    assert punten_per_naam(groep) == {
        "A -> C (Energie-index)": 1.28,
        "Afronding op kwartpunten": -0.03,
    }
    assert groep.punten == 1.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_energie_index_zonder_label_wordt_op_de_index_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Bij een energie-index uit 2018 zonder label bepaalt de index de punten per m².

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.2: "een energie-index die
    is opgenomen op of na 1 januari 2015 tot 1 januari 2021".

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.4: "Bij een energie-index
    wordt het puntenaantal bepaald door het relevante cijfer."

    Een energie-index van 1,0 geeft 0,65 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "A 0,8 < EI ≤
    1,2 2002 en later 0,65 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1970,
        monumenten=[],
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

    assert aantal_per_naam(groep) == {"Energie-index": 3.67}
    assert punten_per_naam(groep) == {
        "Energie-index": 2.38,
        "Afronding op kwartpunten": 0.12,
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zonder geldige energieprestatie: het bouwjaar


def test_woning_met_energielabel_uit_2018_wordt_op_het_bouwjaar_gewaardeerd(
    energieprestatie, vergelijk_met_testreferentie
):
    """Een energielabel uit 2018 telt niet mee: het bouwjaar bepaalt de punten per m².

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.3: "Een energielabel dat
    is afgegeven in de periode van 1 januari 2015 tot 1 januari 2021 krijgt geen
    punten in het woningwaarderingsstelsel."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3: "Een
    energieprestatie van een ander soort dan energie-index in de periode
    2015-2021, of een energie-index zonder bruikbare `waarde`, telt niet mee
    (2.4.3, punt 4); de waardering valt dan terug op het bouwjaar (2.4.5)."

    Bouwjaar 1970 geeft -0,15 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "Indien geen
    energielabel of EI beschikbaar is, wordt gewaardeerd met het bouwjaar" en
    "G EI > 2,7 1976 of ouder – 0,15 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1970,
        monumenten=[],
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

    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 3.67}
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.3: "Een
    energieprestatie van een ander soort dan energie-index in de periode
    2015-2021, of een energie-index zonder bruikbare `waarde`, telt niet mee
    (2.4.3, punt 4); de waardering valt dan terug op het bouwjaar (2.4.5). Bij
    een energie-index zonder `waarde` gebeurt dit met een `UserWarning`
    (standaard een error)."

    Bouwjaar 1970 geeft -0,15 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "G EI > 2,7
    1976 of ouder – 0,15 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
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

    assert aantal_per_naam(groep) == {"Bouwjaar 1970": 3.67}
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

    De package slaat een energieprestatie zonder soort over zonder te
    waarschuwen. De implementatietoelichting noemt die keuze niet; de test legt
    het huidige gedrag vast. Het label heeft hier alleen een naam, geen code.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "Indien geen
    energielabel of EI beschikbaar is, wordt gewaardeerd met het bouwjaar".

    Bouwjaar 1921 geeft -0,15 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "G EI > 2,7
    1976 of ouder – 0,15 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[],
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

    assert aantal_per_naam(groep) == {"Bouwjaar 1921": 3.67}
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

    Bron: wettekst, Bijlage I onder B, onderdeel 4.2: "Indien de woonruimte
    bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
    of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
    rubriek geen minpunten toegekend. Voor energielabel E, F en G en daaraan
    gelijkgestelde Energie-indexen en bouwjaren, geldt in afwijking van de
    bovenstaande tabellen in dat geval een toekenning van nul punten."

    De eenheid heeft geen energieprestaties. De package waarschuwt daarvoor en
    waardeert op het bouwjaar.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bouwjaar 1921 geeft zonder de uitzondering -0,15 punt per m².

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1, tabel met de kolommen
    energieprestatie, energie-index, bouwjaar en punten per m²: "Indien geen
    energielabel of EI beschikbaar is, wordt gewaardeerd met het bouwjaar" en
    "G EI > 2,7 1976 of ouder – 0,15 punt".

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
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

    assert aantal_per_naam(groep) == {"Bouwjaar 1921": 3.67}
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

    Bron: wettekst, Bijlage I onder B, onderdeel 4.2: "Indien de woonruimte
    bestaat uit of deel uitmaakt van een rijksmonument, een provinciaal monument
    of een gemeentelijke monument als bedoeld in artikel 8a worden voor deze
    rubriek geen minpunten toegekend. Voor energielabel E, F en G en daaraan
    gelijkgestelde Energie-indexen en bouwjaren, geldt in afwijking van de
    bovenstaande tabellen in dat geval een toekenning van nul punten."

    De punten komen hier uit de energieprestatievergoeding: 0,50 punt per m².

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.6.3: "Bij een EPV wordt
    de energieprestatie daarom gewaardeerd met een 0,50 punt per m2."

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1921,
        monumenten=[Eenheidmonument.rijksmonument],
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

    assert aantal_per_naam(groep) == {"Energieprestatievergoeding": 3.67}
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

    Bron: beleidsboek onzelfstandige woonruimten, 2.4.6.3: "Bij een EPV wordt
    de energieprestatie daarom gewaardeerd met een 0,50 punt per m2."

    Bijlage I onder B van de wettekst heeft geen onderdeel over de
    energieprestatievergoeding. De toelichting bij Bijlage I onder A, die voor
    onzelfstandige woonruimten van overeenkomstige toepassing is, noemt een vast
    aantal punten per woning. De package volgt het beleidsboek; de test legt
    dat gedrag vast.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 4.3: "In die gevallen
    wordt de energieprestatie met 32 punten voor een ééngezinswoning en 28
    punten voor meergezins- en duplexwoningen."

    De m² zijn die van de vertrekken die aan de huurder zijn toe te rekenen:
    elk gemeenschappelijk vertrek gedeeld door het aantal onzelfstandige
    woonruimten, onafgerond opgeteld.

    Bron: wettekst, Bijlage I onder B, onderdeel 4.1: "Punten per m² die
    volgens rubriek 1 zijn toe te rekenen aan de huurder".

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4: volgens
    rubriek 1 toe te rekenen "is de onafgeronde toerekening (eerst delen, dan
    salderen), niet het afgeronde puntenresultaat van rubriek 1."
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

    assert aantal_per_naam(groep) == {"Energieprestatievergoeding": 3.67}
    assert punten_per_naam(groep) == {
        "Energieprestatievergoeding": 1.83,
        "Afronding op kwartpunten": -0.08,
    }
    assert groep.punten == 1.75
    vergelijk_met_testreferentie(eenheid, groep)
