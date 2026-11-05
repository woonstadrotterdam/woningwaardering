"""Oppervlakte van overige ruimten, zelfstandige woonruimten (rubriek 2)."""

import pytest

from tests.input import element, elementen, ruimte
from tests.utils import (
    aantal_per_naam,
    punten_per_naam,
    zolders_met_aftrek,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import (
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


# Afronding


def test_oppervlakte_wordt_afgerond_na_optellen_van_alle_overige_ruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakten van alle overige ruimten worden eerst opgeteld en dan afgerond op hele m².

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.1
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    # Elke ruimte apart afgerond geeft 2 + 2 = 4 m²; samen opgeteld is het 4,8 m², afgerond 5.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.bijkeuken, oppervlakte=2.4),
            ruimte(Ruimtedetailsoort.berging, oppervlakte=2.4),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        Ruimtedetailsoort.bijkeuken.naam: 2.4,
        Ruimtedetailsoort.berging.naam: 2.4,
    }
    assert groep.punten == 3.75
    vergelijk_met_testreferentie(eenheid, groep)


# Voorwaarden van een overige ruimte


def test_toiletruimte_kleiner_dan_2m2_wordt_niet_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een toiletruimte kleiner dan 2 m² wordt niet als overige ruimte gewaardeerd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.2
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    # 0,01 m² onder de grens van 2 m² en precies op de grens.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte1", oppervlakte=1.99
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte2", oppervlakte=2.0
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Toiletruimte2": 2.0}
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_kleiner_dan_4m2_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², wordt als overige ruimte gewaardeerd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.2
    - wettekst, Bijlage I onder A, toelichting rubriek 2
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


# Privé parkeerruimte


def test_garage_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een garage die bij de woning hoort, wordt als overige ruimte gewaardeerd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.5
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    eenheid = EenhedenEenheid(ruimten=[ruimte(Ruimtedetailsoort.garage)])

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.garage.naam: 10.0}
    assert groep.punten == 7.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte zonder vaste trap


def test_zolder_zonder_vaste_trap_krijgt_5_punten_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder zonder vaste trap krijgt 5 punten aftrek.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Een vlizotrap is geen vaste trap (implementatietoelichting 2.2.2.3).
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zolder,
                naam="Zolder1",
                elementen=[element(Bouwkundigelementdetailsoort.trap)],
            ),
            # Zonder trap-element: de detailsoort gaat uit van een vaste trap.
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder2"),
            ruimte(
                Ruimtedetailsoort.zolder,
                naam="Zolder3",
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Subtotaal": 30.0,
        "Zolder1": 10.0,
        "Zolder2": 10.0,
        "Zolder3": 10.0,
    }
    assert zolders_met_aftrek(groep) == ["zolder3"]
    assert punten_per_naam(groep) == {
        "Subtotaal": 22.5,
        "Correctie: zolder zonder vaste trap": -5.0,
    }
    assert groep.punten == 17.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_zolder_met_trap_en_vlizotrap_krijgt_geen_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder met zowel een trap als een vlizotrap krijgt geen aftrek.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
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

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
    - wettekst, Bijlage I onder A, toelichting rubriek 2
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


# Zolderruimte aangeleverd als vertrek


def test_zoldervertrek_met_alleen_een_vlizotrap_krijgt_de_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zoldervertrek dat alleen via een vlizotrap bereikbaar is, krijgt als overige ruimte 5 punten aftrek.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                soort=Ruimtesoort.vertrek,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Subtotaal": 10.0,
        Ruimtedetailsoort.zoldervertrek.naam: 10.0,
    }
    assert punten_per_naam(groep) == {
        "Subtotaal": 7.5,
        "Correctie: zolder zonder vaste trap": -5.0,
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_zolder_die_als_vertrek_is_aangeleverd_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder die als vertrek is aangeleverd, wordt als overige ruimte gewaardeerd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    # De detailsoort zolder voldoet niet aan de afwerkingseisen van een vertrek.
    eenheid = EenhedenEenheid(
        ruimten=[ruimte(Ruimtedetailsoort.zolder, soort=Ruimtesoort.vertrek)]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.zolder.naam: 10.0}
    assert groep.punten == 7.5
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_zoldervertrek_kleiner_dan_4m2_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zoldervertrek dat als vertrek is aangeleverd maar kleiner is dan 4 m², wordt als overige ruimte gewaardeerd.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.2.3
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    # 0,01 m² onder de grens van 4 m² van een vertrek.
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                soort=Ruimtesoort.vertrek,
                oppervlakte=3.99,
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.zoldervertrek.naam: 3.99}
    # 3,99 m² is afgerond 4 m², 3 punten.
    assert groep.punten == 3.0
    vergelijk_met_testreferentie(eenheid, groep)


# Kasten


def test_kast_telt_mee_in_het_subtotaal_van_de_overige_ruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast telt mee in het subtotaal van de overige ruimten.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.4
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.2)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging, oppervlakte=2.6, verbonden_ruimten=[kast]
            ),
            # De zolder zonder vaste trap zorgt dat het subtotaal in de uitkomst staat.
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=2.4,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Subtotaal": 5.2,
        "Berging (+1 kast)": 2.8,
        Ruimtedetailsoort.zolder.naam: 2.4,
    }
    assert punten_per_naam(groep) == {
        "Subtotaal": 3.75,
        # De zolder brengt het totaal van 3 op 5 hele m²; de 1,5 punt daarvoor
        # vervalt.
        "Correctie: zolder zonder vaste trap": -1.5,
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_kast_telt_mee_in_de_oppervlakte_van_een_zolder_zonder_vaste_trap(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een zolder zonder vaste trap.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.2.4
    - wettekst, Bijlage I onder A, toelichting rubriek 2
    """
    # Met de kast komt de zolder van 2,6 op 3,5 m²: afgerond 4 m² in plaats van 3.
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.9)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=2.6,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                verbonden_ruimten=[kast],
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Subtotaal": 3.5, "Zolder (+1 kast)": 3.5}
    assert punten_per_naam(groep) == {
        "Subtotaal": 3.0,
        # De zolder met kast is 3,50 m², afgerond 4 m², en daarmee 3 punten waard;
        # meer dan dat vervalt er niet. Zonder de kast zou de aftrek 2,25 zijn.
        "Correctie: zolder zonder vaste trap": -3.0,
    }
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)
