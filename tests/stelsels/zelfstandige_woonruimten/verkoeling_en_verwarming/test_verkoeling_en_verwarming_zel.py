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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.3; wettekst,
    Bijlage I onder A, onderdeel 3.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.3;
    wettekst, Bijlage I onder A, onderdeel 3.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.3;
    wettekst, Bijlage I onder A, onderdeel 3.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3; wettekst,
    Bijlage I onder A, onderdeel 3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.keuken, verwarmd=False)]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_verwarmde_overige_ruimten_en_verkeersruimten_delen_het_maximum_van_4_punten(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Verwarmde overige ruimten en verkeersruimten krijgen samen hooguit 4 punten.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3; wettekst,
    Bijlage I onder A, onderdeel 3.
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
    """Een aanrecht in een verwarmd woon- of slaapvertrek is een open keuken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3.
    """
    # Aanrecht(en) langer dan 1 m, de lengte vanaf waar een open keuken geldt.
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

    # Het vertrek en de open keuken krijgen elk 2 punten.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3.
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
    """Een aanrecht zonder lengte is in een verwarmde woonkamer geen open keuken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2.
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
    """Een verwarmde woonkamer/keuken of woon-/slaapkamer/keuken is ook zonder aanrecht een vertrek met open keuken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3.
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


def test_aanrecht_in_serre_overig_vertrek_of_berging_als_vertrek_is_een_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde serre, een overig vertrek of een berging die als vertrek is aangeleverd, is een open keuken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2.

    Een open keuken geldt als afzonderlijk verwarmd vertrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3.
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

    # Het vertrek en de open keuken krijgen elk 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {
            "Serre met open keuken": 4.0,
            "Overig vertrek met open keuken": 4.0,
            "Berging met open keuken": 4.0,
        }
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_aanrecht_in_keuken_bijkeuken_badkamer_of_doucheruimte_is_geen_open_keuken(
    verkoeling_en_verwarming, vergelijk_met_testreferentie
):
    """Een aanrecht in een verwarmde keuken, badkamer, doucheruimte of als vertrek aangeleverde bijkeuken is geen open keuken.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2;
    wettekst, Bijlage I onder A, toelichting rubriek 3.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1.2;
    implementatietoelichting zelfstandige woonruimten, 2.3.2; wettekst,
    Bijlage I onder A, toelichting rubriek 1; wettekst, Bijlage I onder A,
    toelichting rubriek 3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.overig_vertrek,
                oppervlakte=3.99,
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
    """Een verwarmde doucheruimte is ook kleiner dan 4 m² een vertrek.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.1;
    wettekst, Bijlage I onder A, toelichting rubriek 1.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.doucheruimte, oppervlakte=3.99, verwarmd=True)
        ]
    )

    groep = verkoeling_en_verwarming.waardeer(eenheid)

    # Zonder open keuken krijgt een verwarmd vertrek 2 punten.
    assert punten_per_bovenliggende(groep) == {
        "Verwarmde vertrekken": {Ruimtedetailsoort.doucheruimte.naam: 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)
