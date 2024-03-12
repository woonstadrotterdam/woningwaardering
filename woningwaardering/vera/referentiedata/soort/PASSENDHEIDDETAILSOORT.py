
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PASSENDHEIDDETAILSOORT:

    bijzondere_gezinssituatie = Referentiedata(
        code="BIJ",
        naam="Bijzondere gezinssituatie",
    )
    # bijzondere_gezinssituatie = ("BIJ", "Bijzondere gezinssituatie")
    """
    Niet-passende toewijzing, noodzakelijk geacht omdat sprake is van een bijzondere
    woonbehoefte waarvoor geen regulier passende woning beschikbaar is. Bijvoorbeeld een
    zeer groot gezin of een bijzondere gezinssamenstelling.
    """

    herstructurering = Referentiedata(
        code="HER",
        naam="Herstructurering",
    )
    # herstructurering = ("HER", "Herstructurering")
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. herstructurering
    """

    herhuisvesting = Referentiedata(
        code="HHV",
        naam="Herhuisvesting",
    )
    # herhuisvesting = ("HHV", "Herhuisvesting")
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. calamiteit of andere dringende
    oorzaak. Let op: voor herhuisvesting in verband met herstructurering gebruik
    passenheiddetailsoort 'Herstructurering'
    """
