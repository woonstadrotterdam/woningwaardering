"""Aftrekpunten, onzelfstandige woonruimten (rubriek 13)."""

import pytest

from tests.input import ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Aftrekpunten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Ruimtedetailsoort,
    RuimtedetailsoortReferentiedata,
    Ruimtesoort,
)


@pytest.fixture()
def aftrekpunten(peildatum):
    return Aftrekpunten(peildatum=peildatum)


def test_Aftrekpunten_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Aftrekpunten,
    )


# Oppervlakte van vertrekken minder dan 8 m²


def test_een_vertrek_van_7m2_geeft_4_punten_aftrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een woonruimte met één privévertrek van 7 m² krijgt 4 punten aftrek.

    Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
    oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
    punten".
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(Ruimtedetailsoort.keuken, oppervlakte=7)])

    groep = aftrekpunten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    "detailsoort",
    [
        pytest.param(Ruimtedetailsoort.woonkamer, id="woonkamer"),
        pytest.param(Ruimtedetailsoort.keuken, id="keuken"),
    ],
)
def test_een_vertrek_van_precies_8m2_geeft_geen_aftrek(
    aftrekpunten, vergelijk_met_testreferentie, detailsoort
):
    """Een woonruimte met één privévertrek van precies 8 m² krijgt geen aftrek.

    Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
    oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
    punten".
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(detailsoort, oppervlakte=8)])

    groep = aftrekpunten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijk_vertrek_telt_voor_de_aftrek_met_de_toe_te_rekenen_oppervlakte(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijk vertrek van 6 m² dat met 2 onzelfstandige woonruimten wordt gedeeld, telt voor de aftrek als 3 m².

    Het scenario onderscheidt niet of de grens van 8 m² aan de toe te rekenen
    of aan de hele oppervlakte wordt getoetst: 3 m² en 6 m² zijn beide minder
    dan 8 m².

    Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
    oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
    punten".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 1: "Het aantal m² dat
    volgens rubriek 1 aan de huurder is toe te rekenen is 10 m² + (40 m²/4) =
    20 m²."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=6,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = aftrekpunten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 3.0
    }
    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)


# Geen vertrekken


def test_ruimte_met_onbekende_detailsoort_telt_niet_mee_als_vertrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een ruimte met een detailsoort die de package niet kent, wordt niet als vertrek geteld.

    De ruimte van 10 m² heeft een detailsoort met de code BRG, die niet in de
    VERA-referentiedata staat (een berging heeft de code BER). De package
    classificeert zo'n ruimte niet en geeft daar geen waarschuwing voor. De
    woonruimte heeft daardoor geen vertrekken en krijgt 4 punten aftrek. De
    test legt dat huidige gedrag vast; de implementatietoelichting spreekt er
    niet over.

    Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
    oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
    punten".

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                RuimtedetailsoortReferentiedata(code="BRG", naam="Berging"),
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=10,
            )
        ]
    )

    groep = aftrekpunten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 0.0
    }
    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_eenheid_zonder_ruimten_krijgt_4_punten_aftrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een eenheid zonder ruimten krijgt 4 punten aftrek.

    Naar de letter van de wettekst is 0 m² minder dan 8 m², maar een eenheid
    zonder ruimten is onvolledige input. De package geeft daar geen
    waarschuwing voor. De test legt dat huidige gedrag vast.

    Bron: wettekst, Bijlage I onder B, onderdeel 13: "Wanneer de totale
    oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m²", "– 4
    punten".

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid()

    groep = aftrekpunten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 0.0
    }
    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)
