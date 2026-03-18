from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BestemmingReferentiedata(Referentiedata):
    pass


class Bestemming(Referentiedatasoort):
    bouwkundig_splitsen = BestemmingReferentiedata(
        code="BOU",
        naam="Bouwkundig splitsen",
    )
    """
    Eenheid is bestemd om bouwkundig gesplitst te worden in meerdere zelfstandige
    eenheden bij mutatie.
    """

    huur = BestemmingReferentiedata(
        code="HUU",
        naam="Huur",
    )
    """
    Eenheid is bestemd voor verhuur bij mutatie.
    """

    kadastraal_en_of_juridisch_splitsen = BestemmingReferentiedata(
        code="KAD",
        naam="Kadastraal/juridisch splitsen",
    )
    """
    Eenheid is bestemd om kadastraal en juridisch gesplitst te worden in meerdere
    eenheden bij mutatie.
    """

    kamergewijze_verhuur = BestemmingReferentiedata(
        code="KAM",
        naam="Kamergewijze verhuur",
    )
    """
    Eenheid is bestemd voor kamergewijze verhuur bij mutatie.
    """

    koop = BestemmingReferentiedata(
        code="KOO",
        naam="Koop",
    )
    """
    Eenheid is bestemd voor verkoop bij mutatie.
    """

    sloop = BestemmingReferentiedata(
        code="SLO",
        naam="Sloop",
    )
    """
    Eenheid is bestemd voor sloop bij mutatie.
    """

    splitsen = BestemmingReferentiedata(
        code="SPL",
        naam="Splitsen",
    )
    """
    Eenheid is bestemd voor splitsing bij mutatie, waarbij de wijze van splitsen (zacht,
    bouwkundig en/of kadastraal/juridisch) nog niet is bepaald.
    """

    samenvoegen = BestemmingReferentiedata(
        code="SAM",
        naam="Samenvoegen",
    )
    """
    Eenheid is bestemd samengevoegd te worden met een andere eenheid bij mutatie.
    """

    zachte_splitsing = BestemmingReferentiedata(
        code="ZAC",
        naam="Zachte splitsing",
    )
    """
    Eenheid is bestemd voor zachte splitsing (meerdere huishoudens binnen één juridische
    eenheid) bij mutatie.
    """
