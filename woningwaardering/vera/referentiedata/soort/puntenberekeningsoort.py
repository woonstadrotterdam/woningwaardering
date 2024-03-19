from vera.bvg.generated import Referentiedata


class Puntenberekeningsoort:
    intrekken_gebeurtenis_of_sanctie = Referentiedata(
        code="INT",
        naam="Intrekken gebeurtenis of sanctie",
    )

    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    koppelen_inschrijving = Referentiedata(
        code="KOP",
        naam="Koppelen inschrijving",
    )

    maandelijkse_herberekening = Referentiedata(
        code="MAA",
        naam="Maandelijkse herberekening",
    )

    nieuwe_inschrijving = Referentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )
