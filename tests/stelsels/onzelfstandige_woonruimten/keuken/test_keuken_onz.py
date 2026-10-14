"""Keuken, onzelfstandige woonruimten (rubriek 5)."""

import pytest

from tests.input import aanrecht, badkamer, element, ruimte
from tests.utils import (
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Keuken,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def keuken(peildatum):
    return Keuken(peildatum=peildatum)


def test_Keuken_output(onzelfstandige_woonruimten_input_en_outputmodel, peildatum):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Keuken,
    )


# Lengte van het aanrecht


def test_punten_voor_de_lengte_van_het_aanrecht(keuken, vergelijk_met_testreferentie):
    """Een aanrecht van 1 meter krijgt 4 punten, een van 2 meter 7 punten en een van 3,5 meter 10 punten.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "1 tot 2 m 4 punten",
    "2 tot 3 m 7 punten" en "3 m en meer 10 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken1", elementen=[aanrecht(1000)]
            ),
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken2", elementen=[aanrecht(2000)]
            ),
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken3", elementen=[aanrecht(3500)]
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Keuken1": {"Lengte aanrecht": 4.0},
        "Keuken2": {"Lengte aanrecht": 7.0},
        "Keuken3": {"Lengte aanrecht": 10.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_van_5500mm_krijgt_13_punten_in_een_keuken_gedeeld_met_8_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 5,5 meter krijgt 13 punten als de keuken met 8 onzelfstandige woonruimten wordt gedeeld.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "5 m en meer (indien er
    minimaal 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot
    deze keuken) 13 punten" en "De hieronder weergegeven punten dienen te
    worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(5500)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # 13 punten gedeeld door 8 woonruimten is 1,625 punt: in het rapport 1,63
    # en afgerond op kwartpunten 1,75.
    assert punten_per_naam(groep)["Lengte aanrecht"] == 1.63
    assert groep.punten == 1.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_van_5500mm_krijgt_10_punten_in_een_keuken_gedeeld_met_7_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 5,5 meter krijgt 10 punten als de keuken met 7 onzelfstandige woonruimten wordt gedeeld.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten",
    "5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
    gebruiksrecht hebben tot deze keuken) 13 punten" en "De hieronder
    weergegeven punten dienen te worden gedeeld door het aantal onzelfstandige
    woonruimten dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(5500)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=7,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # 10 punten gedeeld door 7 woonruimten is 1,43 punt, afgerond op kwartpunten
    # 1,5; 13 punten zouden 1,86 punt geven.
    assert punten_per_naam(groep)["Lengte aanrecht"] == 1.43
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_van_5500mm_krijgt_10_punten_in_een_privekeuken(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 5,5 meter krijgt in een privékeuken 10 punten.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten"
    en "5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
    gebruiksrecht hebben tot deze keuken) 13 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(5500)])]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Lengte aanrecht": 10.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_van_3001mm_krijgt_10_punten_in_een_keuken_gedeeld_met_8_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van net iets meer dan 3 meter krijgt 10 punten, ook in een keuken die met 8 onzelfstandige woonruimten wordt gedeeld.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten",
    "5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
    gebruiksrecht hebben tot deze keuken) 13 punten" en "De hieronder
    weergegeven punten dienen te worden gedeeld door het aantal onzelfstandige
    woonruimten dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(3001)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # 10 punten gedeeld door 8 woonruimten; 13 punten zouden 1,63 punt geven.
    assert punten_per_naam(groep) == {"Lengte aanrecht": 1.25}
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_korter_dan_1m_krijgt_geen_punten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht korter dan 1 meter krijgt geen punten.

    De package geeft daarbij een waarschuwing: de keuken heeft geen aanrecht
    van minimaal 1 meter.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "Minder dan 1 m 0 punten".

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(900)])]
    )

    with pytest.warns(UserWarning, match="geen aanrecht") as waarschuwingen:
        groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


@pytest.mark.parametrize(
    ("aanrechten", "aantal_woonruimten"),
    [
        pytest.param([], None, id="geen_aanrecht"),
        pytest.param(
            [],
            2,
            id="geen_aanrecht_in_een_gedeelde_keuken",
            marks=pytest.mark.toelichting(
                "de keuken wordt met 2 onzelfstandige woonruimten gedeeld."
            ),
        ),
        pytest.param(
            [element(Bouwkundigelementdetailsoort.aanrecht)],
            None,
            id="alleen_een_aanrecht_zonder_lengte",
            marks=pytest.mark.toelichting(
                "het enige aanrecht heeft geen lengte en telt daarom niet als aanrecht."
            ),
        ),
        pytest.param(
            [element(Bouwkundigelementdetailsoort.aanrecht)],
            2,
            id="alleen_een_aanrecht_zonder_lengte_in_een_gedeelde_keuken",
            marks=pytest.mark.toelichting(
                "het enige aanrecht heeft geen lengte en telt daarom niet als "
                "aanrecht; de keuken wordt met 2 onzelfstandige woonruimten gedeeld."
            ),
        ),
    ],
)
def test_keuken_zonder_aanrecht_geeft_een_waarschuwing(
    keuken, vergelijk_met_testreferentie, aanrechten, aantal_woonruimten
):
    """Een keuken zonder aanrecht is incomplete input en wordt niet gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Indien de keuken
    niet voldoet aan het basisniveau, worden geen punten toegekend."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=aanrechten,
                gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_woonruimten,
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen aanrecht") as waarschuwingen:
        groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_aanrecht_zonder_lengte_geeft_een_waarschuwing(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht zonder lengte is incomplete input.

    De keuken wordt gewaardeerd op het aanrecht dat wel een lengte heeft.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(2000, id="aanrecht_1"),
                    element(Bouwkundigelementdetailsoort.aanrecht, id="aanrecht_2"),
                ],
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen lengte") as waarschuwingen:
        groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Lengte aanrecht": 7.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Meer dan één aanrecht


def test_kort_aanrechtdeel_telt_mee_naast_een_aanrecht_vanaf_1m(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrechtdeel korter dan 1 meter telt mee in de aanrechtlengte naast een aanrecht vanaf 1 meter.

    De keuken wordt met 4 onzelfstandige woonruimten gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2: "Als een
    ruimte meerdere `aanrecht`-elementen bevat, telt de package hun lengtes bij
    elkaar op voordat de puntentabel wordt toegepast. Een deel korter dan 1
    meter telt daarbij mee zodra in dezelfde ruimte ook een aanrechtdeel van
    minimaal 1 meter aanwezig is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="kort_aanrecht"),
                    aanrecht(1200, id="lang_aanrecht"),
                ],
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # Samen 2 meter: 7 punten, gedeeld door 4 woonruimten. Zonder het korte
    # deel zou het aanrecht van 1,2 meter 4 punten krijgen, gedeeld 1,0.
    assert punten_per_naam(groep) == {"Totale aanrechtlengte": 1.75}
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_voor_extra_voorzieningen_volgt_uit_de_opgetelde_aanrechtlengte(
    keuken, vergelijk_met_testreferentie
):
    """Bij meer dan één aanrecht volgt het maximum voor extra voorzieningen uit de opgetelde aanrechtlengte.

    De keuken wordt met 2 onzelfstandige woonruimten gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.3: "Bij
    meerdere `aanrecht`-elementen in dezelfde ruimte wordt deze maximering
    gebaseerd op de basispunten uit de gesommeerde aanrechtlengte."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                *[Installatiesoort.inbouw_koelkast] * 8,
                elementen=[
                    aanrecht(1500, id="aanrecht_1"),
                    aanrecht(900, id="aanrecht_2"),
                ],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # Samen 2,4 meter: 7 punten, dus van de 8 punten voor koelkasten gaat er 1
    # af; alles gedeeld door 2 woonruimten. Met alleen het aanrecht van 1,5
    # meter (4 punten) zou de aftrek 4 punten zijn, gedeeld 2,0.
    assert punten_per_naam(groep) == {
        "Totale aanrechtlengte": 3.5,
        Installatiesoort.inbouw_koelkast.naam: 4.0,
        "Maximaal evenveel punten als aanrecht": -0.5,
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Extra voorzieningen


def test_twee_inbouwkoelkasten_krijgen_elk_een_punt(
    keuken, vergelijk_met_testreferentie
):
    """Twee inbouwkoelkasten in een keuken krijgen elk 1 punt.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Inbouw koelkast 1 punt".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_koelkast,
                elementen=[aanrecht(1000)],
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep)[Installatiesoort.inbouw_koelkast.naam] == 2.0
    assert groep.punten == 6.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_koelvriescombinatie_krijgt_de_punten_van_koelkast_en_vrieskast(
    keuken, vergelijk_met_testreferentie
):
    """Een inbouw koelvriescombinatie krijgt de punten van een koelkast en een vrieskast samen.

    De keuken wordt met 2 onzelfstandige woonruimten gedeeld.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 5.2: "Wanneer een
    object twee voorzieningen heeft, bijvoorbeeld een ingebouwde combi
    magnetron/oven of een gecombineerde koel- en vrieskast, worden beide
    voorzieningen in dit object gewaardeerd conform de rubriek."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Inbouw koelkast 1 punt"
    en "Inbouw vrieskast 0,75 punt".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_koelvriescombinatie,
                elementen=[aanrecht(2500)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # Samen 1,75 punt, gedeeld door 2 woonruimten 0,875: in het rapport 0,88.
    # Met de 3,5 punt voor het aanrecht is het totaal 4,375, afgerond op
    # kwartpunten 4,5.
    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.inbouw_koelvriescombinatie.naam] == 0.88
    assert groep.punten == 4.5
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    ("aantal_koelkasten", "verwachte_punten"),
    [
        pytest.param(
            2,
            {
                "Lengte aanrecht": 4.0,
                Installatiesoort.inbouw_koelkast.naam: 2.0,
                Installatiesoort.inbouw_oven_elektrisch.naam: 1.0,
            },
            id="3_punten_aan_voorzieningen",
        ),
        pytest.param(
            4,
            {
                "Lengte aanrecht": 4.0,
                Installatiesoort.inbouw_koelkast.naam: 4.0,
                Installatiesoort.inbouw_oven_elektrisch.naam: 1.0,
                "Maximaal evenveel punten als aanrecht": -1.0,
            },
            id="5_punten_aan_voorzieningen",
        ),
    ],
)
def test_extra_voorzieningen_krijgen_hooguit_de_punten_van_het_aanrecht(
    keuken, vergelijk_met_testreferentie, aantal_koelkasten, verwachte_punten
):
    """Extra voorzieningen krijgen samen hooguit de punten van het aanrecht.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Voorzieningen (tot
    maximaal het aantal punten extra dat voor de lengte van het aanrecht is
    verkregen)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                *[Installatiesoort.inbouw_koelkast] * aantal_koelkasten,
                Installatiesoort.inbouw_oven_elektrisch,
                elementen=[aanrecht(1000)],
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    (
        "lengte_mm",
        "aantal_woonruimten",
        "aantal_koelkasten",
        "punten_aanrecht",
        "punten_koelkasten",
        "totaal",
    ),
    [
        pytest.param(
            3500,
            2,
            8,
            5.0,
            4.0,
            9.0,
            id="aanrecht_van_10_punten",
            marks=pytest.mark.toelichting(
                "de 8 punten voor koelkasten blijven onder de 10 punten van het "
                "aanrecht; bij een maximum van 7 punten zou er 1 punt afgaan. "
                "De keuken wordt met 2 onzelfstandige woonruimten gedeeld."
            ),
        ),
        # 13 en 12 punten gedeeld door 8 woonruimten: 1,625 (in het rapport
        # 1,63) en 1,5 punt, samen 3,125 en afgerond op kwartpunten 3,25.
        pytest.param(
            5500,
            8,
            12,
            1.63,
            1.5,
            3.25,
            id="aanrecht_van_13_punten",
            marks=pytest.mark.toelichting(
                "de 12 punten voor koelkasten blijven onder de 13 punten van het "
                "aanrecht; bij een maximum van 10 punten zouden er 2 punten "
                "afgaan. De keuken wordt met 8 onzelfstandige woonruimten gedeeld."
            ),
        ),
    ],
)
def test_maximum_voor_extra_voorzieningen_stijgt_mee_met_de_punten_van_het_aanrecht(
    keuken,
    vergelijk_met_testreferentie,
    lengte_mm,
    aantal_woonruimten,
    aantal_koelkasten,
    punten_aanrecht,
    punten_koelkasten,
    totaal,
):
    """Het maximum voor extra voorzieningen stijgt mee met de punten voor een aanrecht langer dan 3 meter.

    De toelichting onder A (rubriek 5.2) kent extra punten toe "tot maximaal
    zeven punten indien het aanrecht op basis van rubriek 5.1. een lengte heeft
    van 2 m of meer". De package volgt de tabel onder B, waarin het aanrecht 10
    of 13 punten kan krijgen en de voorzieningen tot dat aantal meetellen.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Voorzieningen (tot
    maximaal het aantal punten extra dat voor de lengte van het aanrecht is
    verkregen)".

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten"
    en "5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
    gebruiksrecht hebben tot deze keuken) 13 punten".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 5: "Ook geldt dat
    een aanrecht tot 3 meter gewaardeerd kan worden tot 10 punten, in afwijking
    van het maximum van 7 punten (tot 2 meter) onder de bijlage I, onder A."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                *[Installatiesoort.inbouw_koelkast] * aantal_koelkasten,
                elementen=[aanrecht(lengte_mm)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_woonruimten,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten["Lengte aanrecht"] == punten_aanrecht
    assert punten[Installatiesoort.inbouw_koelkast.naam] == punten_koelkasten
    assert "Maximaal evenveel punten als aanrecht" not in punten
    assert groep.punten == totaal
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    ("aantal_woonruimten", "punten_aanrecht"),
    [
        pytest.param(None, 4.0, id="privekeuken"),
        pytest.param(
            2,
            2.0,
            id="gedeelde_keuken",
            marks=pytest.mark.toelichting(
                "de keuken wordt met 2 onzelfstandige woonruimten gedeeld; de "
                "badkamer is privé."
            ),
        ),
    ],
)
def test_extra_voorzieningen_in_een_ruimte_zonder_aanrecht_krijgen_geen_punten(
    keuken, vergelijk_met_testreferentie, aantal_woonruimten, punten_aanrecht
):
    """Extra voorzieningen in een ruimte zonder aanrecht krijgen geen punten.

    Bron: beleidsboek onzelfstandige woonruimten, 2.5.3: "Een ruimte die
    beschikt over de basisvoorzieningen voor een keuken kan ook extra punten
    voor voorzieningen in de keuken krijgen."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_woonruimten,
            ),
            badkamer(
                Installatiesoort.inbouw_koelkast, Installatiesoort.inbouw_koelkast
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.keuken.naam: {"Lengte aanrecht": punten_aanrecht}
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Aanrecht buiten de keuken


def test_vertrek_met_aanrecht_telt_als_keuken(keuken, vergelijk_met_testreferentie):
    """Een vertrek telt voor de keuken mee zodra er een aanrecht in staat.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.1: "Rubriek 5
    stelt eisen aan de keuken zelf, niet aan de ruimte waarin die ligt. Een
    aanrecht telt daarom in elke ruimte mee."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer_en_of_keuken, elementen=[aanrecht(2000)]
            ),
            ruimte(Ruimtedetailsoort.woonkamer, elementen=[aanrecht(1000)]),
            ruimte(Ruimtedetailsoort.woon_en_of_slaapkamer, elementen=[aanrecht(2000)]),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                elementen=[aanrecht(1000)],
            ),
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer2"),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.woonkamer_en_of_keuken.naam: {"Lengte aanrecht": 7.0},
        Ruimtedetailsoort.woonkamer.naam: {"Lengte aanrecht": 4.0},
        Ruimtedetailsoort.woon_en_of_slaapkamer.naam: {"Lengte aanrecht": 7.0},
        "Slaapkamer1": {"Lengte aanrecht": 4.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Gemeenschappelijke keuken


def test_punten_voor_het_aanrecht_worden_gedeeld_door_het_aantal_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """De punten voor het aanrecht worden gedeeld door het aantal onzelfstandige woonruimten waarmee de keuken wordt gedeeld.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "De hieronder weergegeven
    punten dienen te worden gedeeld door het aantal onzelfstandige woonruimten
    dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken1",
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken2",
                elementen=[aanrecht(2000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken3",
                elementen=[aanrecht(3001)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken4",
                elementen=[aanrecht(3001)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Keuken1": {"Lengte aanrecht": 2.0},
        "Keuken2": {"Lengte aanrecht": 3.5},
        "Keuken3": {"Lengte aanrecht": 5.0},
        "Keuken4": {"Lengte aanrecht": 1.25},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_in_een_keuken_gedeeld_met_2_woonruimten_krijgen_de_helft_van_hun_punten(
    keuken, vergelijk_met_testreferentie
):
    """In een keuken die met 2 onzelfstandige woonruimten wordt gedeeld, krijgen extra voorzieningen de helft van hun punten.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "De hieronder weergegeven
    punten dienen te worden gedeeld door het aantal onzelfstandige woonruimten
    dat toegang en gebruiksrecht heeft" en "Inbouw koelkast 1 punt".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_koelkast,
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep)[Installatiesoort.inbouw_koelkast.naam] == 1.0
    assert groep.punten == 3.0
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    ("aantal_koelkasten", "verwachte_punten"),
    [
        pytest.param(
            2,
            {
                "Lengte aanrecht": 2.0,
                Installatiesoort.inbouw_koelkast.naam: 1.0,
                Installatiesoort.inbouw_oven_elektrisch.naam: 0.5,
            },
            id="3_punten_aan_voorzieningen",
        ),
        pytest.param(
            4,
            {
                "Lengte aanrecht": 2.0,
                Installatiesoort.inbouw_koelkast.naam: 2.0,
                Installatiesoort.inbouw_oven_elektrisch.naam: 0.5,
                "Maximaal evenveel punten als aanrecht": -0.5,
            },
            id="5_punten_aan_voorzieningen",
        ),
    ],
)
def test_extra_voorzieningen_in_een_gedeelde_keuken_krijgen_hooguit_de_punten_van_het_aanrecht(
    keuken, vergelijk_met_testreferentie, aantal_koelkasten, verwachte_punten
):
    """Ook in een gedeelde keuken krijgen extra voorzieningen samen hooguit de punten van het aanrecht.

    De keuken wordt met 2 onzelfstandige woonruimten gedeeld. De id van een
    geval noemt de punten voor extra voorzieningen vóór de deling.

    Bron: beleidsboek onzelfstandige woonruimten, 2.5.3: "Het aantal punten
    voor de extra voorzieningen kan niet meer zijn dan het aantal punten voor de
    basisvoorzieningen (de aanrechtlengte). Als het aantal punten voor de extra
    voorzieningen hoger uitvalt, dan wordt dit afgetopt. De toegekende punten
    worden gedeeld door het aantal onzelfstandige woningen dat toegang en
    gebruiksrecht heeft."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                *[Installatiesoort.inbouw_koelkast] * aantal_koelkasten,
                Installatiesoort.inbouw_oven_elektrisch,
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


def test_punten_voor_een_aanrecht_worden_per_vertrek_gedeeld_door_het_eigen_aantal_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Staat het aanrecht in gedeelde vertrekken, dan worden de punten per vertrek gedeeld door het aantal onzelfstandige woonruimten waarmee dat vertrek wordt gedeeld.

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
    adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
    een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
    aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
    het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
    toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
    voorziening(en)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer_en_of_keuken,
                elementen=[aanrecht(2000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.woon_en_of_slaapkamer,
                elementen=[aanrecht(2000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.woonkamer_en_of_keuken.naam: {"Lengte aanrecht": 3.5},
        Ruimtedetailsoort.woonkamer.naam: {"Lengte aanrecht": 2.0},
        Ruimtedetailsoort.woon_en_of_slaapkamer.naam: {"Lengte aanrecht": 1.75},
        "Slaapkamer1": {"Lengte aanrecht": 1.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)
