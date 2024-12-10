from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InkoopfactuurstatusReferentiedata(Referentiedata):
    pass


class Inkoopfactuurstatus(Referentiedatasoort):
    afgewezen = InkoopfactuurstatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Inkoopfactuur is afgewezen.
    """

    afgehandeld = InkoopfactuurstatusReferentiedata(
        code="AFH",
        naam="Afgehandeld",
    )
    """
    Inkoopfactuur is afgehandeld.
    """

    afgekeurd = InkoopfactuurstatusReferentiedata(
        code="AGK",
        naam="Afgekeurd",
    )
    """
    Inkoopfactuur is afgekeurd.
    """

    aangeboden_ter_betaling = InkoopfactuurstatusReferentiedata(
        code="ATB",
        naam="Aangeboden ter betaling",
    )
    """
    Inkoopfactuur is aangeboden ter betaling.
    """

    aangeboden_ter_goedkeuring = InkoopfactuurstatusReferentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    """
    Inkoopfactuur is aangeboden ter goedkeuring.
    """

    betaald = InkoopfactuurstatusReferentiedata(
        code="BET",
        naam="Betaald",
    )
    """
    Inkoopfactuur is betaald.
    """

    geblokkeerd = InkoopfactuurstatusReferentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )
    """
    Inkoopfactuur is geblokkeerd.
    """

    goedgekeurd = InkoopfactuurstatusReferentiedata(
        code="GDK",
        naam="Goedgekeurd",
    )
    """
    Inkoopfactuur is goedgekeurd.
    """

    historisch = InkoopfactuurstatusReferentiedata(
        code="HIS",
        naam="Historisch",
    )
    """
    Inkoopfactuur is gearchiveerd/historisch.
    """

    in_behandeling = InkoopfactuurstatusReferentiedata(
        code="IBH",
        naam="In behandeling",
    )
    """
    Inkoopfactuur is in behandeling.
    """

    geregistreerd = InkoopfactuurstatusReferentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    """
    Inkoopfactuur is geregistreerd.
    """

    wacht_op_creditfactuur = InkoopfactuurstatusReferentiedata(
        code="WOC",
        naam="Wacht op creditfactuur",
    )
    """
    Er wordt gewacht op een creditfactuur.
    """
