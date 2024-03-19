from vera.bvg.generated import Referentiedata


class Leningdetailsoort:
    collegiaal = Referentiedata(
        code="COL",
        naam="Collegiaal",
    )

    converteerbaar = Referentiedata(
        code="CON",
        naam="Converteerbaar",
    )

    extendible = Referentiedata(
        code="EXT",
        naam="Extendible",
    )
    """
    De financier (geldverstrekker) kan de lening verlengen.
    """

    hypothecaire_lening = Referentiedata(
        code="HYP",
        naam="Hypothecaire lening",
    )

    intern = Referentiedata(
        code="INT",
        naam="Intern",
    )
    """
    De lening betreft een interne lening. Bijvoorbeeld tussen een toegelaten instelling
    en een dochtermaatschappij.
    """

    obligatielening = Referentiedata(
        code="OBL",
        naam="Obligatielening",
    )
