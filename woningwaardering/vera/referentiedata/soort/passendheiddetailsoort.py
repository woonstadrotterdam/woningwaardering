from vera.referentiedata.models import Referentiedata


class Passendheiddetailsoort:
    bijzondere_gezinssituatie = Referentiedata(
        code="BIJ",
        naam="Bijzondere gezinssituatie",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht omdat sprake is van een bijzondere
    woonbehoefte waarvoor geen regulier passende woning beschikbaar is. Bijvoorbeeld een
    zeer groot gezin of een bijzondere gezinssamenstelling.
    """

    herstructurering = Referentiedata(
        code="HER",
        naam="Herstructurering",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. herstructurering
    """

    herhuisvesting = Referentiedata(
        code="HHV",
        naam="Herhuisvesting",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. calamiteit of andere dringende
    oorzaak. Let op: voor herhuisvesting in verband met herstructurering gebruik
    passenheiddetailsoort &#39;Herstructurering&#39;
    """
