from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AuthentiekgegevenbronReferentiedata(Referentiedata):
    pass


class Authentiekgegevenbron(Referentiedatasoort):
    klantcontact = AuthentiekgegevenbronReferentiedata(
        code="KLA",
        naam="Klantcontact",
    )
    """
    Gegevens zijn aangeleverd via de balie of klantcontactcentrum.
    """

    bvbsn = AuthentiekgegevenbronReferentiedata(
        code="BSN",
        naam="BvBSN",
    )
    """
    Gegevens zijn gedeeld vanuit de basisvoorziening burgerservicenummer
    """

    dienst_uitvoering_onderwijs = AuthentiekgegevenbronReferentiedata(
        code="DUO",
        naam="Dienst uitvoering onderwijs",
    )
    """
    Gegevens zijn gedeeld vanuit DUO.
    """

    inkomensregistratieformulier = AuthentiekgegevenbronReferentiedata(
        code="IRF",
        naam="Inkomensregistratieformulier",
    )
    """
    Gegevens zijn gedeeld vanuit het Inkomensregistratieformulier.
    """

    mijn_overheid = AuthentiekgegevenbronReferentiedata(
        code="MIJ",
        naam="Mijn Overheid",
    )
    """
    Gegevens zijn gedeeld vanuit Mijn Overheid.
    """

    qii = AuthentiekgegevenbronReferentiedata(
        code="QII",
        naam="Qii",
    )
    """
    Gegevens zijn gedeeld vanuit Qii.
    """

    uwv = AuthentiekgegevenbronReferentiedata(
        code="UWV",
        naam="UWV",
    )
    """
    Gegevens zijn gedeeld vanuit UWV.
    """
