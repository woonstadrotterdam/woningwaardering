from vera.bvg.generated import Referentiedata


class Contactgegevendetailsoort:
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
