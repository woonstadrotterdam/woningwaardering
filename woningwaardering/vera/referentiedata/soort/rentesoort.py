from vera.referentiedata.models import Referentiedata


class Rentesoort:
    variabel = Referentiedata(
        code="VAR",
        naam="Variabel",
    )

    vast = Referentiedata(
        code="VST",
        naam="Vast",
    )
