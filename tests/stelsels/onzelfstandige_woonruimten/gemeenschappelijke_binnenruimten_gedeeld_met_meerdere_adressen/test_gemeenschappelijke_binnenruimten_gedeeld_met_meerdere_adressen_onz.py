"""Gemeenschappelijke binnenruimten gedeeld met meerdere adressen, onzelfstandige woonruimten (rubriek 9)."""

import pytest

from tests.input import aanrecht, element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen import (
    GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Installatiesoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen(peildatum):
    return GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(
        peildatum=peildatum
    )


def test_GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    )


# Oppervlakte


def test_gemeenschappelijke_overige_ruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijke overige ruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

    Bron: wettekst, Bijlage I onder B, rubriek 9: "Gemeenschappelijke overige
    ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft, en daarna gedeeld door het aantal onzelfstandige
    woonruimten op dat adres".

    De package deelt de punten en niet de oppervlakte. De berging telt daardoor
    mee, ook al is haar oppervlakte per adres kleiner dan de 2 m² die een
    overige ruimte minimaal groot is.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1: "Anders
    dan rubriek 1 en 2 deelt rubriek 9 niet de oppervlakte, maar de punten."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal of het
    een vertrek of een overige ruimte is en bereken de oppervlaktepunten:" en
    "Deel dit aantal punten door het aantal adressen dat toegang heeft tot de
    gemeenschappelijke binnenruimten."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
    een oppervlakte te hebben van minimaal 2 m²."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    In het totaal zit ook het punt voor de verwarming van de berging, op
    dezelfde manier gedeeld; het wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal de punten
    voor verkoeling en verwarming conform rubriek 3;"

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
    overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
    waardering van één punt toegepast".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 9: "De punten voor
    een gemeenschappelijke binnenruimte worden na verdeling over de meerdere
    adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat
    adres."

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=19,
                verwarmd=True,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        # 19 m² is 14,25 punten; gedeeld door 10 adressen en 2 woonruimten is
        # dat 0,7125 punt, in het rapport 0,71. De oppervlakte delen zou 0,95 m²
        # geven: minder dan 2 m², of afgerond 1 m² en 0,75 punt.
        "Gedeeld met 10 adressen": {"Oppervlakte van overige ruimten": 0.71},
        # 1 punt gedeeld door 10 adressen en 2 woonruimten.
        "Verwarmde overige en verkeersruimten": {Ruimtedetailsoort.berging.naam: 0.05},
        # Samen 0,7625 punt, afgerond op kwartpunten 0,75.
        None: {"Afronding op kwartpunten": -0.01},
    }
    assert groep.punten == 0.75
    vergelijk_met_testreferentie(eenheid, groep)


# Gedeeld met meerdere adressen


def test_vertrek_dat_niet_met_een_ander_adres_wordt_gedeeld_krijgt_geen_punten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Een gemeenschappelijk vertrek dat niet met een ander adres wordt gedeeld, krijgt in deze rubriek geen punten.

    De slaapkamers worden met 2 onzelfstandige woonruimten op hetzelfde adres
    gedeeld en hebben geen `gedeeld_met_aantal_adressen`. Pas vanaf twee
    adressen hoort een ruimte in rubriek 9.

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

    Bron: implementatietoelichting, datamodel-uitbreidingen, "Gedeeld met aantal
    adressen": "Het attribuut `gedeeld_met_aantal_adressen` geeft het aantal
    adressen weer waarmee een bepaalde ruimte wordt gedeeld."
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
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {}
    assert groep.punten == 0.0
    vergelijk_met_testreferentie(eenheid, groep)


# Zolderruimte zonder vaste trap


def test_aftrek_voor_gemeenschappelijke_zolder_zonder_vaste_trap_wordt_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De aftrek van 5 punten voor een gemeenschappelijke zolder zonder vaste trap wordt gedeeld door het aantal adressen dat toegang heeft.

    De ruimten worden niet met andere onzelfstandige woonruimten op het adres
    gedeeld; het scenario toont daardoor alleen de deling door het aantal
    adressen.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
    ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

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
                Ruimtedetailsoort.berging,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=16,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {
        # 22 m² is 16,5 punten, gedeeld door 2 adressen.
        "Subtotaal": 8.25,
        "Correctie: zolder zonder vaste trap": -2.5,
    }
    assert groep.punten == 5.75
    vergelijk_met_testreferentie(eenheid, groep)


def test_aftrek_is_niet_hoger_dan_de_punten_voor_de_gemeenschappelijke_zolder(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De aftrek voor een gemeenschappelijke zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
    trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
    zolderruimte met vijf verminderd, doch niet met meer punten dan voor de
    oppervlakte van de zolderruimten wordt gegeven." en "Waardering in punten
    vindt na saldering en afronding plaats."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
    ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=6.33,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {
        # 12,33 m² is afgerond 12 m² en 9 punten, gedeeld door 2 adressen.
        "Subtotaal": 4.5,
        # De zolder brengt het totaal van 6 op 12 hele m²; de 4,5 punten
        # daarvoor vervallen, gedeeld door 2 adressen.
        "Correctie: zolder zonder vaste trap": -2.25,
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijke_zolder_zonder_vaste_trap(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijke zolder zonder vaste trap.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
    oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
    boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
    woning behorende kasten" en "Indien geen vaste trap aanwezig is, wordt het
    aantal punten van de vloeroppervlakte van de zolderruimte met vijf
    verminderd, doch niet met meer punten dan voor de oppervlakte van de
    zolderruimten wordt gegeven."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
    kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
    (4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
    onder meer energieprestatie, gemeenschappelijke ruimten en
    zoldercorrecties."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
    overige ruimten wordt onder deze rubriek aangesloten bij definities en de
    meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
    ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    kast = ruimte(Ruimtedetailsoort.kast, oppervlakte=0.9)
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                oppervlakte=6,
                gedeeld_met_aantal_adressen=2,
            ),
            ruimte(
                Ruimtedetailsoort.zolder,
                oppervlakte=2.6,
                elementen=[element(Bouwkundigelementdetailsoort.vlizotrap)],
                verbonden_ruimten=[kast],
                gedeeld_met_aantal_adressen=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert aantal_per_naam(groep) == {
        "Subtotaal": 9.5,
        Ruimtedetailsoort.berging.naam: 6.0,
        "Zolder (+1 kast)": 3.5,
    }
    assert punten_per_naam(groep) == {
        # 9,5 m² is afgerond 10 m² en 7,5 punten, gedeeld door 2 adressen.
        "Subtotaal": 3.75,
        # Met haar kast brengt de zolder het totaal van 6 op 10 hele m²; de 3
        # punten daarvoor vervallen, gedeeld door 2 adressen. Zonder de kast
        # zou het totaal 9 hele m² zijn en de aftrek 1,125 punt.
        "Correctie: zolder zonder vaste trap": -1.5,
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


# Verkoeling en verwarming


def test_voor_vertrekken_met_verkoelingsfunctie_geldt_geen_maximum_van_2_punten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Voor gemeenschappelijke vertrekken met verkoelingsfunctie geldt in deze rubriek geen maximum van 2 punten.

    De wettekst verwijst voor verkoeling en verwarming naar rubriek 3, die voor
    de verkoelingsfunctie een maximum van 2 punten kent. De package neemt de
    puntwaarden van rubriek 3 over en de maxima niet; de test legt dat gedrag
    vast.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal de punten
    voor verkoeling en verwarming conform rubriek 3;"

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Er kan één punt
    worden behaald per vertrek, met een totaal maximum van twee punten."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2: "Wij
    nemen daarvan de puntwaarden over (2 per verwarmd vertrek, 1 extra per
    verwarmd én verkoeld vertrek, 1 per verwarmde overige ruimte of
    verkeersruimte), niet de maxima van rubriek 3 (max. 4 verwarmde
    overige/verkeersruimten, max. 2 extra verkoelingspunten). Dit is conform de
    huurprijscheck die in deze rubriek geen maximering toepast."

    Elk punt wordt gedeeld door het aantal adressen en daarna door het aantal
    onzelfstandige woonruimten op het adres.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 9: "De punten voor
    een gemeenschappelijke binnenruimte worden na verdeling over de meerdere
    adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat
    adres."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    In het totaal zitten ook de punten voor de oppervlakte en de verwarming van
    de drie vertrekken en voor het aanrecht van ruim 3 meter in beide keukens.

    Bron: wettekst, Bijlage I onder B, rubriek 9: "Gemeenschappelijke vertrek 1
    punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
    heeft, en daarna gedeeld door het aantal onzelfstandige woonruimten op dat
    adres".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmd
    vertrek wordt, ongeacht de verwarmingswijze, een waardering van twee punten
    toegepast".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal eventueel
    van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7;"

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=20,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken1",
                elementen=[aanrecht(3001)],
                oppervlakte=20,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                naam="Keuken2",
                elementen=[aanrecht(3001)],
                oppervlakte=20,
                verwarmd=True,
                verkoeld=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    # Elk vertrek krijgt 1 punt, gedeeld door 2 adressen en 2 woonruimten. Met
    # het maximum van rubriek 3 zouden de drie vertrekken samen 2 punten
    # krijgen: gedeeld door 4 is dat 0,5 punt.
    assert punten_per_bovenliggende(groep)["Verkoelde vertrekken"] == {
        Ruimtedetailsoort.woonkamer.naam: 0.25,
        "Keuken1": 0.25,
        "Keuken2": 0.25,
    }
    # 60 punten voor de oppervlakte, 6 voor de verwarming, 3 voor de
    # verkoelingsfunctie en 20 voor de aanrechten: 89 punten, gedeeld door 4.
    assert groep.punten == 22.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_vijfde_verwarmde_overige_ruimte_krijgt_ook_een_punt(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Ook de vijfde verwarmde gemeenschappelijke overige ruimte krijgt 1 punt: het maximum van 4 punten uit rubriek 3 geldt niet over de ruimten van deze rubriek samen.

    De wettekst verwijst voor verkoeling en verwarming naar rubriek 3, die voor
    verwarmde overige ruimten een maximum van 4 punten kent. De package neemt
    de puntwaarden van rubriek 3 over en de maxima niet; de test legt dat
    gedrag vast.

    Vier bergingen worden met 2 adressen gedeeld en de vijfde met 3. Een
    maximum per groep ruimten met dezelfde deling zou hier dezelfde punten
    geven; dat onderscheidt het scenario niet.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal de punten
    voor verkoeling en verwarming conform rubriek 3;"

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
    overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
    waardering van één punt toegepast, voor zover de verwarming tot de
    onroerende zaak en zijn onroerende aanhorigheden behoort. Hiervoor geldt
    een maximum van vier punten."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2: "Wij
    nemen daarvan de puntwaarden over (2 per verwarmd vertrek, 1 extra per
    verwarmd én verkoeld vertrek, 1 per verwarmde overige ruimte of
    verkeersruimte), niet de maxima van rubriek 3 (max. 4 verwarmde
    overige/verkeersruimten, max. 2 extra verkoelingspunten). Dit is conform de
    huurprijscheck die in deze rubriek geen maximering toepast."

    Elk punt wordt gedeeld door het aantal adressen en daarna door het aantal
    onzelfstandige woonruimten op het adres.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Deel dit aantal
    punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
    binnenruimten."

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 9: "De punten voor
    een gemeenschappelijke binnenruimte worden na verdeling over de meerdere
    adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat
    adres."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    In het totaal zitten ook de punten voor de oppervlakte van de bergingen;
    het wordt afgerond op een kwart punt.

    Bron: wettekst, Bijlage I onder B, rubriek 9: "Gemeenschappelijke overige
    ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft, en daarna gedeeld door het aantal onzelfstandige
    woonruimten op dat adres".

    Bron: wettekst, Bijlage I onder A, toelichting, inleiding: "De waardering in
    punten per rubriek wordt na saldering afgerond op 0,25 punt waarbij een
    achtste (1/8) punt naar boven wordt afgerond."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging1",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging2",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging3",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging4",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=2,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.berging,
                naam="Berging5",
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_bovenliggende(groep) == {
        # 80 m² is 60 punten, gedeeld door 2 adressen en 2 woonruimten.
        "Gedeeld met 2 adressen": {"Oppervlakte van overige ruimten": 15.0},
        # 20 m² is 15 punten, gedeeld door 3 adressen en 2 woonruimten.
        "Gedeeld met 3 adressen": {"Oppervlakte van overige ruimten": 2.5},
        "Verwarmde overige en verkeersruimten": {
            "Berging1": 0.25,
            "Berging2": 0.25,
            "Berging3": 0.25,
            "Berging4": 0.25,
            # 1 punt gedeeld door 3 adressen en 2 woonruimten is 0,1666… punt:
            # in het rapport 0,17.
            "Berging5": 0.17,
        },
        # Samen 18,67 punten, afgerond op kwartpunten 18,75.
        None: {"Afronding op kwartpunten": 0.08},
    }
    assert groep.punten == 18.75
    vergelijk_met_testreferentie(eenheid, groep)


# Rekenvoorbeeld


def test_rekenvoorbeeld_met_keuken_en_toilet_uit_de_wettekst(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Het rekenvoorbeeld uit de wettekst: een keuken van 20 m² en een toilet van 2 m² die vier adressen delen, geven een van de vier onzelfstandige woonruimten op een adres 2,50 punten.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 9: "(A) een
    gemeenschappelijke binnenruimte met keuken van 20 m², en daarnaast (B) een
    gedeeld toilet van 2 m². Tot beiden hebben vier adressen toegang. Op één
    van deze adressen zijn vier onzelfstandige woonruimten. Vertrek A voldoet
    aan de eisen van een vertrek en wordt gewaardeerd met 20 m² x 1 punt (= 20
    punten) conform rubriek 1. Ruimte B voldoet aan de eisen van een overige
    ruimte en wordt gewaardeerd met 2 m² x 0,75 punten (= 1,5 punt) conform
    rubriek 2. Vertrek A is verwarmd middels een radiator en krijgt daarvoor 2
    punten conform rubriek 3. Het toilet is onverwarmd en ontvangt daarvoor
    geen punten. In vertrek A wordt voldaan aan de minimumeisen van een keuken
    conform rubriek 5. Voor deze rubriek wordt 10 punten toegekend (7 voor het
    aanrecht, en 3 voor de voorzieningen). De toiletruimte B krijgt 4,75 punt
    (3,75 voor het hangend toilet en 1 voor de wastafel). Saldering levert op:
    20 + 1,5 + 2 + 10 + 4,75 = 38,25 punten. Delen door het aantal adressen
    levert op: 38,25 punten / 4 = 9,5625 punten per adres. Vervolgens wordt
    gedeeld door het aantal onzelfstandige woonruimten op het adres, dus
    9,5625/4 = 2,390625 punten per onzelfstandige woonruimte. Afronden
    geschiedt op een kwart punt per onzelfstandige woonruimte op 2,50 punten."

    De 7 punten voor het aanrecht zijn in de input een aanrecht van 2.999 mm,
    de 3 punten voor de voorzieningen een inbouwkoelkast, een elektrische
    inbouwoven en een inbouwmagnetron.

    Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "2 tot 3 m 7 punten".

    Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Inbouw koelkast 1 punt",
    "Inbouw oven elektrisch 1 punt" en "Inbouw magnetron 1 punt".

    De radiator is in de input een bouwkundig element van de keuken. De package
    leest de verwarming af aan `verwarmd`.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.3: "Daarom
    hebben wij `verwarmd` en `verkoeld` als boolean-kenmerken van een
    `EenhedenRuimte` toegevoegd."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                Installatiesoort.inbouw_magnetron,
                Installatiesoort.inbouw_koelkast,
                Installatiesoort.inbouw_oven_elektrisch,
                elementen=[
                    aanrecht(2999),
                    element(Bouwkundigelementdetailsoort.radiator),
                ],
                oppervlakte=20,
                verwarmd=True,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                Installatiesoort.wastafel,
                Installatiesoort.hangend_toilet,
                oppervlakte=2,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
            ),
        ]
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    # Elke waardering is een zestiende van de punten uit het rekenvoorbeeld:
    # gedeeld door 4 adressen en 4 woonruimten. Het rapport toont twee
    # decimalen.
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 4 adressen": {
            "Oppervlakte van vertrekken": 1.25,
            # 1,5 punt gedeeld door 16 is 0,09375 punt.
            "Oppervlakte van overige ruimten": 0.09,
        },
        # 2 punten gedeeld door 16 is 0,125 punt.
        "Verwarmde vertrekken": {Ruimtedetailsoort.keuken.naam: 0.13},
        # 7 punten gedeeld door 16 is 0,4375 punt.
        Ruimtedetailsoort.keuken.naam: {"Lengte aanrecht": 0.44},
        # 1 punt gedeeld door 16 is 0,0625 punt.
        "Extra voorzieningen": {
            Installatiesoort.inbouw_koelkast.naam: 0.06,
            Installatiesoort.inbouw_oven_elektrisch.naam: 0.06,
            Installatiesoort.inbouw_magnetron.naam: 0.06,
        },
        Ruimtedetailsoort.toiletruimte.naam: {
            # 3,75 punten gedeeld door 16 is 0,234375 punt.
            Installatiesoort.hangend_toilet.naam: 0.23,
            Installatiesoort.wastafel.naam: 0.06,
        },
        # De waarderingen in het rapport zijn samen 2,38 punten; het totaal van
        # 2,390625 punten wordt afgerond op kwartpunten 2,50.
        None: {"Afronding op kwartpunten": 0.12},
    }
    assert groep.punten == 2.5
    vergelijk_met_testreferentie(eenheid, groep)


# Zorgwoning


def test_zorgwoning_krijgt_3_punten(
    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    vergelijk_met_testreferentie,
):
    """Een zorgwoning krijgt 3 punten voor de gemeenschappelijke ruimten en voorzieningen.

    Bron: beleidsboek onzelfstandige woonruimten, 2.9.4: "Om arbeidsintensief
    meetwerk te voorkomen kent de Huurcommissie in dat geval een waardering van
    3 punten per woning toe."

    De eenheid heeft de doelgroep zorg en alleen een eigen woonkamer. De
    gemeenschappelijke ruimten zijn niet meegegeven; het scenario toont
    daardoor niet dat de 3 punten in de plaats komen van hun waardering.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1: "Bij een
    zorgwoning tellen ruimten gedeeld met meerdere adressen niet mee, omdat die
    stelselgroep daar door een vaste waardering wordt vervangen."

    De package leest een zorgwoning af aan de doelgroep van de eenheid. De
    implementatietoelichting voor onzelfstandige woonruimten noemt dat niet;
    die voor zelfstandige woonruimten wel.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.12.1: "Wanneer
    een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als
    zorgwoning gewaardeerd."
    """
    eenheid = EenhedenEenheid(
        doelgroep=Doelgroep.zorg,
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer)],
    )

    groep = gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen.waardeer(
        eenheid
    )

    assert punten_per_naam(groep) == {"Zorgwoning": 3.0}
    vergelijk_met_testreferentie(eenheid, groep)
