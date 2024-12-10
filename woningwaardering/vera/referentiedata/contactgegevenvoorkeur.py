from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ContactgegevenvoorkeurReferentiedata(Referentiedata):
    pass


class Contactgegevenvoorkeur(Referentiedatasoort):
    eerste = ContactgegevenvoorkeurReferentiedata(
        code="EER",
        naam="Eerste",
    )

    tweede = ContactgegevenvoorkeurReferentiedata(
        code="TWE",
        naam="Tweede",
    )
