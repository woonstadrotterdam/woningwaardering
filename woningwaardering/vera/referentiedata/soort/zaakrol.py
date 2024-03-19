from vera.referentiedata.models import Referentiedata


class Zaakrol:
    adviseur = Referentiedata(
        code="ADV",
        naam="Adviseur",
    )

    behandelaar = Referentiedata(
        code="BEH",
        naam="Behandelaar",
    )
    """
    De medewerker die de zaak in behandeling heeft
    """

    beklaagde = Referentiedata(
        code="BEK",
        naam="Beklaagde",
    )
    """
    De betrokkene binnen de zaak waarover geklaagd wordt bij een (sociale) klacht
    """

    belanghebbende = Referentiedata(
        code="BEL",
        naam="Belanghebbende",
    )

    beslisser = Referentiedata(
        code="BES",
        naam="Beslisser",
    )

    initiator = Referentiedata(
        code="INI",
        naam="Initiator",
    )

    klantcontacter = Referentiedata(
        code="KLA",
        naam="Klantcontacter",
    )

    klager = Referentiedata(
        code="KLG",
        naam="Klager",
    )
    """
    De betrokkene binnen de zaak die een klacht heeft ingediend
    """

    melder = Referentiedata(
        code="MEL",
        naam="Melder",
    )
    """
    De melder van de zaak
    """

    overige_betrokkene = Referentiedata(
        code="OVE",
        naam="Overige betrokkene",
    )
    """
    Overige betrokkene binnen de zaak zoals instanties als bijvoorbeeld politie,
    gemeente, sociale dienst, etc.
    """

    zaakcoordinator = Referentiedata(
        code="ZAA",
        naam="Zaakcoördinator",
    )
