
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class CONTACTGEGEVENSOORT:

    e_mail = Referentiedata(
        code="EMA",
        naam="E-mail",
    )
    # e_mail = ("EMA", "E-mail")

    fax = Referentiedata(
        code="FAX",
        naam="Fax",
    )
    # fax = ("FAX", "Fax")

    mobiele_telefoon = Referentiedata(
        code="MOB",
        naam="Mobiele telefoon",
    )
    # mobiele_telefoon = ("MOB", "Mobiele telefoon")
    """
    Mobiel telefoonnummer, ook geschikt voor SMS
    """

    pager = Referentiedata(
        code="PAG",
        naam="Pager",
    )
    # pager = ("PAG", "Pager")

    post = Referentiedata(
        code="POS",
        naam="Post",
    )
    # post = ("POS", "Post")

    social_media = Referentiedata(
        code="SOC",
        naam="Social media",
    )
    # social_media = ("SOC", "Social media")

    telefoon = Referentiedata(
        code="TEL",
        naam="Telefoon",
    )
    # telefoon = ("TEL", "Telefoon")
    """
    Gewoon telefoonnummer
    """
