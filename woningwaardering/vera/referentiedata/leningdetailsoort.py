from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Leningdetailsoort(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
