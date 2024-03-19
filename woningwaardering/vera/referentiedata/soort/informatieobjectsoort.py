from vera.bvg.generated import Referentiedata


class Informatieobjectsoort:
    brochure = Referentiedata(
        code="BRO",
        naam="Brochure",
    )

    document = Referentiedata(
        code="DOC",
        naam="Document",
    )
    """
    Text bestand met (HTML) of zonder opmaak (Text)
    """

    foto = Referentiedata(
        code="FOT",
        naam="Foto",
    )
    """
    Foto, Image, Plaatje, Afbeelding
    """

    kopie = Referentiedata(
        code="KOP",
        naam="Kopie",
    )

    notitie = Referentiedata(
        code="NOT",
        naam="Notitie",
    )
    """
    Het informatieobject is een notitie- of memo (tekst)
    """

    overeenkomst = Referentiedata(
        code="OVE",
        naam="Overeenkomst",
    )

    plattegrond = Referentiedata(
        code="PLA",
        naam="Plattegrond",
    )

    plan = Referentiedata(
        code="PLN",
        naam="Plan",
    )

    rapport = Referentiedata(
        code="RAP",
        naam="Rapport",
    )

    verslag = Referentiedata(
        code="VER",
        naam="Verslag",
    )

    video = Referentiedata(
        code="VID",
        naam="Video",
    )
