from woningwaardering.vera.bvg.models import Referentiedata


class CONTACTGEGEVENDETAILSOORT:
    in_case_of_emergency = Referentiedata(
        code="ICE",
        naam="In case of emergency",
    )

    prive = Referentiedata(
        code="PRI",
        naam="Privé",
    )

    zakelijk = Referentiedata(
        code="ZAK",
        naam="Zakelijk",
    )
