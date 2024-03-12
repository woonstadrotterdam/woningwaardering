
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INKOOPFACTUURSTATUS:

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    # afgewezen = ("AFG", "Afgewezen")
    """
    Inkoopfactuur is afgewezen.
    """

    afgehandeld = Referentiedata(
        code="AFH",
        naam="Afgehandeld",
    )
    # afgehandeld = ("AFH", "Afgehandeld")
    """
    Inkoopfactuur is afgehandeld.
    """

    afgekeurd = Referentiedata(
        code="AGK",
        naam="Afgekeurd",
    )
    # afgekeurd = ("AGK", "Afgekeurd")
    """
    Inkoopfactuur is afgekeurd.
    """

    aangeboden_ter_betaling = Referentiedata(
        code="ATB",
        naam="Aangeboden ter betaling",
    )
    # aangeboden_ter_betaling = ("ATB", "Aangeboden ter betaling")
    """
    Inkoopfactuur is aangeboden ter betaling.
    """

    aangeboden_ter_goedkeuring = Referentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    # aangeboden_ter_goedkeuring = ("ATG", "Aangeboden ter goedkeuring")
    """
    Inkoopfactuur is aangeboden ter goedkeuring.
    """

    betaald = Referentiedata(
        code="BET",
        naam="Betaald",
    )
    # betaald = ("BET", "Betaald")
    """
    Inkoopfactuur is betaald.
    """

    geblokkeerd = Referentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )
    # geblokkeerd = ("BLK", "Geblokkeerd")
    """
    Inkoopfactuur is geblokkeerd.
    """

    goedgekeurd = Referentiedata(
        code="GDK",
        naam="Goedgekeurd",
    )
    # goedgekeurd = ("GDK", "Goedgekeurd")
    """
    Inkoopfactuur is goedgekeurd.
    """

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
    # historisch = ("HIS", "Historisch")
    """
    Inkoopfactuur is gearchiveerd/historisch.
    """

    in_behandeling = Referentiedata(
        code="IBH",
        naam="In behandeling",
    )
    # in_behandeling = ("IBH", "In behandeling")
    """
    Inkoopfactuur is in behandeling.
    """

    geregistreerd = Referentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    # geregistreerd = ("REG", "Geregistreerd")
    """
    Inkoopfactuur is geregistreerd.
    """

    wacht_op_creditfactuur = Referentiedata(
        code="WOC",
        naam="Wacht op creditfactuur",
    )
    # wacht_op_creditfactuur = ("WOC", "Wacht op creditfactuur")
    """
    Er wordt gewacht op een creditfactuur.
    """
