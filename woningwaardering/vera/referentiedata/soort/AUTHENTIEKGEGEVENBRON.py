
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AUTHENTIEKGEGEVENBRON:

    klantcontact = Referentiedata(
        code="KLA",
        naam="Klantcontact",
    )
    # klantcontact = ("KLA", "Klantcontact")
    """
    Gegevens zijn aangeleverd via de balie of klantcontactcentrum.
    """

    bvbsn = Referentiedata(
        code="BSN",
        naam="BvBSN",
    )
    # bvbsn = ("BSN", "BvBSN")
    """
    Gegevens zijn gedeeld vanuit de basisvoorziening burgerservicenummer
    """

    dienst_uitvoering_onderwijs = Referentiedata(
        code="DUO",
        naam="Dienst uitvoering onderwijs",
    )
    # dienst_uitvoering_onderwijs = ("DUO", "Dienst uitvoering onderwijs")
    """
    Gegevens zijn gedeeld vanuit DUO.
    """

    inkomensregistratieformulier = Referentiedata(
        code="IRF",
        naam="Inkomensregistratieformulier",
    )
    # inkomensregistratieformulier = ("IRF", "Inkomensregistratieformulier")
    """
    Gegevens zijn gedeeld vanuit het Inkomensregistratieformulier.
    """

    mijn_overheid = Referentiedata(
        code="MIJ",
        naam="Mijn Overheid",
    )
    # mijn_overheid = ("MIJ", "Mijn Overheid")
    """
    Gegevens zijn gedeeld vanuit Mijn Overheid.
    """

    qii = Referentiedata(
        code="QII",
        naam="Qii",
    )
    # qii = ("QII", "Qii")
    """
    Gegevens zijn gedeeld vanuit Qii.
    """

    uwv = Referentiedata(
        code="UWV",
        naam="UWV",
    )
    # uwv = ("UWV", "UWV")
    """
    Gegevens zijn gedeeld vanuit UWV.
    """
