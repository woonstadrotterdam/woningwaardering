from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PersonelefunctiesoortReferentiedata(Referentiedata):
    pass


class Personelefunctiesoort(Referentiedatasoort):
    leidinggevende_functie = PersonelefunctiesoortReferentiedata(
        code="LEI",
        naam="Leidinggevende functie",
    )
