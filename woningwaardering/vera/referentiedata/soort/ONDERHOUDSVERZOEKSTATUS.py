
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ONDERHOUDSVERZOEKSTATUS:

    afgehandeld = Referentiedata(
        code="AFG",
        naam="Afgehandeld",
    )
    # afgehandeld = ("AFG", "Afgehandeld")
    """
    Het onderhoudsverzoek is volledig afgehandeld
    """

    ter_beoordeling = Referentiedata(
        code="BEO",
        naam="Ter beoordeling",
    )
    # ter_beoordeling = ("BEO", "Ter beoordeling")
    """
    Voor de situatie dat het KCC een verzoek mag aanmaken maar niet als opdracht
    verstrekken. (Verschil in verantwoordelijkheid bedrijfsproces Klantbediening en
    Onderhouden eenheden)
    """

    financieel_afwikkelen = Referentiedata(
        code="FIN",
        naam="Financieel afwikkelen",
    )
    # financieel_afwikkelen = ("FIN", "Financieel afwikkelen")
    """
    Het onderhoudsverzoek wordt financieel afgewikkeld. Dit kan betekenen dat er kosten
    in rekening gebracht worden bij huurders of derden (bijv. verzekering)
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    # geannuleerd = ("GEA", "Geannuleerd")
    """
    Het onderhoudsverzoek is geannuleerd, dat wil zeggen dat het verzoek niet is
    uitgevoerd.
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    # in_behandeling = ("INB", "In behandeling")
    """
    Het onderhoudsverzoek is in behandeling genomen en de uitvoering is nog niet
    afgerond
    """

    geregistreerd = Referentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    # geregistreerd = ("REG", "Geregistreerd")
    """
    Het onderzhoudsverzoek is geregistreerd maar nog niet in behandeling genomen.
    """

    technisch_gereed = Referentiedata(
        code="TEC",
        naam="Technisch gereed",
    )
    # technisch_gereed = ("TEC", "Technisch gereed")
    """
    Het onderhoudsverzoek is technisch afgehandeld en de uitvoering hiervan kan
    beoordeeld worden. Is het onderhoudsverzoek naar tevredenheid uitgevoerd?
    """
