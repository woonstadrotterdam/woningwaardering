"""Sanitair, zelfstandige woonruimten (rubriek 6)."""

import pytest

from tests.input import aanrecht, badkamer, elementen, keuken, ruimte
from tests.utils import (
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import Sanitair
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def sanitair(peildatum):
    return Sanitair(peildatum=peildatum)


def test_Sanitair_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Sanitair,
    )


# Bad en douche


def test_punten_voor_bad_en_douche(sanitair, vergelijk_met_testreferentie):
    """Een douche krijgt 4 punten, een bad 6 punten en een bad/douche 7 punten.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Douche 4 punten",
    "Bad 6 punten", "Bad/douche 7 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(Installatiesoort.douche, naam="Badkamer1"),
            badkamer(Installatiesoort.bad, naam="Badkamer2"),
            badkamer(Installatiesoort.bad_en_douche, naam="Badkamer3"),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {"Douche": 4.0},
        "Badkamer2": {"Bad": 6.0},
        "Badkamer3": {"Bad en douche": 7.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_bad_en_douche_in_dezelfde_ruimte_is_een_voorziening(
    sanitair, vergelijk_met_testreferentie
):
    """Een bad en een douche in dezelfde ruimte tellen samen als één bad/douche.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Bad/douche 7 punten".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1: "Een
    badruimte met een bad én een afzonderlijke douche kan als `bad_en_douche`
    worden meegegeven of als losse `bad` en `douche`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[badkamer(Installatiesoort.bad, Installatiesoort.douche)]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Bad en douche": 7.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_bad_douche_naast_los_bad_en_losse_douche_zijn_twee_voorzieningen(
    sanitair, vergelijk_met_testreferentie
):
    """Een bad/douche naast een los bad en een losse douche telt als twee keer bad/douche.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1: "Een
    badruimte met een bad én een afzonderlijke douche kan als `bad_en_douche`
    worden meegegeven of als losse `bad` en `douche`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(
                Installatiesoort.bad_en_douche,
                Installatiesoort.bad,
                Installatiesoort.douche,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Bad en douche": 14.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_douche_buiten_de_badkamer_telt_mee(sanitair, vergelijk_met_testreferentie):
    """Een douche in een slaapkamer krijgt dezelfde punten als in een badkamer.

    Bron: beleidsboek zelfstandige woonruimten, 2.6: "De waardering van sanitair
    is niet beperkt tot de badkamer en toiletruimte, maar kan ook gaan over
    sanitaire voorzieningen in andere ruimten. Bijvoorbeeld een douche in een
    woon- of slaapkamer."
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer, Installatiesoort.douche)]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Douche": 4.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_drempelloze_inrijdouche_telt_als_douche(
    sanitair, vergelijk_met_testreferentie
):
    """Een drempelloze inrijdouche telt als een gewone douche.

    Bron: beleidsboek zelfstandige woonruimten, 2.6.1: "Als douche wordt iedere,
    door de verhuurder aangebrachte, installatie voor het nemen van een stortbad
    geteld."
    """
    inrijdouche = Installatiesoort.drempelloze_inrijdouche
    bad = Installatiesoort.bad
    douche = Installatiesoort.douche
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(inrijdouche, naam="Badkamer1"),
            badkamer(inrijdouche, bad, naam="Badkamer2"),
            badkamer(inrijdouche, douche, naam="Badkamer3"),
            badkamer(inrijdouche, bad, douche, naam="Badkamer4"),
            badkamer(inrijdouche, bad, bad, naam="Badkamer5"),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {"Drempelloze inrijdouche": 4.0},
        # Het bad en de inrijdouche vormen samen één bad/douche.
        "Badkamer2": {"Bad en douche": 7.0},
        "Badkamer3": {
            "Douche": 4.0,
            "Drempelloze inrijdouche": 4.0,
        },
        # Het bad vormt een bad/douche met de gewone douche; de inrijdouche telt
        # daarnaast als douche.
        "Badkamer4": {
            "Bad en douche": 7.0,
            "Drempelloze inrijdouche": 4.0,
        },
        # Eén bad vormt een bad/douche met de inrijdouche; het andere bad telt los.
        "Badkamer5": {"Bad en douche": 7.0, "Bad": 6.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Toilet


def test_toilet_krijgt_in_toiletruimte_een_punt_meer_dan_in_badkamer(
    sanitair, vergelijk_met_testreferentie
):
    """Een toilet krijgt in een toiletruimte een punt meer dan in een badkamer.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: een toilet krijgt in een
    "Aparte toiletruimte" "3 punten" en "In badkamer" "2 punten"; een hangend
    toilet "3,75 punten" en "2,75 punten".
    """
    toiletten = (Installatiesoort.staand_toilet, Installatiesoort.hangend_toilet)
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(*toiletten),
            ruimte(Ruimtedetailsoort.toiletruimte, *toiletten),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer": {"Staand Toilet": 2.0, "Hangend toilet": 2.75},
        "Toiletruimte": {"Staand Toilet": 3.0, "Hangend toilet": 3.75},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_toilet_in_doucheruimte_telt_als_toilet_in_badkamer(
    sanitair, vergelijk_met_testreferentie
):
    """Een toilet in een doucheruimte krijgt de punten van een toilet in een badkamer.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1: "Een
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

    assert punten_per_naam(groep)["Staand Toilet"] == 2.0
    assert groep.punten == 7.0
    vergelijk_met_testreferentie(eenheid, groep)


# Wastafel


def test_wastafels_in_de_badkamer_tellen_allemaal(
    sanitair, vergelijk_met_testreferentie
):
    """In een badkamer geldt geen maximum voor wastafels.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Wastafel 1 punt (tot een
    maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)" en
    "Meerpersoonswastafel (minimale breedte van 70cm en met twee kranen) 1,5
    punten (tot een maximum van 1,5 punt per vertrek of overige ruimte m.u.v. de
    badkamer)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Wastafel": 2.0,
        "Meerpersoonswastafel": 3.0,
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_wastafels_buiten_de_badkamer_krijgen_een_maximum_per_ruimte(
    sanitair, vergelijk_met_testreferentie
):
    """Buiten de badkamer krijgen wastafels per ruimte hooguit de punten van één wastafel.

    Het maximum geldt apart voor wastafels (1 punt) en voor
    meerpersoonswastafels (1,5 punt).

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Wastafel 1 punt (tot een
    maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)" en
    "Meerpersoonswastafel (minimale breedte van 70cm en met twee kranen) 1,5
    punten (tot een maximum van 1,5 punt per vertrek of overige ruimte m.u.v. de
    badkamer)".
    """
    wastafels = (
        Installatiesoort.wastafel,
        Installatiesoort.wastafel,
        Installatiesoort.meerpersoonswastafel,
        Installatiesoort.meerpersoonswastafel,
    )
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.toiletruimte, *wastafels),
            # Een aanrecht van minimaal 1 meter telt niet als wastafel en
            # verandert de uitkomst dus niet.
            ruimte(Ruimtedetailsoort.woonkamer, *wastafels, elementen=[aanrecht(1000)]),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    met_maximum = {
        "Wastafel": 2.0,
        "Max 1.0 punt voor Wastafel": -1.0,
        "Meerpersoonswastafel": 3.0,
        "Max 1.5 punt voor Meerpersoonswastafel": -1.5,
    }
    assert punten_per_bovenliggende(groep) == {
        "Toiletruimte": met_maximum,
        "Woonkamer": met_maximum,
    }
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    ("aanrecht_mm", "verwachte_punten"),
    [
        pytest.param(
            999, {"Wastafel (spoelbak in aanrecht < 1m)": 1.0}, id="net_onder_1m"
        ),
        pytest.param(
            1000,
            {},
            id="precies_1m",
            marks=pytest.mark.toelichting(
                "de keuken heeft een aanrecht van minimaal 1 meter, dus de "
                "spoelbak hoort bij de keuken en is geen wastafel"
            ),
        ),
    ],
)
def test_spoelbak_in_aanrecht_korter_dan_1m_telt_als_wastafel(
    sanitair, vergelijk_met_testreferentie, aanrecht_mm, verwachte_punten
):
    """Een spoelbak in een aanrecht korter dan 1 meter telt als wastafel.

    Bron: beleidsboek zelfstandige woonruimten, 2.6.1: niet als wastafel wordt
    gewaardeerd "een spoelbak in het keukenaanrecht, tenzij deze onderdeel
    uitmaakt van een keukenaanrecht dat korter is dan één meter".
    """
    eenheid = EenhedenEenheid(ruimten=[keuken(aanrechten_mm=[aanrecht_mm])])

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


def test_kort_aanrecht_buiten_de_keuken_telt_als_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een aanrecht korter dan 1 meter telt ook in een bijkeuken als wastafel.

    Bron: beleidsboek zelfstandige woonruimten, 2.5.2: "Een aanrecht met
    spoelbak dat korter is dan 1 meter voldoet niet aan de basisvoorzieningen en
    krijgt daarom géén punten in de rubriek keuken. Wel kan de spoelbak als
    wastafel nog één punt krijgen in de rubriek sanitair."
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.bijkeuken, elementen=[aanrecht(800)])]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Wastafel (spoelbak in aanrecht < 1m)": 1.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_spoelbak_telt_mee_in_het_maximum_voor_wastafels(
    sanitair, vergelijk_met_testreferentie
):
    """Een spoelbak in een kort aanrecht valt onder het maximum van 1 punt voor wastafels.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Wastafel 1 punt (tot een
    maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)".

    Bron: beleidsboek zelfstandige woonruimten, 2.6.1: niet als wastafel wordt
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
    assert punten["Wastafel"] == 2.0
    assert punten["Max 1.0 punt voor Wastafel"] == -2.0
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_kort_aanrechtdeel_naast_aanrecht_vanaf_1m_is_geen_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een kort aanrechtdeel telt niet als wastafel naast een aanrecht vanaf 1 meter.

    Het korte deel telt dan mee in de aanrechtlengte van de keuken (rubriek 5).

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Een spoelbak in
    een keuken die voldoet aan het basisniveau, krijgt geen waardering."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1: "Staat in
    dezelfde ruimte ook een aanrecht vanaf 1 meter, dan telt het korte deel mee
    in de aanrechtlengte van de keuken en niet als wastafel."
    """
    eenheid = EenhedenEenheid(ruimten=[keuken(aanrechten_mm=[800, 1200])])

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Extra voorzieningen


def test_meerdere_kastruimtes_tellen_samen_als_een(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.2: "Kastruimte (minimale
    breedte van 40 cm, en minimale hoogte van 40 cm) 0,75 punt (tot een maximum
    van 0,75)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(
                Installatiesoort.bad,
                Installatiesoort.wastafel,
                Installatiesoort.kastruimte,
                Installatiesoort.kastruimte,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten["Kastruimte"] == 1.5
    assert punten["Max 0.75 punten voor Kastruimte"] == -0.75
    assert groep.punten == 7.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_krijgen_hooguit_de_punten_van_het_bad(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen in de badkamer krijgen samen hooguit de punten van het bad.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.2: "Voorzieningen in de bad-
    of doucheruimte (tot maximaal het aantal punten extra dat reeds voor douche,
    bad en bad/douche is verkregen)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(
                Installatiesoort.bad,
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
    assert punten["Bad"] == 6.0
    assert punten["Max verdubbeling punten bad en douche"] == -0.25
    assert groep.punten == 13.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_zonder_bad_of_douche_krijgen_geen_punten(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen tellen alleen in een ruimte met een bad of een douche.

    Bron: wettekst, Bijlage I onder A, onderdeel 6.2: "Voorzieningen in de bad-
    of doucheruimte (tot maximaal het aantal punten extra dat reeds voor douche,
    bad en bad/douche is verkregen)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte,
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

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_drempelloze_inrijdouche_geeft_recht_op_extra_voorzieningen(
    sanitair, vergelijk_met_testreferentie
):
    """Een drempelloze inrijdouche maakt van de ruimte een doucheruimte met extra voorzieningen.

    Bron: beleidsboek zelfstandige woonruimten, 2.6.1: "Als douche wordt iedere,
    door de verhuurder aangebrachte, installatie voor het nemen van een stortbad
    geteld."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(
                Installatiesoort.drempelloze_inrijdouche,
                Installatiesoort.wastafel,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.thermostatische_mengkraan,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten["Handdoekenradiator"] == 0.75
    assert punten["Thermostatische mengkraan"] == 0.5
    assert groep.punten == 6.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_rekenvoorbeeld_extra_voorzieningen_uit_het_beleidsboek(
    sanitair, vergelijk_met_testreferentie
):
    """Het rekenvoorbeeld van het beleidsboek: extra voorzieningen blijven onder het maximum.

    Het beleidsboek komt op 16,75 punten en noemt geen wastafel. De package
    waardeert extra voorzieningen alleen in een ruimte met een wastafel; die
    staat daarom in de input en levert 1 punt extra op.

    Bron: beleidsboek zelfstandige woonruimten, 2.6.2: "De punten worden voor de
    extra sanitaire voorzieningen (5,75 punten) worden niet afgetopt, omdat het
    puntenaantal lager is dan het totaal aantal punten voor de douche en
    bad/douchecombinatie (11 punten)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(
                Installatiesoort.bad,
                Installatiesoort.douche,
                Installatiesoort.wastafel,
                Installatiesoort.bubbelfunctie_van_het_bad,
                Installatiesoort.douchewand,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.handdoekenradiator,
                Installatiesoort.stopcontact_bij_wastafel,
                Installatiesoort.stopcontact_bij_wastafel,
                Installatiesoort.thermostatische_mengkraan,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.eenhandsmengkraan,
            ),
            ruimte(Ruimtedetailsoort.slaapkamer, Installatiesoort.douche),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten["Bad en douche"] == 7.0
    assert punten["Douche"] == 4.0
    assert "Max verdubbeling punten bad en douche" not in punten
    assert groep.punten == 17.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_ingebouwd_kastje_zonder_wastafel_geeft_een_waarschuwing(
    sanitair, vergelijk_met_testreferentie
):
    """Een ingebouwd kastje met wastafel zonder wastafel in de ruimte is onjuiste input.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.6.2: "Voor een
    ingebouwde kast met wastafel moet de wastafel als aparte voorziening worden
    meegegeven."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            badkamer(Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel)
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
            badkamer(
                naam="Badkamer1",
                elementen=elementen(Bouwkundigelementdetailsoort.wastafel),
            ),
            badkamer(
                naam="Badkamer2",
                elementen=elementen(Bouwkundigelementdetailsoort.closetcombinatie),
            ),
            badkamer(naam="Badkamer3", elementen=elementen(douche)),
            badkamer(naam="Badkamer4", elementen=elementen(bad)),
            badkamer(naam="Badkamer5", elementen=elementen(bad, douche)),
            badkamer(
                naam="Badkamer6",
                elementen=elementen(bad, bad, douche, douche),
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {"Wastafel": 1.0},
        "Badkamer2": {"Staand Toilet": 2.0},
        "Badkamer3": {"Douche": 4.0},
        "Badkamer4": {"Bad": 6.0},
        "Badkamer5": {"Bad en douche": 7.0},
        "Badkamer6": {"Bad en douche": 14.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_ruimte_zonder_sanitair_krijgt_geen_waardering(
    sanitair, vergelijk_met_testreferentie
):
    """Een ruimte zonder sanitair komt niet voor in de waardering.

    Bron: beleidsboek zelfstandige woonruimten, 2.6: "Sanitair in de woonruimte
    komt voor waardering in aanmerking."
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)])

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
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
