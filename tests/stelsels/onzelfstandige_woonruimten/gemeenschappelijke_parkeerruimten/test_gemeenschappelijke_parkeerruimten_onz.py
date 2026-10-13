"""Gemeenschappelijke parkeerruimten, onzelfstandige woonruimten (rubriek 10)."""

import pytest

from tests.input import element, ruimte
from tests.utils import (
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_bovenliggende,
    punten_per_naam,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)


@pytest.fixture()
def gemeenschappelijke_parkeerruimten(peildatum):
    return GemeenschappelijkeParkeerruimten(peildatum=peildatum)


def test_GemeenschappelijkeParkeerruimten_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeParkeerruimten,
    )


# Type parkeerplek


def test_parkeerplek_krijgt_9_6_of_4_punten_naar_type_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek krijgt 9 punten als Type I, 6 punten als Type II en 4 punten als Type III, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft en daarna door het aantal onzelfstandige woonruimten op het adres.

    De vier parkeerplekken worden elk met 10 adressen gedeeld en op het eigen
    adres met 2 onzelfstandige woonruimten.

    Bron: wettekst, Bijlage I onder B, rubriek 10: "Type I Parkeerplek in
    afgesloten parkeergarage behorende tot het complex 9 punten gedeeld door het
    aantal adressen dat toegang en gebruiksrecht heeft, en daarna gedeeld door
    het aantal onzelfstandige woonruimten op dat adres", "Type II Parkeerplek
    buiten behorende tot het complex met dak 6 punten gedeeld door het aantal
    adressen dat toegang en gebruiksrecht heeft, en daarna gedeeld door het
    aantal onzelfstandige woonruimten op dat adres" en "Type III Parkeerplek
    buiten behorende tot het complex zonder dak 4 punten gedeeld door het aantal
    adressen dat toegang en gebruiksrecht heeft, en daarna gedeeld door het
    aantal onzelfstandige woonruimten op dat adres".

    Welke ruimtedetailsoort bij welk type hoort, staat in de
    implementatietoelichting. Een parkeerplek in een uitpandige afgesloten
    parkeergarage is net als een inpandige Type I.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type I:
    `Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage`
    (`PIP`) en
    `Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage`
    (`PUP`). Bepalend is de afgesloten parkeergarage, niet of die in- of
    uitpandig is: de wettekst maakt dat onderscheid niet.", "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex`
    (`PBD`)" en "Type III:
    `Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 10 adressen": {
            "Parkeerplek in inpandige afgesloten parkeergarage (Type I)": 0.45,
            "Parkeerplek in uitpandige afgesloten parkeergarage (Type I)": 0.45,
            "Parkeerplek buiten met dak behorend bij complex (Type II)": 0.3,
            "Parkeerplek buiten behorend bij complex (Type III)": 0.2,
        },
        # Samen 1,4 punten, afgerond op kwartpunten 1,5.
        None: {"Afronding op kwartpunten": 0.1},
    }
    assert groep.punten == 1.5
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_carport_wordt_als_type_ii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke carport wordt als Type II gewaardeerd.

    De carport wordt met 3 adressen gedeeld; op het eigen adres heeft één
    onzelfstandige woonruimte toegang.

    Bron: beleidsboek onzelfstandige woonruimten, 2.10.3: "Type II: een
    parkeerplek buiten behorende tot het complex of de woning met dak
    (hieronder telt een carport)".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
    en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

    Bron: wettekst, Bijlage I onder B, rubriek 10: "Type II Parkeerplek buiten
    behorende tot het complex met dak 6 punten gedeeld door het aantal adressen
    dat toegang en gebruiksrecht heeft, en daarna gedeeld door het aantal
    onzelfstandige woonruimten op dat adres".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 3 adressen": {"Carport (Type II)": 2.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_gemeenschappelijke_parkeerplaats_wordt_als_type_iii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke parkeerplaats wordt als Type III gewaardeerd.

    De parkeerplaats wordt met 3 adressen gedeeld; op het eigen adres heeft één
    onzelfstandige woonruimte toegang. De package waarschuwt dat bij een
    gemeenschappelijke parkeerplek een Type-detailsoort hoort.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type
    III: `Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`) en,
    wanneer die gemeenschappelijk is, `Ruimtedetailsoort.parkeerplaats` (`PAR`).
    Bij die laatste volgt een `UserWarning` dat een Type-detailsoort meer op
    zijn plaats is: `PAR` legt het type niet vast."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder B, rubriek 10: "Type III Parkeerplek buiten
    behorende tot het complex zonder dak 4 punten gedeeld door het aantal
    adressen dat toegang en gebruiksrecht heeft, en daarna gedeeld door het
    aantal onzelfstandige woonruimten op dat adres".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    with pytest.warns(UserWarning, match="Gebruik Type I, II of III") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 4 punten gedeeld door 3 adressen is 1,333… punt: in het rapport 1,33 en
    # afgerond op kwartpunten 1,25.
    assert punten_per_bovenliggende(groep)["Gedeeld met 3 adressen"] == {
        "Parkeerplaats (Type III)": 1.33
    }
    assert groep.punten == 1.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Rekenmethode


def test_parkeerplekken_worden_elk_door_hun_eigen_aantal_adressen_en_onzelfstandige_woonruimten_gedeeld(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Parkeerplekken met een verschillend aantal adressen en onzelfstandige woonruimten worden elk door hun eigen aantallen gedeeld.

    De parkeerplek in de parkeergarage wordt met 3 adressen en 2 onzelfstandige
    woonruimten gedeeld, de carport met 4 adressen en 3 onzelfstandige
    woonruimten en de parkeerplek buiten met 5 adressen en 3 onzelfstandige
    woonruimten.

    Bron: beleidsboek onzelfstandige woonruimten, 2.10.4: "Het puntenaantal moet
    worden berekend door het puntenaantal per gemeenschappelijke parkeerplek te
    delen door aantal adressen dat toegang heeft tot de parkeerplek. Dit getal
    moet daarna worden gedeeld door het aantal onzelfstandige woonruimten op het
    eigen woonadres, om tot het puntenaantal voor de onzelfstandige woonruimte
    te komen."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
    adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
    een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
    aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
    het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
    toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
    voorziening(en)."

    Bron: wettekst, Bijlage I onder B, rubriek 10: "Type I Parkeerplek in
    afgesloten parkeergarage behorende tot het complex 9 punten", "Type II
    Parkeerplek buiten behorende tot het complex met dak 6 punten" en "Type III
    Parkeerplek buiten behorende tot het complex zonder dak 4 punten".

    De gemeenschappelijke carport is een parkeerplek van Type II.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
    en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            ),
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=4,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=5,
                gedeeld_met_aantal_onzelfstandige_woonruimten=3,
            ),
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 3 adressen": {
            "Parkeerplek in inpandige afgesloten parkeergarage (Type I)": 1.5
        },
        "Gedeeld met 4 adressen": {"Carport (Type II)": 0.5},
        # 4 punten gedeeld door 5 adressen en door 3 woonruimten is 0,266… punt:
        # in het rapport 0,27.
        "Gedeeld met 5 adressen": {
            "Parkeerplek buiten behorend bij complex (Type III)": 0.27
        },
        # Samen 2,266… punten, afgerond op kwartpunten 2,25.
        None: {"Afronding op kwartpunten": -0.02},
    }
    assert groep.punten == 2.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_rekenvoorbeeld_met_vijf_parkeerplekken_uit_de_wettekst(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Het rekenvoorbeeld uit de wettekst: vijf Type III-parkeerplekken die tien adressen delen, geven een van de vier onzelfstandige woonruimten op een adres 0,50 punt.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 10: "in een
    woongebouw bevinden zich tien adressen. Op één van deze adressen zijn vier
    onzelfstandige woonruimten.", "Bij het woongebouw horen vijf type-III
    parkeerplaatsen. De vijf parkeerplaatsen leveren 5 x 4 = 20 punten op. De
    parkeerplaatsen worden gedeeld door tien adressen, dus 20/10 = 2 punten per
    adres. Op het adres van A zijn vier onzelfstandige woonruimten, dus voor A
    resulteert dit in 2/4 = 0,50 punt in de rubriek parkeerruimte."

    De vijf parkeerplekken zijn één ruimte met `aantal` 5.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Daartoe
    is het attribuut `Eenhedenruimte.aantal` als uitbreiding op het VERA-model
    toegevoegd. Hierdoor is het mogelijk om aan te geven tot hoeveel van de
    parkeerruimten de eenheid toegang heeft zonder dat elk parkeervak van een
    parkeergarage of parkeerterrein meegegeven dient te worden."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type
    III: `Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex` (`PBC`)".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=4,
                aantal=5,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Parkeerplek buiten behorend bij complex (Type III)": 5.0
    }
    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 10 adressen": {
            "Parkeerplek buiten behorend bij complex (Type III)": 0.5
        }
    }
    assert groep.punten == 0.5
    vergelijk_met_testreferentie(eenheid, groep)


# Laadpaal


def test_laadpaal_bij_parkeerplek_krijgt_2_punten_gedeeld_door_het_aantal_adressen(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek krijgt 2 punten extra, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

    De carport wordt met 3 adressen gedeeld; op het eigen adres heeft één
    onzelfstandige woonruimte toegang.

    Bron: beleidsboek onzelfstandige woonruimten, 2.10.5: "Als de parkeerplek
    beschikt over een laadpaal voor elektrisch rijden, die exclusief is voor
    gebruik door bewoners, dan worden 2 extra punten toegekend, gedeeld door het
    aantal adressen dat toegang en gebruiksrecht heeft."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Indien er sprake
    is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee
    punten extra per parkeerplek met laadpaal." en "Daarna wordt dit
    puntentotaal gedeeld door het aantal adressen dat gebruik kan maken van de
    parkeerplek(ken)."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=15,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    # 2 punten gedeeld door 3 adressen is 0,666… punt: in het rapport 0,67.
    assert punten_per_naam(groep)["Laadpaal"] == 0.67
    # Met de 2 punten van de carport samen 2,67 punten, afgerond op kwartpunten
    # 2,75.
    assert groep.punten == 2.75
    vergelijk_met_testreferentie(eenheid, groep)


# Parkeerruimte gedeeld binnen het eigen adres


def test_carport_gedeeld_met_onzelfstandige_woonruimten_op_hetzelfde_adres_wordt_als_type_ii_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, wordt in deze rubriek als Type II gewaardeerd.

    De carport hoort bij één adres en wordt daar met 2 onzelfstandige
    woonruimten gedeeld. De package leest een parkeerplek die binnen het eigen
    adres wordt gedeeld als gemeenschappelijk; de test legt die keuze uit de
    implementatietoelichting vast.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Voor
    een onzelfstandige woonruimte telt daarnaast
    `Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` groter dan 1
    als gemeenschappelijk: de plek wordt dan binnen het eigen adres gedeeld."

    De wettekst noemt een parkeerruimte pas gemeenschappelijk bij ten minste
    twee adressen en verwijst een parkeerruimte van één adres naar rubriek 2 of
    8; de keuze van de package wijkt daarvan af.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
    gemeenschappelijke parkeerruimte is een ruimte die toegankelijk is voor
    bewoners van tenminste twee adressen die daar exclusief gebruiksrecht op
    hebben, waarin zich tenminste één parkeerplek bevindt" en "Een parkeerruimte
    waartoe bewoners van één adres krachtens de huurovereenkomst exclusieve
    toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens rubriek 2
    (binnen, bijvoorbeeld een garagebox behorende tot de woning) of rubriek 8
    (buiten, bijvoorbeeld een oprit exclusief behorende tot de woning)."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    De 6 punten van Type II worden door de 2 onzelfstandige woonruimten
    gedeeld.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type II:
    `Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
    en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

    Bron: wettekst, Bijlage I onder B, rubriek 10: "Type II Parkeerplek buiten
    behorende tot het complex met dak 6 punten".

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 10: "De punten voor
    een parkeerplaats worden na eventuele verdeling over de meerdere adressen
    nog gedeeld door het aantal onzelfstandige woonruimten op dat adres."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=1,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Gedeeld met 2 onzelfstandige woonruimten": {"Carport (Type II)": 3.0}
    }
    vergelijk_met_testreferentie(eenheid, groep)


def test_laadpaal_bij_parkeerplek_op_hetzelfde_adres_krijgt_2_punten_gedeeld_door_het_aantal_onzelfstandige_woonruimten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek die alleen door onzelfstandige woonruimten op hetzelfde adres wordt gedeeld, krijgt 2 punten extra, gedeeld door het aantal onzelfstandige woonruimten.

    De carport hoort bij één adres en wordt daar met 2 onzelfstandige
    woonruimten gedeeld.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Indien er sprake
    is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee
    punten extra per parkeerplek met laadpaal."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 10: "De punten voor
    een parkeerplaats worden na eventuele verdeling over de meerdere adressen
    nog gedeeld door het aantal onzelfstandige woonruimten op dat adres."

    Het beleidsboek noemt bij de laadpaal alleen de deling door het aantal
    adressen. De package deelt de laadpaal door dezelfde deler als de
    parkeerplek waar hij bij hoort.

    Bron: beleidsboek onzelfstandige woonruimten, 2.10.5: "dan worden 2 extra
    punten toegekend, gedeeld door het aantal adressen dat toegang en
    gebruiksrecht heeft."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3: "de
    laadpaal deelt de rubriek én de deler van de parkeerruimte waar hij bij
    hoort. Krijgt die ruimte in rubriek 10 punten, dan wordt de laadpaal daar
    gewaardeerd; in alle andere gevallen hier, met dezelfde deler (aantal
    adressen × aantal onzelfstandige woonruimten)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=12,
                gedeeld_met_aantal_adressen=1,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep)["Laadpaal"] == 1.0
    # Met de 3 punten van de carport samen 4 punten.
    assert groep.punten == 4.0
    vergelijk_met_testreferentie(eenheid, groep)


# Privé-parkeerruimte


def test_prive_carport_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een privé-carport krijgt in deze rubriek geen punten.

    De carport hoort bij één adres en het aantal onzelfstandige woonruimten is
    niet aangeleverd. Ze is daarmee niet gemeenschappelijk, maar een
    privé-buitenruimte die in rubriek 8 hoort.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Voor
    een onzelfstandige woonruimte telt daarnaast
    `Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` groter dan 1
    als gemeenschappelijk: de plek wordt dan binnen het eigen adres gedeeld."

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
    `carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
    gewaardeerd, gemeenschappelijk in rubriek 10".

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een
    parkeerruimte waartoe bewoners van één adres krachtens de huurovereenkomst
    exclusieve toegang tot en gebruiksrecht op hebben, wordt gewaardeerd volgens
    rubriek 2 (binnen, bijvoorbeeld een garagebox behorende tot de woning) of
    rubriek 8 (buiten, bijvoorbeeld een oprit exclusief behorende tot de
    woning)."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                oppervlakte=12,
                gedeeld_met_aantal_adressen=1,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Minimale oppervlakte


def test_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek met een oppervlakte onder 12 m² krijgt geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: beleidsboek onzelfstandige woonruimten, 2.10.3: "Een parkeerplek is
    een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waarin een
    gangbare personenauto in zijn geheel past."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=11,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
                aantal=2,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_laadpaal_bij_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een laadpaal bij een parkeerplek met een oppervlakte onder 12 m² krijgt in deze rubriek geen punten.

    De gemeenschappelijke carport van 10 m² krijgt zelf geen punten.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    De laadpaal volgt de carport en hoort dan in rubriek 12.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3: "Krijgt
    die ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in
    alle andere gevallen hier, met dezelfde deler (aantal adressen × aantal
    onzelfstandige woonruimten)."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=10,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


# Onvolledige of onjuiste input


def test_gemeenschappelijke_parkeerplaats_kleiner_dan_12_m2_geeft_ook_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een gemeenschappelijke parkeerplaats geeft de waarschuwing over haar detailsoort ook wanneer zij met een oppervlakte onder 12 m² geen punten krijgt.

    Dat de waarschuwing ook onder 12 m² volgt, is een keuze van de package die
    in geen bron staat.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Bij die
    laatste volgt een `UserWarning` dat een Type-detailsoort meer op zijn plaats
    is: `PAR` legt het type niet vast."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplaats,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=10,
                gedeeld_met_aantal_adressen=3,
                gedeeld_met_aantal_onzelfstandige_woonruimten=1,
            )
        ]
    )

    with pytest.warns(UserWarning, match="Gebruik Type I, II of III") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_parkeerplek_zonder_aantal_adressen_wordt_als_prive_parkeerplek_gewaardeerd(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek zonder aantal adressen wordt gewaardeerd als een privé-parkeerplek van één adres.

    De package waarschuwt dat `gedeeld_met_aantal_adressen` ontbreekt en gaat
    uit van één adres. Ook het aantal onzelfstandige woonruimten is niet
    aangeleverd; de package leest dat zonder waarschuwing als niet gedeeld. De
    implementatietoelichting voor onzelfstandige woonruimten vraagt beide
    attributen, maar noemt de waarschuwing en de aanname van één adres niet.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2:
    "Daarnaast zijn ook `Eenhedenruimte.gedeeld_met_aantal_adressen` en
    `Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` als
    uitbreiding toegevoegd. Deze attributen dienen ook op elk type parkeerplek
    meegegeven te worden wanneer het een onzelfstandige woonruimte betreft."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    De twee parkeerplekken van Type III worden ook als privé-parkeerplek in
    deze rubriek gewaardeerd: hun punten worden opgeteld en door 1 gedeeld. De
    wettekst waardeert in deze rubriek alleen parkeerplekken in een
    gemeenschappelijke parkeerruimte; de package volgt hier de
    implementatietoelichting.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2:
    "waarderen we altijd in deze rubriek, ook wanneer ze privé zijn of alleen
    tussen onzelfstandige woonruimten op hetzelfde adres worden gedeeld."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "In deze rubriek
    worden alleen parkeerplekken gewaardeerd die zich in een gemeenschappelijke
    parkeerruimte bevinden.", "Bij meerdere parkeerplekken worden de punten bij
    elkaar opgeteld." en "Indien sprake is van een privé parkeerplek voor één
    adres, wordt gedeeld door 1."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."

    Bron: wettekst, Bijlage I onder B, rubriek 10: "Type III Parkeerplek buiten
    behorende tot het complex zonder dak 4 punten".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                oppervlakte=12,
                aantal=2,
            )
        ]
    )

    with pytest.warns(
        UserWarning, match="geen 'gedeeld_met_aantal_adressen'"
    ) as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_bovenliggende(groep) == {
        "Privé": {"Parkeerplek buiten behorend bij complex (Type III)": 8.0}
    }
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_carport_zonder_aantal_adressen_krijgt_geen_punten(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

    Ook het aantal onzelfstandige woonruimten is niet aangeleverd. De package
    leest beide ontbrekende aantallen als niet gedeeld. De carport is dan een
    privé-buitenruimte en hoort in rubriek 8.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
    `carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
    gewaardeerd, gemeenschappelijk in rubriek 10".

    De implementatietoelichting vraagt beide attributen op elk type
    parkeerplek. Bij een carport waarschuwt de package in deze rubriek niet dat
    ze ontbreken; de test legt het huidige gedrag vast.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Deze
    attributen dienen ook op elk type parkeerplek meegegeven te worden wanneer
    het een onzelfstandige woonruimte betreft."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.carport,
                elementen=[element(Bouwkundigelementdetailsoort.laadpaal)],
                oppervlakte=12,
                aantal=5,
            )
        ]
    )

    groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep)


def test_parkeerplek_zonder_oppervlakte_geeft_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een parkeerplek zonder oppervlakte geeft een waarschuwing over incomplete input.

    De package waardeert de parkeerplek niet: zonder oppervlakte is niet vast te
    stellen of ze de minimale oppervlakte heeft.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
    is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
    gangbare personenauto in zijn geheel op past."

    Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
    dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
    overeenkomstige toepassing is."
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            EenhedenRuimte(
                id="parkeerplek",
                naam="Parkeerplek",
                soort=Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
                detail_soort=Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
                gedeeld_met_aantal_adressen=10,
                aantal=2,
            )
        ]
    )

    with pytest.warns(UserWarning, match="geen oppervlakte") as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_open_parkeergarage_niet_specifieke_plek_geeft_een_waarschuwing(
    gemeenschappelijke_parkeerruimten, vergelijk_met_testreferentie
):
    """Een ruimte met de detailsoort open parkeergarage, niet specifieke plek, geeft een waarschuwing dat een andere detailsoort nodig is.

    De package waardeert de ruimte niet, ook niet nu ze 100 m² groot is en met
    10 adressen en 2 onzelfstandige woonruimten wordt gedeeld. De waarschuwing
    noemt de detailsoorten die in deze rubriek wel worden gewaardeerd. Dat de
    package deze detailsoort met een waarschuwing afwijst, staat in geen bron.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."

    Bron: implementatietoelichting, datamodel-uitbreidingen,
    "Parkeergelegenheden": "Als uitbreiding op de referentiedata zijn er
    verschillende parkeerruimten (`Ruimtedetailsoort`) toegevoegd, die
    overeenkomen met Type I, II en III parkeergelegenheden vanuit het
    WWS-beleidsboek".
    """
    eenheid = EenhedenEenheid(
        ruimten=[
            ruimte(
                Ruimtedetailsoort.open_parkeergarage_niet_specifieke_plek,
                oppervlakte=100,
                gedeeld_met_aantal_adressen=10,
                gedeeld_met_aantal_onzelfstandige_woonruimten=2,
            )
        ]
    )

    with pytest.warns(
        UserWarning, match="heeft als ruimtedetailsoort"
    ) as waarschuwingen:
        groep = gemeenschappelijke_parkeerruimten.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)
