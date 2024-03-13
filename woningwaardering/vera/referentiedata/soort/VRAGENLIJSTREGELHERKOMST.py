from woningwaardering.vera.bvg.models import Referentiedata


class VRAGENLIJSTREGELHERKOMST:
    aedes_benchmark = Referentiedata(
        code="AED",
        naam="Aedes-benchmark",
    )
    """
    De herkomst van de vraag is van de Aedes benchmark.
    """

    kwh_keurmerk = Referentiedata(
        code="KWH",
        naam="KWH Keurmerk",
    )
    """
    De herkomst van de vraag is van KWH in het kader van het eigen keurmerk.
    """

    eigen_vraag = Referentiedata(
        code="EIG",
        naam="Eigen vraag",
    )
    """
    De kwaliteitsmetingsvraag is door de eigen organisatie opgesteld
    """
