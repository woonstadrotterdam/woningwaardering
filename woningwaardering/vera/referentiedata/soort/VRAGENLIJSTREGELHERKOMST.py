
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VRAGENLIJSTREGELHERKOMST:

    aedes_benchmark = Referentiedata(
        code="AED",
        naam="Aedes-benchmark",
    )
    # aedes_benchmark = ("AED", "Aedes-benchmark")
    """
    De herkomst van de vraag is van de Aedes benchmark.
    """

    kwh_keurmerk = Referentiedata(
        code="KWH",
        naam="KWH Keurmerk",
    )
    # kwh_keurmerk = ("KWH", "KWH Keurmerk")
    """
    De herkomst van de vraag is van KWH in het kader van het eigen keurmerk.
    """

    eigen_vraag = Referentiedata(
        code="EIG",
        naam="Eigen vraag",
    )
    # eigen_vraag = ("EIG", "Eigen vraag")
    """
    De kwaliteitsmetingsvraag is door de eigen organisatie opgesteld
    """
