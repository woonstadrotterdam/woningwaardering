"""Oppervlakte van overige ruimten, zelfstandige woonruimten (rubriek 2)."""

import pytest

from tests.input import element, elementen, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
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


def test_OppervlakteVanOverigeRuimten_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        OppervlakteVanOverigeRuimten,
    )


# Voorwaarden van een overige ruimte


def test_toiletruimte_kleiner_dan_2m2_wordt_niet_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een toiletruimte kleiner dan 2 m² wordt niet als overige ruimte gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
    een oppervlakte te hebben van minimaal 2 m²." en "Een toiletruimte wordt
    gewaardeerd als overige ruimte als het voldoet aan de voorwaarden van een
    overige ruimte."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte1", oppervlakte=1.9
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte2", oppervlakte=2.1
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Toiletruimte2": 2.1}
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_kleiner_dan_4m2_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², wordt als overige ruimte gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: een overige ruimte
    is een ruimte waarvoor geldt "De ruimte voldoet niet aan de eisen voor een
    vertrek (zie vaste toelichting onder 1) of een verkeersruimte".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.2: "Een
    ruimte met `Ruimtesoort` `vertrek` komt in aanmerking voor waardering in de
    rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minder dan 4 m²
    en minimaal 2 m² is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer, soort=Ruimtesoort.vertrek, oppervlakte=3
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.slaapkamer.naam: 3.0}
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


# Privé parkeerruimte


def test_garage_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een garage die bij de woning hoort, wordt als overige ruimte gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Parkeerruimte die
    exclusief tot één adres behoort (privé-garage), wordt gewaardeerd als
    overige ruimte." en "Overige ruimten worden gewaardeerd met driekwart punt
    per vierkante meter."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.garage, naam="Garage1", oppervlakte=15),
            ruimte(Ruimtedetailsoort.garage, naam="Garage2", oppervlakte=15),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Garage1": 15.0, "Garage2": 15.0}
    assert groep.punten == 22.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte zonder vaste trap


def test_zolder_zonder_vaste_trap_krijgt_5_punten_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder zonder vaste trap krijgt 5 punten aftrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Is er een
    `vlizotrap` en geen `trap`, dan geldt daarbij de puntenaftrek van 2.2.2.3."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "De
    detailsoort draagt eis 1 dus zelf; alleen het `Bouwkundigelement`
    `vlizotrap` weerspreekt dat."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zolder,
                naam="Zolder1",
                elementen=[element(Bouwkundigelementdetailsoort.trap)],
            ),
            # Zonder trap als bouwkundig element: de detailsoort gaat uit van
            # een vaste trap.
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

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Staan er
    zowel een `trap` als een `vlizotrap` op de ruimte, dan is de vaste trap
    leidend."
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
            6.0,
            4.4,
            -3.0,
            4.5,
            id="totaal_naar_beneden_afgerond",
            marks=pytest.mark.toelichting(
                "de zolder van 4,40 m² brengt het totaal van 6,00 op 10,40 m², "
                "afgerond van 6 op 10 m²; de 3 punten voor die 4 m² vervallen."
            ),
        ),
        pytest.param(
            6.85,
            2.67,
            -2.25,
            5.25,
            id="totaal_naar_boven_afgerond",
            marks=pytest.mark.toelichting(
                "de zolder van 2,67 m² brengt het totaal van 6,85 op 9,52 m², "
                "afgerond van 7 op 10 m²; de 2,25 punten voor die 3 m² vervallen."
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd, doch niet met meer punten dan voor de
    oppervlakte van de zolderruimten wordt gegeven." en "Waardering in punten
    vindt na saldering en afronding plaats."
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
        "Subtotaal": 7.5,
        "Correctie: zolder zonder vaste trap": verwachte_aftrek,
    }
    assert groep.punten == verwachte_punten
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte aangeleverd als vertrek


def test_zoldervertrek_met_alleen_een_vlizotrap_krijgt_de_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zoldervertrek dat alleen via een vlizotrap bereikbaar is, krijgt als overige ruimte 5 punten aftrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Een
    zolderruimte van minimaal 2m2 wordt daarmee altijd gewaardeerd onder
    `Oppervlakte van overige ruimten`. Is er een `vlizotrap` en geen `trap`, dan
    geldt daarbij de puntenaftrek van 2.2.2.3."
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


def test_zolderruimte_die_geen_vertrek_kan_zijn_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolderruimte die als vertrek is aangeleverd maar niet aan de eisen van een vertrek voldoet, wordt als overige ruimte gewaardeerd.

    De package waarschuwt bij de ruimte met de detailsoort `zolder`.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Onder overige
    ruimten, voor zover zij niet voldoen aan de eisen voor een vertrek, worden
    onder andere verstaan: bijkeukens, bergingen, wasruimten, schuren, zolders
    en kelders."

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Voldoet
    een zolderruimte niet aan die eisen, dan wordt gekeken of deze als overige
    ruimte kan worden gewaardeerd. Dat gebeurt ook wanneer de ruimte is
    ingeschoten met `ruimtesoort` `vertrek`, net zoals bij andere vertrekken die
    de minimale oppervlakte van 4m2 niet halen (zie 2.2.1.2)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Te klein voor een vertrek.
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek1",
                soort=Ruimtesoort.vertrek,
                oppervlakte=3,
            ),
            # Geen vaste trap; als overige ruimte geldt daarvoor de aftrek.
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek2",
                soort=Ruimtesoort.vertrek,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
            # De detailsoort zolder voldoet niet aan de afwerkingseisen van een
            # vertrek.
            ruimte(Ruimtedetailsoort.zolder, soort=Ruimtesoort.vertrek),
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Subtotaal": 23.0,
        "Zoldervertrek1": 3.0,
        "Zoldervertrek2": 10.0,
        Ruimtedetailsoort.zolder.naam: 10.0,
    }
    assert zolders_met_aftrek(groep) == ["zoldervertrek2"]
    assert punten_per_naam(groep) == {
        "Subtotaal": 17.25,
        "Correctie: zolder zonder vaste trap": -5.0,
    }
    assert groep.punten == 12.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Kasten


def test_kast_telt_mee_in_het_subtotaal_van_de_overige_ruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast telt mee in het subtotaal van de overige ruimten.

    Het subtotaal staat in de uitkomst wanneer er een zolder zonder vaste trap
    is; de aftrek voor die zolder komt daarop in mindering.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
    oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
    boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
    woning behorende kasten".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.2)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging, oppervlakte=2.6, verbonden_ruimten=[kast]
            ),
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
    oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
    boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
    woning behorende kasten".

    Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.2)
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

    assert aantal_per_naam(groep) == {"Subtotaal": 2.8, "Zolder (+1 kast)": 2.8}
    assert punten_per_naam(groep) == {
        "Subtotaal": 2.25,
        # De zolder is 2,25 punten waard; meer dan dat vervalt er niet.
        "Correctie: zolder zonder vaste trap": -2.25,
    }
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)
