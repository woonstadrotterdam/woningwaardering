from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OnderhoudsverzoekstatusReferentiedata(Referentiedata):
    pass


class Onderhoudsverzoekstatus(Referentiedatasoort):
    afgehandeld = OnderhoudsverzoekstatusReferentiedata(
        code="AFG",
        naam="Afgehandeld",
    )
    """
    Het onderhoudsverzoek is volledig afgehandeld
    """

    ter_beoordeling = OnderhoudsverzoekstatusReferentiedata(
        code="BEO",
        naam="Ter beoordeling",
    )
    """
    Voor de situatie dat het KCC een verzoek mag aanmaken maar niet als opdracht
    verstrekken. (Verschil in verantwoordelijkheid bedrijfsproces Klantbediening en
    Onderhouden eenheden)
    """

    financieel_afwikkelen = OnderhoudsverzoekstatusReferentiedata(
        code="FIN",
        naam="Financieel afwikkelen",
    )
    """
    Het onderhoudsverzoek wordt financieel afgewikkeld. Dit kan betekenen dat er kosten
    in rekening gebracht worden bij huurders of derden (bijv. verzekering)
    """

    geannuleerd = OnderhoudsverzoekstatusReferentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    Het onderhoudsverzoek is geannuleerd, dat wil zeggen dat het verzoek niet  is
    uitgevoerd.
    """

    in_behandeling = OnderhoudsverzoekstatusReferentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    Het onderhoudsverzoek is in behandeling genomen en de uitvoering is nog niet
    afgerond
    """

    geregistreerd = OnderhoudsverzoekstatusReferentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    """
    Het onderzhoudsverzoek is geregistreerd maar nog niet in behandeling genomen.
    """

    technisch_gereed = OnderhoudsverzoekstatusReferentiedata(
        code="TEC",
        naam="Technisch gereed",
    )
    """
    Het onderhoudsverzoek is technisch afgehandeld en de uitvoering hiervan kan
    beoordeeld worden. Is het onderhoudsverzoek naar tevredenheid uitgevoerd?
    """
