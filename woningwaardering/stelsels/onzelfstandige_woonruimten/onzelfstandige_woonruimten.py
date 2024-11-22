from datetime import date

from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Aftrekpunten,
    BijzondereVoorzieningen,
    Buitenruimten,
    Energieprestatie,
    GemeenschappelijkeParkeerruimten,
    Keuken,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
    PrijsopslagMonumenten,
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
                GemeenschappelijkeParkeerruimten,
                # PuntenVoorDeWOZWaarde,
                BijzondereVoorzieningen,
                Aftrekpunten,
                PrijsopslagMonumenten,
            ],
        )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=OnzelfstandigeWoonruimten(),
        eenheid_input="tests/data/onzelfstandige_woonruimten/input/15004000185.json",
        strict=False,
    )
