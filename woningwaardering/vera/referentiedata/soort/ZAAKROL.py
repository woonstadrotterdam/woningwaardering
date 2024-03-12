
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ZAAKROL:

    adviseur = Referentiedata(
        code="ADV",
        naam="Adviseur",
    )
    # adviseur = ("ADV", "Adviseur")

    behandelaar = Referentiedata(
        code="BEH",
        naam="Behandelaar",
    )
    # behandelaar = ("BEH", "Behandelaar")
    """
    De medewerker die de zaak in behandeling heeft
    """

    beklaagde = Referentiedata(
        code="BEK",
        naam="Beklaagde",
    )
    # beklaagde = ("BEK", "Beklaagde")
    """
    De betrokkene binnen de zaak waarover geklaagd wordt bij een (sociale) klacht
    """

    belanghebbende = Referentiedata(
        code="BEL",
        naam="Belanghebbende",
    )
    # belanghebbende = ("BEL", "Belanghebbende")

    beslisser = Referentiedata(
        code="BES",
        naam="Beslisser",
    )
    # beslisser = ("BES", "Beslisser")

    initiator = Referentiedata(
        code="INI",
        naam="Initiator",
    )
    # initiator = ("INI", "Initiator")

    klantcontacter = Referentiedata(
        code="KLA",
        naam="Klantcontacter",
    )
    # klantcontacter = ("KLA", "Klantcontacter")

    klager = Referentiedata(
        code="KLG",
        naam="Klager",
    )
    # klager = ("KLG", "Klager")
    """
    De betrokkene binnen de zaak die een klacht heeft ingediend
    """

    melder = Referentiedata(
        code="MEL",
        naam="Melder",
    )
    # melder = ("MEL", "Melder")
    """
    De melder van de zaak
    """

    overige_betrokkene = Referentiedata(
        code="OVE",
        naam="Overige betrokkene",
    )
    # overige_betrokkene = ("OVE", "Overige betrokkene")
    """
    Overige betrokkene binnen de zaak zoals instanties als bijvoorbeeld politie,
    gemeente, sociale dienst, etc.
    """

    zaakcoordinator = Referentiedata(
        code="ZAA",
        naam="Zaakcoördinator",
    )
    # zaakcoordinator = ("ZAA", "Zaakcoördinator")
