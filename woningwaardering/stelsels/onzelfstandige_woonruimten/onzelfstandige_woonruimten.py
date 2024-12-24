from datetime import date

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Aftrekpunten,
    BijzondereVoorzieningen,
    Buitenruimten,
    Energieprestatie,
    GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    GemeenschappelijkeParkeerruimten,
    Keuken,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
    PrijsopslagMonumenten,
    PuntenVoorDeWozWaarde,
    Sanitair,
    VerkoelingEnVerwarming,
)
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class OnzelfstandigeWoonruimten(Stelsel):
    def __init__(self, peildatum: date = date.today()) -> None:
        super().__init__(
            stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
            stelselgroepen=[
                OppervlakteVanVertrekken,
                OppervlakteVanOverigeRuimten,
                VerkoelingEnVerwarming,
                Energieprestatie,
                Keuken,
                Sanitair,
                Buitenruimten,
                GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
                GemeenschappelijkeParkeerruimten,
                PuntenVoorDeWozWaarde,
                BijzondereVoorzieningen,
                Aftrekpunten,
                PrijsopslagMonumenten,
            ],
        )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=OnzelfstandigeWoonruimten(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/input/voorbeeld_beleidsboek.json"
        )
