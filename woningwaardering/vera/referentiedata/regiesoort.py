from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RegiesoortReferentiedata(Referentiedata):
    pass


class Regiesoort(Referentiedatasoort):
    bouwteam = RegiesoortReferentiedata(
        code="BOU",
        naam="Bouwteam",
    )
    """
    De aannemende partij wordt al tijdens de ontwerpfase bij het project betrokken. Deze
    aanpak zorgt ervoor dat uitvoerende expertise reeds in een vroeg stadium van het
    bouwproject beschikbaar is: de aannemer heeft meer verantwoordelijkheid en
    draagt actief bij aan het verfijnen van het ontwerp (bron:
    https://www.igg.nl/diensten/bouworganisatievormen/).Wordt ook wel een
    twee-fasen-contract genoemd, omdat er sprake is van een bouwteamfase en daarna
    een realisatiefase.
    """

    traditioneel = RegiesoortReferentiedata(
        code="TRA",
        naam="Traditioneel",
    )
    """
    Bij traditionele bouworganisatievormen zijn ontwerp en uitvoering gescheiden. De
    opdrachtgever heeft zowel met de ontwerper als de met de aannemer een aparte
    contractuele relatie en het proces is sequentieel ingedeeld, waardoor deze
    organisatievorm doorgaans relatief eenvoudig is (bron:
    https://www.igg.nl/diensten/bouworganisatievormen/)
    """

    turnkey = RegiesoortReferentiedata(
        code="TUR",
        naam="Turnkey",
    )
    """
    Bij Turn-Key bouwprojecten is de opdrachtgever meestal alleen betrokken bij het
    opstellen van het Programma van Eisen. Het PvE wordt vervolgens overgedragen aan
    één opdrachtnemer die de verantwoordelijkheid krijgt voor het gehele resultaat
    en zorgt dat alles conform de wensen van de opdrachtgever wordt opgeleverd
    (bron: https://www.igg.nl/diensten/bouworganisatievormen/).
    """
