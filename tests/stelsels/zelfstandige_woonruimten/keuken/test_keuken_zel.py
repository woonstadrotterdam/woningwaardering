"""Keuken, zelfstandige woonruimten (rubriek 5)."""

import pytest

from tests.input import aanrecht, badkamer, element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import Keuken
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def keuken(peildatum):
    return Keuken(peildatum=peildatum)


def test_Keuken_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Keuken,
    )


# Lengte van het aanrecht


def test_punten_voor_de_lengte_van_het_aanrecht(keuken, vergelijk_met_testreferentie):
    """De punten voor een aanrecht hangen af van zijn lengte.

    Het beleidsboek (2.5.2) geeft de 7 punten aan een aanrecht "Langer dan 2
    meter". De package volgt de wettekst en geeft ze ook bij precies 2 meter.

    Bron: wettekst, Bijlage I onder A, onderdeel 5.1: "1 tot 2 m 4 punten" en
    "2 m en meer 7 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken1", elementen=[aanrecht(1000)]
            ),
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken2", elementen=[aanrecht(1999)]
            ),
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken3", elementen=[aanrecht(2000)]
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Keuken1": {"Lengte aanrecht": 4.0},
        "Keuken2": {"Lengte aanrecht": 4.0},
        "Keuken3": {"Lengte aanrecht": 7.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_korter_dan_1m_krijgt_geen_punten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht korter dan 1 meter krijgt geen punten.

    De package geeft daarbij twee waarschuwingen: de keuken heeft geen aanrecht
    van minimaal 1 meter, en de eenheid heeft daardoor geen keuken.

    Bron: wettekst, Bijlage I onder A, onderdeel 5.1: "Minder dan 1 m 0 punten".

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(999)])],
    )

    with pytest.warns(UserWarning, match="geen aanrecht") as waarschuwingen:
        groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


@pytest.mark.parametrize(
    "aanrechten",
    [
        pytest.param([], id="geen_aanrecht"),
        pytest.param(
            [element(Bouwkundigelementdetailsoort.aanrecht)],
            id="alleen_een_aanrecht_zonder_lengte",
            marks=pytest.mark.toelichting(
                "het enige aanrecht heeft geen lengte en telt daarom niet als aanrecht."
            ),
        ),
    ],
)
def test_keuken_zonder_aanrecht_geeft_een_waarschuwing(
    keuken, vergelijk_met_testreferentie, aanrechten
):
    """Een keuken zonder aanrecht is incomplete input en wordt niet gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Indien de keuken
    niet voldoet aan het basisniveau, worden geen punten toegekend."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=aanrechten)],
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


def test_bouwkundig_element_zonder_detailsoort_geeft_een_waarschuwing(
    keuken, vergelijk_met_testreferentie
):
    """Een bouwkundig element zonder detailsoort is incomplete input en wordt niet gewaardeerd.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(2000, id="aanrecht_1"),
                    BouwkundigElementenBouwkundigElement(
                        id="aanrecht_2", naam="Aanrecht", lengte=2000
                    ),
                ],
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen detailsoort") as waarschuwingen:
        groep = keuken.waardeer(eenheid)

    # Telde het element van 2000 mm mee, dan stond hier een "Totale
    # aanrechtlengte" van 4000 mm.
    assert aantal_per_naam(groep) == {"Lengte aanrecht": 2000.0}
    assert punten_per_naam(groep) == {"Lengte aanrecht": 7.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Meer dan één aanrecht


def test_kort_aanrechtdeel_telt_mee_naast_een_aanrecht_vanaf_1m(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrechtdeel korter dan 1 meter telt mee in de aanrechtlengte naast een aanrecht vanaf 1 meter.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.2: "Als een
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
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Totale aanrechtlengte": 7.0}
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    "lengtes_mm",
    [
        pytest.param((1000, 1000), id="twee_aanrechten_van_1m"),
        pytest.param((1500, 900), id="kort_aanrechtdeel_van_900mm"),
        pytest.param((1500, 600), id="kort_aanrechtdeel_van_600mm"),
    ],
)
def test_maximum_voor_extra_voorzieningen_volgt_uit_de_opgetelde_aanrechtlengte(
    keuken, vergelijk_met_testreferentie, lengtes_mm
):
    """Bij meer dan één aanrecht volgt het maximum voor extra voorzieningen uit de opgetelde aanrechtlengte.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.3: "Bij
    meerdere `aanrecht`-elementen in dezelfde ruimte wordt deze maximering
    gebaseerd op de basispunten uit de gesommeerde aanrechtlengte."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                *[Installatiesoort.inbouw_koelkast] * 8,
                elementen=[
                    aanrecht(lengte_mm, id=f"aanrecht_{nummer}")
                    for nummer, lengte_mm in enumerate(lengtes_mm, start=1)
                ],
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Totale aanrechtlengte": 7.0,
        Installatiesoort.inbouw_koelkast.naam: 8.0,
        "Maximaal evenveel punten als aanrecht": -1.0,
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Extra voorzieningen


def test_twee_inbouwkoelkasten_krijgen_elk_een_punt(
    keuken, vergelijk_met_testreferentie
):
    """Twee inbouwkoelkasten in een keuken krijgen elk 1 punt.

    Bron: wettekst, Bijlage I onder A, onderdeel 5.2: "Inbouw koelkast 1 punt".
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Wanneer een
    object twee voorzieningen heeft, bijvoorbeeld een ingebouwde combi
    magnetron/oven of een gecombineerde koel- en vrieskast, worden beide
    voorzieningen in dit object gewaardeerd conform de rubriek."

    Bron: wettekst, Bijlage I onder A, onderdeel 5.2: "Inbouw koelkast 1 punt"
    en "Inbouw vrieskast 0,75 punt".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_koelvriescombinatie,
                elementen=[aanrecht(2500)],
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.inbouw_koelvriescombinatie.naam] == 1.75
    assert groep.punten == 8.75
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

    Bron: wettekst, Bijlage I onder A, onderdeel 5.2: "Voorzieningen (tot
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


def test_rekenvoorbeeld_extra_voorzieningen_uit_het_beleidsboek(
    keuken, vergelijk_met_testreferentie
):
    """Het rekenvoorbeeld van het beleidsboek: de extra voorzieningen worden afgetopt op de punten van het aanrecht.

    Bron: beleidsboek zelfstandige woonruimten, 2.5.3: "Voor deze extra
    voorzieningen zou 4,5 punt gekregen kunnen worden. Maar omdat voor het
    aanrechtblad 4 punten zijn toegekend, wordt het aantal punten voor de extra
    voorzieningen afgetopt (gemaximeerd) op 4 punten. Deze keuken krijgt in
    totaal dus 8 punten."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_kookplaat_inductie,
                Installatiesoort.inbouw_afzuiginstallatie,
                Installatiesoort.inbouw_oven_elektrisch,
                Installatiesoort.inbouw_koelkast,
                elementen=[aanrecht(1600)],
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Lengte aanrecht": 4.0,
        Installatiesoort.inbouw_kookplaat_inductie.naam: 1.75,
        Installatiesoort.inbouw_afzuiginstallatie.naam: 0.75,
        Installatiesoort.inbouw_oven_elektrisch.naam: 1.0,
        Installatiesoort.inbouw_koelkast.naam: 1.0,
        "Maximaal evenveel punten als aanrecht": -0.5,
    }
    assert groep.punten == 8.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_in_een_ruimte_zonder_aanrecht_krijgen_geen_punten(
    keuken, vergelijk_met_testreferentie
):
    """Extra voorzieningen in een ruimte zonder aanrecht krijgen geen punten.

    Bron: beleidsboek zelfstandige woonruimten, 2.5.1: "Als een of meer van de
    basisvoorzieningen niet aanwezig zijn, dan worden geen punten toegekend voor
    het onderdeel 'keuken' in de woningwaardering. Dus ook niet voor eventuele
    extra voorzieningen als hierna in paragraaf 2.5.3 benoemd."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(1000)]),
            badkamer(
                Installatiesoort.inbouw_koelkast, Installatiesoort.inbouw_koelkast
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.keuken.naam: {"Lengte aanrecht": 4.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Aanrecht buiten de keuken


def test_vertrek_met_aanrecht_telt_als_keuken(keuken, vergelijk_met_testreferentie):
    """Een vertrek telt voor de keuken mee zodra er een aanrecht in staat.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1: "Rubriek 5
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


def test_overige_ruimte_met_aanrecht_telt_als_keuken(
    keuken, vergelijk_met_testreferentie
):
    """Een overige ruimte met een aanrecht telt voor de keuken mee.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1: "Rubriek 5
    stelt eisen aan de keuken zelf, niet aan de ruimte waarin die ligt. Een
    aanrecht telt daarom in elke ruimte mee."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.bijkeuken, elementen=[aanrecht(2200)]),
            ruimte(Ruimtedetailsoort.garage, elementen=[aanrecht(1500)]),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.bijkeuken.naam: {"Lengte aanrecht": 7.0},
        Ruimtedetailsoort.garage.naam: {"Lengte aanrecht": 4.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Gemeenschappelijke keuken


def test_keuken_gedeeld_met_andere_adressen_telt_niet_mee(
    keuken, vergelijk_met_testreferentie
):
    """Een keuken die met andere adressen wordt gedeeld, krijgt in rubriek 5 geen punten.

    Zo'n keuken hoort bij rubriek 9. De package geeft hier een waarschuwing,
    omdat de eenheid zonder deze keuken geen keuken heeft.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal eventueel
    van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2: "Een waarde
    van 2 of hoger wordt geïnterpreteerd als een gemeenschappelijke ruimte."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_kookplaat_inductie,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.inbouw_koelkast,
                elementen=[aanrecht(3150)],
                gedeeld_met_aantal_adressen=4,
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen keuken") as waarschuwingen:
        groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
