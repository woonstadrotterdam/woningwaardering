
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDINTERIEUR:

    gemeubileerd = Referentiedata(
        code="GEM",
        naam="Gemeubileerd",
    )
    # gemeubileerd = ("GEM", "Gemeubileerd")

    gestoffeerd = Referentiedata(
        code="GES",
        naam="Gestoffeerd",
    )
    # gestoffeerd = ("GES", "Gestoffeerd")

    houten_vloer = Referentiedata(
        code="HOU",
        naam="Houten vloer",
    )
    # houten_vloer = ("HOU", "Houten vloer")

    laminaat = Referentiedata(
        code="LAM",
        naam="Laminaat",
    )
    # laminaat = ("LAM", "Laminaat")

    plavuizen = Referentiedata(
        code="PLA",
        naam="Plavuizen",
    )
    # plavuizen = ("PLA", "Plavuizen")
    """
    Plavuizen of tegels
    """

    vloerbedekking = Referentiedata(
        code="VLB",
        naam="Vloerbedekking",
    )
    # vloerbedekking = ("VLB", "Vloerbedekking")

    zelf_inrichten = Referentiedata(
        code="ZEL",
        naam="Zelf inrichten",
    )
    # zelf_inrichten = ("ZEL", "Zelf inrichten")
