"""Punten voor de WOZ-waarde, onzelfstandige woonruimten (rubriek 11)."""

from datetime import date
from types import SimpleNamespace

import pytest

from tests.utils import assert_stelselgroep_output, punten_per_naam
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


@pytest.mark.parametrize(
    ("woz_waarde", "verwachte_punten"),
    [
        pytest.param(
            318329,
            10.0,
            id="net_meer_dan_10_procent_lager",
            marks=pytest.mark.toelichting(
                "het verschil is -10,0003%; het rapport rondt af op -10,00"
            ),
        ),
        pytest.param(318330, 12.0, id="precies_10_procent_lager"),
        pytest.param(389070, 12.0, id="precies_10_procent_hoger"),
        pytest.param(
            389071,
            14.0,
            id="net_meer_dan_10_procent_hoger",
            marks=pytest.mark.toelichting(
                "het verschil is 10,0003%; het rapport rondt af op 10,00"
            ),
        ),
    ],
)
def test_punten_hangen_af_van_het_verschil_met_het_gemiddelde_van_het_corop_gebied(
    punten_voor_de_woz_waarde,
    vergelijk_met_testreferentie,
    woz_waarde,
    verwachte_punten,
):
    """De punten voor de WOZ-waarde hangen af van hoeveel de WOZ-waarde per m² afwijkt van het gemiddelde van het COROP-gebied.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.11.2
    - wettekst, Bijlage I onder B, onderdeel 11.1
    """
    # Rotterdam (Groot-Rijnmond, € 3.537 per m²) met 100 m²: 10% lager is € 318.330, 10% hoger € 389.070.
    eenheid = EenhedenEenheid(
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=100
        ),
        woz_eenheden=[
            EenhedenWozEenheid(
                waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=woz_waarde
            ),
        ],
    )

    groep = punten_voor_de_woz_waarde.waardeer(eenheid)

    assert punten_per_naam(groep) == {"Percentage verschil": verwachte_punten}
    vergelijk_met_testreferentie(eenheid, groep)


# Geen WOZ-waarde


def test_eenheid_zonder_recente_woz_waarde_krijgt_met_waarschuwing_het_laagste_puntenaantal(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid zonder recente WOZ-waarde krijgt met een waarschuwing het laagste puntenaantal van 10 punten.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.11.1

    De package beschouwt alleen een WOZ-waarde met waardepeildatum 1 januari van
    een van de twee jaren vóór de peildatum van de procedure als relevant.

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.11.1
    - wettekst, Bijlage I onder B, toelichting rubriek 11
    """
    # Alleen een WOZ-waarde met waardepeildatum 1 januari 2023, één jaar te oud bij peildatum 2026.
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
                waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=124000
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
    """Een eenheid zonder gebruiksoppervlakte krijgt met een waarschuwing geen waardering voor de WOZ-waarde."""
    # Alleen de gebruiksoppervlakte ontbreekt; de rest van de input is volledig.
    eenheid = EenhedenEenheid(
        id="eenheid",
        adres=EenhedenEenheidadres(
            woonplaats=EenhedenWoonplaats(code="3086", naam="ROTTERDAM")
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
    # Geen waardering is iets anders dan 0 punten: de stelselgroep heeft geen punten.
    assert groep.punten is None
    vergelijk_met_testreferentie(eenheid, groep, waarschuwingen)


def test_woz_waarde_die_niet_door_de_gebruiksoppervlakte_te_delen_is_krijgt_met_waarschuwing_geen_waardering(
    punten_voor_de_woz_waarde, vergelijk_met_testreferentie
):
    """Een eenheid waarvan de WOZ-waarde niet door de gebruiksoppervlakte te delen is, krijgt met een waarschuwing geen waardering voor de WOZ-waarde."""
    # Een gebruiksoppervlakte van 0 m², waardoor de WOZ-waarde niet te delen is.
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
    """Een eenheid zonder adres krijgt met een waarschuwing geen waardering voor de WOZ-waarde."""
    # Alleen het adres ontbreekt; de rest van de input is volledig.
    eenheid = EenhedenEenheid(
        id="eenheid",
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58
        ),
        woz_eenheden=[
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
    """Een eenheid met een woonplaatscode waarbij de package geen COROP-gebied kent, krijgt met een waarschuwing geen waardering voor de WOZ-waarde."""
    # Woonplaatscode 0100 staat niet in het extract van CBS-data waarin de package de COROP-gebieden opzoekt.
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

    Bron:
    - implementatietoelichting onzelfstandige woonruimten, 2.11.2
    """
    # Het antwoord van het Kadaster op 1013GS 22, zodat de test zonder netwerk draait.
    antwoord_van_het_kadaster = SimpleNamespace(
        raise_for_status=lambda: None,
        json=lambda: [{"identificatie": "3594", "naam": "Amsterdam"}],
    )
    monkeypatch.setattr(
        "woningwaardering.stelsels.utils.requests.post",
        lambda *args, **kwargs: antwoord_van_het_kadaster,
    )
    # Zonder woonplaatscode vraagt de package het Kadaster; dat geeft Amsterdam, de eenheid noemt Rotterdam.
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
    """De package geeft een foutmelding bij een waardepeildatum waarvoor ze geen gemiddelde WOZ-waarden per COROP-gebied heeft.

    De gemiddelde WOZ-waarden per m² staan per jaar van de waardepeildatum in
    een lookuptabel. Ontbreekt het jaar daarin, dan rekent de package niet met
    het gemiddelde van een ander jaar.

    Bron:
    - wettekst, Bijlage I onder B, toelichting rubriek 11
    - docs/voor-ontwikkelaars/data, "Gemiddelde WOZ-waarden per vierkante meter per COROP-gebied"
    """
    punten_voor_de_woz_waarde = PuntenVoorDeWozWaarde(peildatum)

    # 2021 ligt voor het eerste jaar in de lookuptabel en komt er dus niet meer bij.
    with pytest.raises(ValueError, match="2021"):
        punten_voor_de_woz_waarde._gemiddelde_woz_voor_corop_gebied(
            {"code": "40", "naam": "Groot-Rijnmond"},
            2021,
        )
