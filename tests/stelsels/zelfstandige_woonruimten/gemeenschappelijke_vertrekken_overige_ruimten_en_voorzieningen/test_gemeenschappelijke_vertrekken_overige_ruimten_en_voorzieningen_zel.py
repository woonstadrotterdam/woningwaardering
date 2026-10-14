"""Gemeenschappelijke vertrekken, overige ruimten en voorzieningen, zelfstandige woonruimten (rubriek 9)."""

import pytest

from tests.input import aanrecht, element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen import (
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen(peildatum):
    return GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=peildatum
    )


def test_GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
    )


# Oppervlakte


def test_gemeenschappelijk_vertrek_krijgt_1_punt_per_m2_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijk vertrek krijgt 1 punt per m², gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft."

    Het totaal van de rubriek wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10,
                gedeeld_met_aantal_adressen=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10,
                gedeeld_met_aantal_adressen=6,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 5 adressen": {"Oppervlakte van vertrekken": 2.0},
        # 10 punten gedeeld door 6 adressen is 1,666… punt: in het rapport 1,67.
        "Gedeeld met 6 adressen": {"Oppervlakte van vertrekken": 1.67},
        # Samen 3,67 punten, afgerond op kwartpunten 3,75.
        None: {"Afronding op kwartpunten": 0.08},
    }
    assert groep.punten == 3.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_overige_ruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijke overige ruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke overige
    ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging1",
                oppervlakte=10,
                gedeeld_met_aantal_adressen=5,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging2",
                oppervlakte=10,
                gedeeld_met_aantal_adressen=6,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 5 adressen": {"Oppervlakte van overige ruimten": 1.5},
        "Gedeeld met 6 adressen": {"Oppervlakte van overige ruimten": 1.25},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_toiletruimte_wordt_als_overige_ruimte_gewaardeerd(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijke toiletruimte wordt als overige ruimte gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Een toiletruimte
    wordt gewaardeerd als overige ruimte als het voldoet aan de voorwaarden van
    een overige ruimte."

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke overige
    ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                naam="Toiletruimte1",
                oppervlakte=10,
                gedeeld_met_aantal_adressen=5,
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                naam="Toiletruimte2",
                oppervlakte=10,
                gedeeld_met_aantal_adressen=6,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 5 adressen": {"Oppervlakte van overige ruimten": 1.5},
        "Gedeeld met 6 adressen": {"Oppervlakte van overige ruimten": 1.25},
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Kasten


def test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijk_vertrek(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijk vertrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Meting van de
    oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van
    1,50 meter boven de vloer, inclusief de oppervlakte van alle tot de woning
    behorende losse en vaste kasten."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=2)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10,
                verbonden_ruimten=[kast],
                gedeeld_met_aantal_adressen=2,
            )
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert aantal_per_naam(groep) == {"Woonkamer (+1 kast)": 12.0}
    assert punten_per_naam(groep) == {"Oppervlakte van vertrekken": 6.0}
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    (
        "oppervlakte_berging",
        "oppervlakte_met_kast",
        "verwachte_punten",
        "verwacht_totaal",
    ),
    [
        pytest.param(
            8.0,
            10.0,
            {"Oppervlakte van overige ruimten": 3.75},
            3.75,
            id="berging_van_8m2",
        ),
        pytest.param(
            3.0,
            5.0,
            {
                "Oppervlakte van overige ruimten": 1.88,
                "Afronding op kwartpunten": 0.12,
            },
            2.0,
            id="berging_van_3m2",
            marks=pytest.mark.toelichting(
                "de 5 m² geeft 3,75 punten; gedeeld door 2 adressen is dat 1,875 "
                "punt, in het rapport 1,88. Dat is precies een achtste punt boven "
                "1,75 en wordt naar boven afgerond op 2 punten."
            ),
        ),
    ],
)
def test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijke_overige_ruimte(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
    oppervlakte_berging,
    oppervlakte_met_kast,
    verwachte_punten,
    verwacht_totaal,
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijke overige ruimte.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
    oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
    boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
    woning behorende kasten".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke overige
    ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft."

    Het totaal van de rubriek wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=2)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=oppervlakte_berging,
                verbonden_ruimten=[kast],
                gedeeld_met_aantal_adressen=2,
            )
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert aantal_per_naam(groep) == {"Berging (+1 kast)": oppervlakte_met_kast}
    assert punten_per_naam(groep) == verwachte_punten
    assert groep.punten == verwacht_totaal
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte zonder vaste trap


def test_aftrek_voor_gemeenschappelijke_zolder_zonder_vaste_trap_wordt_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De aftrek van 5 punten voor een gemeenschappelijke zolder zonder vaste trap wordt gedeeld door het aantal adressen dat toegang heeft.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
    ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Is er een
    `vlizotrap` en geen `trap`, dan geldt daarbij de puntenaftrek van 2.2.2.3."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=16,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {
        # 22 m² is 16,5 punten, gedeeld door 2 adressen.
        "Subtotaal": 8.25,
        "Correctie: zolder zonder vaste trap": -2.5,
    }
    assert groep.punten == 5.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_aftrek_is_niet_hoger_dan_de_punten_voor_de_gemeenschappelijke_zolder(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De aftrek voor een gemeenschappelijke zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd, doch niet met meer punten dan voor de
    oppervlakte van de zolderruimten wordt gegeven." en "Waardering in punten
    vindt na saldering en afronding plaats."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
    ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=6.33,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {
        # 12,33 m² is afgerond 12 m² en 9 punten, gedeeld door 2 adressen.
        "Subtotaal": 4.5,
        # De zolder brengt het totaal van 6 op 12 hele m²; de 4,5 punten
        # daarvoor vervallen, gedeeld door 2 adressen.
        "Correctie: zolder zonder vaste trap": -2.25,
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijke_zolder_zonder_vaste_trap(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijke zolder zonder vaste trap.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
    oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
    boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
    woning behorende kasten" en "Indien geen vaste trap aanwezig is, wordt het
    aantal punten van de vloeroppervlakte van de zolderruimte met vijf
    verminderd, doch niet met meer punten dan voor de oppervlakte van de
    zolderruimten wordt gegeven."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
    ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.9)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=2.6,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                verbonden_ruimten=[kast],
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert aantal_per_naam(groep) == {
        "Subtotaal": 9.5,
        Ruimtedetailsoort.berging.naam: 6.0,
        "Zolder (+1 kast)": 3.5,
    }
    assert punten_per_naam(groep) == {
        # 9,5 m² is afgerond 10 m² en 7,5 punten, gedeeld door 2 adressen.
        "Subtotaal": 3.75,
        # Met haar kast brengt de zolder het totaal van 6 op 10 hele m²; de 3
        # punten daarvoor vervallen, gedeeld door 2 adressen. Zonder de kast
        # zou het totaal 9 hele m² zijn en de aftrek 1,125 punt.
        "Correctie: zolder zonder vaste trap": -1.5,
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


# Verwarming


def test_verwarmd_gemeenschappelijk_vertrek_krijgt_2_punten_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een verwarmd gemeenschappelijk vertrek krijgt 2 punten, gedeeld door het aantal adressen dat toegang heeft.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal de punten
    voor verkoeling en verwarming conform rubriek 3;" en "Deel dit aantal punten
    door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten".

    In het totaal zitten ook de punten voor de oppervlakte van beide vertrekken;
    het wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft."

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=10,
                verwarmd=True,
                gedeeld_met_aantal_adressen=5,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10,
                verwarmd=True,
                gedeeld_met_aantal_adressen=6,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep)["Verwarmde vertrekken"] == {
        Ruimtedetailsoort.slaapkamer.naam: 0.4,
        # 2 punten gedeeld door 6 adressen is 0,333… punt: in het rapport 0,33.
        Ruimtedetailsoort.woonkamer.naam: 0.33,
    }
    # Met 2 en 1,67 punten voor de oppervlakte samen 4,4 punten, afgerond op
    # kwartpunten 4,5.
    assert groep.punten == 4.5
    vergelijk_met_testreferentie(eenheid, groep)


# Keuken


def test_punten_voor_keuken_in_gemeenschappelijke_ruimte_worden_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De punten voor een keuken in een gemeenschappelijke ruimte worden gedeeld door het aantal adressen dat toegang heeft.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal eventueel
    van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7;" en "Deel
    dit aantal punten door het aantal adressen dat toegang heeft tot de
    gemeenschappelijke binnenruimten."

    De keuken heeft een aanrecht van 1 meter en twee inbouwkoelkasten.

    Bron: wettekst, Bijlage I onder A, onderdeel 5.1: "1 tot 2 m 4 punten".

    Bron: wettekst, Bijlage I onder A, onderdeel 5.2: "Inbouw koelkast 1 punt".

    In het totaal zitten ook de punten voor de oppervlakte en de verwarming van
    de keuken; het wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft."

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten".

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_koelkast,
                elementen=[aanrecht(1000)],
                oppervlakte=10,
                verwarmd=True,
                gedeeld_met_aantal_adressen=5,
            )
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.keuken.naam] == {"Lengte aanrecht": 0.8}
    assert punten["Extra voorzieningen"] == {Installatiesoort.inbouw_koelkast.naam: 0.4}
    # Met 2 punten voor de oppervlakte en 0,4 punt voor de verwarming samen 3,6
    # punten, afgerond op kwartpunten 3,5.
    assert groep.punten == 3.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_keuken_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_vertrek_gewaardeerd(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een keuken die als gemeenschappelijke ruimte is aangeleverd, wordt als vertrek gewaardeerd.

    De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
    ruimtesoort waarmee de keuken is gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
    bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
    badkamer of doucheruimte altijd een vertrek."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2:
    "Uitzonderingen: keuken, badkamer en doucheruimte zijn volgens het
    beleidsboek altijd een vertrek, en zo waarderen wij die ook, los van het
    meegegeven `Ruimtesoort`."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Als vertrek krijgt de keuken 1 punt per m² en 2 punten voor verwarming, elk
    gedeeld door het aantal adressen.

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft."

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Het aanrecht van 2 meter telt ook in een ruimte met deze ruimtesoort mee
    voor de keuken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1: "Rubriek 5
    stelt eisen aan de keuken zelf, niet aan de ruimte waarin die ligt. Een
    aanrecht telt daarom in elke ruimte mee."

    Bron: wettekst, Bijlage I onder A, onderdeel 5.1: "2 m en meer 7 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                soort=Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
                elementen=[aanrecht(2000)],
                oppervlakte=10,
                verwarmd=True,
                gedeeld_met_aantal_adressen=4,
            )
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
            eenheid
        )

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 4 adressen": {"Oppervlakte van vertrekken": 2.5},
        "Verwarmde vertrekken": {Ruimtedetailsoort.keuken.naam: 0.5},
        Ruimtedetailsoort.keuken.naam: {"Lengte aanrecht": 1.75},
    }
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Sanitair


def test_punten_voor_sanitair_in_gemeenschappelijke_ruimte_worden_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door het aantal adressen dat toegang heeft.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal eventueel
    van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7;" en "Deel
    dit aantal punten door het aantal adressen dat toegang heeft tot de
    gemeenschappelijke binnenruimten."

    De badkamer heeft een bad, een wastafel en extra voorzieningen. De maxima
    van rubriek 6 gelden vóór het delen.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Wastafel 1 punt" en "Bad
    6 punten".

    Bron: wettekst, Bijlage I onder A, onderdeel 6.2: "Voorzieningen in de bad-
    of doucheruimte (tot maximaal het aantal punten extra dat reeds voor douche,
    bad en bad/douche is verkregen)", "Bubbelfunctie van het bad 1,5 punten",
    "Gemonteerde volledige afscheiding van de douche 1,25 punten",
    "Handdoekenradiator 0,75 punt", "Ingebouwd kastje met in- of opgebouwde
    wastafel 1 punt", "Kastruimte (minimale breedte van 40 cm, en minimale
    hoogte van 40 cm) 0,75 punt (tot een maximum van 0,75)", "Stopcontact 0,25
    punt", "Éénhandsmengkraan 0,25 punt" en "Thermostatische mengkraan 0,5
    punt".

    In het totaal zitten ook de punten voor de oppervlakte van de badkamer; het
    wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft."

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad,
                Installatiesoort.wastafel,
                Installatiesoort.bubbelfunctie_van_het_bad,
                Installatiesoort.douchewand,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel,
                Installatiesoort.kastruimte,
                Installatiesoort.kastruimte,
                Installatiesoort.stopcontact_bij_wastafel,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.thermostatische_mengkraan,
                oppervlakte=10,
                gedeeld_met_aantal_adressen=2,
            )
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    # Elke waardering is de helft van de punten uit rubriek 6. Het rapport toont
    # twee decimalen: 0,625 staat er als 0,63, 0,375 als 0,38 en 0,125 als 0,13.
    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.badkamer.naam] == {
        Installatiesoort.wastafel.naam: 0.5,
        Installatiesoort.bad.naam: 3.0,
    }
    assert punten["Extra voorzieningen"] == {
        Installatiesoort.bubbelfunctie_van_het_bad.naam: 0.75,
        Installatiesoort.douchewand.naam: 0.63,
        Installatiesoort.handdoekenradiator.naam: 0.38,
        Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.naam: 0.5,
        # Twee kastruimtes van 0,75 punt, samen hooguit 0,75 punt.
        Installatiesoort.kastruimte.naam: 0.75,
        "Maximering voor Kastruimte": -0.38,
        Installatiesoort.stopcontact_bij_wastafel.naam: 0.13,
        Installatiesoort.eenhandsmengkraan.naam: 0.13,
        Installatiesoort.thermostatische_mengkraan.naam: 0.25,
        # De extra voorzieningen zijn samen 6,25 punten, een kwart punt meer dan
        # de 6 punten van het bad.
        "Max verdubbeling punten bad en douche": -0.13,
    }
    # 0,5 en 3 punten voor wastafel en bad, 3 punten voor de extra voorzieningen
    # en 5 punten voor de oppervlakte.
    assert groep.punten == 11.5
    vergelijk_met_testreferentie(eenheid, groep)


# Rekenvoorbeeld


def test_rekenvoorbeeld_met_keuken_en_toilet_uit_de_wettekst(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Het rekenvoorbeeld uit de wettekst: een keuken van 20 m² en een toilet van 2 m² die vier adressen delen, geven elk adres 9,50 punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "(A) een
    gemeenschappelijke binnenruimte met keuken van 20 m², en daarnaast (B) een
    gedeelde toiletruimte van 2 m². Tot beiden hebben 4 adressen toegang.",
    "4. Saldering levert op: 20 + 1,5 + 2 + 10 + 4,75 = 38,25. 5. Delen door
    het aantal adressen levert op: 38,25 punten / 4 = 9.5625 per adres. 6.
    Afronden geschiedt op een kwart punt per adres op 9,50."

    De 7 punten voor het aanrecht zijn in de input een aanrecht van 2.999 mm,
    de 3 punten voor de voorzieningen een inbouwkoelkast, een elektrische
    inbouwoven en een inbouwmagnetron.

    Bron: wettekst, Bijlage I onder A, onderdeel 5.1: "2 m en meer 7 punten".

    Bron: wettekst, Bijlage I onder A, onderdeel 5.2: "Inbouw koelkast 1 punt",
    "Inbouw oven elektrisch 1 punt" en "Inbouw magnetron 1 punt".

    De radiator is in de input een bouwkundig element van de keuken. De package
    leest de verwarming af aan `verwarmd`.

    Bron: implementatietoelichting datamodel-uitbreidingen, Verkoeld en
    verwarmd: "Hierom hebben wij twee boolean kenmerken toegevoegd aan
    `EenhedenRuimte`: `verwarmd` en `verkoeld`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_magnetron,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_oven_elektrisch,
                elementen=[
                    aanrecht(2999),
                    element(Bouwkundigelementdetailsoort.radiator),
                ],
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=4,
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                Installatiesoort.wastafel,
                Installatiesoort.hangend_toilet,
                oppervlakte=2,
                gedeeld_met_aantal_adressen=4,
            ),
        ]
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    # Elke waardering is een kwart van de punten uit het rekenvoorbeeld. Het
    # rapport toont twee decimalen.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 4 adressen": {
            "Oppervlakte van vertrekken": 5.0,
            # 1,5 punt gedeeld door 4 is 0,375 punt.
            "Oppervlakte van overige ruimten": 0.38,
        },
        "Verwarmde vertrekken": {Ruimtedetailsoort.keuken.naam: 0.5},
        Ruimtedetailsoort.keuken.naam: {"Lengte aanrecht": 1.75},
        "Extra voorzieningen": {
            Installatiesoort.inbouw_koelkast.naam: 0.25,
            Installatiesoort.inbouw_oven_elektrisch.naam: 0.25,
            Installatiesoort.inbouw_magnetron.naam: 0.25,
        },
        Ruimtedetailsoort.toiletruimte.naam: {
            # 3,75 punten gedeeld door 4 is 0,9375 punt.
            Installatiesoort.hangend_toilet.naam: 0.94,
            Installatiesoort.wastafel.naam: 0.25,
        },
        # De waarderingen in het rapport zijn samen 9,57 punten; het totaal van
        # 9,5625 punten wordt afgerond op kwartpunten 9,50.
        None: {"Afronding op kwartpunten": -0.07},
    }
    assert groep.punten == 9.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zorgwoning


def test_zorgwoning_krijgt_3_punten(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een zorgwoning krijgt 3 punten voor de gemeenschappelijke ruimten en voorzieningen.

    Bron: beleidsboek zelfstandige woonruimten, 2.9.4: "Om arbeidsintensief
    meetwerk te voorkomen kent de Huurcommissie in dat geval een waardering van
    3 punten per woning toe."

    De eenheid heeft de doelgroep zorg en alleen een eigen woonkamer; de
    gemeenschappelijke ruimten zijn niet meegegeven.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.4: "Dit
    voorbeeld toont hoe een zorgwoning wordt aangegeven door de doelgroep op
    'zorg' te zetten. Voor een zorgwoning hoeven de gemeenschappelijke ruimten
    en voorzieningen niet verder gespecificeerd te worden."
    """
    eenheid = EenhedenEenheid(
        doelgroep=Doelgroep.zorg,
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer)],
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {"Zorgwoning": 3.0}
    vergelijk_met_testreferentie(eenheid, groep)
