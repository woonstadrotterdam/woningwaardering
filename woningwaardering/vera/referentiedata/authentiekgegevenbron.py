from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Authentiekgegevenbron(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
