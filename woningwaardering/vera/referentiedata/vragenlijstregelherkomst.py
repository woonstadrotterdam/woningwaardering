from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VragenlijstregelherkomstReferentiedata(Referentiedata):
    pass


class Vragenlijstregelherkomst(Referentiedatasoort):
    aedes_benchmark = VragenlijstregelherkomstReferentiedata(
        code="AED",
        naam="Aedes-benchmark",
    )
    """
    De herkomst van de vraag is van de Aedes benchmark.
    """

    kwh_keurmerk = VragenlijstregelherkomstReferentiedata(
        code="KWH",
        naam="KWH Keurmerk",
    )
    """
    De herkomst van de vraag is van KWH in het kader van het eigen keurmerk.
    """

    eigen_vraag = VragenlijstregelherkomstReferentiedata(
        code="EIG",
        naam="Eigen vraag",
    )
    """
    De kwaliteitsmetingsvraag is door de eigen organisatie opgesteld
    """
