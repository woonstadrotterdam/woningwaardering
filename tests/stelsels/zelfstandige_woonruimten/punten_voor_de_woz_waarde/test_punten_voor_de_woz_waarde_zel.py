"""Punten voor de WOZ-waarde, zelfstandige woonruimten (rubriek 11)."""

import sys
from datetime import date
from types import SimpleNamespace

import pytest

from tests.input import aanrecht, element, elementen, ruimte
from tests.utils import (
    aantal_per_bovenliggende,
    aantal_per_naam,
    assert_stelselgroep_output,
    punten_per_naam,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.vera.bvg.generated import (
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Energielabel,
    Energieprestatiesoort,
    EnergieprestatiesoortReferentiedata,
    Energieprestatiestatus,
    Pandsoort,
    Ruimtedetailsoort,
)


@pytest.fixture()
def punten_voor_de_woz_waarde(peildatum):
    return PuntenVoorDeWozWaarde(peildatum=peildatum)


@pytest.fixture()
def vervanger_voor_package_monumenten(monkeypatch):
    """Vervang de optionele package `monumenten` door een lege vervanger.

    Is `monumenten` op de eenheid niet opgegeven, dan zoekt de package de
    monumentstatus op met de package `monumenten`. Die is optioneel; zonder haar
    geeft de waardering een extra waarschuwing. Met deze vervanger verloopt de
    waardering in elke omgeving hetzelfde: zonder BAG-identificatie wordt
    `MonumentenClient` niet aangeroepen.
    """
    monkeypatch.setitem(
        sys.modules, "monumenten", SimpleNamespace(MonumentenClient=None)
    )


def test_PuntenVoorDeWozWaarde_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PuntenVoorDeWozWaarde,
    )


# De berekening van onderdeel I en II


def test_rekenvoorbeeld_uit_het_beleidsboek_geeft_36_25_punten(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een WOZ-waarde van € 300.000 met waardepeildatum 1 januari 2025 geeft bij 60 m² aan vertrekken 36,25 punten, zoals in het rekenvoorbeeld van het beleidsboek.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "De WOZ-waarde van een
    woning is op 1 januari 2026 vastgesteld op € 300.000, met de
    waardepeildatum 1 januari 2025. De oppervlakte van de vertrekken en overige
    ruimten van de woning is 60 m².", "Onderdeel I: € 300.000 / € 16.954 =
    17,6949392474 punten", "Onderdeel II: € 300.000 / 60 (m²) / € 268 =
    18,6567164179 punten" en "Totaal = 36,3516556653. Dit is afgerond 36,25
    punten."

    In de output staan de punten van onderdeel I en II op twee decimalen. De
    waardering 'Afronding op kwartpunten' is het verschil tussen de som van die
    twee rijen en het totaal.

    Bron: docs/voor-ontwikkelaars/criteriumstrategie, Structuur van de output:
    "Bij het vastleggen in de output krijgen de rijen wel twee decimalen.
    Afronding op kwartpunten sluit het verschil tussen de som van die getoonde
    rijen en het stelselgroeptotaal".

    De eenheid heeft alleen een bouwjaar, een WOZ-waarde en een woonkamer. Deze
    rubriek rekent met de uitkomst van de andere rubrieken: de oppervlakte uit
    rubriek 1 en 2, en de punten waaraan het minimum van 40 punten en de cap op
    de WOZ worden getoetst. De package waardeert die rubrieken daarom mee en
    waarschuwt voor de energieprestatie, de monumenten, de pandsoort en de
    keuken die ontbreken.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2025, 1, 1), vastgestelde_waarde=300000
            ),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=60.0, verwarmd=True)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2025": 300000.0,
        "Factor I": 16954.0,
        "Oppervlakte van vertrekken en overige ruimten": 60.0,
        "Factor II": 268.0,
    }
    assert punten_per_naam(groep) == {
        "Onderdeel I": 17.69,
        "Onderdeel II": 18.66,
        "Afronding op kwartpunten": -0.1,
    }
    assert groep.punten == 36.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_onderdeel_i_en_ii_worden_niet_afgerond_voordat_ze_worden_opgeteld(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """De punten van onderdeel I en onderdeel II worden niet afgerond voordat ze bij elkaar worden opgeteld.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "1 punt voor iedere
    € 16.954 van de laatstelijk vastgestelde WOZ-waarde met waardepeildatum 1
    januari 2025 , 85% van de taxatiewaarde of de minimum WOZ-waarde. Rond dit
    puntenaantal niet af.", "Deel de WOZ-waarde door het aantal berekende m² en
    vervolgens door € 268 (bij een WOZ-waarde met waardepeildatum 1 januari
    2025 , 85% van de taxatiewaarde of minimum WOZ-waarde). Dit geeft het
    puntenaantal voor onderdeel II. Rond dit puntenaantal niet af." en "Tel de
    punten van de twee onderdelen bij elkaar op en rond volgens de instructie
    van paragraaf 2.1.4 af op een kwart punt."

    In de output staan de punten van onderdeel I en II wel op twee decimalen.
    De waardering 'Afronding op kwartpunten' is het verschil tussen de som van
    die twee rijen en het totaal.

    Bron: docs/voor-ontwikkelaars/criteriumstrategie, Structuur van de output:
    "Punten van een waardering worden in de berekening niet tussentijds op twee
    decimalen afgerond; alleen het rubriektotaal wordt op een kwart punt
    afgerond. Bij het vastleggen in de output krijgen de rijen wel twee
    decimalen. Afronding op kwartpunten sluit het verschil tussen de som van
    die getoonde rijen en het stelselgroeptotaal".

    De eenheid heeft alleen een bouwjaar, een WOZ-waarde en een slaapkamer.
    Deze rubriek rekent met de uitkomst van de andere rubrieken: de oppervlakte
    uit rubriek 1 en 2, en de punten waaraan het minimum van 40 punten en de
    cap op de WOZ worden getoetst. De package waardeert die rubrieken daarom
    mee en waarschuwt voor de energieprestatie, de monumenten, de pandsoort en
    de keuken die ontbreken.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=1980,
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2025, 1, 1), vastgestelde_waarde=50000
            ),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.slaapkamer, oppervlakte=26.0, verwarmd=True)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert punten_per_naam(groep) == {
        "Onderdeel I": 2.95,
        "Onderdeel II": 7.18,
        "Afronding op kwartpunten": -0.13,
    }
    # Onafgerond tellen de onderdelen op tot 10,1248 en dat wordt 10 punten.
    # Waren ze eerst op twee decimalen afgerond, dan was de som 10,13 en werd
    # dat 10,25 punten.
    assert groep.punten == 10.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# De WOZ-waarde waarmee wordt gerekend


def test_woz_waarde_onder_de_minimum_woz_waarde_wordt_niet_verhoogd_tot_dat_minimum(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een vastgestelde WOZ-waarde van € 79.999, lager dan de minimum WOZ-waarde van € 85.806, wordt niet tot dat minimum verhoogd.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "de voor de woning
    laatstelijk vastgestelde waarde op voet van hoofdstuk IV van de Wet
    waardering onroerende zaken of 85% van de taxatiewaarde indien er geen
    WOZ-waarde is vastgesteld, en anders een minimumwaarde van € 85.806."

    Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "De minimum WOZ-waarde
    komt pas aan bod als er voor een woonruimte geen relevante WOZ-waarde
    aanwezig is én de verhuurder geen taxatierapport (zoals hierboven bedoeld)
    heeft ingediend."

    De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2022, 2023 en
    2024. De package rekent met de meest recente, die van 1 januari 2024, en
    met de kengetallen die bij die waardepeildatum horen.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2024." en "€ 242 bij
    WOZ-beschikkingen met waardepeildatum 1 januari 2024."

    De oppervlakte in onderdeel II is die van de drie vertrekken, afgerond op
    hele vierkante meters.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "Rond hierna de
    oppervlakte af op hele vierkante meters."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=1990,
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=59999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=69999
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=79999
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 22),
                einddatum=date(2028, 6, 22),
                label=Energielabel.c,
                waarde="1.67",
            )
        ],
        monumenten=[],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=3.59507,
                verwarmd=True,
                elementen=[aanrecht(2100)],
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=3.13436,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                    Bouwkundigelementdetailsoort.closetcombinatie,
                ),
            ),
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=21.4327, verwarmd=True),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 79999.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 28.0,
        "Factor II": 242.0,
    }
    punten = punten_per_naam(groep)
    assert punten["Onderdeel I"] == 5.22
    assert punten["Onderdeel II"] == 11.81
    assert groep.punten == 17.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_woz_eenheid_zonder_vastgestelde_waarde_wordt_overgeslagen(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """Een WOZ-eenheid zonder vastgestelde waarde slaat de package over: zij rekent met de meest recente WOZ-waarde die wel is vastgesteld.

    De WOZ-eenheid met waardepeildatum 1 januari 2025 heeft geen vastgestelde
    waarde. De package rekent met de WOZ-waarde van 1 januari 2024 en met de
    kengetallen die bij die waardepeildatum horen. De implementatietoelichting
    noemt die keuze niet; de test legt het huidige gedrag vast.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2024." en "€ 242 bij
    WOZ-beschikkingen met waardepeildatum 1 januari 2024."

    De eenheid heeft alleen WOZ-eenheden en een woonkamer. Deze rubriek rekent
    met de uitkomst van de andere rubrieken: de oppervlakte uit rubriek 1 en 2,
    en de punten waaraan het minimum van 40 punten en de cap op de WOZ worden
    getoetst. De package waardeert die rubrieken daarom mee en waarschuwt voor
    de energieprestatie, de monumenten, de pandsoort, de keuken en het bouwjaar
    die ontbreken.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=100000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=100000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=100000
            ),
            EenhedenWozEenheid(waardepeildatum=date(2025, 1, 1)),
        ],
        ruimten=[ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=10.0)],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 100000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 10.0,
        "Factor II": 242.0,
    }
    assert groep.punten == 47.75
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_eenheid_zonder_woz_waarde_wordt_met_waarschuwing_gewaardeerd_met_de_minimum_woz_waarde(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid zonder WOZ-waarde wordt met een waarschuwing gewaardeerd met de minimum WOZ-waarde van € 85.806.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "de voor de woning
    laatstelijk vastgestelde waarde op voet van hoofdstuk IV van de Wet
    waardering onroerende zaken of 85% van de taxatiewaarde indien er geen
    WOZ-waarde is vastgesteld, en anders een minimumwaarde van € 85.806."

    Bij de minimumwaarde horen de kengetallen van waardepeildatum 1 januari
    2025.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 16.954
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2025, taxatiewaarden
    en minimumwaarden." en "€ 268 bij WOZ-beschikkingen met waardepeildatum 1
    januari 2025, taxatiewaarden en minimumwaarden."

    De oppervlakte in onderdeel II is die van de vijf vertrekken van het
    appartement, afgerond op hele vierkante meters. De vaste kasten van de
    keuken en de woonkamer tellen daarin mee.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "Rond hierna de
    oppervlakte af op hele vierkante meters."

    Bron: implementatietoelichting, datamodel-uitbreidingen, "Ruimtedetailsoort
    kast": "Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden
    de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur
    van de kast zich bevindt."

    Het appartement is in 2016 gebouwd en haalt voor de rubrieken 1 tot en met
    10 en 12 meer dan 110 punten. Het krijgt daarom minimaal 40 punten: de
    waardering 'Nieuwbouw: min. 40 punten' vult de punten van onderdeel I en II
    aan tot dat minimum.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.2: "Indien een woning is
    gebouwd in het kalenderjaar 2015, 2016, 2017, 2018 of 2019 en het totaal
    aantal punten na saldering van de punten van de onderdelen 1 tot en met 10
    en 12, 110 of meer is, worden minimaal 40 punten toegekend."

    De package waarschuwt dat er geen WOZ-waarde is aangeleverd. De
    implementatietoelichting noemt die waarschuwing niet; de test legt het
    huidige gedrag vast. De eenheid heeft ook geen energieprestatie; daarvoor
    waarschuwt de rubriek energieprestatie, die de package voor het minimum
    van 40 punten meewaardeert.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    # De vaste kasten, de meterruimte en de technische ruimte zijn ruimten van
    # de eenheid en ook de verbonden ruimten van de keuken, de woonkamer en de
    # hal.
    kast1 = ruimte(Ruimtedetailsoort.kast, naam="Kast1", oppervlakte=0.856)
    kast2 = ruimte(Ruimtedetailsoort.kast, naam="Kast2", oppervlakte=0.312)
    kast3 = ruimte(Ruimtedetailsoort.kast, naam="Kast3", oppervlakte=0.308)
    kast4 = ruimte(Ruimtedetailsoort.kast, naam="Kast4", oppervlakte=0.3575)
    meterruimte = ruimte(Ruimtedetailsoort.meterruimte, oppervlakte=0.2205)
    technische_ruimte = ruimte(
        Ruimtedetailsoort.technische_ruimte,
        oppervlakte=0.3456,
        elementen=[element(Bouwkundigelementdetailsoort.verwarmingstoestellen)],
    )
    eenheid = EenhedenEenheid(
        id="eenheid",
        bouwjaar=2016,
        adres=EenhedenEenheidadres(
            huisnummer="44",
            huisnummer_toevoeging="",
            postcode="3012CJ",
            woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0599010000320510"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        energieprestaties=[],
        gebruiksoppervlakte=71,
        monumenten=[],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.balkon,
                oppervlakte=1.82259,
                lengte_mm=1290,
                breedte_mm=1500,
                hoogte_mm=2600,
            ),
            technische_ruimte,
            ruimte(Ruimtedetailsoort.schuur, oppervlakte=0.2345),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=3.584,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                ),
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=9.5565,
                verwarmd=True,
                elementen=[aanrecht(2100)],
                verbonden_ruimten=[kast3, technische_ruimte, kast2],
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=25.96,
                verwarmd=True,
                verbonden_ruimten=[kast1],
            ),
            ruimte(
                Ruimtedetailsoort.hal,
                oppervlakte=6.198,
                verwarmd=True,
                verbonden_ruimten=[kast4, meterruimte],
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                oppervlakte=6.486,
                verwarmd=True,
            ),
            kast1,
            meterruimte,
            kast2,
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                oppervlakte=1.26375,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.wastafel,
                    Bouwkundigelementdetailsoort.closetcombinatie,
                ),
            ),
            kast3,
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                oppervlakte=12.978,
                verwarmd=True,
            ),
            kast4,
        ],
    )

    with pytest.warns(
        UserWarning, match="geen WOZ-waarde aangeleverd"
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_bovenliggende(groep) == {
        None: {"Minimum WOZ-waarde (geen relevante WOZ-waarde beschikbaar)": 85806.0},
        "Onderdeel I": {
            "Minimum WOZ-waarde gebruikt voor berekening": 85806.0,
            "Factor I": 16954.0,
        },
        "Onderdeel II": {
            "Minimum WOZ-waarde gebruikt voor berekening": 85806.0,
            "Oppervlakte van vertrekken en overige ruimten": 60.0,
            "Factor II": 268.0,
        },
    }
    assert punten_per_naam(groep) == {
        "Onderdeel I": 5.06,
        "Onderdeel II": 5.34,
        "Nieuwbouw: min. 40 punten": 29.6,
    }
    assert groep.punten == 40.0
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# De oppervlakte in onderdeel II


def test_onderdeel_ii_rekent_met_de_oppervlakte_van_vertrekken_overige_ruimten_en_parkeerplekken_type_i(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    vervanger_voor_package_monumenten,
):
    """In onderdeel II telt de oppervlakte mee van de vertrekken en overige ruimten uit rubriek 1 en 2 en van de parkeerplekken type I uit rubriek 10.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "die waarde, gedeeld
    door het aantal m² van de vertrekken, de overige ruimten en parkeerplekken,
    bedoeld in de rubrieken 1,2 en 10 voor zover het parkeerplek type I
    betreft".

    De woonkamer van 10 m² is een vertrek en de eerste toiletruimte van 10 m²
    een overige ruimte. De tweede toiletruimte telt niet mee: met 1,9 m² is zij
    geen overige ruimte in rubriek 2.

    Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
    een oppervlakte te hebben van minimaal 2 m²."

    Van een parkeerplek type I telt de oppervlakte gedeeld door het aantal
    adressen. De eerste ruimte staat voor twee parkeerplekken van elk 20 m²,
    gedeeld met 4 adressen, en telt voor 10 m². De tweede ruimte telt niet mee:
    een parkeerplek van 10 m² valt niet onder rubriek 10.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.2: "Wij gaan
    er vanuit dat de oppervlakte van de parkeerplekken ook nog gedeeld moet
    worden door het aantal adressen dat toegang heeft tot de parkeerplek, omdat
    er anders onredelijk veel punten kunnen worden toegewezen voor
    parkeerplekken. Wij hanteren geen standaardmaat van 12m2, omdat een
    parkeerplek Type I kleiner dan12m2 niet onder rubriek 10 valt."

    Bron: implementatietoelichting, datamodel-uitbreidingen, "Aantal":
    "Hierdoor is het mogelijk om aan te geven hoeveel van deze specifieke
    ruimte er zijn."

    De WOZ-waarde heeft waardepeildatum 1 januari 2024.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2024." en "€ 242 bij
    WOZ-beschikkingen met waardepeildatum 1 januari 2024."

    De eenheid heeft alleen een WOZ-waarde en deze ruimten. Deze rubriek rekent
    met de uitkomst van de andere rubrieken: de oppervlakte uit rubriek 1 en 2,
    en de punten waaraan het minimum van 40 punten en de cap op de WOZ worden
    getoetst. De package waardeert die rubrieken daarom mee en waarschuwt voor
    de energieprestatie, de monumenten, de pandsoort, de keuken en het bouwjaar
    die ontbreken.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=100000
            ),
        ],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte1", oppervlakte=10.0
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte, naam="Toiletruimte2", oppervlakte=1.9
            ),
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=10.0),
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                naam="Parkeerplek1",
                oppervlakte=20.0,
                aantal=2,
                gedeeld_met_aantal_adressen=4,
            ),
            ruimte(
                Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
                naam="Parkeerplek2",
                oppervlakte=10.0,
                aantal=2,
                gedeeld_met_aantal_adressen=4,
            ),
        ],
    )

    with pytest.warns(UserWarning) as waarschuwingen:
        # De package zet `monumenten` op de eenheid die zij waardeert. De kopie
        # houdt de input in de testreferentie zoals de test hem opgeeft.
        groep = punten_voor_de_woz_waarde.waardeer(eenheid.model_copy())

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 100000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 30.0,
        "Factor II": 242.0,
    }
    assert punten_per_naam(groep)["Onderdeel II"] == 13.77
    assert groep.punten == 20.25
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Kleine nieuwbouwwoningen in het COROP-gebied Amsterdam of Utrecht


def test_woning_van_35_m2_uit_2020_in_corop_gebied_amsterdam_krijgt_in_onderdeel_ii_het_lagere_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning van 35 m² uit 2020 in het COROP-gebied Amsterdam krijgt in onderdeel II het lagere kengetal van € 103.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "a. indien sprake is van
    een woning tot 40 m² gebouwd in het kalenderjaar 2018, 2019, 2020, 2021 of
    2022 die is gelegen in een gemeente, gelegen in het COROP-gebied Amsterdam
    of Utrecht, vervolgens gedeeld door" en "€ 103 voor WOZ-beschikkingen met
    waardepeildatum 1 januari 2024."

    De package toetst de 40 m² aan de gebruiksoppervlakte van de eenheid en
    bepaalt het COROP-gebied met de woonplaatscode: 3594 is Amsterdam, in het
    COROP-gebied Groot-Amsterdam.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6: "Wij gaan
    er vanuit dat de 40m2 verwijst naar de gebruiksoppervlakte van de woning."
    en "Het COROP-gebied wordt bepaald op basis van de woonplaatscode van de
    woonplaats waarin de eenheid zich bevindt."

    De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2023 en 2024. De
    package rekent met de meest recente, die van 1 januari 2024.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2024."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=2020,
        adres=EenhedenEenheidadres(
            huisnummer="1",
            huisnummer_toevoeging="",
            postcode="1012LG",
            woonplaats=EenhedenWoonplaats(code="3594", naam="Amsterdam"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0363010012111931"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=300000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                # De soortcode is geen VERA-code (die is "EI"). De package
                # gebruikt deze energieprestatie daardoor niet en waardeert de
                # energieprestatie naar het bouwjaar.
                soort=EnergieprestatiesoortReferentiedata(
                    code="energie_index", naam="Energie-index"
                ),
                status=Energieprestatiestatus.definitief,
                label=Energielabel.c,
                waarde="1.2",
                begindatum=date(2020, 1, 1),
                einddatum=date(2030, 1, 1),
            )
        ],
        gebruiksoppervlakte=35,
        monumenten=[],
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=20.0, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=8.0,
                verwarmd=True,
                elementen=[aanrecht(1800)],
            ),
            ruimte(Ruimtedetailsoort.badkamer, oppervlakte=4.0, verwarmd=True),
            ruimte(Ruimtedetailsoort.toiletruimte, oppervlakte=3.0),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 310000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 35.0,
        "Factor II": 103.0,
    }
    assert punten_per_naam(groep)["Onderdeel II"] == 85.99
    assert groep.punten == 106.25
    vergelijk_met_testreferentie(eenheid, groep)


def test_woning_van_38_m2_uit_2021_in_corop_gebied_utrecht_krijgt_in_onderdeel_ii_het_lagere_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning van 38 m² uit 2021 in het COROP-gebied Utrecht krijgt in onderdeel II het lagere kengetal van € 103.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "a. indien sprake is van
    een woning tot 40 m² gebouwd in het kalenderjaar 2018, 2019, 2020, 2021 of
    2022 die is gelegen in een gemeente, gelegen in het COROP-gebied Amsterdam
    of Utrecht, vervolgens gedeeld door" en "€ 103 voor WOZ-beschikkingen met
    waardepeildatum 1 januari 2024."

    De package toetst de 40 m² aan de gebruiksoppervlakte van de eenheid en
    bepaalt het COROP-gebied met de woonplaatscode: 3295 is Utrecht, in het
    COROP-gebied Utrecht.

    Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6: "Wij gaan
    er vanuit dat de 40m2 verwijst naar de gebruiksoppervlakte van de woning."
    en "Het COROP-gebied wordt bepaald op basis van de woonplaatscode van de
    woonplaats waarin de eenheid zich bevindt."

    De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2023 en 2024. De
    package rekent met de meest recente, die van 1 januari 2024.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2024."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=2021,
        adres=EenhedenEenheidadres(
            huisnummer="100",
            huisnummer_toevoeging="",
            postcode="3511AD",
            woonplaats=EenhedenWoonplaats(code="3295", naam="Utrecht"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0344010000000001"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=280000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=290000
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                # De soortcode is geen VERA-code (die is "EI"). De package
                # gebruikt deze energieprestatie daardoor niet en waardeert de
                # energieprestatie naar het bouwjaar.
                soort=EnergieprestatiesoortReferentiedata(
                    code="energie_index", naam="Energie-index"
                ),
                status=Energieprestatiestatus.definitief,
                label=Energielabel.c,
                waarde="1.2",
                begindatum=date(2021, 1, 1),
                einddatum=date(2031, 1, 1),
            )
        ],
        gebruiksoppervlakte=38,
        monumenten=[],
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=22.0, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=9.0,
                verwarmd=True,
                elementen=[aanrecht(2000)],
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=4.5,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                ),
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                oppervlakte=2.5,
                elementen=[element(Bouwkundigelementdetailsoort.closetcombinatie)],
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 290000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 38.0,
        "Factor II": 103.0,
    }
    assert punten_per_naam(groep)["Onderdeel II"] == 74.09
    assert groep.punten == 93.0
    vergelijk_met_testreferentie(eenheid, groep)


def test_woning_van_35_m2_uit_2023_in_corop_gebied_amsterdam_krijgt_in_onderdeel_ii_het_gewone_kengetal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een woning van 35 m² in het COROP-gebied Amsterdam die in 2023 is gebouwd, krijgt in onderdeel II het gewone kengetal van € 242.

    Het lagere kengetal geldt alleen voor een woning die in 2018 tot en met
    2022 is gebouwd.

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "a. indien sprake is van
    een woning tot 40 m² gebouwd in het kalenderjaar 2018, 2019, 2020, 2021 of
    2022 die is gelegen in een gemeente, gelegen in het COROP-gebied Amsterdam
    of Utrecht, vervolgens gedeeld door", "b. in alle andere gevallen dan
    bedoeld onder a, vervolgens gedeeld door:" en "€ 242 bij WOZ-beschikkingen
    met waardepeildatum 1 januari 2024."

    De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2023 en 2024. De
    package rekent met de meest recente, die van 1 januari 2024.

    Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
    voor WOZ-beschikkingen met waardepeildatum 1 januari 2024."
    """
    eenheid = EenhedenEenheid(
        bouwjaar=2023,
        adres=EenhedenEenheidadres(
            huisnummer="2",
            huisnummer_toevoeging="",
            postcode="1012LG",
            woonplaats=EenhedenWoonplaats(code="3594", naam="Amsterdam"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0363010000000002"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=300000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=310000
            ),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                # De soortcode is geen VERA-code (die is "EI"). De package
                # gebruikt deze energieprestatie daardoor niet en waardeert de
                # energieprestatie naar het bouwjaar.
                soort=EnergieprestatiesoortReferentiedata(
                    code="energie_index", naam="Energie-index"
                ),
                status=Energieprestatiestatus.definitief,
                label=Energielabel.c,
                waarde="1.2",
                begindatum=date(2023, 1, 1),
                einddatum=date(2033, 1, 1),
            )
        ],
        gebruiksoppervlakte=35,
        monumenten=[],
        ruimten=[
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=20.0, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=8.0,
                verwarmd=True,
                elementen=[aanrecht(1800)],
            ),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=4.0,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                ),
            ),
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                oppervlakte=3.0,
                elementen=[element(Bouwkundigelementdetailsoort.closetcombinatie)],
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "WOZ-waarde op waardepeildatum 01-01-2024": 310000.0,
        "Factor I": 15329.0,
        "Oppervlakte van vertrekken en overige ruimten": 35.0,
        "Factor II": 242.0,
    }
    assert punten_per_naam(groep)["Onderdeel II"] == 36.6
    assert groep.punten == 56.75
    vergelijk_met_testreferentie(eenheid, groep)
