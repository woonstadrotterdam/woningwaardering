from vera.referentiedata.models import Referentiedata


class Eenheidinterieur:
    gemeubileerd = Referentiedata(
        code="GEM",
        naam="Gemeubileerd",
    )

    gestoffeerd = Referentiedata(
        code="GES",
        naam="Gestoffeerd",
    )

    houten_vloer = Referentiedata(
        code="HOU",
        naam="Houten vloer",
    )

    laminaat = Referentiedata(
        code="LAM",
        naam="Laminaat",
    )

    plavuizen = Referentiedata(
        code="PLA",
        naam="Plavuizen",
    )
    """
    Plavuizen of tegels
    """

    vloerbedekking = Referentiedata(
        code="VLB",
        naam="Vloerbedekking",
    )

    zelf_inrichten = Referentiedata(
        code="ZEL",
        naam="Zelf inrichten",
    )
