
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class LENINGDETAILSOORT:

    collegiaal = Referentiedata(
        code="COL",
        naam="Collegiaal",
    )
    # collegiaal = ("COL", "Collegiaal")

    converteerbaar = Referentiedata(
        code="CON",
        naam="Converteerbaar",
    )
    # converteerbaar = ("CON", "Converteerbaar")

    extendible = Referentiedata(
        code="EXT",
        naam="Extendible",
    )
    # extendible = ("EXT", "Extendible")
    """
    De financier (geldverstrekker) kan de lening verlengen.
    """

    hypothecaire_lening = Referentiedata(
        code="HYP",
        naam="Hypothecaire lening",
    )
    # hypothecaire_lening = ("HYP", "Hypothecaire lening")

    intern = Referentiedata(
        code="INT",
        naam="Intern",
    )
    # intern = ("INT", "Intern")
    """
    De lening betreft een interne lening. Bijvoorbeeld tussen een toegelaten instelling
    en een dochtermaatschappij.
    """

    obligatielening = Referentiedata(
        code="OBL",
        naam="Obligatielening",
    )
    # obligatielening = ("OBL", "Obligatielening")
