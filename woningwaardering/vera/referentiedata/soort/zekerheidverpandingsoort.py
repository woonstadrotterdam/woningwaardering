from vera.referentiedata.models import Referentiedata


class Zekerheidverpandingsoort:
    hypotheek_en_pandrecht_huurpenningen = Referentiedata(
        code="HPH",
        naam="Hypotheek en pandrecht huurpenningen",
    )
    """
    Hypotheek en pandrecht huurpenningen
    """

    hypotheek_en_positieve_verkaring_pandrecht_huurpenningen = Referentiedata(
        code="HPO",
        naam="Hypotheek en positieve verkaring pandrecht huurpenningen",
    )
    """
    Hypotheek en positieve verkaring pandrecht huurpenningen
    """

    hypotheek = Referentiedata(
        code="HYP",
        naam="Hypotheek",
    )
    """
    Hypotheek
    """

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Overig, bijvoorbeeld vastgelegd in onderhandse akte
    """

    pandrecht_huurpenningen = Referentiedata(
        code="PHU",
        naam="Pandrecht huurpenningen",
    )
    """
    Pandrecht huurpenningen
    """

    positieve_verklaring = Referentiedata(
        code="POV",
        naam="Positieve verklaring",
    )
    """
    Positieve verklaring hypotheek en/of positieve verkaring pandrecht huurpenningen
    """

    pandrecht_huurpenningen_en_positieve_verklaring_hypotheek = Referentiedata(
        code="PPO",
        naam="Pandrecht huurpenningen en positieve verklaring hypotheek",
    )
    """
    Pandrecht huurpenningen en positieve verklaring hypotheek
    """
