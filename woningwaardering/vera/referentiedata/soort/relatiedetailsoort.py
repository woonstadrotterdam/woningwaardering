from vera.referentiedata.models import Referentiedata


class Relatiedetailsoort:
    huishouden = Referentiedata(
        code="HUI",
        naam="Huishouden",
    )
    """
    Een huishouden bestaat uit één of meer personen die op hetzelfde adres wonen en een
    economisch-consumptieve eenheid vormen. (CORA)
    """
