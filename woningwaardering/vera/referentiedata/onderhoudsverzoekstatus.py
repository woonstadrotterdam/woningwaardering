from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Onderhoudsverzoekstatus(Enum):
    afgehandeld = Referentiedata(
        code="AFG",
        naam="Afgehandeld",
    )
    """
    Het onderhoudsverzoek is volledig afgehandeld
    """

    ter_beoordeling = Referentiedata(
        code="BEO",
        naam="Ter beoordeling",
    )
    """
    Voor de situatie dat het KCC een verzoek mag aanmaken maar niet als opdracht
    verstrekken. (Verschil in verantwoordelijkheid bedrijfsproces Klantbediening en
    Onderhouden eenheden)
    """

    financieel_afwikkelen = Referentiedata(
        code="FIN",
        naam="Financieel afwikkelen",
    )
    """
    Het onderhoudsverzoek wordt financieel afgewikkeld. Dit kan betekenen dat er kosten
    in rekening gebracht worden bij huurders of derden (bijv. verzekering)
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    Het onderhoudsverzoek is geannuleerd, dat wil zeggen dat het verzoek niet  is
    uitgevoerd.
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    Het onderhoudsverzoek is in behandeling genomen en de uitvoering is nog niet
    afgerond
    """

    geregistreerd = Referentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    """
    Het onderzhoudsverzoek is geregistreerd maar nog niet in behandeling genomen.
    """

    technisch_gereed = Referentiedata(
        code="TEC",
        naam="Technisch gereed",
    )
    """
    Het onderhoudsverzoek is technisch afgehandeld en de uitvoering hiervan kan
    beoordeeld worden. Is het onderhoudsverzoek naar tevredenheid uitgevoerd?
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
