"""Sanitair, onzelfstandige woonruimten (rubriek 6)."""

import pytest

from tests.input import aanrecht, elementen, ruimte
from tests.utils import (
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Sanitair,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def sanitair(peildatum):
    return Sanitair(peildatum=peildatum)


# Bad en douche


def test_punten_voor_bad_en_douche(sanitair, vergelijk_met_testreferentie):
    """Een douche krijgt 3 punten, een bad 5 punten en een bad/douche 6 punten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer, Installatiesoort.douche, naam="Badkamer1"
            ),
            ruimte(Ruimtedetailsoort.badkamer, Installatiesoort.bad, naam="Badkamer2"),
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad_en_douche,
                naam="Badkamer3",
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {Installatiesoort.douche.naam: 3.0},
        "Badkamer2": {Installatiesoort.bad.naam: 5.0},
        "Badkamer3": {Installatiesoort.bad_en_douche.naam: 6.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_bad_en_douche_in_dezelfde_ruimte_is_een_voorziening(
    sanitair, vergelijk_met_testreferentie
):
    """Een bad en een douche in dezelfde ruimte tellen samen als één bad/douche.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 6.1 (via Bijlage I onder B, toelichting, inleiding)
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad,
                Installatiesoort.douche,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {Installatiesoort.bad_en_douche.naam: 6.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_douche_buiten_de_badkamer_telt_mee(sanitair, vergelijk_met_testreferentie):
    """Een douche telt ook mee buiten de badkamer.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer, Installatiesoort.douche)]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {Installatiesoort.douche.naam: 3.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_drempelloze_inrijdouche_krijgt_de_punten_van_een_douche(
    sanitair, vergelijk_met_testreferentie
):
    """Een drempelloze inrijdouche krijgt de punten van een douche.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 6.1 (via Bijlage I onder B, toelichting, inleiding)
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.badkamer, Installatiesoort.drempelloze_inrijdouche)
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        Installatiesoort.drempelloze_inrijdouche.naam: 3.0
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Toilet


def test_toilet_krijgt_in_toiletruimte_een_punt_meer_dan_in_badkamer(
    sanitair, vergelijk_met_testreferentie
):
    """Een toilet krijgt in een toiletruimte meer punten dan in een badkamer.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    # Het hangend toilet heet in de wettekst een zwevend toilet.
    toiletten = (Installatiesoort.staand_toilet, Installatiesoort.hangend_toilet)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.badkamer, *toiletten),
            ruimte(Ruimtedetailsoort.toiletruimte, *toiletten),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.badkamer.naam: {
            Installatiesoort.staand_toilet.naam: 2.0,
            Installatiesoort.hangend_toilet.naam: 2.75,
        },
        Ruimtedetailsoort.toiletruimte.naam: {
            Installatiesoort.staand_toilet.naam: 3.0,
            Installatiesoort.hangend_toilet.naam: 3.75,
        },
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_toilet_in_doucheruimte_telt_als_toilet_in_badkamer(
    sanitair, vergelijk_met_testreferentie
):
    """Een toilet in een doucheruimte krijgt de punten van een toilet in een badkamer.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.doucheruimte, Installatiesoort.staand_toilet)]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {Installatiesoort.staand_toilet.naam: 2.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Wastafel


def test_wastafels_in_de_badkamer_tellen_allemaal(
    sanitair, vergelijk_met_testreferentie
):
    """In een badkamer geldt geen maximum voor wastafels.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        Installatiesoort.wastafel.naam: 2.0,
        Installatiesoort.meerpersoonswastafel.naam: 3.0,
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_wastafels_buiten_de_badkamer_krijgen_een_maximum(
    sanitair, vergelijk_met_testreferentie
):
    """Buiten de badkamer geldt per ruimte een maximum van 1 punt voor wastafels en 1,5 punt voor meerpersoonswastafels.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        Installatiesoort.wastafel.naam: 2.0,
        "Max 1.0 punt voor Wastafel": -1.0,
        Installatiesoort.meerpersoonswastafel.naam: 3.0,
        "Max 1.5 punt voor Meerpersoonswastafel": -1.5,
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_spoelbak_telt_mee_in_het_maximum_voor_wastafels(
    sanitair, vergelijk_met_testreferentie
):
    """Een spoelbak in een kort aanrecht valt onder het maximum van 1 punt voor wastafels.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    # De spoelbak komt bovenop de wastafels in dezelfde ruimte, waar het maximum geldt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                elementen=[aanrecht(900)],
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    # De spoelbak en 2 wastafels geven 3 punten; het maximum laat 1 punt over.
    assert punten_per_naam(groep) == {
        "Wastafel (spoelbak in aanrecht < 1m)": 1.0,
        Installatiesoort.wastafel.naam: 2.0,
        "Max 1.0 punt voor Wastafel": -2.0,
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_spoelbak_in_aanrecht_van_1m_telt_niet_als_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een spoelbak in een aanrecht van 1 meter telt niet als wastafel.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 5 (via Bijlage I onder B, toelichting, inleiding)
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, elementen=[aanrecht(1000)])]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_meerdere_korte_aanrechten_tellen_samen_als_een_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere aanrechten korter dan 1 meter in dezelfde ruimte tellen samen als één wastafel.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="aanrecht1"),
                    aanrecht(900, id="aanrecht2"),
                ],
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Wastafel (spoelbak in aanrecht < 1m)": 1.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_kort_aanrechtdeel_naast_aanrecht_vanaf_1m_is_geen_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een kort aanrechtdeel telt niet als wastafel naast een aanrecht vanaf 1 meter.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 5 (via Bijlage I onder B, toelichting, inleiding)
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="kort_aanrecht"),
                    aanrecht(1000, id="lang_aanrecht"),
                ],
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Gemeenschappelijk sanitair


def test_punten_voor_gemeenschappelijk_sanitair_worden_gedeeld_door_het_aantal_woonruimten(
    sanitair, vergelijk_met_testreferentie
):
    """De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door het aantal onzelfstandige woonruimten waarmee de ruimte wordt gedeeld.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.wastafel,
                Installatiesoort.douche,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    # Een wastafel van 1 punt en een douche van 3 punten, gedeeld door 4
    assert punten_per_naam(groep) == {
        Installatiesoort.wastafel.naam: 0.25,
        Installatiesoort.douche.naam: 0.75,
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Wastafels op een adres met 8 of meer onzelfstandige woonruimten


@pytest.mark.parametrize(
    ("aantal_woonruimten", "punten_woonkamer1", "punten_woonkamer2", "totaal"),
    [
        pytest.param(
            7,
            {
                Installatiesoort.wastafel.naam: 0.43,
                "Maximering voor Wastafel": -0.29,
                Installatiesoort.meerpersoonswastafel.naam: 0.64,
                "Maximering voor Meerpersoonswastafel": -0.43,
            },
            {
                Installatiesoort.wastafel.naam: 0.29,
                "Maximering voor Wastafel": -0.14,
                Installatiesoort.meerpersoonswastafel.naam: 0.43,
                "Maximering voor Meerpersoonswastafel": -0.21,
            },
            5.75,
            id="7_woonruimten",
            marks=pytest.mark.toelichting(
                "het adres blijft net onder de grens, dus het maximum geldt in "
                "elke ruimte buiten de badkamer"
            ),
        ),
        pytest.param(
            8,
            {
                Installatiesoort.wastafel.naam: 0.38,
                Installatiesoort.meerpersoonswastafel.naam: 0.56,
            },
            {
                Installatiesoort.wastafel.naam: 0.25,
                "Maximering voor Wastafel": -0.13,
                Installatiesoort.meerpersoonswastafel.naam: 0.38,
                "Maximering voor Meerpersoonswastafel": -0.19,
            },
            6.25,
            id="8_woonruimten",
        ),
    ],
)
def test_vanaf_8_onzelfstandige_woonruimten_geldt_het_wastafelmaximum_niet_voor_een_ruimte(
    sanitair,
    vergelijk_met_testreferentie,
    aantal_woonruimten,
    punten_woonkamer1,
    punten_woonkamer2,
    totaal,
):
    """Op een adres met 8 of meer onzelfstandige woonruimten geldt het maximum voor wastafels niet voor één ruimte buiten de badkamer.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    # Woonkamer1 heeft de meeste wastafels en krijgt bij 8 woonruimten de uitzondering.
    wastafel = Installatiesoort.wastafel
    meerpersoonswastafel = Installatiesoort.meerpersoonswastafel
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                wastafel,
                wastafel,
                meerpersoonswastafel,
                meerpersoonswastafel,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                wastafel,
                wastafel,
                wastafel,
                meerpersoonswastafel,
                meerpersoonswastafel,
                meerpersoonswastafel,
                naam="Woonkamer1",
                gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_woonruimten,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                wastafel,
                wastafel,
                meerpersoonswastafel,
                meerpersoonswastafel,
                naam="Woonkamer2",
                gedeeld_met_aantal_onzelfstandige_woonruimten=aantal_woonruimten,
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.badkamer.naam] == {
        wastafel.naam: 2.0,
        meerpersoonswastafel.naam: 3.0,
    }
    assert punten["Woonkamer1"] == punten_woonkamer1
    assert punten["Woonkamer2"] == punten_woonkamer2
    assert groep.punten == totaal
    vergelijk_met_testreferentie(eenheid, groep)


def test_ruimte_met_de_hoogste_puntenwinst_krijgt_de_uitzondering_op_het_wastafelmaximum(
    sanitair, vergelijk_met_testreferentie
):
    """Van de ruimten met meer dan één wastafel krijgt de ruimte met de hoogste puntenwinst de uitzondering op het maximum.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    """
    # Evenveel wastafels; de berging (als tweede) heeft de meerpersoonswastafels.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    # 3 wastafels van 1 punt gedeeld door 8; het maximum laat 1 punt gedeeld door 8 over
    assert punten[Ruimtedetailsoort.woonkamer.naam] == {
        Installatiesoort.wastafel.naam: 0.38,
        "Maximering voor Wastafel": -0.25,
    }
    # 3 meerpersoonswastafels van 1,5 punt gedeeld door 8, zonder maximum
    assert punten[Ruimtedetailsoort.berging.naam] == {
        Installatiesoort.meerpersoonswastafel.naam: 0.56
    }
    # 0,38 - 0,25 + 0,56 = 0,69 punt, afgerond op een kwart punt
    assert groep.punten == 0.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_puntenwinst_voor_de_uitzondering_telt_na_deling_door_het_aantal_woonruimten(
    sanitair, vergelijk_met_testreferentie
):
    """De puntenwinst die de uitzonderingsruimte bepaalt, telt na deling door het aantal onzelfstandige woonruimten waarmee de ruimte wordt gedeeld.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    """
    # Zonder deling wint de slaapkamer; na deling door 20 en 8 wint de berging.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=20,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.slaapkamer.naam] == {
        Installatiesoort.wastafel.naam: 0.15,
        "Maximering voor Wastafel": -0.1,
    }
    assert punten[Ruimtedetailsoort.berging.naam] == {
        Installatiesoort.meerpersoonswastafel.naam: 0.38
    }
    # 0,15 - 0,1 + 0,38 = 0,43 punt, afgerond op een kwart punt
    assert groep.punten == 0.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_priveruimte_kan_de_uitzondering_op_het_wastafelmaximum_krijgen(
    sanitair, vergelijk_met_testreferentie
):
    """Ook een privéruimte kan de uitzondering op het maximum voor wastafels krijgen.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    """
    # De berging (8 woonruimten) schakelt de uitzondering in; de slaapkamer wint die.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.slaapkamer.naam] == {
        Installatiesoort.wastafel.naam: 3.0
    }
    assert punten[Ruimtedetailsoort.berging.naam] == {
        Installatiesoort.wastafel.naam: 0.25,
        "Maximering voor Wastafel": -0.13,
    }
    assert groep.punten == 3.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_meerdere_korte_aanrechten_tellen_ook_in_een_gemeenschappelijke_keuken_als_een_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere aanrechten korter dan 1 meter tellen ook in een gemeenschappelijke keuken samen als één wastafel.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1

    De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door
    het aantal onzelfstandige woonruimten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6
    - wettekst, Bijlage I onder B, onderdeel 6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="aanrecht1"),
                    aanrecht(900, id="aanrecht2"),
                ],
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Wastafel (spoelbak in aanrecht < 1m)": 0.25}
    vergelijk_met_testreferentie(eenheid, groep)


# Extra voorzieningen


def test_meerdere_kastruimtes_tellen_samen_als_een(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder B, onderdeel 6.2
    """
    # Een bad en een wastafel maken de badkamer geschikt voor extra voorzieningen.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad,
                Installatiesoort.wastafel,
                Installatiesoort.kastruimte,
                Installatiesoort.kastruimte,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.kastruimte.naam] == 1.5
    assert punten["Max 0.75 punten voor Kastruimte"] == -0.75
    # 5 punten voor het bad, 1 voor de wastafel en 0,75 voor de kastruimte
    assert groep.punten == 6.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_krijgen_hooguit_de_punten_van_bad_en_douche(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen in de badkamer krijgen samen hooguit de punten van het bad en de douche.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder B, onderdeel 6.2
    """
    # Samen leveren de extra voorzieningen 6,25 punten op, meer dan bad/douche (6).
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad,
                Installatiesoort.douche,
                Installatiesoort.wastafel,
                Installatiesoort.bubbelfunctie_van_het_bad,
                Installatiesoort.douchewand,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel,
                Installatiesoort.kastruimte,
                Installatiesoort.stopcontact_bij_wastafel,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.thermostatische_mengkraan,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.bad_en_douche.naam] == 6.0
    assert punten["Max verdubbeling punten bad en douche"] == -0.25
    # 6 punten voor het bad/douche, 1 voor de wastafel en 6 voor de extra voorzieningen
    assert groep.punten == 13.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_zonder_bad_of_douche_krijgen_geen_punten(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen in een ruimte zonder bad of douche krijgen geen punten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, toelichting rubriek 6.2 (via Bijlage I onder B, toelichting, inleiding)
    """
    # Een badkamer met een wastafel, maar zonder bad of douche.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.wastafel,
                Installatiesoort.bubbelfunctie_van_het_bad,
                Installatiesoort.douchewand,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.kastruimte,
                Installatiesoort.kastruimte,
                Installatiesoort.stopcontact_bij_wastafel,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.thermostatische_mengkraan,
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen bad of douche") as waarschuwingen:
        groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {Installatiesoort.wastafel.naam: 1.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_drempelloze_inrijdouche_geeft_recht_op_extra_voorzieningen(
    sanitair, vergelijk_met_testreferentie
):
    """Een drempelloze inrijdouche telt als douche voor het recht op extra voorzieningen.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, toelichting rubriek 6.2 (via Bijlage I onder B, toelichting, inleiding)

    Een drempelloze inrijdouche telt als douche.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 6.1 (via Bijlage I onder B, toelichting, inleiding)
    """
    # De inrijdouche is hier het enige bad of de enige douche in de badkamer.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.drempelloze_inrijdouche,
                Installatiesoort.wastafel,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.thermostatische_mengkraan,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.handdoekenradiator.naam] == 0.75
    assert punten[Installatiesoort.thermostatische_mengkraan.naam] == 0.5
    # 3 (douche) + 1 (wastafel) + 0,75 + 0,5 (extra voorzieningen)
    assert groep.punten == 5.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_ingebouwd_kastje_zonder_wastafel_geeft_een_waarschuwing(
    sanitair, vergelijk_met_testreferentie
):
    """Een ingebouwd kastje met wastafel zonder wastafel in de ruimte is onjuiste input."""
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel,
            )
        ]
    )

    with pytest.warns(UserWarning, match="wastafel") as waarschuwingen:
        groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Bouwkundige elementen


def test_sanitair_als_bouwkundig_element_telt_als_installatie(
    sanitair, vergelijk_met_testreferentie
):
    """Sanitair dat als bouwkundig element is meegegeven, telt als de installatie.

    Bron:
    - implementatietoelichting datamodel-uitbreidingen, "Bouwkundige elementen naast installaties"
    """
    bad = Bouwkundigelementdetailsoort.bad
    douche = Bouwkundigelementdetailsoort.douche
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                naam="Badkamer1",
                elementen=elementen(Bouwkundigelementdetailsoort.wastafel),
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                elementen=elementen(Bouwkundigelementdetailsoort.closetcombinatie),
            ),
            ruimte(Ruimtedetailsoort.doucheruimte, elementen=elementen(douche)),
            ruimte(
                Ruimtedetailsoort.badkamer, naam="Badkamer2", elementen=elementen(bad)
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                naam="Badkamer3",
                elementen=elementen(bad, douche),
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                naam="Badkamer4",
                # Elk bouwkundig element telt mee, ook als het van dezelfde soort is.
                elementen=elementen(bad, bad, douche, douche),
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {Installatiesoort.wastafel.naam: 1.0},
        Ruimtedetailsoort.toiletruimte.naam: {Installatiesoort.staand_toilet.naam: 3.0},
        Ruimtedetailsoort.doucheruimte.naam: {Installatiesoort.douche.naam: 3.0},
        "Badkamer2": {Installatiesoort.bad.naam: 5.0},
        "Badkamer3": {Installatiesoort.bad_en_douche.naam: 6.0},
        "Badkamer4": {Installatiesoort.bad_en_douche.naam: 12.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_ruimte_zonder_detailsoort_geeft_een_waarschuwing(
    sanitair, vergelijk_met_testreferentie
):
    """Een ruimte zonder detailsoort is incomplete input en wordt niet gewaardeerd."""
    eenheid = EenhedenEenheid(ruimten=[EenhedenRuimte(id="ruimte")])

    with pytest.warns(UserWarning, match="geen detailsoort") as waarschuwingen:
        groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
