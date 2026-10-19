"""Sanitair, zelfstandige woonruimten (rubriek 6)."""

import pytest

from tests.input import aanrecht, elementen, ruimte
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, onderdeel 6.1
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
        "Badkamer1": {Installatiesoort.douche.naam: 4.0},
        "Badkamer2": {Installatiesoort.bad.naam: 6.0},
        "Badkamer3": {Installatiesoort.bad_en_douche.naam: 7.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_bad_en_douche_in_dezelfde_ruimte_is_een_voorziening(
    sanitair, vergelijk_met_testreferentie
):
    """Een bad en een douche in dezelfde ruimte tellen samen als één bad/douche.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 6.1
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

    assert punten_per_naam(groep) == {Installatiesoort.bad_en_douche.naam: 7.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_bad_douche_naast_los_bad_en_losse_douche_zijn_twee_voorzieningen(
    sanitair, vergelijk_met_testreferentie
):
    """Een bad/douche naast een los bad en een losse douche telt als twee keer bad/douche.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    """
    # Het losse bad en de losse douche vormen samen een tweede bad/douche.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
                Installatiesoort.bad_en_douche,
                Installatiesoort.bad,
                Installatiesoort.douche,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    # Twee keer 7 punten voor bad/douche
    assert punten_per_naam(groep) == {Installatiesoort.bad_en_douche.naam: 14.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_douche_buiten_de_badkamer_telt_mee(sanitair, vergelijk_met_testreferentie):
    """Een douche telt ook mee buiten de badkamer.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer, Installatiesoort.douche)]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {Installatiesoort.douche.naam: 4.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_drempelloze_inrijdouche_telt_als_douche(
    sanitair, vergelijk_met_testreferentie
):
    """Een drempelloze inrijdouche telt als een gewone douche.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 6.1
    """
    inrijdouche = Installatiesoort.drempelloze_inrijdouche
    bad = Installatiesoort.bad
    douche = Installatiesoort.douche
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.badkamer, inrijdouche, naam="Badkamer1"),
            ruimte(Ruimtedetailsoort.badkamer, inrijdouche, bad, naam="Badkamer2"),
            ruimte(Ruimtedetailsoort.badkamer, inrijdouche, douche, naam="Badkamer3"),
            ruimte(
                Ruimtedetailsoort.badkamer, inrijdouche, bad, douche, naam="Badkamer4"
            ),
            ruimte(Ruimtedetailsoort.badkamer, inrijdouche, bad, bad, naam="Badkamer5"),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {inrijdouche.naam: 4.0},
        # Het bad en de inrijdouche vormen samen één bad/douche.
        "Badkamer2": {Installatiesoort.bad_en_douche.naam: 7.0},
        "Badkamer3": {
            douche.naam: 4.0,
            inrijdouche.naam: 4.0,
        },
        # Het bad vormt een bad/douche met de gewone douche; de inrijdouche telt
        # daarnaast als douche.
        "Badkamer4": {
            Installatiesoort.bad_en_douche.naam: 7.0,
            inrijdouche.naam: 4.0,
        },
        # Eén bad vormt een bad/douche met de inrijdouche; het andere bad telt los.
        "Badkamer5": {Installatiesoort.bad_en_douche.naam: 7.0, bad.naam: 6.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Toilet


def test_toilet_krijgt_in_toiletruimte_een_punt_meer_dan_in_badkamer(
    sanitair, vergelijk_met_testreferentie
):
    """Een toilet krijgt in een toiletruimte meer punten dan in een badkamer.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, onderdeel 6.1
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
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
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, onderdeel 6.1
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


def test_wastafels_buiten_de_badkamer_krijgen_een_maximum_per_ruimte(
    sanitair, vergelijk_met_testreferentie
):
    """Buiten de badkamer geldt per ruimte een maximum van 1 punt voor wastafels en 1,5 punt voor meerpersoonswastafels.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, onderdeel 6.1
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
            ruimte(Ruimtedetailsoort.woonkamer, *wastafels),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    met_maximum = {
        Installatiesoort.wastafel.naam: 2.0,
        "Max 1.0 punt voor Wastafel": -1.0,
        Installatiesoort.meerpersoonswastafel.naam: 3.0,
        "Max 1.5 punt voor Meerpersoonswastafel": -1.5,
    }
    assert punten_per_bovenliggende(groep) == {
        Ruimtedetailsoort.toiletruimte.naam: met_maximum,
        Ruimtedetailsoort.woonkamer.naam: met_maximum,
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, elementen=[aanrecht(aanrecht_mm)])]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


def test_kort_aanrecht_buiten_de_keuken_telt_als_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een aanrecht korter dan 1 meter buiten de keuken telt als wastafel.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.5.2
    """
    # Een bijkeuken: de beleidsregel geldt ook in een andere ruimte dan de keuken.
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, onderdeel 6.1
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


def test_kort_aanrechtdeel_naast_aanrecht_vanaf_1m_is_geen_wastafel(
    sanitair, vergelijk_met_testreferentie
):
    """Een kort aanrechtdeel telt niet als wastafel naast een aanrecht vanaf 1 meter.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 5
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


# Extra voorzieningen


def test_meerdere_kastruimtes_tellen_samen_als_een(
    sanitair, vergelijk_met_testreferentie
):
    """Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, onderdeel 6.2
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
    # 6 punten voor het bad, 1 voor de wastafel en 0,75 voor de kastruimte
    assert groep.punten == 7.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_krijgen_hooguit_de_punten_van_het_bad(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen in de badkamer krijgen samen hooguit de punten van het bad.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, onderdeel 6.2
    """
    # Samen leveren de extra voorzieningen 6,25 punten op, meer dan het bad (6).
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
                Installatiesoort.stopcontact_bij_wastafel,
                Installatiesoort.eenhandsmengkraan,
                Installatiesoort.thermostatische_mengkraan,
            )
        ]
    )

    groep = sanitair.waardeer(eenheid)

    punten = punten_per_naam(groep)
    assert punten[Installatiesoort.bad.naam] == 6.0
    assert punten["Max verdubbeling punten bad en douche"] == -0.25
    # 6 punten voor het bad, 1 voor de wastafel en 6 voor de extra voorzieningen
    assert groep.punten == 13.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_zonder_bad_of_douche_krijgen_geen_punten(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen tellen alleen in een ruimte met een bad of een douche.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, toelichting rubriek 6.2
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
    - implementatietoelichting zelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, toelichting rubriek 6.2

    Een drempelloze inrijdouche telt als douche.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.1
    - wettekst, Bijlage I onder A, toelichting rubriek 6.1
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
    # 4 (douche) + 1 (wastafel) + 0,75 + 0,5 (extra voorzieningen)
    assert groep.punten == 6.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_extra_voorzieningen_onder_het_maximum_worden_niet_afgetopt(
    sanitair, vergelijk_met_testreferentie
):
    """Extra voorzieningen die samen minder punten opleveren dan de douche, het bad en de bad/douche, worden niet afgetopt.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6.2
    - wettekst, Bijlage I onder A, toelichting rubriek 6.2
    """
    # Het voorbeeld uit 2.6.2, met de wastafel die de package voor extra voorzieningen eist.
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

    assert punten_per_naam(groep) == {
        Installatiesoort.bad_en_douche.naam: 7.0,
        Installatiesoort.douche.naam: 4.0,
        Installatiesoort.wastafel.naam: 1.0,
        Installatiesoort.bubbelfunctie_van_het_bad.naam: 1.5,
        Installatiesoort.douchewand.naam: 1.25,
        Installatiesoort.handdoekenradiator.naam: 1.5,
        Installatiesoort.stopcontact_bij_wastafel.naam: 0.5,
        Installatiesoort.thermostatische_mengkraan.naam: 0.5,
        Installatiesoort.eenhandsmengkraan.naam: 0.5,
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_ingebouwd_kastje_zonder_wastafel_geeft_een_waarschuwing(
    sanitair, vergelijk_met_testreferentie
):
    """Een ingebouwd kastje met wastafel zonder wastafel in de ruimte is onjuiste input."""
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.badkamer,
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
                Ruimtedetailsoort.badkamer,
                naam="Badkamer2",
                elementen=elementen(Bouwkundigelementdetailsoort.closetcombinatie),
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                naam="Badkamer3",
                elementen=elementen(douche),
            ),
            ruimte(
                Ruimtedetailsoort.badkamer, naam="Badkamer4", elementen=elementen(bad)
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                naam="Badkamer5",
                elementen=elementen(bad, douche),
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                naam="Badkamer6",
                # Elk bouwkundig element telt mee, ook als het van dezelfde soort is.
                elementen=elementen(bad, bad, douche, douche),
            ),
        ]
    )

    groep = sanitair.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Badkamer1": {Installatiesoort.wastafel.naam: 1.0},
        "Badkamer2": {Installatiesoort.staand_toilet.naam: 2.0},
        "Badkamer3": {Installatiesoort.douche.naam: 4.0},
        "Badkamer4": {Installatiesoort.bad.naam: 6.0},
        "Badkamer5": {Installatiesoort.bad_en_douche.naam: 7.0},
        "Badkamer6": {Installatiesoort.bad_en_douche.naam: 14.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_ruimte_zonder_sanitair_krijgt_geen_waardering(
    sanitair, vergelijk_met_testreferentie
):
    """Een ruimte zonder sanitair komt niet voor in de waardering.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.6
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(Ruimtedetailsoort.slaapkamer)])

    groep = sanitair.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
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
