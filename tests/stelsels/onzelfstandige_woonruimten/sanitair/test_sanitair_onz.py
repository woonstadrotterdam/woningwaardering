"""Sanitair, onzelfstandige woonruimten (rubriek 6)."""

import pytest

from tests.input import aanrecht, elementen, ruimte
from tests.utils import (
    assert_stelselgroep_output,
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


def test_Sanitair_output(onzelfstandige_woonruimten_input_en_outputmodel, peildatum):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Sanitair,
    )


# Bad en douche


def test_punten_voor_bad_en_douche(sanitair, vergelijk_met_testreferentie):
    """Een douche krijgt 3 punten, een bad 5 punten en een bad/douche 6 punten.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Douche 3 punten",
    "Bad 5 punten", "Bad/douche 6 punten".
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

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Bad/douche 6 punten".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Een
    badruimte met een bad én een afzonderlijke douche kan als `bad_en_douche`
    worden meegegeven of als losse `bad` en `douche`."
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
    """Een douche in een slaapkamer krijgt dezelfde punten als in een badkamer.

    Bron: beleidsboek onzelfstandige woonruimten, 2.6: "De waardering van
    sanitair is niet beperkt tot de badkamer en toiletruimte, maar kan ook gaan
    over sanitaire voorzieningen in andere ruimten. Bijvoorbeeld een douche in
    een woon- of slaapkamer."
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 6.1: "Als douche
    moet worden meegeteld iedere door de verhuurder aangebrachte installatie
    voor het nemen van een stortbad."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Douche 3 punten".
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
    """Een toilet krijgt in een toiletruimte een punt meer dan in een badkamer.

    De wettekst noemt het hangend toilet in deze tabel een zwevend toilet.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: een toilet krijgt in een
    "Aparte toiletruimte" "3 punten" en "In badkamer" "2 punten"; een "Zwevend
    toilet" "3,75 punten" en "2,75 punten".
    """
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Een
    VERA-`doucheruimte` telt voor toiletwaardering mee als badkamer. Toiletten
    in een doucheruimte krijgen daarom de punten voor toilet in een badkamer."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.doucheruimte,
                Installatiesoort.staand_toilet,
                Installatiesoort.douche,
                Installatiesoort.wastafel,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep)[Installatiesoort.staand_toilet.naam] == 2.0
    assert groep.punten == 6.0
    vergelijk_met_testreferentie(eenheid, groep)


# Wastafel


def test_wastafels_in_de_badkamer_tellen_allemaal(
    sanitair, vergelijk_met_testreferentie
):
    """In een badkamer geldt geen maximum voor wastafels.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Wastafel 1 punt (tot een
    maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)" en
    "Meerpersoonswastafel (minimale breedte van 70cm en met twee kranen) 1,5
    punten (tot een maximum van 1,5 punt per vertrek of overige ruimte m.u.v. de
    badkamer)".
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
    """Buiten de badkamer krijgen wastafels in een ruimte hooguit de punten van één wastafel.

    Het maximum geldt apart voor wastafels (1 punt) en voor
    meerpersoonswastafels (1,5 punt).

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Wastafel 1 punt (tot een
    maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)" en
    "Meerpersoonswastafel (minimale breedte van 70cm en met twee kranen) 1,5
    punten (tot een maximum van 1,5 punt per vertrek of overige ruimte m.u.v. de
    badkamer)".
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

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Wastafel 1 punt (tot een
    maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)".

    Bron: beleidsboek onzelfstandige woonruimten, 2.6.1: niet als wastafel wordt
    gewaardeerd "een spoelbak in het keukenaanrecht, tenzij deze onderdeel
    uitmaakt van een keukenaanrecht dat korter is dan één meter".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                elementen=[aanrecht(900)],
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten["Wastafel (spoelbak in aanrecht < 1m)"] == 1.0
    assert punten[Installatiesoort.wastafel.naam] == 2.0
    assert punten["Max 1.0 punt voor Wastafel"] == -2.0
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_spoelbak_in_aanrecht_van_1m_telt_niet_als_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een spoelbak in een aanrecht van 1 meter telt niet als wastafel.

    Naast het aanrecht heeft de woonkamer wastafels. Een spoelbak die als
    wastafel telt, zou een eigen waardering krijgen en het maximum voor
    wastafels verder overschrijden.

    Bron: beleidsboek onzelfstandige woonruimten, 2.6.1: niet als wastafel wordt
    gewaardeerd "een spoelbak in het keukenaanrecht, tenzij deze onderdeel
    uitmaakt van een keukenaanrecht dat korter is dan één meter".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                elementen=[aanrecht(1000)],
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert "Wastafel (spoelbak in aanrecht < 1m)" not in punten
    assert punten["Max 1.0 punt voor Wastafel"] == -1.0
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_meerdere_korte_aanrechten_tellen_samen_als_een_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere aanrechten korter dan 1 meter in dezelfde ruimte tellen samen als één wastafel.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Meerdere
    aanrechten korter dan één meter in dezelfde ruimte tellen samen als één
    wastafel."
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

    Het korte deel telt dan mee in de aanrechtlengte van de keuken (rubriek 5).

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Een spoelbak in
    een keuken die voldoet aan het basisniveau, krijgt geen waardering."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Staat in
    dezelfde ruimte ook een aanrecht vanaf 1 meter, dan telt het korte deel mee
    in de aanrechtlengte van de keuken en niet als wastafel."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="kort_aanrecht"),
                    aanrecht(1200, id="lang_aanrecht"),
                ],
                # De keuken is gemeenschappelijk; dat verandert de uitkomst niet.
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
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

    Het adres heeft 8 onzelfstandige woonruimten. Daardoor geldt het maximum
    voor wastafels niet in de slaapkamer, naast de badkamer waar het nooit
    geldt.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "De hieronder weergegeven
    punten dienen te worden gedeeld door het aantal onzelfstandige woonruimten
    dat toegang en gebruiksrecht heeft".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 6: "Daarnaast geldt
    er voor adressen met 8 of meer onzelfstandige woonruimten dat er voor
    maximaal één ruimte, naast de badkamer, een ruimte mag zijn met meer dan
    één wastafel die voor waardering in aanmerking komt."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.douche,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.badkamer.naam] == {
        Installatiesoort.wastafel.naam: 0.25,
        Installatiesoort.douche.naam: 0.38,
    }
    assert punten[Ruimtedetailsoort.slaapkamer.naam] == {
        Installatiesoort.wastafel.naam: 0.38
    }
    assert groep.punten == 1.0
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

    De package leest het aantal onzelfstandige woonruimten op het adres af aan
    de ruimten van de eenheid.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "Op een adres met
    minimaal 8 of meer onzelfstandige woonruimten geldt het bovengenoemde
    maximum niet voor maximaal één ruimte."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Omdat
    het VERA-model geen aantal onzelfstandige woonruimten op het adres bevat,
    geldt als benadering dat ten minste één ruimte
    `gedeeldMetAantalOnzelfstandigeWoonruimten >= 8` heeft."
    """
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

    De berging staat als tweede in de input en heeft evenveel wastafels als de
    woonkamer, maar het zijn meerpersoonswastafels. De uitzondering geldt voor
    één ruimte, voor wastafels en meerpersoonswastafels samen.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1:
    "Vervolgens kiezen we over alle niet-badkamer-ruimten van de eenheid precies
    één uitzonderingsruimte voor beide wastafelsoorten samen." en "De kandidaat
    met de hoogste netto puntenwinst wint".
    """
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
    assert punten[Ruimtedetailsoort.woonkamer.naam] == {
        Installatiesoort.wastafel.naam: 0.38,
        "Maximering voor Wastafel": -0.25,
    }
    assert punten[Ruimtedetailsoort.berging.naam] == {
        Installatiesoort.meerpersoonswastafel.naam: 0.56
    }
    assert groep.punten == 0.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_puntenwinst_voor_de_uitzondering_telt_na_deling_door_het_aantal_woonruimten(
    sanitair, vergelijk_met_testreferentie
):
    """De puntenwinst die de uitzonderingsruimte bepaalt, telt na deling door het aantal onzelfstandige woonruimten waarmee de ruimte wordt gedeeld.

    De slaapkamer levert zonder maximum de meeste punten op, maar wordt met 20
    onzelfstandige woonruimten gedeeld. Na deling wint de berging, die met 8
    onzelfstandige woonruimten wordt gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "De
    kandidaat met de hoogste netto puntenwinst wint, na deling door het aantal
    adressen en onzelfstandige woonruimten waarmee de ruimte wordt gedeeld".
    """
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
    assert groep.punten == 0.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_priveruimte_kan_de_uitzondering_op_het_wastafelmaximum_krijgen(
    sanitair, vergelijk_met_testreferentie
):
    """Ook een privéruimte kan de uitzondering op het maximum voor wastafels krijgen.

    De berging is met 8 onzelfstandige woonruimten gedeeld; daarmee geldt de
    uitzondering op dit adres. De privéslaapkamer heeft de hoogste puntenwinst.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Ook een
    privé-ruimte kan de uitzondering krijgen."
    """
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

    De berging met drie wastafels krijgt de uitzondering op het maximum voor
    wastafels. Twee spoelbakken in de keuken zouden daardoor een maximering
    krijgen; één spoelbak krijgt die niet.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Meerdere
    aanrechten korter dan één meter in dezelfde ruimte tellen samen als één
    wastafel."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="aanrecht1"),
                    aanrecht(900, id="aanrecht2"),
                ],
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    assert punten[Ruimtedetailsoort.keuken.naam] == {
        "Wastafel (spoelbak in aanrecht < 1m)": 0.13
    }
    assert punten[Ruimtedetailsoort.berging.naam] == {
        Installatiesoort.wastafel.naam: 0.38
    }
    assert groep.punten == 0.5
    vergelijk_met_testreferentie(eenheid, groep)


# Extra voorzieningen


def test_meerdere_kastruimtes_tellen_samen_als_een(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.2: "Kastruimte (minimale
    breedte van 40 cm, en minimale hoogte van 40 cm) 0,75 punt (tot een maximum
    van 0,75 punt)".
    """
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
    assert groep.punten == 6.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_krijgen_hooguit_de_punten_van_bad_en_douche(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen in de badkamer krijgen samen hooguit de punten van het bad en de douche.

    Bron: wettekst, Bijlage I onder B, onderdeel 6.2: "Voorzieningen in de bad-
    of doucheruimte (tot maximaal het aantal punten extra dat reeds voor douche,
    bad en bad/douche is verkregen)".
    """
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
    assert groep.punten == 13.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_in_een_toiletruimte_krijgen_geen_punten(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen in een toiletruimte zonder bad of douche krijgen geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 6.2: "Punten onder
    de rubriek extra voorzieningen worden enkel toegekend indien deze zich
    bevinden in een bad- of doucheruimte."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                Installatiesoort.hangend_toilet,
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

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {Installatiesoort.hangend_toilet.naam: 3.75}
    vergelijk_met_testreferentie(eenheid, groep)


def test_drempelloze_inrijdouche_geeft_recht_op_extra_voorzieningen(
    sanitair, vergelijk_met_testreferentie
):
    """Een drempelloze inrijdouche telt als douche voor het recht op extra voorzieningen.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 6.1: "Als douche
    moet worden meegeteld iedere door de verhuurder aangebrachte installatie
    voor het nemen van een stortbad."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 6.2: "Bad- of
    doucheruimten moeten voldoen aan de volgende eisen en hebben" onder meer
    "een douche of bad met aansluitpunten voor warm en koud water".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
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
    assert groep.punten == 5.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_ingebouwd_kastje_zonder_wastafel_geeft_een_waarschuwing(
    sanitair, vergelijk_met_testreferentie
):
    """Een ingebouwd kastje met wastafel zonder wastafel in de ruimte is onjuiste input.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.2: "Voor een
    ingebouwde kast met wastafel moet de wastafel als aparte voorziening worden
    meegegeven."
    """
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

    Bron: implementatietoelichting, datamodel-uitbreidingen, "Bouwkundige
    elementen naast installaties": "Dezelfde voorziening mag zowel als
    bouwkundig element als als installatie op een ruimte worden meegegeven;
    beide attributen zijn geldige modelleringen."
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
    """Een ruimte zonder detailsoort is incomplete input en wordt niet gewaardeerd.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(ruimten=[EenhedenRuimte(id="ruimte")])

    with pytest.warns(UserWarning, match="geen detailsoort") as waarschuwingen:
        groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
