from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class LeningdetailsoortReferentiedata(Referentiedata):
    pass


class Leningdetailsoort(Referentiedatasoort):
    collegiaal = LeningdetailsoortReferentiedata(
        code="COL",
        naam="Collegiaal",
    )

    converteerbaar = LeningdetailsoortReferentiedata(
        code="CON",
        naam="Converteerbaar",
    )

    extendible = LeningdetailsoortReferentiedata(
        code="EXT",
        naam="Extendible",
    )
    """
    De financier (geldverstrekker) kan de lening verlengen.
    """

    hypothecaire_lening = LeningdetailsoortReferentiedata(
        code="HYP",
        naam="Hypothecaire lening",
    )

    intern = LeningdetailsoortReferentiedata(
        code="INT",
        naam="Intern",
    )
    """
    De lening betreft een interne lening. Bijvoorbeeld tussen een toegelaten instelling
    en een dochtermaatschappij.
    """

    obligatielening = LeningdetailsoortReferentiedata(
        code="OBL",
        naam="Obligatielening",
    )
