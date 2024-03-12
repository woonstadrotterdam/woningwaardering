
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class REDENOPZEGGING:

    woning_geaccepteerd = Referentiedata(
        code="ACC",
        naam="Woning geaccepteerd",
    )
    # woning_geaccepteerd = ("ACC", "Woning geaccepteerd")
    """
    De overeenkomst is opgezegd in verband met het accepteren van een (andere) woning.
    """

    op_verzoek_corporatie = Referentiedata(
        code="COR",
        naam="Op verzoek corporatie",
    )
    # op_verzoek_corporatie = ("COR", "Op verzoek corporatie")
    """
    De overeenkomst is beeindigd door de woningcorporatie of vastgoedeigenaar.
    """

    inschrijfkosten_niet_betaald = Referentiedata(
        code="INB",
        naam="Inschrijfkosten niet betaald",
    )
    # inschrijfkosten_niet_betaald = ("INB", "Inschrijfkosten niet betaald")
    """
    Inschrijfkosten niet betaald
    """

    opzegging_woonconsument = Referentiedata(
        code="OPZ",
        naam="Opzegging woonconsument",
    )
    # opzegging_woonconsument = ("OPZ", "Opzegging woonconsument")
    """
    De overeenkomst is opgezegd, geannuleerd of beeindigd op verzoek van de
    woonconsument.
    """

    overleden = Referentiedata(
        code="OVE",
        naam="Overleden",
    )
    # overleden = ("OVE", "Overleden")
    """
    De contractant is overleden.
    """

    samengevoegd = Referentiedata(
        code="SAM",
        naam="Samengevoegd",
    )
    # samengevoegd = ("SAM", "Samengevoegd")
    """
    De overeenkomst is samengevoegd of ontdubbeld in verband met overlap met een andere
    overeenkomst voor dezelfde contractant.
    """

    niet_verlengd = Referentiedata(
        code="VER",
        naam="Niet verlengd",
    )
    # niet_verlengd = ("VER", "Niet verlengd")
    """
    De einddatum van de overeenkomst (met een optie op verlenging) is bereikt en er is
    geen bevestiging van een verlenging ontvangen.
    """
