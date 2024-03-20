from woningwaardering.vera.bvg.generated import Referentiedata


class Contactgegevensoort:
    e_mail = Referentiedata(
        code="EMA",
        naam="E-mail",
    )

    fax = Referentiedata(
        code="FAX",
        naam="Fax",
    )

    mobiele_telefoon = Referentiedata(
        code="MOB",
        naam="Mobiele telefoon",
    )
    """
    Mobiel telefoonnummer, ook geschikt voor SMS
    """

    pager = Referentiedata(
        code="PAG",
        naam="Pager",
    )

    post = Referentiedata(
        code="POS",
        naam="Post",
    )

    social_media = Referentiedata(
        code="SOC",
        naam="Social media",
    )

    telefoon = Referentiedata(
        code="TEL",
        naam="Telefoon",
    )
    """
    Gewoon telefoonnummer
    """
