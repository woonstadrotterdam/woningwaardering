from woningwaardering.vera.bvg.generated import Referentiedata


class Informatieobjectdetailsoort:
    advertentietekst = Referentiedata(
        code="ADT",
        naam="Advertentietekst",
    )
    """
    Advertentietekst met (HTML) of zonder opmaak (Text).
    """

    advies = Referentiedata(
        code="ADV",
        naam="Advies",
    )

    agenda = Referentiedata(
        code="AGE",
        naam="Agenda",
    )

    dag = Referentiedata(
        code="DAG",
        naam="Dag",
    )

    evaluatie = Referentiedata(
        code="EVA",
        naam="Evaluatie",
    )

    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )

    jaar = Referentiedata(
        code="JAA",
        naam="Jaar",
    )

    kwartaal = Referentiedata(
        code="KWA",
        naam="Kwartaal",
    )

    maand = Referentiedata(
        code="MAA",
        naam="Maand",
    )

    notulen = Referentiedata(
        code="NOT",
        naam="Notulen",
    )

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )

    programma = Referentiedata(
        code="PRG",
        naam="Programma",
    )

    project = Referentiedata(
        code="PRJ",
        naam="Project",
    )

    week = Referentiedata(
        code="WEE",
        naam="Week",
    )
