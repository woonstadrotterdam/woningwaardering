from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ZekerheidverpandingsoortReferentiedata(Referentiedata):
    pass


class Zekerheidverpandingsoort(Referentiedatasoort):
    hypotheek_en_pandrecht_huurpenningen = ZekerheidverpandingsoortReferentiedata(
        code="HPH",
        naam="Hypotheek en pandrecht huurpenningen",
    )
    """
    Hypotheek en pandrecht huurpenningen
    """

    hypotheek_en_positieve_verkaring_pandrecht_huurpenningen = (
        ZekerheidverpandingsoortReferentiedata(
            code="HPO",
            naam="Hypotheek en positieve verkaring pandrecht huurpenningen",
        )
    )
    """
    Hypotheek en positieve verkaring pandrecht huurpenningen
    """

    hypotheek = ZekerheidverpandingsoortReferentiedata(
        code="HYP",
        naam="Hypotheek",
    )
    """
    Hypotheek
    """

    overig = ZekerheidverpandingsoortReferentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Overig, bijvoorbeeld vastgelegd in onderhandse akte
    """

    pandrecht_huurpenningen = ZekerheidverpandingsoortReferentiedata(
        code="PHU",
        naam="Pandrecht huurpenningen",
    )
    """
    Pandrecht huurpenningen
    """

    positieve_verklaring = ZekerheidverpandingsoortReferentiedata(
        code="POV",
        naam="Positieve verklaring",
    )
    """
    Positieve verklaring hypotheek en/of positieve verkaring pandrecht huurpenningen
    """

    pandrecht_huurpenningen_en_positieve_verklaring_hypotheek = (
        ZekerheidverpandingsoortReferentiedata(
            code="PPO",
            naam="Pandrecht huurpenningen en positieve verklaring hypotheek",
        )
    )
    """
    Pandrecht huurpenningen en positieve verklaring hypotheek
    """
