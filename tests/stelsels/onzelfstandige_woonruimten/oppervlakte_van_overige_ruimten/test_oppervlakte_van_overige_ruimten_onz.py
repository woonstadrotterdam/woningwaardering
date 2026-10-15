"""Oppervlakte van overige ruimten, onzelfstandige woonruimten (rubriek 2)."""

import pytest

from tests.input import element, elementen, ruimte
from tests.utils import (
    aantal_per_bovenliggende,
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_naam,
    zolders_met_aftrek,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    OppervlakteVanOverigeRuimten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def oppervlakte_van_overige_ruimten(peildatum):
    return OppervlakteVanOverigeRuimten(peildatum=peildatum)


def test_OppervlakteVanOverigeRuimten_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        OppervlakteVanOverigeRuimten,
    )


# Gemeenschappelijke overige ruimten


def test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van privé overige ruimten en de toe te rekenen oppervlakte van gemeenschappelijke overige ruimten worden opgeteld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1;
    wettekst, Bijlage I onder B, toelichting rubriek 2.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Aangeleverd als overige ruimte, zodat de slaapkamer hier telt.
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=4,
            ),
            # Garage en bijkeuken uit het rekenvoorbeeld bij de wettekst.
            ruimte(
                Ruimtedetailsoort.garage,
                oppervlakte=19.34,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
            ruimte(
                Ruimtedetailsoort.bijkeuken,
                oppervlakte=6.06,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 4.0},
        "Gedeeld met 3 onzelfstandige woonruimten": {
            Ruimtedetailsoort.garage.naam: 19.34,
            Ruimtedetailsoort.bijkeuken.naam: 6.06,
        },
    }
    # De toe te rekenen oppervlakte is 4 + (19,34 + 6,06) / 3 = 12,47 m²,
    # afgerond 12 m². Punten delen zou 9,25 punten geven. Eén keer of per soort
    # ruimte afronden maakt hier geen verschil: beide geven 9 punten.
    assert groep.punten == 9.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_overige_ruimte_wordt_gedeeld_door_aantal_woonruimten_met_toegang(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke overige ruimte wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot die ruimte.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2; wettekst,
    Bijlage I onder B, onderdeel 2; wettekst, Bijlage I onder B, toelichting,
    inleiding.
    """
    # Elke ruimte heeft een eigen aantal woonruimten; één deler voor alle ruimten geeft een ander totaal.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.bijkeuken,
                oppervlakte=12,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
            ruimte(
                Ruimtedetailsoort.garage,
                oppervlakte=12,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Gedeeld met 4 onzelfstandige woonruimten": {
            Ruimtedetailsoort.bijkeuken.naam: 12.0
        },
        "Gedeeld met 6 onzelfstandige woonruimten": {
            Ruimtedetailsoort.garage.naam: 12.0
        },
    }
    # De toe te rekenen oppervlakte is 12 / 4 + 12 / 6 = 5 m². Alles door 4
    # delen geeft 4,5 punten, alles door 6 geeft 3,0 punten.
    assert groep.punten == 3.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_oppervlakte_wordt_een_keer_afgerond_na_optellen_van_alle_overige_ruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte wordt één keer afgerond op hele vierkante meters, nadat de toe te rekenen oppervlakte van alle overige ruimten is opgeteld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.berging, oppervlakte=10.4),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=40.4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.berging.naam: 10.4},
        "Gedeeld met 4 onzelfstandige woonruimten": {
            Ruimtedetailsoort.zolder.naam: 40.4
        },
    }
    # De toe te rekenen oppervlakte is 10,4 + 40,4 / 4 = 20,5 m², afgerond 21 m²;
    # apart afronden geeft 10 + 10 = 20 m² en 15,0 punten.
    assert groep.punten == 15.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_overige_ruimte_gedeeld_met_minder_dan_2_onzelfstandige_woonruimten_is_prive(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een overige ruimte met `gedeeld_met_aantal_onzelfstandige_woonruimten` kleiner dan 2 wordt als privéruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Aangeleverd als overige ruimte, zodat de slaapkamer hier telt.
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 4.0}
    }
    assert groep.punten == 3.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_overige_ruimte_die_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_2(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een overige ruimte die niet met een ander adres wordt gedeeld, wordt in rubriek 2 gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
    Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Gedeeld met 1 adres: pas vanaf 2 adressen hoort een ruimte in rubriek 9.
            ruimte(
                Ruimtedetailsoort.bijkeuken,
                oppervlakte=8,
                gedeeld_met_aantal_adressen=1,
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.bijkeuken.naam: 8.0}
    }
    assert groep.punten == 6.0
    vergelijk_met_testreferentie(eenheid, groep)


# Voorwaarden van een overige ruimte


def test_overige_ruimte_moet_minimaal_2m2_groot_zijn(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een ruimte kleiner dan 2 m² wordt niet als overige ruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.2;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    # 0,01 m² onder de grens van 2 m² en precies op de grens.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.bijkeuken, naam="Bijkeuken1", oppervlakte=1.99),
            ruimte(Ruimtedetailsoort.bijkeuken, naam="Bijkeuken2", oppervlakte=2.0),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Bijkeuken2": 2.0}
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_kleiner_dan_4m2_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², wordt als overige ruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.2;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                soort=Ruimtesoort.vertrek,
                oppervlakte=3.99,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                soort=Ruimtesoort.vertrek,
                oppervlakte=4.0,
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Slaapkamer1": 3.99}
    assert groep.punten == 3.0
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte zonder vaste trap


def test_zolder_zonder_vaste_trap_krijgt_5_punten_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder zonder vaste trap krijgt 5 punten aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Een vlizotrap is geen vaste trap (implementatietoelichting 2.2.1.3).
            ruimte(
                Ruimtedetailsoort.zolder,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Subtotaal": 7.5,
        "Correctie: zolder zonder vaste trap": -5.0,
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_alleen_zolder_met_vlizotrap_krijgt_de_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Alleen een zolder met een vlizotrap krijgt de aftrek voor een zolder zonder vaste trap.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    implementatietoelichting onzelfstandige woonruimten, 2.2.1.3; wettekst,
    Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Zonder trap-element: de detailsoort gaat uit van een vaste trap.
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder1"),
            ruimte(
                Ruimtedetailsoort.zolder,
                naam="Zolder3",
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {"Zolder1": 10.0, "Zolder3": 10.0},
    }
    assert zolders_met_aftrek(groep) == ["zolder3"]
    assert punten_per_naam(groep) == {
        "Subtotaal": 15.0,
        "Correctie: zolder zonder vaste trap": -5.0,
    }
    assert groep.punten == 10.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_zolder_met_trap_en_vlizotrap_krijgt_geen_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder met zowel een trap als een vlizotrap krijgt geen aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zolder,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.trap,
                    Bouwkundigelementdetailsoort.vlizotrap,
                ),
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.zolder.naam: 10.0}
    assert punten_per_naam(groep) == {}
    assert groep.punten == 7.5
    vergelijk_met_testreferentie(eenheid, groep)


@pytest.mark.parametrize(
    (
        "oppervlakte_berging",
        "oppervlakte_zolder",
        "verwachte_aftrek",
        "verwachte_punten",
    ),
    [
        pytest.param(
            6.6,
            2.6,
            -1.5,
            5.25,
            id="totaal_naar_beneden_afgerond",
            marks=pytest.mark.toelichting(
                "de zolder van 2,60 m² brengt het totaal van 6,60 op 9,20 m², "
                "afgerond van 7 op 9 m²; de 1,5 punt voor die 2 m² vervalt."
            ),
        ),
        pytest.param(
            6.4,
            2.4,
            -2.25,
            4.5,
            id="totaal_naar_boven_afgerond",
            marks=pytest.mark.toelichting(
                "de zolder van 2,40 m² brengt het totaal van 6,40 op 8,80 m², "
                "afgerond van 6 op 9 m²; de 2,25 punten voor die 3 m² vervallen."
            ),
        ),
    ],
)
def test_aftrek_is_niet_hoger_dan_de_punten_voor_de_zolder(
    oppervlakte_van_overige_ruimten,
    vergelijk_met_testreferentie,
    oppervlakte_berging,
    oppervlakte_zolder,
    verwachte_aftrek,
    verwachte_punten,
):
    """De aftrek voor een zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    wettekst, Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.berging, oppervlakte=oppervlakte_berging),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=oppervlakte_zolder,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Subtotaal": 6.75,
        "Correctie: zolder zonder vaste trap": verwachte_aftrek,
    }
    assert groep.punten == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


def test_maximale_aftrek_voor_zolder_wordt_gedeeld_door_aantal_woonruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De maximale aftrek van 5 punten voor een gemeenschappelijke zolder zonder vaste trap wordt gedeeld door het aantal onzelfstandige woonruimten.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3;
    wettekst, Bijlage I onder B, toelichting rubriek 2.
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Het voorbeeld uit de implementatietoelichting.
            ruimte(Ruimtedetailsoort.berging, oppervlakte=10.4),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=40.4,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {
        "Subtotaal": 15.75,
        # De huurprijscheck trekt hier de volle 5 punten af; de wettekst deelt
        # de aftrek door 4 woonruimten.
        "Correctie: zolder zonder vaste trap": -1.25,
    }
    assert groep.punten == 14.5
    vergelijk_met_testreferentie(eenheid, groep)


# Kasten


def test_kast_telt_mee_in_de_oppervlakte_van_een_overige_ruimte(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast telt mee in de oppervlakte van de overige ruimte waarop de kast uitkomt.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    # Met de kast komt de berging van 2,4 op 2,6 m²: afgerond 3 m² in plaats van 2.
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.2)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.berging, oppervlakte=2.4, verbonden_ruimten=[kast])
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Berging (+1 kast)": 2.6}
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_kast_telt_mee_in_de_oppervlakte_van_een_zolder_zonder_vaste_trap(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een zolder zonder vaste trap.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4; wettekst,
    Bijlage I onder A, toelichting rubriek 2 (via Bijlage I onder B,
    toelichting, inleiding).
    """
    # Met de kast van 0,9 m² komt de zolder van 2,4 op 3,3 m²: afgerond 3 m² in plaats van 2.
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.9)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=2.4,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                verbonden_ruimten=[kast],
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Zolder (+1 kast)": 3.3}
    assert punten_per_naam(groep) == {
        "Subtotaal": 2.25,
        # De zolder met kast is 3,30 m², afgerond 3 m², en daarmee 2,25 punten
        # waard; meer dan dat vervalt er niet. Zonder de kast zou de aftrek 1,5 zijn.
        "Correctie: zolder zonder vaste trap": -2.25,
    }
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)
