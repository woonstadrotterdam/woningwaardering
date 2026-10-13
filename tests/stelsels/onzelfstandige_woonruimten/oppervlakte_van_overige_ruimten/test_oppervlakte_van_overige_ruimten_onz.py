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

    De garage en de bijkeuken komen uit het rekenvoorbeeld in de toelichting
    bij de wettekst en zijn hier gemeenschappelijk voor drie onzelfstandige
    woonruimten. De wettekst deelt de punten, haar rekenvoorbeeld bij rubriek 1
    de oppervlakte. De package deelt de oppervlakte; punten delen zou hier
    9,25 punten geven. Het scenario onderscheidt niet of er één keer of per
    soort ruimte wordt afgerond: beide geven 9 punten.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 2: "De punten voor
    de oppervlakte van overige ruimten worden gedeeld door het aantal
    onzelfstandige woonruimten op één adres dat toegang en gebruiksrecht
    heeft."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1: "het
    rekenvoorbeeld in de wettekst deelt m²-aandelen en telt die op" en "per
    ruimte delen waar nodig, salderen, daarna éénmaal afronden op hele m²,
    daarna × 0,75."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Aangeleverd als overige ruimte; daardoor telt de slaapkamer in
            # deze rubriek.
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=4,
            ),
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
    assert groep.punten == 9.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_overige_ruimte_wordt_gedeeld_door_aantal_woonruimten_met_toegang(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke overige ruimte wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot die ruimte.

    De wettekst deelt de punten. De package deelt per ruimte de oppervlakte;
    punten delen zou hier 2,75 punten geven.

    Bron: wettekst, Bijlage I onder B, onderdeel 2: "Oppervlakte
    gemeenschappelijke overige ruimte(n) op hetzelfde adres, niet zijnde
    verkeersruimten (o.a. berging, zolder, garage)", "0,75 punt per m², te
    delen door het aantal onzelfstandige woonruimten dat toegang en
    gebruiksrecht heeft".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
    adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
    een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
    aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
    het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
    toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
    voorziening(en)."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1: "per
    ruimte delen waar nodig, salderen, daarna éénmaal afronden op hele m²,
    daarna × 0,75."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.bijkeuken,
                gedeeld_met_aantal_onzelfstandige_woonruimten=5,
            ),
            ruimte(
                Ruimtedetailsoort.garage,
                gedeeld_met_aantal_onzelfstandige_woonruimten=6,
            ),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Gedeeld met 5 onzelfstandige woonruimten": {
            Ruimtedetailsoort.bijkeuken.naam: 10.0
        },
        "Gedeeld met 6 onzelfstandige woonruimten": {
            Ruimtedetailsoort.garage.naam: 10.0
        },
    }
    assert groep.punten == 3.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_oppervlakte_wordt_een_keer_afgerond_na_optellen_van_alle_overige_ruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte wordt één keer afgerond op hele vierkante meters, nadat de toe te rekenen oppervlakte van alle overige ruimten is opgeteld.

    Het beleidsboek rondt privé en gemeenschappelijke overige ruimten
    afzonderlijk af; dat geeft hier 20 m² in plaats van 21 m². De package volgt
    de keuze uit de implementatietoelichting. De zolder heeft een vlizotrap:
    daardoor staat het subtotaal in de uitkomst en komt de aftrek voor die
    zolder daarop in mindering.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De afronding van
    de oppervlakte van alle overige ruimte samen vindt plaats op hele
    vierkante meters na saldering van de oppervlakte van de afzonderlijke
    overige ruimten; bij 0,5 m² of meer wordt naar boven afgerond, bij minder
    dan 0,5 m² naar beneden."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: beleidsboek onzelfstandige woonruimten, 2.2.2.1: "De oppervlakten
    voor privé- en gemeenschappelijke overige ruimten worden afzonderlijk
    berekend."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1: "per
    ruimte delen waar nodig, salderen, daarna éénmaal afronden op hele m²,
    daarna × 0,75." en "dat past bij delen vóór afronden (20,50 → 21 m²), niet
    bij apart afronden per categorie (20 m² → 15,00)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    # Het subtotaal heeft zelf geen aantal: elke ruimte toont haar eigen
    # oppervlakte, de punten volgen uit de toe te rekenen oppervlakte.
    assert aantal_per_bovenliggende(groep) == {
        "Privé": {Ruimtedetailsoort.berging.naam: 10.4},
        "Gedeeld met 4 onzelfstandige woonruimten": {
            Ruimtedetailsoort.zolder.naam: 40.4
        },
    }
    assert punten_per_naam(groep)["Subtotaal"] == 15.75
    assert groep.punten == 14.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_overige_ruimte_gedeeld_met_0_onzelfstandige_woonruimten_is_prive(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een overige ruimte met `gedeeld_met_aantal_onzelfstandige_woonruimten` 0 wordt als privéruimte gewaardeerd.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.1.4: "Indien
    deze property leeg is of kleiner is dan 2, tellen we de ruimte mee als
    zijnde niet gedeeld."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Aangeleverd als overige ruimte; daardoor telt de slaapkamer in
            # deze rubriek.
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                soort=Ruimtesoort.overige_ruimten,
                oppervlakte=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=0,
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

    De bijkeuken heeft `gedeeld_met_aantal_adressen` 1. Pas vanaf twee adressen
    hoort een ruimte in rubriek 9.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9:
    "Gemeenschappelijke vertrekken en overige ruimten zijn tot het woongebouw
    behorende binnenruimten waar de bewoners van tenminste twee adressen in het
    woongebouw krachtens de huurovereenkomst exclusieve toegang en
    gebruiksrecht toe hebben."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: beleidsboek onzelfstandige woonruimten, 2.2: "Gemeenschappelijke
    ruimten die worden gedeeld met twee of meer adressen worden gewaardeerd
    onder rubriek 9."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
    een oppervlakte te hebben van minimaal 2 m²." en "Een toiletruimte wordt
    gewaardeerd als overige ruimte als het voldoet aan de voorwaarden van een
    overige ruimte."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(Ruimtedetailsoort.toiletruimte, oppervlakte=1),
            ruimte(Ruimtedetailsoort.bijkeuken, oppervlakte=2),
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {Ruimtedetailsoort.bijkeuken.naam: 2.0}
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_vertrek_kleiner_dan_4m2_wordt_als_overige_ruimte_gewaardeerd(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een ruimte die als vertrek is aangeleverd maar kleiner is dan 4 m², wordt als overige ruimte gewaardeerd.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: een overige ruimte
    is een ruimte waarvoor geldt "De ruimte voldoet niet aan de eisen voor een
    vertrek (zie vaste toelichting onder 1) of een verkeersruimte".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.2: "Een
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


# Zolderruimte zonder vaste trap


def test_zolder_zonder_vaste_trap_krijgt_5_punten_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder zonder vaste trap krijgt 5 punten aftrek.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "Is er
    een `vlizotrap` en geen `trap`, dan geldt daarbij de puntenaftrek van
    2.2.2.3."
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

    Zolder2 is als vertrek aangeleverd; de package waardeert haar als overige
    ruimte en waarschuwt daarbij. Zolder3 is gemeenschappelijk voor drie
    onzelfstandige woonruimten, waardoor de maximale aftrek door drie wordt
    gedeeld.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: beleidsboek onzelfstandige woonruimten, 2.1.6: "Het totaal aantal
    punten wordt per rubriek afgerond op 0,25 punt".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "De
    detailsoort draagt eis 1 dus zelf; alleen het `Bouwkundigelement`
    `vlizotrap` weerspreekt dat." en "Dat gebeurt ook wanneer de ruimte is
    ingeschoten met `ruimtesoort` `vertrek`".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3: "De
    maximumaftrek van 5 punten wordt gedeeld door het aantal onzelfstandige
    woonruimten."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            # Zonder trap als bouwkundig element: de detailsoort gaat uit van
            # een vaste trap.
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder1"),
            ruimte(Ruimtedetailsoort.zolder, naam="Zolder2", soort=Ruimtesoort.vertrek),
            ruimte(
                Ruimtedetailsoort.zolder,
                naam="Zolder3",
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
        ]
    )

    with pytest.warns(UserWarning, match="aangeleverd als") as waarschuwingen:
        groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        "Privé": {"Zolder1": 10.0, "Zolder2": 10.0},
        "Gedeeld met 3 onzelfstandige woonruimten": {"Zolder3": 10.0},
    }
    assert zolders_met_aftrek(groep) == ["zolder3"]
    assert punten_per_naam(groep) == {
        "Subtotaal": 17.25,
        # De aftrek is 5/3 punt en staat op twee decimalen in de uitkomst; het
        # totaal is met de onafgeronde aftrek berekend en daarna afgerond.
        "Correctie: zolder zonder vaste trap": -1.67,
        "Afronding op kwartpunten": -0.08,
    }
    assert groep.punten == 15.5
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_zolder_met_trap_en_vlizotrap_krijgt_geen_aftrek(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """Een zolder met zowel een trap als een vlizotrap krijgt geen aftrek.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "Staan
    er zowel een `trap` als een `vlizotrap` op de ruimte, dan is de vaste trap
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

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
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


def test_maximale_aftrek_voor_zolder_wordt_gedeeld_door_aantal_woonruimten(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De maximale aftrek van 5 punten voor een gemeenschappelijke zolder zonder vaste trap wordt gedeeld door het aantal onzelfstandige woonruimten.

    Het scenario is het voorbeeld uit de implementatietoelichting. Volgens die
    toelichting trekt de huurprijscheck hier de volle 5 punten af; de package
    volgt de wettekst.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 2: "De punten voor
    de oppervlakte van overige ruimten worden gedeeld door het aantal
    onzelfstandige woonruimten op één adres dat toegang en gebruiksrecht
    heeft."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3: "De
    maximumaftrek van 5 punten wordt gedeeld door het aantal onzelfstandige
    woonruimten.", "maximumaftrek: 5 / 4 = 1,25" en "Omdat wettekst en tool
    botsen, volgen wij de wettekst (gedeelde cap)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
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
        "Correctie: zolder zonder vaste trap": -1.25,
    }
    assert groep.punten == 14.5
    vergelijk_met_testreferentie(eenheid, groep)


# Kasten


def test_kast_telt_mee_in_de_oppervlakte_van_een_overige_ruimte(
    oppervlakte_van_overige_ruimten, vergelijk_met_testreferentie
):
    """De oppervlakte van een kast telt mee in de oppervlakte van de overige ruimte waarop de kast uitkomt.

    De zolder zonder vaste trap hoort bij het scenario: de aftrek voor die
    zolder hangt af van de oppervlakte van de andere overige ruimten, en dus
    van de berging met haar kast.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
    oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
    boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
    woning behorende kasten".

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.2)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging, oppervlakte=2.4, verbonden_ruimten=[kast]
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
        "Berging (+1 kast)": 2.6,
        Ruimtedetailsoort.zolder.naam: 2.4,
    }
    assert punten_per_naam(groep) == {
        "Subtotaal": 3.75,
        # De berging met kast is 2,60 m², afgerond 3 m²; de zolder brengt het
        # totaal op 5 m². De 1,5 punt voor die 2 m² vervalt.
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

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
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
                oppervlakte=2.4,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                verbonden_ruimten=[kast],
            )
        ]
    )

    groep = oppervlakte_van_overige_ruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {"Zolder (+1 kast)": 2.6}
    assert punten_per_naam(groep) == {
        "Subtotaal": 2.25,
        # De zolder met kast is 2,60 m², afgerond 3 m², en daarmee 2,25 punten
        # waard; meer dan dat vervalt er niet.
        "Correctie: zolder zonder vaste trap": -2.25,
    }
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)
