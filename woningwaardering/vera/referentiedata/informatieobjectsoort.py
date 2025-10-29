from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InformatieobjectsoortReferentiedata(Referentiedata):
    pass


class Informatieobjectsoort(Referentiedatasoort):
    brochure = InformatieobjectsoortReferentiedata(
        code="BRO",
        naam="Brochure",
    )

    document = InformatieobjectsoortReferentiedata(
        code="DOC",
        naam="Document",
    )
    """
    Text bestand met (HTML) of zonder opmaak (Text)
    """

    foto = InformatieobjectsoortReferentiedata(
        code="FOT",
        naam="Foto",
    )
    """
    Foto, Image, Plaatje, Afbeelding
    """

    kopie = InformatieobjectsoortReferentiedata(
        code="KOP",
        naam="Kopie",
    )

    notitie = InformatieobjectsoortReferentiedata(
        code="NOT",
        naam="Notitie",
    )
    """
    Het informatieobject is een notitie- of memo (tekst)
    """

    overeenkomst = InformatieobjectsoortReferentiedata(
        code="OVE",
        naam="Overeenkomst",
    )

    plattegrond = InformatieobjectsoortReferentiedata(
        code="PLA",
        naam="Plattegrond",
    )

    plan = InformatieobjectsoortReferentiedata(
        code="PLN",
        naam="Plan",
    )

    rapport = InformatieobjectsoortReferentiedata(
        code="RAP",
        naam="Rapport",
    )

    verslag = InformatieobjectsoortReferentiedata(
        code="VER",
        naam="Verslag",
    )

    video = InformatieobjectsoortReferentiedata(
        code="VID",
        naam="Video",
    )
