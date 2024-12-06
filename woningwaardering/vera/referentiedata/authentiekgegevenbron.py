from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Authentiekgegevenbron(Referentiedatasoort):
    klantcontact = Referentiedata(
        code="KLA",
        naam="Klantcontact",
    )
    """
    Gegevens zijn aangeleverd via de balie of klantcontactcentrum.
    """

    bvbsn = Referentiedata(
        code="BSN",
        naam="BvBSN",
    )
    """
    Gegevens zijn gedeeld vanuit de basisvoorziening burgerservicenummer
    """

    dienst_uitvoering_onderwijs = Referentiedata(
        code="DUO",
        naam="Dienst uitvoering onderwijs",
    )
    """
    Gegevens zijn gedeeld vanuit DUO.
    """

    inkomensregistratieformulier = Referentiedata(
        code="IRF",
        naam="Inkomensregistratieformulier",
    )
    """
    Gegevens zijn gedeeld vanuit het Inkomensregistratieformulier.
    """

    mijn_overheid = Referentiedata(
        code="MIJ",
        naam="Mijn Overheid",
    )
    """
    Gegevens zijn gedeeld vanuit Mijn Overheid.
    """

    qii = Referentiedata(
        code="QII",
        naam="Qii",
    )
    """
    Gegevens zijn gedeeld vanuit Qii.
    """

    uwv = Referentiedata(
        code="UWV",
        naam="UWV",
    )
    """
    Gegevens zijn gedeeld vanuit UWV.
    """
