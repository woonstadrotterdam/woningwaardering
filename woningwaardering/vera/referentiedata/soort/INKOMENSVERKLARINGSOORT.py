
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INKOMENSVERKLARINGSOORT:

    ib60 = Referentiedata(
        code="IB6",
        naam="IB60",
    )
    # ib60 = ("IB6", "IB60")

    inkomensverklaring_belastingdienst = Referentiedata(
        code="IBD",
        naam="Inkomensverklaring belastingdienst",
    )
    # inkomensverklaring_belastingdienst = ("IBD", "Inkomensverklaring belastingdienst")

    ibri = Referentiedata(
        code="IBR",
        naam="IBRI",
    )
    # ibri = ("IBR", "IBRI")

    jaaropgave = Referentiedata(
        code="JAA",
        naam="Jaaropgave",
    )
    # jaaropgave = ("JAA", "Jaaropgave")

    loonstrook = Referentiedata(
        code="LOO",
        naam="Loonstrook",
    )
    # loonstrook = ("LOO", "Loonstrook")

    uitkeringsspecificatie = Referentiedata(
        code="UIT",
        naam="Uitkeringsspecificatie",
    )
    # uitkeringsspecificatie = ("UIT", "Uitkeringsspecificatie")
