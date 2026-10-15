"""Gemeenschappelijke binnenruimten gedeeld met meerdere adressen, onzelfstandige woonruimten (rubriek 9)."""

import pytest

from tests.input import aanrecht, element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen import (
    GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen(peildatum):
    return GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(
        peildatum=peildatum
    )


def test_GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    )


# Oppervlakte


def test_gemeenschappelijke_overige_ruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijke overige ruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9;
    implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
    Bijlage I onder B, onderdeel 9.
    """
    # Per adres blijft er 0,95 m² over, minder dan de 2 m² die een overige ruimte
    # minimaal groot is (Bijlage I onder A, toelichting rubriek 2): de berging
    # telt toch mee, omdat de punten worden gedeeld.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=19,
                verwarmd=True,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        # 19 m² is 14,25 punten; gedeeld door 10 adressen en 2 woonruimten is
        # dat 0,7125 punt, in het rapport 0,71. De oppervlakte delen zou 0,95 m²
        # geven: minder dan 2 m², of afgerond 1 m² en 0,75 punt.
        "Gedeeld met 10 adressen": {"Oppervlakte van overige ruimten": 0.71},
        # 1 punt gedeeld door 10 adressen en 2 woonruimten.
        "Verwarmde overige en verkeersruimten": {Ruimtedetailsoort.berging.naam: 0.05},
        # Samen 0,7625 punt, afgerond op kwartpunten 0,75.
        None: {"Afronding op kwartpunten": -0.01},
    }
    assert groep.punten == 0.75
    vergelijk_met_testreferentie(eenheid, groep)


# Gedeeld met meerdere adressen


def test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_krijgt_geen_punten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijk vertrek dat niet met een ander adres wordt gedeeld, krijgt in deze rubriek geen punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
    Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    # De slaapkamers delen alleen met onzelfstandige woonruimten op hetzelfde
    # adres: er is geen `gedeeld_met_aantal_adressen`.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {}
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte zonder vaste trap


def test_aftrek_voor_gemeenschappelijke_zolder_zonder_vaste_trap_wordt_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De aftrek van 5 punten voor een gemeenschappelijke zolder zonder vaste trap wordt gedeeld door het aantal adressen dat toegang heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
    Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding); wettekst, Bijlage I onder B, onderdeel 9.
    """
    # Een vlizotrap en geen trap geldt als geen vaste trap (implementatietoelichting
    # 2.2.1.3). De ruimten delen met een ander adres, niet met andere
    # onzelfstandige woonruimten op het adres.
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

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
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
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De aftrek voor een gemeenschappelijke zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
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

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
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
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijke zolder zonder vaste trap.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).

    Voor een zolder zonder vaste trap worden 5 punten afgetrokken, niet meer dan
    de punten voor de zolder zelf.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
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

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
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


# Verkoeling en verwarming


def test_voor_vertrekken_met_verkoelingsfunctie_geldt_geen_maximum_van_2_punten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Voor gemeenschappelijke vertrekken met verkoelingsfunctie geldt in deze rubriek geen maximum van 2 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B,
    toelichting, inleiding); wettekst, Bijlage I onder A, toelichting rubriek 3
    (via Bijlage I onder B, toelichting, inleiding).

    Elk punt wordt gedeeld door het aantal adressen en daarna door het aantal
    onzelfstandige woonruimten op het adres.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder B, toelichting rubriek 9.
    """
    # Drie verkoelde vertrekken: samen meer dan het maximum van 2 punten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=20,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken1",
                elementen=[aanrecht(3001)],
                oppervlakte=20,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken2",
                elementen=[aanrecht(3001)],
                oppervlakte=20,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    # Elk vertrek krijgt 1 punt, gedeeld door 2 adressen en 2 woonruimten. Met
    # het maximum van rubriek 3 zouden de drie vertrekken samen 2 punten
    # krijgen: gedeeld door 4 is dat 0,5 punt.
    assert punten_per_bovenliggende(groep)["Verkoelde vertrekken"] == {
        Ruimtedetailsoort.woonkamer.naam: 0.25,
        "Keuken1": 0.25,
        "Keuken2": 0.25,
    }
    # 60 punten voor de oppervlakte, 6 voor de verwarming, 3 voor de
    # verkoelingsfunctie en 20 voor de aanrechten: 89 punten, gedeeld door 4.
    assert groep.punten == 22.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_vijfde_verwarmde_overige_ruimte_krijgt_ook_een_punt(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Voor verwarmde gemeenschappelijke overige ruimten geldt in deze rubriek geen maximum van 4 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B,
    toelichting, inleiding); wettekst, Bijlage I onder A, toelichting rubriek 3
    (via Bijlage I onder B, toelichting, inleiding).

    Elk punt wordt gedeeld door het aantal adressen en daarna door het aantal
    onzelfstandige woonruimten op het adres.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
    Bijlage I onder B, toelichting rubriek 9.
    """
    # Vijf verwarmde bergingen: één meer dan het maximum van 4 punten.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging1",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging2",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging3",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging4",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging5",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        # 80 m² is 60 punten, gedeeld door 2 adressen en 2 woonruimten.
        "Gedeeld met 2 adressen": {"Oppervlakte van overige ruimten": 15.0},
        # 20 m² is 15 punten, gedeeld door 3 adressen en 2 woonruimten.
        "Gedeeld met 3 adressen": {"Oppervlakte van overige ruimten": 2.5},
        "Verwarmde overige en verkeersruimten": {
            "Berging1": 0.25,
            "Berging2": 0.25,
            "Berging3": 0.25,
            "Berging4": 0.25,
            # 1 punt gedeeld door 3 adressen en 2 woonruimten is 0,1666… punt:
            # in het rapport 0,17.
            "Berging5": 0.17,
        },
        # Samen 18,67 punten, afgerond op kwartpunten 18,75.
        None: {"Afronding op kwartpunten": 0.08},
    }
    assert groep.punten == 18.75
    vergelijk_met_testreferentie(eenheid, groep)


# Rekenvoorbeeld


def test_punten_worden_na_verdeling_over_de_adressen_gedeeld_door_de_woonruimten_op_het_adres(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De punten voor een gemeenschappelijke binnenruimte worden na verdeling over de meerdere adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat adres.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
    Bijlage I onder B, toelichting rubriek 9.
    """
    # De keuken en het toilet zijn die uit het voorbeeld, met vier adressen en vier
    # onzelfstandige woonruimten. Het voorbeeld verwarmt de keuken met een radiator;
    # de package leest de verwarming af aan `verwarmd` (implementatietoelichting
    # onzelfstandige woonruimten, 2.3), dus beide staan in de input.
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
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                Installatiesoort.wastafel,
                Installatiesoort.hangend_toilet,
                oppervlakte=2,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    # Elke waardering is een zestiende van de punten uit het rekenvoorbeeld:
    # gedeeld door 4 adressen en 4 woonruimten. Het rapport toont twee
    # decimalen.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 4 adressen": {
            "Oppervlakte van vertrekken": 1.25,
            # 1,5 punt gedeeld door 16 is 0,09375 punt.
            "Oppervlakte van overige ruimten": 0.09,
        },
        # 2 punten gedeeld door 16 is 0,125 punt.
        "Verwarmde vertrekken": {Ruimtedetailsoort.keuken.naam: 0.13},
        # 7 punten gedeeld door 16 is 0,4375 punt.
        Ruimtedetailsoort.keuken.naam: {"Lengte aanrecht": 0.44},
        # 1 punt gedeeld door 16 is 0,0625 punt.
        "Extra voorzieningen": {
            Installatiesoort.inbouw_koelkast.naam: 0.06,
            Installatiesoort.inbouw_oven_elektrisch.naam: 0.06,
            Installatiesoort.inbouw_magnetron.naam: 0.06,
        },
        Ruimtedetailsoort.toiletruimte.naam: {
            # 3,75 punten gedeeld door 16 is 0,234375 punt.
            Installatiesoort.hangend_toilet.naam: 0.23,
            Installatiesoort.wastafel.naam: 0.06,
        },
        # De waarderingen in het rapport zijn samen 2,38 punten; het totaal van
        # 2,390625 punten wordt afgerond op kwartpunten 2,50.
        None: {"Afronding op kwartpunten": 0.12},
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zorgwoning


def test_zorgwoning_krijgt_3_punten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Een zorgwoning krijgt 3 punten voor de gemeenschappelijke ruimten en voorzieningen.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.4.
    """
    # De package leest een zorgwoning af aan de doelgroep (implementatietoelichting
    # zelfstandige woonruimten, 2.12.1: "Wanneer een eenheid de doelgroep Zorg
    # heeft, wordt de woning automatisch als zorgwoning gewaardeerd."). Alleen een
    # eigen woonkamer: de gemeenschappelijke ruimten zijn niet meegegeven.
    eenheid = EenhedenEenheid(
        doelgroep=Doelgroep.zorg,
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer)],
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {"Zorgwoning": 3.0}
    vergelijk_met_testreferentie(eenheid, groep)
