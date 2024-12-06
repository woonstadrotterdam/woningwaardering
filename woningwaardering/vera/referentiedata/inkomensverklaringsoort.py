from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Inkomensverklaringsoort(Referentiedatasoort):
    ib60 = Referentiedata(
        code="IB6",
        naam="IB60",
    )

    inkomensverklaring_belastingdienst = Referentiedata(
        code="IBD",
        naam="Inkomensverklaring belastingdienst",
    )

    ibri = Referentiedata(
        code="IBR",
        naam="IBRI",
    )

    jaaropgave = Referentiedata(
        code="JAA",
        naam="Jaaropgave",
    )

    loonstrook = Referentiedata(
        code="LOO",
        naam="Loonstrook",
    )

    uitkeringsspecificatie = Referentiedata(
        code="UIT",
        naam="Uitkeringsspecificatie",
    )
