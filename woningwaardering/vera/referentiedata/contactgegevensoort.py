from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ContactgegevensoortReferentiedata(Referentiedata):
    pass


class Contactgegevensoort(Referentiedatasoort):
    e_mail = ContactgegevensoortReferentiedata(
        code="EMA",
        naam="E-mail",
    )

    fax = ContactgegevensoortReferentiedata(
        code="FAX",
        naam="Fax",
    )

    mobiele_telefoon = ContactgegevensoortReferentiedata(
        code="MOB",
        naam="Mobiele telefoon",
    )
    """
    Mobiel telefoonnummer, ook geschikt voor SMS
    """

    pager = ContactgegevensoortReferentiedata(
        code="PAG",
        naam="Pager",
    )

    post = ContactgegevensoortReferentiedata(
        code="POS",
        naam="Post",
    )

    social_media = ContactgegevensoortReferentiedata(
        code="SOC",
        naam="Social media",
    )

    telefoon = ContactgegevensoortReferentiedata(
        code="TEL",
        naam="Telefoon",
    )
    """
    Gewoon telefoonnummer
    """
