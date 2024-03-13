from woningwaardering.vera.bvg.models import Referentiedata


class RENTESOORT:
    variabel = Referentiedata(
        code="VAR",
        naam="Variabel",
    )

    vast = Referentiedata(
        code="VST",
        naam="Vast",
    )
