from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RedenopzeggingReferentiedata(Referentiedata):
    pass


class Redenopzegging(Referentiedatasoort):
    woning_geaccepteerd = RedenopzeggingReferentiedata(
        code="ACC",
        naam="Woning geaccepteerd",
    )
    """
    De overeenkomst is opgezegd in verband met het accepteren van een (andere) woning.
    """

    op_verzoek_corporatie = RedenopzeggingReferentiedata(
        code="COR",
        naam="Op verzoek corporatie",
    )
    """
    De overeenkomst is beeindigd door de woningcorporatie of vastgoedeigenaar.
    """

    inschrijfkosten_niet_betaald = RedenopzeggingReferentiedata(
        code="INB",
        naam="Inschrijfkosten niet betaald",
    )
    """
    Inschrijfkosten niet betaald
    """

    opzegging_woonconsument = RedenopzeggingReferentiedata(
        code="OPZ",
        naam="Opzegging woonconsument",
    )
    """
    De overeenkomst is opgezegd, geannuleerd of beeindigd op verzoek van de
    woonconsument.
    """

    overleden = RedenopzeggingReferentiedata(
        code="OVE",
        naam="Overleden",
    )
    """
    De contractant is overleden.
    """

    samengevoegd = RedenopzeggingReferentiedata(
        code="SAM",
        naam="Samengevoegd",
    )
    """
    De overeenkomst is samengevoegd of ontdubbeld in verband met overlap met een andere
    overeenkomst voor dezelfde contractant.
    """

    niet_verlengd = RedenopzeggingReferentiedata(
        code="VER",
        naam="Niet verlengd",
    )
    """
    De einddatum van de overeenkomst (met een optie op verlenging) is bereikt en er is
    geen bevestiging van een verlenging ontvangen.
    """
