
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INFORMATIEOBJECTSOORT:

    brochure = Referentiedata(
        code="BRO",
        naam="Brochure",
    )
    # brochure = ("BRO", "Brochure")

    document = Referentiedata(
        code="DOC",
        naam="Document",
    )
    # document = ("DOC", "Document")
    """
    Text bestand met (HTML) of zonder opmaak (Text)
    """

    foto = Referentiedata(
        code="FOT",
        naam="Foto",
    )
    # foto = ("FOT", "Foto")
    """
    Foto, Image, Plaatje, Afbeelding
    """

    kopie = Referentiedata(
        code="KOP",
        naam="Kopie",
    )
    # kopie = ("KOP", "Kopie")

    notitie = Referentiedata(
        code="NOT",
        naam="Notitie",
    )
    # notitie = ("NOT", "Notitie")
    """
    Het informatieobject is een notitie- of memo (tekst)
    """

    overeenkomst = Referentiedata(
        code="OVE",
        naam="Overeenkomst",
    )
    # overeenkomst = ("OVE", "Overeenkomst")

    plattegrond = Referentiedata(
        code="PLA",
        naam="Plattegrond",
    )
    # plattegrond = ("PLA", "Plattegrond")

    plan = Referentiedata(
        code="PLN",
        naam="Plan",
    )
    # plan = ("PLN", "Plan")

    rapport = Referentiedata(
        code="RAP",
        naam="Rapport",
    )
    # rapport = ("RAP", "Rapport")

    verslag = Referentiedata(
        code="VER",
        naam="Verslag",
    )
    # verslag = ("VER", "Verslag")

    video = Referentiedata(
        code="VID",
        naam="Video",
    )
    # video = ("VID", "Video")
