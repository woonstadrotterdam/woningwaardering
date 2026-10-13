"""Punten voor de WOZ-waarde, onzelfstandige woonruimten (rubriek 11)."""

from datetime import date
from types import SimpleNamespace

import pytest

from tests.utils import aantal_per_naam, assert_stelselgroep_output, punten_per_naam
from woningwaardering.stelsels.onzelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.vera.bvg.generated import (
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)


@pytest.fixture()
def punten_voor_de_woz_waarde(peildatum):
    return PuntenVoorDeWozWaarde(peildatum=peildatum)


def test_PuntenVoorDeWozWaarde_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PuntenVoorDeWozWaarde,
    )


# Punten naar het gemiddelde van het COROP-gebied


def test_woz_waarde_per_m2_net_onder_het_gemiddelde_van_het_corop_gebied_geeft_12_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een WOZ-waarde per m² gebruiksoppervlakte die minder dan 1% onder het gemiddelde van het COROP-gebied ligt, geeft 12 punten.

    Bron: wettekst, Bijlage I onder B, onderdeel 11.1: "De WOZ-waarde of 85%
    van de taxatiewaarde, indien er geen WOZ-waarde is vastgesteld, van het
    adres waar de onzelfstandige woonruimte onderdeel van is, per m²
    gebruiksoppervlakte is maximaal 10% hoger of lager dan de gemiddelde
    WOZ-waarde per m² gebruiksoppervlakte van woningen in het COROP-gebied
    waarbinnen de woonruimte is gelegen." en "12 punten".

    Woonplaatscode 3086 is Rotterdam, in het COROP-gebied Groot-Rijnmond.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
    COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
    waarin de eenheid zich bevindt."

    De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2022, 2023 en
    2024. De package rekent met de meest recente, die van 1 januari 2024.

    Bron: beleidsboek onzelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Het gemiddelde van het COROP-gebied staat per waardepeildatum in de
    Uitvoeringsregeling huurprijzen woonruimte (bijlage IIa): voor
    Groot-Rijnmond bij waardepeildatum 1 januari 2024 is dat € 3.537 per m².

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 11: "In de
    Uitvoeringsregeling huurprijzen woonruimte zijn de COROP-gebieden
    weergegeven alsmede de daarbij behorende gemiddelde WOZ-waarde per m²
    gebruiksoppervlakte van woningen." en "De kolommen geven op basis van de
    peildatum van de WOZ-beschikking weer met welk bedrag moet worden
    gerekend."
    """
    eenheid = EenhedenEenheid(
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=178000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=194000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=205000
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Percentage verschil": pytest.approx(-0.07, abs=0.005),
        "WOZ-waarde op waardepeildatum 01-01-2024": 205000.0,
        "Gebruiksoppervlakte": 58.0,
        "WOZ-waarde per m²": pytest.approx(3534.48, abs=0.005),
        "Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond": 3537.0,
    }
    assert punten_per_naam(groep) == {"Percentage verschil": 12.0}
    vergelijk_met_testreferentie(eenheid, groep)


def test_woz_waarde_per_m2_ruim_60_procent_onder_het_gemiddelde_van_het_corop_gebied_geeft_10_punten(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een WOZ-waarde per m² gebruiksoppervlakte die ruim 60% onder het gemiddelde van het COROP-gebied ligt, geeft 10 punten.

    Bron: wettekst, Bijlage I onder B, onderdeel 11.1: "De WOZ-waarde of 85%
    van de taxatiewaarde, indien er geen WOZ-waarde is vastgesteld, van het
    adres waar de onzelfstandige woonruimte onderdeel van is, per m²
    gebruiksoppervlakte is meer dan 10% lager dan de gemiddelde WOZ-waarde per
    m² gebruiksoppervlakte van woningen in het COROP-gebied waarbinnen de
    woonruimte is gelegen." en "10 punten".

    Woonplaatscode 3086 is Rotterdam, in het COROP-gebied Groot-Rijnmond.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
    COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
    waarin de eenheid zich bevindt."

    De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2022, 2023 en
    2024. De package rekent met de meest recente, die van 1 januari 2024.

    Bron: beleidsboek onzelfstandige woonruimten, 2.11.1: "Met de laatst
    vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
    peildatum van de procedure bedoeld."

    Het gemiddelde van het COROP-gebied staat per waardepeildatum in de
    Uitvoeringsregeling huurprijzen woonruimte (bijlage IIa): voor
    Groot-Rijnmond bij waardepeildatum 1 januari 2024 is dat € 3.537 per m².

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 11: "In de
    Uitvoeringsregeling huurprijzen woonruimte zijn de COROP-gebieden
    weergegeven alsmede de daarbij behorende gemiddelde WOZ-waarde per m²
    gebruiksoppervlakte van woningen." en "De kolommen geven op basis van de
    peildatum van de WOZ-beschikking weer met welk bedrag moet worden
    gerekend."
    """
    eenheid = EenhedenEenheid(
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=58000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=68000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=78000
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert aantal_per_naam(groep) == {
        "Percentage verschil": pytest.approx(-61.98, abs=0.005),
        "WOZ-waarde op waardepeildatum 01-01-2024": 78000.0,
        "Gebruiksoppervlakte": 58.0,
        "WOZ-waarde per m²": pytest.approx(1344.83, abs=0.005),
        "Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond": 3537.0,
    }
    assert punten_per_naam(groep) == {"Percentage verschil": 10.0}
    vergelijk_met_testreferentie(eenheid, groep)


# Geen WOZ-waarde


def test_woz_waarde_met_waardepeildatum_1_januari_2021_krijgt_met_waarschuwing_het_laagste_puntenaantal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid met alleen een WOZ-waarde met waardepeildatum 1 januari 2021 krijgt met een waarschuwing het laagste puntenaantal van 10 punten.

    Bron: beleidsboek onzelfstandige woonruimten, 2.11.1: "Wanneer er geen
    enkele WOZ-waarde of taxatiewaarde bekend is voor het adres van de woning,
    dan wordt het laagste puntenaantal voor de WOZ-waarde toegepast (10
    punten)."

    De package rekent bij de peildatum van de waardering, hier 1 juli 2026,
    alleen met een WOZ-waarde met waardepeildatum 1 januari 2025 of 1 januari
    2024. Een WOZ-waarde met een oudere waardepeildatum behandelt zij als geen
    WOZ-waarde. De implementatietoelichting noemt die keuze niet; de test legt
    het huidige gedrag vast.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 11: "In deze
    regeling zijn twee verschillende kolommen weergegeven: één voor de
    gemiddelden waar nog geen nieuwe WOZ-beschikking voor is afgegeven en één
    voor de gemiddelden waar wel een nieuwe WOZ-beschikking is afgegeven."

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2021, 1, 1), vastgestelde_waarde=124000
            ),
        ],
    )

    with pytest.warns(
        UserWarning,
        match="geen WOZ-waarde gevonden met waardepeildatum 01-01-2025 of 01-01-2024",
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Geen WOZ-waarde bekend": 10.0}
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Onvolledige input: de gebruiksoppervlakte


def test_eenheid_zonder_gebruiksoppervlakte_krijgt_met_waarschuwing_geen_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid zonder gebruiksoppervlakte krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

    De punten volgen uit de WOZ-waarde per m² gebruiksoppervlakte. Zonder
    gebruiksoppervlakte kan de package die niet berekenen.

    Bron: beleidsboek onzelfstandige woonruimten, 2.11.2: "Deel de WOZ-waarde
    door het aantal m² gebruiksoppervlakte van de woning".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "De
    gebruiksoppervlakte dient gespecificeerd te worden in het attribuut
    `adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte` op de
    eenheid."

    De implementatietoelichting noemt niet dat de package bij een ontbrekende
    gebruiksoppervlakte waarschuwt en geen waardering geeft; de test legt het
    huidige gedrag vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=148000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=184000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=205000
            ),
        ],
    )

    with pytest.warns(
        UserWarning, match="geen bruikbare gebruiksoppervlakte"
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    # Geen waardering is iets anders dan 0 punten: de stelselgroep heeft geen punten.
    assert groep.punten is None
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_gebruiksoppervlakte_van_0_m2_krijgt_met_waarschuwing_geen_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid met een gebruiksoppervlakte van 0 m² krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

    De punten volgen uit de WOZ-waarde per m² gebruiksoppervlakte. Door een
    gebruiksoppervlakte van 0 m² is de WOZ-waarde niet te delen.

    Bron: beleidsboek onzelfstandige woonruimten, 2.11.2: "Deel de WOZ-waarde
    door het aantal m² gebruiksoppervlakte van de woning".

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "De
    gebruiksoppervlakte dient gespecificeerd te worden in het attribuut
    `adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte` op de
    eenheid."

    De implementatietoelichting noemt niet dat de package bij een
    gebruiksoppervlakte van 0 m² waarschuwt en geen waardering geeft; de test
    legt het huidige gedrag vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=0
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=205000
            ),
        ],
    )

    with pytest.warns(
        UserWarning, match="geen bruikbare gebruiksoppervlakte"
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    assert groep.punten is None
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Onvolledige input: het adres en de woonplaats


def test_eenheid_zonder_adres_krijgt_met_waarschuwing_geen_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid zonder adres krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

    De package bepaalt het COROP-gebied met de woonplaatscode, of zoekt de
    woonplaats op met postcode en huisnummer. Zonder adres heeft zij geen van
    beide.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
    COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
    waarin de eenheid zich bevindt." en "Indien dit attribuut niet
    gespecificeerd is, wordt op basis van postcode, huisnummer, huisletter en
    huisnummertoevoeging bepaald in welke woonplaats een eenheid zich bevindt."

    De implementatietoelichting noemt niet dat de package bij een ontbrekend
    adres waarschuwt en geen waardering geeft; de test legt het huidige gedrag
    vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=148000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=184000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=205000
            ),
        ],
    )

    with pytest.warns(
        UserWarning,
        match="adres met woonplaatscode of postcode en huisnummer ontbreekt",
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    assert groep.punten is None
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woonplaatscode_zonder_corop_gebied_krijgt_met_waarschuwing_geen_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid met een woonplaatscode waarbij de package geen COROP-gebied kent, krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Het
    COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats
    waarin de eenheid zich bevindt."

    De package zoekt het COROP-gebied bij de woonplaatscode op in een extract
    van CBS-data. Woonplaatscode 0100 staat daar niet in.

    Bron: docs/voor-ontwikkelaars/data, Woonplaatsen en COROP-gebieden: "daarom
    hebben we een script gemaakt dat een extract van deze data als resource in
    de package opslaat in `woningwaardering/data/corop/corop.generated.csv`".

    De implementatietoelichting noemt niet dat de package bij een onbekende
    woonplaatscode waarschuwt en geen waardering geeft; de test legt het
    huidige gedrag vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    eenheid = EenhedenEenheid(
        id="eenheid",
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="0100", naam="Rotjeknor")
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=148000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=184000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=205000
            ),
        ],
    )

    with pytest.warns(
        UserWarning,
        match="Geen COROP-gebied gevonden voor woonplaats Rotjeknor met woonplaatscode 0100",
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    assert groep.punten is None
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woonplaatsnaam_die_afwijkt_van_het_kadaster_krijgt_met_waarschuwing_geen_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie, monkeypatch
):
    """Een eenheid waarvan de opgegeven woonplaatsnaam afwijkt van de woonplaats die het Kadaster bij postcode en huisnummer geeft, krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

    De woonplaats van de eenheid heeft een naam en geen code. De package zoekt
    de woonplaats daarom op bij het Kadaster, met postcode en huisnummer.

    Bron: implementatietoelichting onzelfstandige woonruimten, 2.11.2: "Indien
    dit attribuut niet gespecificeerd is, wordt op basis van postcode,
    huisnummer, huisletter en huisnummertoevoeging bepaald in welke woonplaats
    een eenheid zich bevindt." en "Hierbij is het van belang dat deze waarden
    overeenkomen met de BAG-registratie."

    Het Kadaster geeft bij postcode 1013GS en huisnummer 22 de woonplaats
    Amsterdam; de eenheid noemt Rotterdam. De package rekent dan met geen van
    beide woonplaatsen: zij waarschuwt voor het verschil, en daarna dat zij
    geen woonplaats heeft gevonden. De implementatietoelichting noemt die keuze
    niet; de test legt het huidige gedrag vast.

    Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
    genereert de package een `UserWarning`."
    """
    # Het antwoord van het Kadaster op postcode 1013GS en huisnummer 22. Met
    # deze vervanger verloopt de waardering ook zonder netwerk hetzelfde.
    antwoord_van_het_kadaster = SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [{"identificatie": "3594", "naam": "Amsterdam"}],
    )
    monkeypatch.setattr(
        "woningwaardering.stelsels.utils.requests.post",
        lambda *args, **kwargs: antwoord_van_het_kadaster,
    )
    eenheid = EenhedenEenheid(
        id="eenheid",
        adres=EenhedenEenheidadres(
            postcode="1013GS",
            huisnummer="22",
            woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=178000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=194000
            ),
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=205000
            ),
        ],
    )

    with pytest.warns(
        UserWarning,
        match="Woonplaats Amsterdam is gevonden voor adres 1013GS 22, terwijl "
        "woonplaats ROTTERDAM is opgegeven",
    ) as waarschuwingen:
        groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {}
    assert groep.punten is None
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


# Gemiddelde WOZ-waarden per COROP-gebied


def test_gemiddelde_woz_voor_corop_gebied_weigert_onbekend_jaar(
    peildatum,
) -> None:
    """De package geeft een foutmelding bij een waardepeildatum in 2026, waarvoor zij geen gemiddelde WOZ-waarden per COROP-gebied heeft.

    De gemiddelde WOZ-waarden per m² staan per jaar van de waardepeildatum in
    een lookuptabel. Ontbreekt het jaar daarin, dan rekent de package niet met
    het gemiddelde van een ander jaar.

    Bron: wettekst, Bijlage I onder B, toelichting rubriek 11: "De kolommen
    geven op basis van de peildatum van de WOZ-beschikking weer met welk bedrag
    moet worden gerekend."

    Bron: docs/voor-ontwikkelaars/data, Gemiddelde WOZ-waarden per vierkante
    meter per COROP-gebied: "door een kolom toe te voegen met als kolomnaam het
    jaar van de waardepeildatum waarvoor de nieuwe gemiddelde waarden gelden".
    """
    punten_voor_de_woz_waarde = PuntenVoorDeWozWaarde(peildatum)

    with pytest.raises(ValueError, match="2026"):
        punten_voor_de_woz_waarde._gemiddelde_woz_voor_corop_gebied(
            {"code": "40", "naam": "Groot-Rijnmond"},
            2026,
        )
