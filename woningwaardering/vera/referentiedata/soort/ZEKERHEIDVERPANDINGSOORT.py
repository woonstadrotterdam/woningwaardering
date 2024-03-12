
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ZEKERHEIDVERPANDINGSOORT:

    hypotheek_en_pandrecht_huurpenningen = Referentiedata(
        code="HPH",
        naam="Hypotheek en pandrecht huurpenningen",
    )
    # hypotheek_en_pandrecht_huurpenningen = ("HPH", "Hypotheek en pandrecht huurpenningen")
    """
    Hypotheek en pandrecht huurpenningen
    """

    hypotheek_en_positieve_verkaring_pandrecht_huurpenningen = Referentiedata(
        code="HPO",
        naam="Hypotheek en positieve verkaring pandrecht huurpenningen",
    )
    # hypotheek_en_positieve_verkaring_pandrecht_huurpenningen = ("HPO", "Hypotheek en positieve verkaring pandrecht huurpenningen")
    """
    Hypotheek en positieve verkaring pandrecht huurpenningen
    """

    hypotheek = Referentiedata(
        code="HYP",
        naam="Hypotheek",
    )
    # hypotheek = ("HYP", "Hypotheek")
    """
    Hypotheek
    """

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    # overig = ("OVE", "Overig")
    """
    Overig, bijvoorbeeld vastgelegd in onderhandse akte
    """

    pandrecht_huurpenningen = Referentiedata(
        code="PHU",
        naam="Pandrecht huurpenningen",
    )
    # pandrecht_huurpenningen = ("PHU", "Pandrecht huurpenningen")
    """
    Pandrecht huurpenningen
    """

    positieve_verklaring = Referentiedata(
        code="POV",
        naam="Positieve verklaring",
    )
    # positieve_verklaring = ("POV", "Positieve verklaring")
    """
    Positieve verklaring hypotheek en/of positieve verkaring pandrecht huurpenningen
    """

    pandrecht_huurpenningen_en_positieve_verklaring_hypotheek = Referentiedata(
        code="PPO",
        naam="Pandrecht huurpenningen en positieve verklaring hypotheek",
    )
    # pandrecht_huurpenningen_en_positieve_verklaring_hypotheek = ("PPO", "Pandrecht huurpenningen en positieve verklaring hypotheek")
    """
    Pandrecht huurpenningen en positieve verklaring hypotheek
    """
