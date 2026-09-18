from datetime import date

import pytest

from woningwaardering.stelsels.gedeelde_logica.energieprestatie.energieprestatie import (
    energieprestatie_met_geldig_label,
    in_vereenvoudigd_label_periode,
    parse_energie_index_waarde,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.energieprestatie import (
    Energieprestatie,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
    EenhedenPand,
)
from woningwaardering.vera.referentiedata import (
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Pandsoort,
)


def test_in_vereenvoudigd_label_periode_begin_van_periode() -> None:
    assert in_vereenvoudigd_label_periode(date(2015, 1, 1)) is True


def test_in_vereenvoudigd_label_periode_net_voor_periode() -> None:
    assert in_vereenvoudigd_label_periode(date(2014, 12, 31)) is False


def test_in_vereenvoudigd_label_periode_einde_van_periode_exclusief() -> None:
    assert in_vereenvoudigd_label_periode(date(2021, 1, 1)) is False


def test_in_vereenvoudigd_label_periode_midden_in_periode() -> None:
    assert in_vereenvoudigd_label_periode(date(2018, 6, 1)) is True


def _energieprestatie(
    *,
    soort: Energieprestatiesoort,
    begindatum: date,
    einddatum: date,
    label: Energielabel | None = Energielabel.c,
) -> EenhedenEnergieprestatie:
    return EenhedenEnergieprestatie(
        soort=soort,
        status=Energieprestatiestatus.definitief,
        begindatum=begindatum,
        einddatum=einddatum,
        label=label,
        waarde="1.2",
    )


def test_energieprestatie_met_geldig_label_vindt_geldige_energieprestatie() -> None:
    peildatum = date(2023, 1, 1)
    energieprestatie = _energieprestatie(
        soort=Energieprestatiesoort.energielabel_conform_nta8800,
        begindatum=date(2022, 1, 1),
        einddatum=date(2032, 1, 1),
    )
    eenheid = EenhedenEenheid(energieprestaties=[energieprestatie])

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is energieprestatie


def test_energieprestatie_met_geldig_label_negeert_label_in_vereenvoudigde_periode() -> (
    None
):
    peildatum = date(2020, 1, 1)
    eenheid = EenhedenEenheid(
        energieprestaties=[
            _energieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                begindatum=date(2018, 1, 1),
                einddatum=date(2028, 1, 1),
            )
        ]
    )

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is None


def test_energieprestatie_met_geldig_label_accepteert_energie_index_in_vereenvoudigde_periode() -> (
    None
):
    peildatum = date(2020, 1, 1)
    energieprestatie = _energieprestatie(
        soort=Energieprestatiesoort.energie_index,
        begindatum=date(2018, 1, 1),
        einddatum=date(2028, 1, 1),
        label=None,
    )
    eenheid = EenhedenEenheid(energieprestaties=[energieprestatie])

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is energieprestatie


def test_energieprestatie_met_geldig_label_negeert_energieprestatie_zonder_label() -> (
    None
):
    peildatum = date(2023, 1, 1)
    eenheid = EenhedenEenheid(
        energieprestaties=[
            _energieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                begindatum=date(2022, 1, 1),
                einddatum=date(2032, 1, 1),
                label=None,
            )
        ]
    )

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is None


def test_energieprestatie_met_geldig_label_negeert_energieprestatie_buiten_geldigheidsperiode() -> (
    None
):
    peildatum = date(2035, 1, 1)
    eenheid = EenhedenEenheid(
        energieprestaties=[
            _energieprestatie(
                soort=Energieprestatiesoort.energielabel_conform_nta8800,
                begindatum=date(2022, 1, 1),
                einddatum=date(2032, 1, 1),
            )
        ]
    )

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is None


def test_parse_energie_index_waarde_accepteert_punt() -> None:
    assert (
        parse_energie_index_waarde(
            "1.48", eenheid_id="1", stelselgroep_naam="Energieprestatie"
        )
        == 1.48
    )


def test_parse_energie_index_waarde_komma_geeft_userwarning_en_none() -> None:
    with pytest.warns(
        UserWarning, match="Gebruik een punt als decimaalscheidingsteken"
    ):
        assert (
            parse_energie_index_waarde(
                "1,48", eenheid_id="1", stelselgroep_naam="Energieprestatie"
            )
            is None
        )


def test_parse_energie_index_waarde_ongeldige_string_zonder_komma() -> None:
    with pytest.warns(UserWarning) as records:
        assert (
            parse_energie_index_waarde(
                "abc", eenheid_id="1", stelselgroep_naam="Energieprestatie"
            )
            is None
        )
    assert all(
        "Gebruik een punt als decimaalscheidingsteken" not in str(record.message)
        for record in records
    )


def test_Energieprestatie_ongeldige_energie_index_waarde_naar_bouwjaar() -> None:
    eenheid = EenhedenEenheid(
        id="1",
        bouwjaar=1990,
        monumenten=[],
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2018, 6, 1),
                einddatum=date(2028, 6, 1),
                label=Energielabel.a,
                waarde="1,48",
            )
        ],
    )
    with pytest.warns(
        UserWarning, match="Gebruik een punt als decimaalscheidingsteken"
    ):
        groep = Energieprestatie(peildatum=date(2026, 7, 1)).waardeer(eenheid)

    namen = [
        waardering.criterium.naam
        for waardering in groep.woningwaarderingen or []
        if waardering.criterium is not None
    ]
    assert any(naam is not None and naam.startswith("Bouwjaar") for naam in namen)
