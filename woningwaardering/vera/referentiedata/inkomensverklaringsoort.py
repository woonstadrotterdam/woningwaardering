from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InkomensverklaringsoortReferentiedata(Referentiedata):
    pass


class Inkomensverklaringsoort(Referentiedatasoort):
    ib60 = InkomensverklaringsoortReferentiedata(
        code="IB6",
        naam="IB60",
    )

    inkomensverklaring_belastingdienst = InkomensverklaringsoortReferentiedata(
        code="IBD",
        naam="Inkomensverklaring belastingdienst",
    )

    ibri = InkomensverklaringsoortReferentiedata(
        code="IBR",
        naam="IBRI",
    )

    jaaropgave = InkomensverklaringsoortReferentiedata(
        code="JAA",
        naam="Jaaropgave",
    )

    loonstrook = InkomensverklaringsoortReferentiedata(
        code="LOO",
        naam="Loonstrook",
    )

    uitkeringsspecificatie = InkomensverklaringsoortReferentiedata(
        code="UIT",
        naam="Uitkeringsspecificatie",
    )
