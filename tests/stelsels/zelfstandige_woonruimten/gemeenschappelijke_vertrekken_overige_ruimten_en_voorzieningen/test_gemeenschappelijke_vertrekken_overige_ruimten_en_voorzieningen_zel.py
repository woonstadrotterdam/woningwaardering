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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9; wettekst,
    Bijlage I onder A, onderdeel 9.
    """
    # Twee vertrekken van dezelfde grootte met een ander aantal adressen.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9; wettekst,
    Bijlage I onder A, onderdeel 9.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2; wettekst,
    Bijlage I onder A, toelichting rubriek 2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 1.
    """
    # Een kast is een aparte ruimte, verbonden aan de ruimte waarin ze staat.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 2.
    """
    # Een kast is een aparte ruimte, verbonden aan de ruimte waarin ze staat.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.7; wettekst,
    Bijlage I onder A, toelichting rubriek 9.
    """
    # Een vlizotrap en geen trap geldt als geen vaste trap (implementatietoelichting
    # 2.2.2.3).
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
        # 5 punten gedeeld door 2 adressen.
        "Correctie: zolder zonder vaste trap": -2.5,
    }
    assert groep.punten == 5.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_aftrek_is_niet_hoger_dan_de_punten_voor_de_gemeenschappelijke_zolder(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De aftrek voor een gemeenschappelijke zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3; wettekst,
    Bijlage I onder A, toelichting rubriek 2.
    """
    # De zolder levert op het totaal 4,5 punten op: minder dan de aftrek van 5.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 2.
    """
    # De kast van 0,9 m² maakt de oppervlakte van de zolder 3,5 m² (zonder kast 2,6).
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9; wettekst, Bijlage I onder A,
    onderdeel 3.
    """
    # Twee verwarmde vertrekken van dezelfde grootte met een ander aantal adressen.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9.
    """
    # Het aanrecht van precies 1 m ligt op de ondergrens van de klasse 1 tot 2 m.
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
    # 4 punten gedeeld door 5 adressen.
    assert punten[Ruimtedetailsoort.keuken.naam] == {"Lengte aanrecht": 0.8}
    # 2 punten gedeeld door 5 adressen.
    assert punten["Extra voorzieningen"] == {Installatiesoort.inbouw_koelkast.naam: 0.4}
    # Met 2 punten voor de oppervlakte en 0,4 punt voor de verwarming samen 3,6
    # punten, afgerond op kwartpunten 3,5.
    assert groep.punten == 3.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_keuken_wordt_altijd_als_vertrek_gewaardeerd(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """Een keuken wordt altijd als vertrek gewaardeerd, ook als ze met een andere ruimtesoort is aangeleverd.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2; wettekst,
    Bijlage I onder A, toelichting rubriek 1.

    De punten van een gemeenschappelijke ruimte worden gedeeld door het aantal
    adressen dat toegang heeft.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9.
    """
    # De aangeleverde ruimtesoort wijkt af van de ruimtesoort die voor een keuken geldt.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9.
    """
    # Twee kastruimtes (maximum 0,75 punt) en extra voorzieningen die samen meer
    # punten geven dan het bad.
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

    # Elke waardering is de helft van de punten uit rubriek 6; de maxima van
    # rubriek 6 gelden vóór het delen. Het rapport toont twee decimalen: 0,625 staat er als 0,63, 0,375 als 0,38 en 0,125 als 0,13.
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


def test_gesaldeerde_punten_worden_gedeeld_door_het_aantal_adressen_en_per_adres_afgerond_op_een_kwart_punt(
    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    vergelijk_met_testreferentie,
):
    """De gesaldeerde punten van gemeenschappelijke binnenruimten worden gedeeld door het aantal adressen dat toegang heeft en per adres afgerond op een kwart punt.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.7; wettekst,
    Bijlage I onder A, toelichting rubriek 9.
    """
    # De keuken en het toilet zijn die uit het voorbeeld. Het voorbeeld verwarmt de
    # keuken met een radiator; de package leest de verwarming af aan `verwarmd`
    # (implementatietoelichting datamodel-uitbreidingen, Verkoeld en verwarmd), dus
    # beide staan in de input.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.9.4.
    """
    # Een zorgwoning wordt aangegeven met de doelgroep zorg; de gemeenschappelijke
    # ruimten hoeven dan niet gespecificeerd te worden (implementatietoelichting
    # zelfstandige woonruimten, 2.9.4), dus alleen een eigen woonkamer.
    eenheid = EenhedenEenheid(
        doelgroep=Doelgroep.zorg,
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer)],
    )

    groep = gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {"Zorgwoning": 3.0}
    vergelijk_met_testreferentie(eenheid, groep)
