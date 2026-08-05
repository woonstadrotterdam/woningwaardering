from datetime import date

from woningwaardering.stelsels.gedeelde_logica.energieprestatie.energieprestatie import (
    energieprestatie_met_geldig_label,
    in_vereenvoudigd_label_periode,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
)
from woningwaardering.vera.referentiedata import (
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
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
    peildatum = date(2020, 1, 1)
    energieprestatie = _energieprestatie(
        soort=Energieprestatiesoort.energie_index,
        begindatum=date(2018, 1, 1),
        einddatum=date(2028, 1, 1),
    )
    eenheid = EenhedenEenheid(energieprestaties=[energieprestatie])

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is energieprestatie


def test_energieprestatie_met_geldig_label_negeert_energieprestatie_zonder_label() -> (
    None
):
    peildatum = date(2020, 1, 1)
    eenheid = EenhedenEenheid(
        energieprestaties=[
            _energieprestatie(
                soort=Energieprestatiesoort.energie_index,
                begindatum=date(2018, 1, 1),
                einddatum=date(2028, 1, 1),
                label=None,
            )
        ]
    )

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is None


def test_energieprestatie_met_geldig_label_negeert_energieprestatie_buiten_geldigheidsperiode() -> (
    None
):
    peildatum = date(2030, 1, 1)
    eenheid = EenhedenEenheid(
        energieprestaties=[
            _energieprestatie(
                soort=Energieprestatiesoort.energie_index,
                begindatum=date(2018, 1, 1),
                einddatum=date(2028, 1, 1),
            )
        ]
    )

    assert energieprestatie_met_geldig_label(peildatum, eenheid) is None
