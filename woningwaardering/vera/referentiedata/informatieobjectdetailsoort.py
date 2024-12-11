from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InformatieobjectdetailsoortReferentiedata(Referentiedata):
    pass


class Informatieobjectdetailsoort(Referentiedatasoort):
    advertentietekst = InformatieobjectdetailsoortReferentiedata(
        code="ADT",
        naam="Advertentietekst",
    )
    """
    Advertentietekst met (HTML) of zonder opmaak (Text).
    """

    advies = InformatieobjectdetailsoortReferentiedata(
        code="ADV",
        naam="Advies",
    )

    agenda = InformatieobjectdetailsoortReferentiedata(
        code="AGE",
        naam="Agenda",
    )

    dag = InformatieobjectdetailsoortReferentiedata(
        code="DAG",
        naam="Dag",
    )

    evaluatie = InformatieobjectdetailsoortReferentiedata(
        code="EVA",
        naam="Evaluatie",
    )

    inspectie = InformatieobjectdetailsoortReferentiedata(
        code="INS",
        naam="Inspectie",
    )

    jaar = InformatieobjectdetailsoortReferentiedata(
        code="JAA",
        naam="Jaar",
    )

    kwartaal = InformatieobjectdetailsoortReferentiedata(
        code="KWA",
        naam="Kwartaal",
    )

    maand = InformatieobjectdetailsoortReferentiedata(
        code="MAA",
        naam="Maand",
    )

    notulen = InformatieobjectdetailsoortReferentiedata(
        code="NOT",
        naam="Notulen",
    )

    onderhoud = InformatieobjectdetailsoortReferentiedata(
        code="OND",
        naam="Onderhoud",
    )

    programma = InformatieobjectdetailsoortReferentiedata(
        code="PRG",
        naam="Programma",
    )

    project = InformatieobjectdetailsoortReferentiedata(
        code="PRJ",
        naam="Project",
    )

    week = InformatieobjectdetailsoortReferentiedata(
        code="WEE",
        naam="Week",
    )
