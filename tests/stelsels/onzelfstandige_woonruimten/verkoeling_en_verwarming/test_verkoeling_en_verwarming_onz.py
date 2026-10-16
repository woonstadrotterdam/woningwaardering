"""Verkoeling en verwarming, onzelfstandige woonruimten (rubriek 3)."""

import pytest

from tests.input import aanrecht, element, ruimte
from tests.utils import (
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    VerkoelingEnVerwarming,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def verkoeling_en_verwarming(peildatum):
    return VerkoelingEnVerwarming(peildatum=peildatum)


def test_VerkoelingEnVerwarming_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        VerkoelingEnVerwarming,
    )


# Verwarming en verkoelingsfunctie in privéruimten


def test_verwarmd_privevertrek_met_verkoelingsfunctie_krijgt_een_punt_extra(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd privévertrek met verkoelingsfunctie krijgt 1 punt naast de 2 punten voor verwarming.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer, verwarmd=True, verkoeld=True)]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.slaapkamer.naam: 2.0},
        "Verkoelde vertrekken": {Ruimtedetailsoort.slaapkamer.naam: 1.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_privevertrekken_met_verkoelingsfunctie_krijgen_samen_hooguit_2_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Privévertrekken met verkoelingsfunctie krijgen daarvoor samen hooguit 2 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                verwarmd=True,
                verkoeld=True,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                verwarmd=True,
                verkoeld=True,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer3",
                verwarmd=True,
                verkoeld=True,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    punten = punten_per_bovenliggende(groep)
    assert punten["Verkoelde vertrekken"] == {
        "Slaapkamer1": 1.0,
        "Slaapkamer2": 1.0,
        "Slaapkamer3": 1.0,
        "Maximaal 2 punten": -1.0,
    }
    assert groep.punten == 8.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_met_verkoelingsfunctie_zonder_verwarming_krijgt_geen_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een privévertrek met verkoelingsfunctie dat niet verwarmd is, krijgt geen punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, verwarmd=False, verkoeld=True)]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_onverwarmd_vertrek_krijgt_geen_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een vertrek zonder verwarming krijgt geen punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
    # Een privé- en een gemeenschappelijk vertrek: de bron waardeert beide.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.keuken, naam="Keuken1", verwarmd=False),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken2",
                verwarmd=False,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_verwarmde_prive_overige_ruimten_en_verkeersruimten_delen_het_maximum_van_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde privé overige ruimten en verkeersruimten krijgen samen hooguit 4 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.berging, naam="Berging1", verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging2", verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging3", verwarmd=True),
            ruimte(Ruimtedetailsoort.gang, naam="Gang1", verwarmd=True),
            ruimte(Ruimtedetailsoort.gang, naam="Gang2", verwarmd=True),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde overige en verkeersruimten": {
            "Berging1": 1.0,
            "Berging2": 1.0,
            "Berging3": 1.0,
            "Gang1": 1.0,
            "Gang2": 1.0,
            "Maximaal 4 punten": -1.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Gemeenschappelijke ruimten


def test_punten_voor_een_gemeenschappelijk_vertrek_worden_gedeeld_door_het_aantal_woonruimten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """De punten voor verwarming en verkoelingsfunctie van een gemeenschappelijk vertrek worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # 2 punten voor verwarming en 1 punt voor verkoeling, gedeeld door 2 woonruimten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.slaapkamer.naam: 1.0},
        "Verkoelde vertrekken": {Ruimtedetailsoort.slaapkamer.naam: 0.5},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_voor_gemeenschappelijke_vertrekken_met_verkoelingsfunctie_wordt_gedeeld_door_het_aantal_woonruimten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Het maximum van 2 punten voor gemeenschappelijke vertrekken met verkoelingsfunctie wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
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
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer3",
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Eerst delen en daarna het maximum van 2 punten toepassen zou 1,5 punt
    # geven, zonder aftrek.
    punten = punten_per_bovenliggende(groep)
    assert punten["Verkoelde vertrekken"] == {
        "Slaapkamer1": 0.5,
        "Slaapkamer2": 0.5,
        "Slaapkamer3": 0.5,
        "Maximering": -0.5,
    }
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_voor_verwarmde_gemeenschappelijke_overige_ruimten_wordt_gedeeld_door_het_aantal_woonruimten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Het maximum van 4 punten voor verwarmde gemeenschappelijke overige ruimten wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3; wettekst, Bijlage I onder A,
    toelichting rubriek 3 (via Bijlage I onder B, toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging1",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging2",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging3",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging4",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging5",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Eerst delen en daarna het maximum van 4 punten toepassen zou 2,5 punt
    # geven, zonder aftrek.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde overige en verkeersruimten": {
            "Berging1": 0.5,
            "Berging2": 0.5,
            "Berging3": 0.5,
            "Berging4": 0.5,
            "Berging5": 0.5,
            "Maximering": -0.5,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_voor_verkoelingsfunctie_geldt_apart_voor_prive_en_gemeenschappelijke_vertrekken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Het maximum van 2 punten voor vertrekken met verkoelingsfunctie geldt apart voor privévertrekken en voor gemeenschappelijke vertrekken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3.

    De punten van een gemeenschappelijke ruimte worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3; wettekst,
    Bijlage I onder B, onderdeel 3.
    """
    # Drie privé- en drie gemeenschappelijke vertrekken: beide maxima bereikt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                verwarmd=True,
                verkoeld=True,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                verwarmd=True,
                verkoeld=True,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer3",
                verwarmd=True,
                verkoeld=True,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer4",
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer5",
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer6",
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Privé 2 punten en gemeenschappelijk 2 punten gedeeld door 2. Eén maximum
    # voor alle zes vertrekken samen zou na de privévertrekken niets overlaten.
    punten = punten_per_bovenliggende(groep)
    assert punten["Verkoelde vertrekken"] == {
        "Slaapkamer1": 1.0,
        "Slaapkamer2": 1.0,
        "Slaapkamer3": 1.0,
        "Maximaal 2 punten": -1.0,
        "Slaapkamer4": 0.5,
        "Slaapkamer5": 0.5,
        "Slaapkamer6": 0.5,
        "Maximering": -0.5,
    }
    assert groep.punten == 12.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximum_voor_verwarmde_verkeersruimten_telt_prive_en_gemeenschappelijk_niet_bij_elkaar_op(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Het maximum van 4 punten voor verwarmde verkeersruimten telt privéruimten en gemeenschappelijke ruimten niet bij elkaar op.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3; wettekst, Bijlage I onder A,
    toelichting rubriek 3 (via Bijlage I onder B, toelichting, inleiding).

    De punten van een gemeenschappelijke ruimte worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3; wettekst,
    Bijlage I onder B, onderdeel 3.
    """
    # Drie privé- en drie gemeenschappelijke gangen: per soort onder het maximum.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.gang, naam="Gang1", verwarmd=True),
            ruimte(Ruimtedetailsoort.gang, naam="Gang2", verwarmd=True),
            ruimte(Ruimtedetailsoort.gang, naam="Gang3", verwarmd=True),
            ruimte(
                Ruimtedetailsoort.gang,
                naam="Gang4",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.gang,
                naam="Gang5",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.gang,
                naam="Gang6",
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Zes verwarmde gangen zonder aftrek: privé en gemeenschappelijk blijven
    # elk met drie gangen onder het maximum van 4 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde overige en verkeersruimten": {
            "Gang1": 1.0,
            "Gang2": 1.0,
            "Gang3": 1.0,
            "Gang4": 0.5,
            "Gang5": 0.5,
            "Gang6": 0.5,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Open keuken


def test_aanrecht_in_een_woon_of_slaapvertrek_is_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmd privé woon- of slaapvertrek is een open keuken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # Aanrecht(en) langer dan 1 m, de lengte vanaf waar een open keuken geldt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                elementen=[aanrecht(2700)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.woon_en_of_slaapkamer,
                elementen=[aanrecht(2700)],
                verwarmd=True,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Het vertrek en de open keuken krijgen elk 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Slaapkamer met open keuken": 4.0,
            "Woon-/slaapkamer met open keuken": 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_met_open_keuken_krijgt_een_punt_voor_de_verkoelingsfunctie(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd privévertrek met open keuken krijgt voor de verkoelingsfunctie 1 punt.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.3;
    wettekst, Bijlage I onder B, onderdeel 3.
    """
    # Aanrecht(en) langer dan 1 m, de lengte vanaf waar een open keuken geldt.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                elementen=[aanrecht(2700)],
                verwarmd=True,
                verkoeld=True,
            )
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # 4 punten voor verwarming (vertrek en open keuken), 1 punt voor verkoeling.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {"Woonkamer met open keuken": 4.0},
        "Verkoelde vertrekken": {Ruimtedetailsoort.woonkamer.naam: 1.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_is_vanaf_1m_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde privéwoonkamer is vanaf 1 meter een open keuken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                naam="Woonkamer1",
                elementen=[aanrecht(999)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                naam="Woonkamer2",
                elementen=[aanrecht(1000)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                naam="Woonkamer3",
                elementen=[aanrecht(1001)],
                verwarmd=True,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Zonder open keuken krijgt een verwarmd vertrek 2 punten, met open keuken 4.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Woonkamer1": 2.0,
            "Woonkamer2 met open keuken": 4.0,
            "Woonkamer3 met open keuken": 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_zonder_lengte_is_geen_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht zonder lengte is in een verwarmde privéwoonkamer geen open keuken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                elementen=[element(Bouwkundigelementdetailsoort.aanrecht)],
                verwarmd=True,
            )
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Zonder open keuken krijgt een verwarmd vertrek 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.woonkamer.naam: 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_woonkamer_met_keuken_heeft_ook_zonder_aanrecht_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmde privé woonkamer/keuken of woon-/slaapkamer/keuken is ook zonder aanrecht een vertrek met open keuken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer_en_of_keuken, verwarmd=True),
            ruimte(Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken, verwarmd=True),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Het vertrek en de open keuken krijgen elk 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            Ruimtedetailsoort.woonkamer_en_of_keuken.naam: 4.0,
            Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken.naam: 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_in_keuken_bijkeuken_badkamer_of_doucheruimte_is_geen_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde keuken, badkamer, doucheruimte of als vertrek aangeleverde bijkeuken is geen open keuken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.
    """
    # Aanrechten vanaf 1 m, zodat alleen de detailsoort de open keuken uitsluit.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.bijkeuken,
                soort=Ruimtesoort.vertrek,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.badkamer_met_toilet,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.doucheruimte,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Zonder open keuken krijgt een verwarmd vertrek 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            Ruimtedetailsoort.keuken.naam: 2.0,
            Ruimtedetailsoort.bijkeuken.naam: 2.0,
            Ruimtedetailsoort.badkamer.naam: 2.0,
            Ruimtedetailsoort.badkamer_met_toilet.naam: 2.0,
            Ruimtedetailsoort.doucheruimte.naam: 2.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_open_keuken_in_een_onverwarmd_vertrek_krijgt_geen_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een open keuken in een vertrek zonder verwarming krijgt geen punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # Open keuken via aanrecht en via detailsoort, privé en gemeenschappelijk.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                elementen=[aanrecht(2700)],
                verwarmd=False,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer_en_of_keuken,
                naam="Woonkamer/keuken1",
                verwarmd=False,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                elementen=[aanrecht(2700)],
                verwarmd=False,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer_en_of_keuken,
                naam="Woonkamer/keuken2",
                verwarmd=False,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Open keuken in een gemeenschappelijk vertrek


def test_gemeenschappelijk_vertrek_met_open_keuken_krijgt_de_punten_gedeeld_door_het_aantal_woonruimten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd gemeenschappelijk vertrek met open keuken krijgt de punten gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
    wettekst, Bijlage I onder B, onderdeel 3.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                elementen=[aanrecht(2700)],
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                elementen=[aanrecht(2700)],
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer_en_of_keuken,
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # 4 punten voor vertrek en open keuken, gedeeld door 2 woonruimten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Woonkamer met open keuken": 2.0,
            "Slaapkamer met open keuken": 2.0,
            Ruimtedetailsoort.woonkamer_en_of_keuken.naam: 2.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_in_een_overig_vertrek_is_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmd overig vertrek is een open keuken.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
    B, toelichting, inleiding).
    """
    # Een overig vertrek is geen woon- of slaapvertrek, maar telt toch mee.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.overig_vertrek,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            )
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Het vertrek en de open keuken krijgen elk 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {"Overig vertrek met open keuken": 4.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)
