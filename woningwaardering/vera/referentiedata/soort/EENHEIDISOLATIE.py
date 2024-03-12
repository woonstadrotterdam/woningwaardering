
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDISOLATIE:

    dakisolatie = Referentiedata(
        code="DAK",
        naam="Dakisolatie",
    )
    # dakisolatie = ("DAK", "Dakisolatie")

    dubbel_glas = Referentiedata(
        code="DGL",
        naam="Dubbel glas",
    )
    # dubbel_glas = ("DGL", "Dubbel glas")

    eco_bouw = Referentiedata(
        code="ECO",
        naam="Eco-bouw",
    )
    # eco_bouw = ("ECO", "Eco-bouw")
    """
    Ecologische, duurzame bouw
    """

    gedeeltelijk_dubbel_glas = Referentiedata(
        code="GDG",
        naam="Gedeeltelijk dubbel glas",
    )
    # gedeeltelijk_dubbel_glas = ("GDG", "Gedeeltelijk dubbel glas")

    muurisolatie = Referentiedata(
        code="MUU",
        naam="Muurisolatie",
    )
    # muurisolatie = ("MUU", "Muurisolatie")

    vloerisolatie = Referentiedata(
        code="VLO",
        naam="Vloerisolatie",
    )
    # vloerisolatie = ("VLO", "Vloerisolatie")

    volledig_geisoleerd = Referentiedata(
        code="VOL",
        naam="Volledig geïsoleerd",
    )
    # volledig_geisoleerd = ("VOL", "Volledig geïsoleerd")
