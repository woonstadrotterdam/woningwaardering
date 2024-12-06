from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Personelefunctiesoort(Referentiedatasoort):
    leidinggevende_functie = Referentiedata(
        code="LEI",
        naam="Leidinggevende functie",
    )
