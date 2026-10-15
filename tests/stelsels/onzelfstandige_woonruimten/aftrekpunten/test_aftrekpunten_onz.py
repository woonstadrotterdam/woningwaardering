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


def test_minder_dan_8m2_aan_vertrekken_geeft_4_punten_aftrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Eén vertrek van 7 m², onder de grens van 8 m².
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
    """Een totale oppervlakte van vertrekken van precies 8 m² geeft geen aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Eén vertrek van precies 8 m²; zowel een woonkamer als een keuken is een vertrek.
    eenheid = EenhedenEenheid(ruimten=[ruimte(detailsoort, oppervlakte=8)])

    groep = aftrekpunten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijk_vertrek_telt_voor_de_aftrek_met_de_toe_te_rekenen_oppervlakte(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijk vertrek telt voor de aftrek mee met de oppervlakte die aan de huurder is toe te rekenen.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1; wettekst,
    Bijlage I onder B, toelichting rubriek 1.

    Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Het vertrek van 12 m² is zelf niet minder dan 8 m²; toe te rekenen is dat 6 m².
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=12,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = aftrekpunten.waardeer(eenheid)

    # 12 m² gedeeld door 2 onzelfstandige woonruimten
    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 6.0
    }
    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_oppervlakte_van_alle_vertrekken_samen_telt_voor_de_aftrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Voor de aftrek telt de totale oppervlakte van alle vertrekken samen.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Twee vertrekken van 4 m² zijn elk kleiner dan 8 m², samen niet.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer1", oppervlakte=4),
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer2", oppervlakte=4),
        ]
    )

    groep = aftrekpunten.waardeer(eenheid)

    # 4 m² + 4 m² is 8 m², niet minder dan 8 m²
    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_ruimte_kleiner_dan_4m2_telt_niet_mee_voor_de_aftrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een ruimte kleiner dan 4 m² is geen vertrek en telt niet mee voor de aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.2;
    wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B,
    toelichting, inleiding).

    Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Telde Slaapkamer2 mee, dan was het totaal 8,5 m² en kwam er geen aftrek.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer1", oppervlakte=5),
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer2", oppervlakte=3.5),
        ]
    )

    groep = aftrekpunten.waardeer(eenheid)

    # Alleen Slaapkamer1 van 5 m² telt mee
    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 5.0
    }
    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_gedeeld_met_een_ander_adres_telt_niet_mee_voor_de_aftrek(
    aftrekpunten, vergelijk_met_testreferentie
):
    """Een vertrek dat met een ander adres wordt gedeeld, telt niet mee voor de aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2; wettekst,
    Bijlage I onder B, onderdeel 1.

    Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Telde de gedeelde woonkamer wel mee, dan was het totaal niet minder dan 8 m².
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=6),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=10,
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = aftrekpunten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 6.0
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.2.
    """
    # De detailsoortcode BRG staat niet in de VERA-referentiedata (een berging is BER).
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

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.13; wettekst,
    Bijlage I onder B, onderdeel 13.
    """
    # Zonder ruimten is de oppervlakte van vertrekken 0 m², minder dan 8 m².
    eenheid = EenhedenEenheid()

    groep = aftrekpunten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": 0.0
    }
    assert punten_per_naam(groep) == {
        "Oppervlakte van vertrekken is minder dan 8 m²": -4.0
    }
    vergelijk_met_testreferentie(eenheid, groep)
