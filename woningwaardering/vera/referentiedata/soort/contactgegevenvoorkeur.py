from vera.referentiedata.models import Referentiedata


class Contactgegevenvoorkeur:
    eerste = Referentiedata(
        code="EER",
        naam="Eerste",
    )

    tweede = Referentiedata(
        code="TWE",
        naam="Tweede",
    )
