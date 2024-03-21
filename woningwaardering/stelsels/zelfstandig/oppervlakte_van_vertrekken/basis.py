from woningwaardering.stelsels.stelselgroep import Stelselgroep


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(self, peildatum) -> None:
        super().__init__(
            peildatum,
            stelsel="zelfstandig",
            module="oppervlakte_van_vertrekken",
        )
