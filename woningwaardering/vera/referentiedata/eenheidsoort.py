from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidsoortReferentiedata(Referentiedata):
    pass


class Eenheidsoort(Referentiedatasoort):
    bedrijfsruimte = EenheidsoortReferentiedata(
        code="BED",
        naam="Bedrijfsruimte",
    )
    """
    Bedrijfsruimte en winkels
    """

    intramuraal_zorgvastgoed = EenheidsoortReferentiedata(
        code="INT",
        naam="Intramuraal zorgvastgoed",
    )
    """
    Bij intramuraal zorgvastgoed wordt de bewoners van het gebouw een integraal pakket
    van zorg met verblijf geboden (op grond van Wet Langdurige Zorg (WLZ) of
    Zorgverzekeringswet (ZVW) in een beschermde omgeving. De cliënten hebben géén
    huurcontract en er is dus geen sprake van toewijzing van woonruimte. Het kan
    bijvoorbeeld gaan om een verpleeg- of verzorgingshuis, instelling voor
    gehandicapten of instelling voor cliënten met langdurige psychische problemen.
    """

    maatschappelijk_vastgoed = EenheidsoortReferentiedata(
        code="MOG",
        naam="Maatschappelijk vastgoed",
    )
    """
    Gebouwen met een maatschappelijke gebruiksbestemming zoals bedoeld in artikel 49 van
    de Woningwet. Ook wel Maatschappelijk Onroerend goed (MOG).  Voorbeelden zijn
    buurtcentra, scholen en bibliotheken.
    """

    overig = EenheidsoortReferentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Restcategorie voor ligplaatsen, bergingen, bouwkavels, plantsoenen etc.
    """

    parkeergelegenheid = EenheidsoortReferentiedata(
        code="PAR",
        naam="Parkeergelegenheid",
    )
    """
    Parkeergelegenheden, Garage, parkeerplaatsen individueel of collectief
    """

    recreatiebestemming = EenheidsoortReferentiedata(
        code="REC",
        naam="Recreatiebestemming",
    )
    """
    Vastgoed voor recreatief gebruik (lokale regelgeving) zoals Recreatiewoningen
    """

    woonruimte = EenheidsoortReferentiedata(
        code="WOO",
        naam="Woonruimte",
    )
    """
    Synoniemen zijn onder andere: wooneenheden,  woongelegenheden (Handboek MVS)
    """
