from datetime import date

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
