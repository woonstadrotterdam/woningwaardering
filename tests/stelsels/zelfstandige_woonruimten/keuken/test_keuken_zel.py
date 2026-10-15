"""Keuken, zelfstandige woonruimten (rubriek 5)."""

import pytest

from tests.input import aanrecht, element, ruimte
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.2; wettekst,
    Bijlage I onder A, onderdeel 5.1.
    """
    # Per klasse de ondergrens, 1 mm onder de volgende grens en precies 2 m. Bij
    # precies 2 m volgt de package de wettekst ("2 m en meer 7 punten") en niet de
    # implementatietoelichting ("Langer dan 2 meter").
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.2; wettekst,
    Bijlage I onder A, onderdeel 5.1.
    """
    # 1 mm onder de grens van 1 m.
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
    """Een keuken zonder aanrecht is incomplete input en wordt niet gewaardeerd."""
    # Een aanrecht zonder lengte telt niet als aanrecht.
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


def test_bouwkundig_element_zonder_detailsoort_geeft_een_waarschuwing(
    keuken, vergelijk_met_testreferentie
):
    """Een bouwkundig element zonder detailsoort is incomplete input en wordt niet gewaardeerd."""
    # Twee elementen van 2000 mm: alleen het element met detailsoort is een aanrecht.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.3.
    """
    # Aanrechtdelen van samen 2 m of meer (7 punten), met 8 koelkasten (8 punten) erboven.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.3; wettekst,
    Bijlage I onder A, onderdeel 5.2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.4; wettekst,
    Bijlage I onder A, toelichting rubriek 5; wettekst, Bijlage I onder A,
    onderdeel 5.2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.3; wettekst,
    Bijlage I onder A, onderdeel 5.2.
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


def test_extra_voorzieningen_boven_de_punten_van_het_aanrecht_worden_afgetopt(
    keuken, vergelijk_met_testreferentie
):
    """Extra voorzieningen die samen meer punten opleveren dan het aanrecht, worden afgetopt op de punten van het aanrecht.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.3; wettekst,
    Bijlage I onder A, onderdeel 5.2.
    """
    # Het rekenvoorbeeld uit het beleidsboek: aanrecht van 1,6 m (4 punten), voorzieningen samen 4,5 punten.
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

    # 4,5 punten voor de voorzieningen, afgetopt op de 4 punten van het aanrecht.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1; wettekst,
    Bijlage I onder A, toelichting rubriek 5.
    """
    # De koelkasten staan in een badkamer: een ruimte zonder aanrecht.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(1000)]),
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_koelkast,
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1.
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


def test_overige_ruimte_met_aanrecht_telt_als_keuken(
    keuken, vergelijk_met_testreferentie
):
    """Een overige ruimte met een aanrecht telt voor de keuken mee.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.5.1.
    """
    # Overige ruimten met een aanrecht in twee puntenklassen: elk aanrecht telt op zijn eigen lengte.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9.
    """
    # Ook de extra voorzieningen in de gedeelde keuken krijgen in rubriek 5 geen punten.
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
