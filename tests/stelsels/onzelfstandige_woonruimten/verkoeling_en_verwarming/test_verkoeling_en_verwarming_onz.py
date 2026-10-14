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

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privévertrek
    2 punten" en "Verkoelingsfunctie per privévertrek (mits deze voorziening
    tevens een verwarmingsfunctie heeft) 1 punt (maximaal 2 punten bij meerdere
    privévertrekken met verkoelingsfunctie)".
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

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verkoelingsfunctie per
    privévertrek (mits deze voorziening tevens een verwarmingsfunctie heeft) 1
    punt (maximaal 2 punten bij meerdere privévertrekken met
    verkoelingsfunctie)".
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

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verkoelingsfunctie per
    privévertrek (mits deze voorziening tevens een verwarmingsfunctie heeft) 1
    punt".
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

    Keuken1 is privé; Keuken2 wordt met 2 onzelfstandige woonruimten gedeeld.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privévertrek
    2 punten" en "Verwarming per gemeenschappelijk vertrek op hetzelfde adres 2
    punten".
    """
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


def test_verwarmde_prive_overige_ruimten_krijgen_samen_hooguit_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde privé overige ruimten krijgen samen hooguit 4 punten.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privé overige
    ruimte en verkeersruimte 1 punt".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
    overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
    waardering van één punt toegepast, voor zover de verwarming tot de
    onroerende zaak en zijn onroerende aanhorigheden behoort. Hiervoor geldt
    een maximum van vier punten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
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


def test_verwarmde_prive_overige_ruimten_en_verkeersruimten_delen_het_maximum_van_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde privé overige ruimten en verkeersruimten krijgen samen hooguit 4 punten.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privé overige
    ruimte en verkeersruimte 1 punt".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
    overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
    waardering van één punt toegepast, voor zover de verwarming tot de
    onroerende zaak en zijn onroerende aanhorigheden behoort. Hiervoor geldt
    een maximum van vier punten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
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


def test_vertrek_gedeeld_met_2_woonruimten_krijgt_de_helft_van_de_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd vertrek met verkoelingsfunctie dat met 2 onzelfstandige woonruimten wordt gedeeld, krijgt de helft van de punten van een privévertrek.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per
    gemeenschappelijk vertrek op hetzelfde adres 2 punten, te delen door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft" en
    "Verkoelingsfunctie per gemeenschappelijk vertrek op hetzelfde adres (mits
    deze voorziening tevens een verwarmingsfunctie heeft) 1 punt (maximaal 2
    punten bij meerdere gemeenschappelijke vertrekken met verkoelingsfunctie)
    te delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".
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

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.slaapkamer.naam: 1.0},
        "Verkoelde vertrekken": {Ruimtedetailsoort.slaapkamer.naam: 0.5},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrekken_met_verkoelingsfunctie_gedeeld_met_2_woonruimten_krijgen_samen_hooguit_1_punt(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Vertrekken met verkoelingsfunctie die met 2 onzelfstandige woonruimten worden gedeeld, krijgen daarvoor samen hooguit 1 punt: het maximum van 2 punten gedeeld door 2.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verkoelingsfunctie per
    gemeenschappelijk vertrek op hetzelfde adres (mits deze voorziening tevens
    een verwarmingsfunctie heeft) 1 punt (maximaal 2 punten bij meerdere
    gemeenschappelijke vertrekken met verkoelingsfunctie) te delen door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
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


def test_verwarmde_overige_ruimten_gedeeld_met_2_woonruimten_krijgen_samen_hooguit_2_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde overige ruimten die met 2 onzelfstandige woonruimten worden gedeeld, krijgen samen hooguit 2 punten: het maximum van 4 punten gedeeld door 2.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per
    gemeenschappelijke overige ruimte en verkeersruimte op hetzelfde adres 1
    punt, te delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
    overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
    waardering van één punt toegepast, voor zover de verwarming tot de
    onroerende zaak en zijn onroerende aanhorigheden behoort. Hiervoor geldt
    een maximum van vier punten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: beleidsboek onzelfstandige woonruimten, 2.3: "1 punt per verwarmde
    gemeenschappelijke overige ruimte of gemeenschappelijke verkeersruimte (tot
    maximaal 4 punten) / onzelfstandige wooneenheden met toegang en
    gebruiksrecht".
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

    Slaapkamer1 tot en met Slaapkamer3 zijn privé; Slaapkamer4 tot en met
    Slaapkamer6 worden met 2 onzelfstandige woonruimten gedeeld.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verkoelingsfunctie per
    privévertrek (mits deze voorziening tevens een verwarmingsfunctie heeft) 1
    punt (maximaal 2 punten bij meerdere privévertrekken met
    verkoelingsfunctie)" en "Verkoelingsfunctie per gemeenschappelijk vertrek
    op hetzelfde adres (mits deze voorziening tevens een verwarmingsfunctie
    heeft) 1 punt (maximaal 2 punten bij meerdere gemeenschappelijke vertrekken
    met verkoelingsfunctie) te delen door het aantal onzelfstandige
    woonruimten dat toegang en gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3: "De kaders
    hierboven geven max. 4 verwarmde overige/verkeersruimten en max. 2
    verkoelde vertrekken afzonderlijk voor privé en voor gemeenschappelijk."
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

    Gang1 tot en met Gang3 zijn privé; Gang4 tot en met Gang6 worden met 2
    onzelfstandige woonruimten gedeeld.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privé overige
    ruimte en verkeersruimte 1 punt" en "Verwarming per gemeenschappelijke
    overige ruimte en verkeersruimte op hetzelfde adres 1 punt, te delen door
    het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".

    Bron: beleidsboek onzelfstandige woonruimten, 2.3: "1 punt per verwarmde
    privé overige ruimte of privé verkeersruimte (tot maximaal 4 punten)" en "1
    punt per verwarmde gemeenschappelijke overige ruimte of gemeenschappelijke
    verkeersruimte (tot maximaal 4 punten) / onzelfstandige wooneenheden met
    toegang en gebruiksrecht".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3: "De kaders
    hierboven geven max. 4 verwarmde overige/verkeersruimten en max. 2
    verkoelde vertrekken afzonderlijk voor privé en voor gemeenschappelijk."
    """
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
    """Een verwarmd privé woon- of slaapvertrek met een aanrecht krijgt 4 punten als vertrek met open keuken.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Voor deze rubriek
    wordt, in tegenstelling tot de gegeven definities van afzonderlijke
    vertrekken onder de inleiding, een open keuken als afzonderlijk verwarmd
    vertrek beschouwd en krijgt dus twee punten indien er verwarming aanwezig
    is."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: beleidsboek onzelfstandige woonruimten, 2.3.2: "Ook een aanrecht dat
    is geplaatst in een woon- of slaapvertrek is een open keuken, ook als er
    geen duidelijke afscheiding is tussen het keukengedeelte en de rest van het
    vertrek."
    """
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
    """Een verwarmd privévertrek met open keuken krijgt voor de verkoelingsfunctie 1 punt: de open keuken telt alleen voor de verwarming als afzonderlijk vertrek.

    De bronnen noemen dit geval niet uitdrukkelijk; de test legt vast hoe de
    package ze leest.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verkoelingsfunctie per
    privévertrek (mits deze voorziening tevens een verwarmingsfunctie heeft) 1
    punt".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
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

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {"Woonkamer met open keuken": 4.0},
        "Verkoelde vertrekken": {Ruimtedetailsoort.woonkamer.naam: 1.0},
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_is_vanaf_1m_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde privéwoonkamer is vanaf 1 meter een open keuken.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privévertrek
    2 punten".

    Bron: beleidsboek onzelfstandige woonruimten, 2.3.2: "Een privé verwarmde
    woonkamer met open keuken wordt dus gewaardeerd met 4 punten."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2: "Omdat wij
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
    """Een aanrecht zonder lengte is in een verwarmde privéwoonkamer geen open keuken.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privévertrek
    2 punten".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2: "Omdat wij
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
    """Een verwarmde privé woonkamer/keuken of woon-/slaapkamer/keuken krijgt ook zonder aanrecht de 4 punten van een vertrek met open keuken.

    Bron: beleidsboek onzelfstandige woonruimten, 2.3.2: "Een privé verwarmde
    woonkamer met open keuken wordt dus gewaardeerd met 4 punten."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2:
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


def test_aanrecht_in_keuken_of_bijkeuken_is_geen_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde keuken, of in een verwarmde bijkeuken die als vertrek is aangeleverd, is geen open keuken.

    Keuken1 is privé. Keuken2 en de bijkeuken worden met 2 onzelfstandige
    woonruimten gedeeld en krijgen daarom de helft van de 2 punten.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privévertrek
    2 punten" en "Verwarming per gemeenschappelijk vertrek op hetzelfde adres 2
    punten, te delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2: "Elke
    ruimte (uitgezonderd `keuken`, `bijkeuken`, `badkamer`,
    `badkamer_met_toilet` en `doucheruimte`) die als vertrek wordt gewaardeerd
    en waarin een aanrecht vanaf 1 meter staat, heeft dus een open keuken".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken1",
                elementen=[aanrecht(2700)],
                verwarmd=True,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken2",
                elementen=[aanrecht(2700)],
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.bijkeuken,
                soort=Ruimtesoort.vertrek,
                elementen=[aanrecht(1500)],
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Keuken1": 2.0,
            "Keuken2": 1.0,
            Ruimtedetailsoort.bijkeuken.naam: 1.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_open_keuken_in_een_onverwarmd_vertrek_krijgt_geen_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een open keuken in een vertrek zonder verwarming krijgt geen punten.

    Slaapkamer1 en Woonkamer/keuken1 zijn privé; Slaapkamer2 en
    Woonkamer/keuken2 worden met 2 onzelfstandige woonruimten gedeeld.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
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


def test_vertrek_met_open_keuken_gedeeld_met_2_woonruimten_krijgt_de_helft_van_de_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een verwarmd vertrek met open keuken dat met 2 onzelfstandige woonruimten wordt gedeeld, krijgt de helft van de 4 punten.

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per
    gemeenschappelijk vertrek op hetzelfde adres 2 punten, te delen door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
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

    Het vertrek wordt met 2 onzelfstandige woonruimten gedeeld en krijgt
    daarom de helft van de 4 punten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2: "Elke
    ruimte (uitgezonderd `keuken`, `bijkeuken`, `badkamer`,
    `badkamer_met_toilet` en `doucheruimte`) die als vertrek wordt gewaardeerd
    en waarin een aanrecht vanaf 1 meter staat, heeft dus een open keuken, ook
    bijvoorbeeld een `serre`, `overig vertrek` of een `berging` die als vertrek
    wordt aangeleverd."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
    als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
    er verwarming aanwezig is".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per
    gemeenschappelijk vertrek op hetzelfde adres 2 punten, te delen door het
    aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.overig_vertrek,
                elementen=[aanrecht(1500)],
                verwarmd=True,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {"Overig vertrek met open keuken": 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)
