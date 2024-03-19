from vera.referentiedata.models import Referentiedata


class Eenheidisolatie:
    dakisolatie = Referentiedata(
        code="DAK",
        naam="Dakisolatie",
    )

    dubbel_glas = Referentiedata(
        code="DGL",
        naam="Dubbel glas",
    )

    eco_bouw = Referentiedata(
        code="ECO",
        naam="Eco-bouw",
    )
    """
    Ecologische, duurzame bouw
    """

    gedeeltelijk_dubbel_glas = Referentiedata(
        code="GDG",
        naam="Gedeeltelijk dubbel glas",
    )

    muurisolatie = Referentiedata(
        code="MUU",
        naam="Muurisolatie",
    )

    vloerisolatie = Referentiedata(
        code="VLO",
        naam="Vloerisolatie",
    )

    volledig_geisoleerd = Referentiedata(
        code="VOL",
        naam="Volledig geïsoleerd",
    )
