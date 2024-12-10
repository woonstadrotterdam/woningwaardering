from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ZaakrolReferentiedata(Referentiedata):
    pass


class Zaakrol(Referentiedatasoort):
    adviseur = ZaakrolReferentiedata(
        code="ADV",
        naam="Adviseur",
    )

    behandelaar = ZaakrolReferentiedata(
        code="BEH",
        naam="Behandelaar",
    )
    """
    De medewerker die de zaak in behandeling heeft
    """

    beklaagde = ZaakrolReferentiedata(
        code="BEK",
        naam="Beklaagde",
    )
    """
    De betrokkene binnen de zaak waarover geklaagd wordt bij een (sociale) klacht
    """

    belanghebbende = ZaakrolReferentiedata(
        code="BEL",
        naam="Belanghebbende",
    )

    beslisser = ZaakrolReferentiedata(
        code="BES",
        naam="Beslisser",
    )

    initiator = ZaakrolReferentiedata(
        code="INI",
        naam="Initiator",
    )

    klantcontacter = ZaakrolReferentiedata(
        code="KLA",
        naam="Klantcontacter",
    )

    klager = ZaakrolReferentiedata(
        code="KLG",
        naam="Klager",
    )
    """
    De betrokkene binnen de zaak die een klacht heeft ingediend
    """

    melder = ZaakrolReferentiedata(
        code="MEL",
        naam="Melder",
    )
    """
    De melder van de zaak
    """

    overige_betrokkene = ZaakrolReferentiedata(
        code="OVE",
        naam="Overige betrokkene",
    )
    """
    Overige betrokkene binnen de zaak zoals instanties als bijvoorbeeld politie,
    gemeente, sociale dienst, etc.
    """

    zaakcoordinator = ZaakrolReferentiedata(
        code="ZAA",
        naam="Zaakcoördinator",
    )
