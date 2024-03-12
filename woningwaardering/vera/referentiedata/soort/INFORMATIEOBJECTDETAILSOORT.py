
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INFORMATIEOBJECTDETAILSOORT:

    advertentietekst = Referentiedata(
        code="ADT",
        naam="Advertentietekst",
    )
    # advertentietekst = ("ADT", "Advertentietekst")
    """
    Advertentietekst met (HTML) of zonder opmaak (Text).
    """

    advies = Referentiedata(
        code="ADV",
        naam="Advies",
    )
    # advies = ("ADV", "Advies")

    agenda = Referentiedata(
        code="AGE",
        naam="Agenda",
    )
    # agenda = ("AGE", "Agenda")

    dag = Referentiedata(
        code="DAG",
        naam="Dag",
    )
    # dag = ("DAG", "Dag")

    evaluatie = Referentiedata(
        code="EVA",
        naam="Evaluatie",
    )
    # evaluatie = ("EVA", "Evaluatie")

    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )
    # inspectie = ("INS", "Inspectie")

    jaar = Referentiedata(
        code="JAA",
        naam="Jaar",
    )
    # jaar = ("JAA", "Jaar")

    kwartaal = Referentiedata(
        code="KWA",
        naam="Kwartaal",
    )
    # kwartaal = ("KWA", "Kwartaal")

    maand = Referentiedata(
        code="MAA",
        naam="Maand",
    )
    # maand = ("MAA", "Maand")

    notulen = Referentiedata(
        code="NOT",
        naam="Notulen",
    )
    # notulen = ("NOT", "Notulen")

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )
    # onderhoud = ("OND", "Onderhoud")

    programma = Referentiedata(
        code="PRG",
        naam="Programma",
    )
    # programma = ("PRG", "Programma")

    project = Referentiedata(
        code="PRJ",
        naam="Project",
    )
    # project = ("PRJ", "Project")

    week = Referentiedata(
        code="WEE",
        naam="Week",
    )
    # week = ("WEE", "Week")
