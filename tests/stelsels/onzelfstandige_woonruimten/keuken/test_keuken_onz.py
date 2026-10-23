"""Keuken, onzelfstandige woonruimten (rubriek 5)."""

import pytest

from tests.input import aanrecht, element, ruimte
from tests.utils import (
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


# Lengte van het aanrecht


def test_punten_voor_de_lengte_van_het_aanrecht(keuken, vergelijk_met_testreferentie):
    """De punten voor een aanrecht hangen af van zijn lengte.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # Per klasse de ondergrens en 1 mm onder de volgende grens.
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
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken4", elementen=[aanrecht(2999)]
            ),
            ruimte(
                Ruimtedetailsoort.keuken, naam="Keuken5", elementen=[aanrecht(3000)]
            ),
        ]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Keuken1": {"Lengte aanrecht": 4.0},
        "Keuken2": {"Lengte aanrecht": 4.0},
        "Keuken3": {"Lengte aanrecht": 7.0},
        "Keuken4": {"Lengte aanrecht": 7.0},
        "Keuken5": {"Lengte aanrecht": 10.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_van_5m_of_meer_krijgt_13_punten_bij_minimaal_8_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 5 meter of meer krijgt 13 punten als minimaal 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot de keuken.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1

    De punten worden gedeeld door het aantal onzelfstandige woonruimten met
    toegang en gebruiksrecht.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # Een aanrecht van precies 5 m, gedeeld met precies de 8 woonruimten waarbij 13 punten gelden.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(5000)],
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


def test_aanrecht_van_5m_of_meer_krijgt_10_punten_bij_minder_dan_8_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 5 meter of meer krijgt 10 punten als minder dan 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot de keuken.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1

    De punten worden gedeeld door het aantal onzelfstandige woonruimten met
    toegang en gebruiksrecht.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # Een aanrecht boven de 5 m, gedeeld met 7 woonruimten: één minder dan de 8 waarbij 13 punten gelden.
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


def test_aanrecht_van_5m_of_meer_krijgt_10_punten_in_een_privekeuken(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 5 meter of meer krijgt in een privékeuken 10 punten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # Een aanrecht boven de 5 m in een privékeuken: er zijn geen 8 woonruimten.
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(5500)])]
    )

    groep = keuken.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Lengte aanrecht": 10.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_van_3_tot_5m_krijgt_10_punten_ook_bij_8_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """Een aanrecht van 3 tot 5 meter krijgt 10 punten, ook als minimaal 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot de keuken.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1

    De punten worden gedeeld door het aantal onzelfstandige woonruimten met
    toegang en gebruiksrecht.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # Een aanrecht 1 mm onder de 5 m, gedeeld met de 8 woonruimten waarbij 13 punten gelden.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(4999)],
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # 1 mm onder de grens van 1 m.
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(999)])]
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
    """Een keuken zonder aanrecht is incomplete input en wordt niet gewaardeerd."""
    # Een aanrecht zonder lengte telt niet als aanrecht; delen met andere woonruimten verandert dat niet.
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
    """Een aanrecht zonder lengte is incomplete input."""
    # Naast een aanrecht met lengte een aanrecht zonder lengte: alleen het eerste telt mee.
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    """
    # Het korte deel van 0,8 m telt mee omdat er ook een deel van 1,2 m is.
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

    # Samen 2 m: 7 punten; het deel van 1,2 m alleen zou 4 punten geven.
    assert punten_per_naam(groep) == {"Totale aanrechtlengte": 7.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_voor_extra_voorzieningen_volgt_uit_de_opgetelde_aanrechtlengte(
    keuken, vergelijk_met_testreferentie
):
    """Bij meer dan één aanrecht volgt het maximum voor extra voorzieningen uit de opgetelde aanrechtlengte.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    """
    # Aanrechtdelen van samen 2 m of meer (7 punten), met 8 koelkasten (8 punten) erboven.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                *[Installatiesoort.inbouw_koelkast] * 8,
                elementen=[
                    aanrecht(1500, id="aanrecht_1"),
                    aanrecht(900, id="aanrecht_2"),
                ],
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # 8 punten voor koelkasten, afgetopt op de 7 punten van het aanrecht.
    assert punten_per_naam(groep) == {
        "Totale aanrechtlengte": 7.0,
        Installatiesoort.inbouw_koelkast.naam: 8.0,
        "Maximaal evenveel punten als aanrecht": -1.0,
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Extra voorzieningen


def test_elke_inbouwkoelkast_krijgt_1_punt(keuken, vergelijk_met_testreferentie):
    """Elke inbouwkoelkast in een keuken krijgt 1 punt.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    - wettekst, Bijlage I onder B, onderdeel 5.2
    """
    # Twee koelkasten, om te laten zien dat elke koelkast apart telt.
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.4
    - wettekst, Bijlage I onder A, toelichting rubriek 5 (via Bijlage I onder B, toelichting, inleiding)
    - wettekst, Bijlage I onder B, onderdeel 5.2
    """
    # Mét aanrecht, want zonder aanrecht krijgen voorzieningen geen punten.
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

    # 1 punt voor de koelkast plus 0,75 punt voor de vrieskast.
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
            id="voorzieningen_binnen_het_maximum",
        ),
        pytest.param(
            4,
            {
                "Lengte aanrecht": 4.0,
                Installatiesoort.inbouw_koelkast.naam: 4.0,
                Installatiesoort.inbouw_oven_elektrisch.naam: 1.0,
                "Maximaal evenveel punten als aanrecht": -1.0,
            },
            id="voorzieningen_boven_het_maximum",
        ),
    ],
)
def test_extra_voorzieningen_krijgen_hooguit_de_punten_van_het_aanrecht(
    keuken, vergelijk_met_testreferentie, aantal_koelkasten, verwachte_punten
):
    """Extra voorzieningen krijgen samen hooguit de punten van het aanrecht.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    - wettekst, Bijlage I onder B, onderdeel 5.2
    """
    # Een aanrecht van 1 m (4 punten): 3 punten aan voorzieningen blijven eronder, 5 punten erboven.
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
        "verwachte_punten",
    ),
    [
        pytest.param(
            3500,
            None,
            8,
            {"Lengte aanrecht": 10.0, Installatiesoort.inbouw_koelkast.naam: 8.0},
            id="aanrecht_van_3m_of_meer",
            marks=pytest.mark.toelichting(
                "de 8 punten voor koelkasten blijven onder de 10 punten van het "
                "aanrecht; bij een maximum van 7 punten zou er 1 punt afgaan."
            ),
        ),
        pytest.param(
            5500,
            8,
            12,
            {
                "Lengte aanrecht": 1.63,
                Installatiesoort.inbouw_koelkast.naam: 1.5,
                "Afronding op kwartpunten": 0.12,
            },
            id="aanrecht_van_5m_of_meer_met_8_woonruimten",
            marks=pytest.mark.toelichting(
                "de 12 punten voor koelkasten blijven onder de 13 punten van het "
                "aanrecht; bij een maximum van 10 punten zouden er 2 punten "
                "afgaan."
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
    verwachte_punten,
):
    """Het maximum voor extra voorzieningen stijgt mee met de punten voor een aanrecht van 3 meter of meer.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    - wettekst, Bijlage I onder B, onderdeel 5.2

    Een aanrecht van 3 meter of meer krijgt 10 punten, en vanaf 5 meter bij minimaal 8
    onzelfstandige woonruimten 13 punten, gedeeld door het aantal woonruimten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # Koelkasten met meer punten dan het maximum van de lagere klasse, maar minder dan het aanrecht.
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

    assert punten_per_naam(groep) == verwachte_punten
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.1
    - wettekst, Bijlage I onder A, toelichting rubriek 5 (via Bijlage I onder B, toelichting, inleiding)
    """
    # De koelkasten staan in een badkamer: een ruimte zonder aanrecht.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(1000)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_woonruimten,
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_koelkast,
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.1
    """
    # Een aanrecht in elke soort vertrek; de slaapkamer zonder aanrecht krijgt geen punten.
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.2
    - wettekst, Bijlage I onder B, onderdeel 5.1
    """
    # De deling geldt voor elke puntenklasse; Keuken4 laat zien dat het aantal woonruimten de deler bepaalt.
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


def test_punten_voor_aanrecht_en_voorzieningen_samen_worden_gedeeld_door_het_aantal_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """De punten voor het aanrecht en de extra voorzieningen samen worden gedeeld door het aantal onzelfstandige woonruimten dat de keuken deelt.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    - wettekst, Bijlage I onder B, toelichting rubriek 5
    """
    # Het rekenvoorbeeld uit de wettekst: 7 punten voor het aanrecht en 3 voor de voorzieningen.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_kookplaat_keramisch,
                Installatiesoort.inbouw_oven_elektrisch,
                elementen=[aanrecht(2500)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            )
        ]
    )

    groep = keuken.waardeer(eenheid)

    # 7 punten gedeeld door 4 woonruimten is 1,75; 3 punten gedeeld door 4 is
    # 0,75, dus 0,25 per voorziening.
    assert punten_per_naam(groep) == {
        "Lengte aanrecht": 1.75,
        Installatiesoort.inbouw_koelkast.naam: 0.25,
        Installatiesoort.inbouw_kookplaat_keramisch.naam: 0.25,
        Installatiesoort.inbouw_oven_elektrisch.naam: 0.25,
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_punten_voor_extra_voorzieningen_worden_gedeeld_door_het_aantal_woonruimten(
    keuken, vergelijk_met_testreferentie
):
    """De punten voor extra voorzieningen worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot de keuken.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    - wettekst, Bijlage I onder B, onderdeel 5.2
    """
    # Twee koelkasten in een keuken die met 2 woonruimten wordt gedeeld: elke koelkast krijgt de helft.
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

    # 2 punten voor de koelkasten gedeeld door 2 woonruimten is 1; het aanrecht
    # van 1 m geeft 4 punten gedeeld door 2 is 2.
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
            id="voorzieningen_binnen_het_maximum",
        ),
        pytest.param(
            4,
            {
                "Lengte aanrecht": 2.0,
                Installatiesoort.inbouw_koelkast.naam: 2.0,
                Installatiesoort.inbouw_oven_elektrisch.naam: 0.5,
                "Maximaal evenveel punten als aanrecht": -0.5,
            },
            id="voorzieningen_boven_het_maximum",
        ),
    ],
)
def test_extra_voorzieningen_in_een_gedeelde_keuken_krijgen_hooguit_de_punten_van_het_aanrecht(
    keuken, vergelijk_met_testreferentie, aantal_koelkasten, verwachte_punten
):
    """Ook in een gedeelde keuken krijgen extra voorzieningen samen hooguit de punten van het aanrecht.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.5.3
    - wettekst, Bijlage I onder B, onderdeel 5.2
    """
    # Aanrecht van 1 m (4 punten vóór de deling): 3 punten aan voorzieningen blijven eronder, 5 erboven.
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.1.5
    - wettekst, Bijlage I onder B, toelichting, inleiding
    """
    # Elk vertrek heeft een eigen aantal woonruimten; Slaapkamer2 heeft geen aanrecht en krijgt geen punten.
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
