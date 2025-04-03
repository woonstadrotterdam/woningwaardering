import warnings
from datetime import date

from loguru import logger

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


def get_eenheid():
    eenheid = EenhedenEenheid()

    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten

    # vul EenhedenAdres in
    eenheid.adres = EenhedenEenheidadres(
        postcode="26236KB",
        huisnummer="1",
        # huisletter="A", # optioneel
        # huisnummer_toevoeging="2", # optioneel
    )
    # en/of vul EenhedenWoonplaats in
    eenheid.adres = EenhedenEenheidadres(
        woonplaats=EenhedenWoonplaats(naam="ROTTERDAM", code="3086"),
    )

    eenheid.adresseerbaar_object_basisregistratie = (
        EenhedenAdresseerbaarObjectBasisregistratie(
            bag_gebruikers_oppervlakte=58.0,
        )
    )

    eenheid.woz_eenheden = [
        EenhedenWozEenheid(
            waardepeildatum=date(2023, 1, 1),
            vastgestelde_waarde=300000.0,
        )
    ]

    return eenheid


def main():
    logger.enable("woningwaardering")
    warnings.filterwarnings("default")
    eenheid = get_eenheid()
    woningwaardering = Woningwaardering().waardeer(eenheid)
    print(naar_tabel(woningwaardering))


if __name__ == "__main__":
    main()
