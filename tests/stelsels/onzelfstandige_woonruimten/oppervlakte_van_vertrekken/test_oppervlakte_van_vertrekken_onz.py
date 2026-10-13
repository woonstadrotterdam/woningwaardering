"""Oppervlakte van vertrekken, onzelfstandige woonruimten (rubriek 1)."""

import pytest

from tests.input import element, ruimte
from tests.utils import (
    aantal_per_bovenliggende,
    aantal_per_naam,
    assert_stelselgroep_output,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def oppervlakte_van_vertrekken(peildatum):
    return OppervlakteVanVertrekken(peildatum=peildatum)


def test_OppervlakteVanVertrekken_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        OppervlakteVanVertrekken,
    )


# Gemeenschappelijke vertrekken


def test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """De oppervlakte van privévertrekken en de toe te rekenen oppervlakte van gemeenschappelijke vertrekken worden opgeteld.

    Het scenario is het rekenvoorbeeld uit de toelichting bij de wettekst, met
    de keuken als gemeenschappelijk vertrek van drie onzelfstandige
    woonruimten. Het onderscheidt niet of er één keer of per soort vertrek
    wordt afgerond: beide geven 19 punten.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 1: "Het aantal m² dat
    volgens rubriek 1 aan de huurder is toe te rekenen is 10 m² + (40 m²/4) =
    20 m²."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "De oppervlakte
    per vertrek wordt afgerond op twee decimalen. De afronding van de
    oppervlakte van alle vertrekken samen vindt plaats op hele vierkante meters
    na saldering van de oppervlakte van alle vertrekken; bij 0,5 m² of meer
    wordt afgerond naar boven, bij minder dan 0,5 m² naar beneden."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=15.4912),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=11.2395,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 15.49},
        "Gedeeld met 3 onzelfstandige woonruimten": {
            Ruimtedetailsoort.keuken.naam: 11.24
        },
    }
    assert groep.punten == 19.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijk_vertrek_wordt_gedeeld_door_aantal_woonruimten_met_toegang(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een gemeenschappelijk vertrek wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot dat vertrek.

    Bron: wettekst, Bijlage I onder B, onderdeel 1: "Oppervlakte
    gemeenschappelijk(e) vertrek(ken) op hetzelfde adres", "1 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
    adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
    een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
    aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
    het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
    toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
    voorziening(en)."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.1.1: "Daarom
    volgen wij: per ruimte delen waar nodig, salderen, daarna éénmaal afronden
    op hele m²."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Gedeeld met 6 onzelfstandige woonruimten": {
            Ruimtedetailsoort.woonkamer.naam: 10.0
        },
        "Gedeeld met 5 onzelfstandige woonruimten": {
            Ruimtedetailsoort.slaapkamer.naam: 10.0
        },
    }
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_valt_onder_rubriek_1(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een vertrek dat niet met een ander adres wordt gedeeld, wordt in rubriek 1 gewaardeerd en niet in rubriek 9.

    Het vertrek heeft `gedeeld_met_aantal_adressen` 1. Pas vanaf twee adressen
    hoort een ruimte in rubriek 9.

    Bron: beleidsboek onzelfstandige woonruimten, 2.2: "Gemeenschappelijke
    ruimten die worden gedeeld met twee of meer adressen worden gewaardeerd
    onder rubriek 9."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.4:
    "Gemeenschappelijke vertrekken die met meerdere adressen worden gedeeld
    (`gedeeldMetAantalAdressen` ≥ 2)" en "Rubriek 1 dekt alleen privévertrekken
    en gemeenschappelijke vertrekken op hetzelfde adres; ruimten gedeeld met
    meerdere adressen vallen onder rubriek 9".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                oppervlakte=5,
                gedeeld_met_aantal_adressen=1,
            )
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.slaapkamer.naam: 5.0}
    }
    assert groep.punten == 5.0
    vergelijk_met_testreferentie(eenheid, groep)


# Voorwaarden van een vertrek


def test_vertrek_moet_minimaal_4m2_groot_zijn(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een ruimte kleiner dan 4 m² wordt niet als vertrek gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "De ruimte dient
    een oppervlakte te hebben van minimaal 4 m²."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer1", oppervlakte=3),
            ruimte(Ruimtedetailsoort.slaapkamer, naam="Slaapkamer2", oppervlakte=4),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Slaapkamer2": 4.0}
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_keuken_en_badkamer_zijn_ook_onder_4m2_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken en een badkamer zijn ook onder de 4 m² een vertrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
    bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
    badkamer of doucheruimte altijd een vertrek."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.keuken, oppervlakte=2),
            ruimte(Ruimtedetailsoort.badkamer_met_toilet, oppervlakte=2),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        Ruimtedetailsoort.keuken.naam: 2.0,
        Ruimtedetailsoort.badkamer_met_toilet.naam: 2.0,
    }
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


# Aangeleverde ruimtesoort


def test_keuken_aangeleverd_als_overige_ruimte_is_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een keuken die als overige ruimte is aangeleverd, wordt als vertrek gewaardeerd.

    De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
    ruimtesoort waarmee de keuken is gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
    bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
    badkamer of doucheruimte altijd een vertrek."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.2:
    "Uitzonderingen: keuken, badkamer en doucheruimte zijn volgens het
    beleidsboek altijd een vertrek, en zo waarderen wij die ook, los van het
    meegegeven `Ruimtesoort`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=1,
            )
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.keuken.naam: 1.0}
    assert groep.punten == 1.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Zolderruimte


def test_zoldervertrek_is_een_vertrek_tenzij_er_alleen_een_vlizotrap_is(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een zoldervertrek is een vertrek, tenzij het alleen via een vlizotrap bereikbaar is.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Zolderruimten
    slechts als vertrek gewaardeerd worden, indien deze bereikbaar zijn via een
    vaste trap en indien de vloer begaanbaar en het dak beschoten is."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "De
    detailsoort draagt eis 1 dus zelf; alleen het `Bouwkundigelement`
    `vlizotrap` weerspreekt dat."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek1",
                elementen=[element(Bouwkundigelementdetailsoort.trap)],
            ),
            # Zonder trap als bouwkundig element: de detailsoort gaat uit van
            # een vaste trap.
            ruimte(Ruimtedetailsoort.zoldervertrek, naam="Zoldervertrek2"),
            ruimte(
                Ruimtedetailsoort.zoldervertrek,
                naam="Zoldervertrek3",
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
            ),
        ]
    )

    groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Zoldervertrek1": 10.0,
        "Zoldervertrek2": 10.0,
    }
    assert groep.punten == 20.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_zolder_is_nooit_een_vertrek(
    oppervlakte_van_vertrekken, vergelijk_met_testreferentie
):
    """Een zolderruimte met de detailsoort `zolder` wordt nooit als vertrek gewaardeerd.

    De package waarschuwt bij de zolder die als vertrek is aangeleverd: die
    wordt als overige ruimte gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Zolderruimten
    slechts als vertrek gewaardeerd worden, indien deze bereikbaar zijn via een
    vaste trap en indien de vloer begaanbaar en het dak beschoten is."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "Alleen
    een `zoldervertrek` voldoet aan eis 2"; een `zolder` "voldoet niet aan de
    afwerkingseisen" en "wordt daarom nooit als vertrek gewaardeerd". En:
    "Andersom geldt dit niet: een zolderruimte die is ingeschoten met
    `ruimtesoort` `overige ruimte` wordt nooit als vertrek gewaardeerd."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder1", soort=Ruimtesoort.vertrek),
            # Aangeleverd als overige ruimte.
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder2", oppervlakte=1),
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_vertrekken.waardeer(eenheid)

    assert aantal_per_naam(groep) == {}
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
