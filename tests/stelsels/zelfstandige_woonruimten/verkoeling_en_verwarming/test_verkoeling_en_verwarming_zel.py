"""Verkoeling en verwarming, zelfstandige woonruimten (rubriek 3)."""

import pytest

from tests.input import aanrecht, element, ruimte
from tests.utils import (
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import VerkoelingEnVerwarming
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
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        VerkoelingEnVerwarming,
    )


# Verwarming en verkoelingsfunctie


def test_verwarmd_vertrek_met_verkoelingsfunctie_krijgt_een_punt_extra(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd vertrek met verkoelingsfunctie krijgt 1 punt naast de 2 punten voor verwarming.

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten" en "Verkoelingsfunctie per vertrek (mits deze voorziening tevens een
    verwarmingsfunctie heeft) 1 punt (maximaal 2 punten bij meerdere vertrekken
    met verkoelingsfunctie)".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Dit betekent dat
    een vertrek met verkoelingsvoorziening (die ook kan verwarmen) ook als
    verwarmd vertrek geldt en aanspraak kan maken op bijbehorende waardering."
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


def test_vertrekken_met_verkoelingsfunctie_krijgen_samen_hooguit_2_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Vertrekken met verkoelingsfunctie krijgen daarvoor samen hooguit 2 punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Er kan één punt
    worden behaald per vertrek, met een totaal maximum van twee punten."
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
    """Een vertrek met verkoelingsfunctie dat niet verwarmd is, krijgt geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Een
    verkoelingsvoorziening moet tevens kunnen verwarmen."
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmd
    vertrek wordt, ongeacht de verwarmingswijze, een waardering van twee punten
    toegepast, voor zover de verwarming tot de onroerende zaak en zijn
    onroerende aanhorigheden behoort."
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, verwarmd=False)]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_verwarmde_overige_ruimten_krijgen_samen_hooguit_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde overige ruimten krijgen samen hooguit 4 punten.

    Bron: wettekst, Bijlage I onder A, rubriek 3: "verwarming per overige ruimte
    en verkeersruimte 1 punt (maximaal 4 punten)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.berging, naam="Berging1", verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging2", verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging3", verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging4", verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging5", verwarmd=True),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde overige en verkeersruimten": {
            "Berging1": 1.0,
            "Berging2": 1.0,
            "Berging3": 1.0,
            "Berging4": 1.0,
            "Berging5": 1.0,
            "Maximaal 4 punten": -1.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_verwarmde_overige_ruimten_en_verkeersruimten_delen_het_maximum_van_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde overige ruimten en verkeersruimten krijgen samen hooguit 4 punten.

    Bron: wettekst, Bijlage I onder A, rubriek 3: "verwarming per overige ruimte
    en verkeersruimte 1 punt (maximaal 4 punten)".
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


# Open keuken


def test_aanrecht_in_een_woon_of_slaapvertrek_is_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd woon- of slaapvertrek met een aanrecht krijgt 4 punten als vertrek met open keuken.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Voor deze rubriek
    wordt, in tegenstelling tot de gegeven definities van afzonderlijke
    vertrekken onder de inleiding, een open keuken als afzonderlijk verwarmd
    vertrek beschouwd en krijgt dus twee punten indien er verwarming aanwezig
    is."

    Bron: beleidsboek zelfstandige woonruimten, 2.3.2: "Ook een aanrecht dat is
    geplaatst in een woon- of slaapvertrek is een open keuken, ook als er geen
    duidelijke afscheiding is tussen het keukengedeelte en de rest van het
    vertrek."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                elementen=[aanrecht(2700)],
                verwarmd=True,
            ),
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

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Woonkamer met open keuken": 4.0,
            "Slaapkamer met open keuken": 4.0,
            "Woon-/slaapkamer met open keuken": 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_is_vanaf_1m_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde woonkamer is vanaf 1 meter een open keuken.

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "Omdat wij
    in de package niet (kunnen) controleren op keukenkastjes, doen wij de
    aanname dat een aanrecht vanaf 1 meter een open keuken is."
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
    """Een aanrecht zonder lengte is in een verwarmde woonkamer geen open keuken.

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "Omdat wij
    in de package niet (kunnen) controleren op keukenkastjes, doen wij de
    aanname dat een aanrecht vanaf 1 meter een open keuken is."
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

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.woonkamer.naam: 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_woonkamer_met_keuken_heeft_ook_zonder_aanrecht_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmde woonkamer/keuken of woon-/slaapkamer/keuken krijgt ook zonder aanrecht de 4 punten van een vertrek met open keuken.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2:
    "Ruimtedetailsoorten die de keuken al in zich hebben
    (`woonkamer_en_of_keuken`, `woon_en_of_slaapkamer_en_of_keuken`) tellen
    altijd als open keuken, ook zonder aanrecht in de input."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer_en_of_keuken, verwarmd=True),
            ruimte(Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken, verwarmd=True),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            Ruimtedetailsoort.woonkamer_en_of_keuken.naam: 4.0,
            Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken.naam: 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_in_serre_overig_vertrek_of_berging_als_vertrek_is_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde serre, een overig vertrek of een berging die als vertrek is aangeleverd, is een open keuken.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "Elke ruimte
    (uitgezonderd `keuken`, `bijkeuken`, `badkamer`, `badkamer_met_toilet` en
    `doucheruimte`) die als vertrek wordt gewaardeerd en waarin een aanrecht
    vanaf 1 meter staat, heeft dus een open keuken, ook bijvoorbeeld een
    `serre`, `overig vertrek` of een `berging` die als vertrek wordt
    aangeleverd."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.serre,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.overig_vertrek,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                soort=Ruimtesoort.vertrek,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Serre met open keuken": 4.0,
            "Overig vertrek met open keuken": 4.0,
            "Berging met open keuken": 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_in_keuken_bijkeuken_of_doucheruimte_is_geen_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde keuken, doucheruimte of bijkeuken die als vertrek is aangeleverd, is geen open keuken.

    Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
    punten".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "Elke ruimte
    (uitgezonderd `keuken`, `bijkeuken`, `badkamer`, `badkamer_met_toilet` en
    `doucheruimte`) die als vertrek wordt gewaardeerd en waarin een aanrecht
    vanaf 1 meter staat, heeft dus een open keuken".
    """
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
                Ruimtedetailsoort.doucheruimte,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            Ruimtedetailsoort.keuken.naam: 2.0,
            Ruimtedetailsoort.bijkeuken.naam: 2.0,
            Ruimtedetailsoort.doucheruimte.naam: 2.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_open_keuken_in_een_onverwarmd_vertrek_krijgt_geen_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een open keuken in een vertrek zonder verwarming krijgt geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                elementen=[aanrecht(2700)],
                verwarmd=False,
            ),
            ruimte(Ruimtedetailsoort.woonkamer_en_of_keuken, verwarmd=False),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Vertrek tegenover overige ruimte


def test_vertrek_kleiner_dan_4m2_krijgt_ook_met_aanrecht_het_punt_van_een_overige_ruimte(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmde ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², krijgt ook met een aanrecht alleen het punt van een overige ruimte.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Alleen vertrekken
    die met oppervlaktepunten als vertrek zijn gewaardeerd, worden in dit kader
    meegeteld." en "Per verwarmde overige ruimte en verkeersruimte wordt,
    ongeacht de verwarmingswijze, een waardering van één punt toegepast".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "wij lezen
    dat als de eis dat de ruimte minimaal aan de voorwaarden van een vertrek
    voldoet".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.overig_vertrek,
                oppervlakte=3,
                elementen=[aanrecht(1500)],
                verwarmd=True,
            )
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde overige en verkeersruimten": {
            Ruimtedetailsoort.overig_vertrek.naam: 1.0
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_doucheruimte_kleiner_dan_4m2_krijgt_de_punten_van_een_verwarmd_vertrek(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmde doucheruimte kleiner dan 4 m² krijgt de 2 punten van een verwarmd vertrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
    bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
    badkamer of doucheruimte altijd een vertrek."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmd
    vertrek wordt, ongeacht de verwarmingswijze, een waardering van twee punten
    toegepast".
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.doucheruimte, oppervlakte=2, verwarmd=True)]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.doucheruimte.naam: 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)
