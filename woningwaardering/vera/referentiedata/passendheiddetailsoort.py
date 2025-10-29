from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PassendheiddetailsoortReferentiedata(Referentiedata):
    pass


class Passendheiddetailsoort(Referentiedatasoort):
    bijzondere_gezinssituatie = PassendheiddetailsoortReferentiedata(
        code="BIJ",
        naam="Bijzondere gezinssituatie",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht omdat sprake is van een bijzondere
    woonbehoefte waarvoor geen regulier passende woning beschikbaar is. Bijvoorbeeld
    een zeer groot gezin of een bijzondere gezinssamenstelling.
    """

    herstructurering = PassendheiddetailsoortReferentiedata(
        code="HER",
        naam="Herstructurering",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. herstructurering
    """

    herhuisvesting = PassendheiddetailsoortReferentiedata(
        code="HHV",
        naam="Herhuisvesting",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. calamiteit of andere dringende
    oorzaak. Let op: voor herhuisvesting in verband met herstructurering gebruik
    passenheiddetailsoort 'Herstructurering'
    """
