
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PUNTENBEREKENINGSOORT:

    intrekken_gebeurtenis_of_sanctie = Referentiedata(
        code="INT",
        naam="Intrekken gebeurtenis of sanctie",
    )
    # intrekken_gebeurtenis_of_sanctie = ("INT", "Intrekken gebeurtenis of sanctie")

    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    # intrekken_toewijzing = ("ITO", "Intrekken toewijzing")
    """
    Intrekken toewijzing van de eenheid.
    """

    koppelen_inschrijving = Referentiedata(
        code="KOP",
        naam="Koppelen inschrijving",
    )
    # koppelen_inschrijving = ("KOP", "Koppelen inschrijving")

    maandelijkse_herberekening = Referentiedata(
        code="MAA",
        naam="Maandelijkse herberekening",
    )
    # maandelijkse_herberekening = ("MAA", "Maandelijkse herberekening")

    nieuwe_inschrijving = Referentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )
    # nieuwe_inschrijving = ("NIE", "Nieuwe inschrijving")
