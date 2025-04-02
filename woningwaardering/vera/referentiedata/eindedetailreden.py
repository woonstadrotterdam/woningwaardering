from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eindereden import (
    Eindereden,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EindedetailredenReferentiedata(Referentiedata):
    pass


class Eindedetailreden(Referentiedatasoort):
    faillissement = EindedetailredenReferentiedata(
        code="FAI",
        naam="Faillissement",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd wegens faillissement.
    """

    herstructurering = EindedetailredenReferentiedata(
        code="HER",
        naam="Herstructurering",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd vanwege herstructurering van de woonomgeving. Dit kan
    bijvoorbeeld het gevolg zijn van sloop, renovatie of grootschalige
    gebiedsontwikkeling, waardoor de huidige woning niet langer beschikbaar is.
    """

    koop_eigen_woning = EindedetailredenReferentiedata(
        code="KOO",
        naam="Koop eigen woning",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens koop eigen woning.
    """

    leefbaarheid = EindedetailredenReferentiedata(
        code="LEE",
        naam="Leefbaarheid",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens redenen van leefbaarheid. Bijvoorbeeld
    geluidsoverlast, onveiligheid, slechte voorzieningen of negatieve sociale
    dynamiek.
    """

    noorderzon = EindedetailredenReferentiedata(
        code="NOO",
        naam="Noorderzon",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd omdat de huurder(s) met de noorderzon is (zijn)
    vertrokken.
    """

    ontruiming = EindedetailredenReferentiedata(
        code="ONT",
        naam="Ontruiming",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd omdat de woning is ontruimd.
    """

    overlijden = EindedetailredenReferentiedata(
        code="OVE",
        naam="Overlijden",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd wegens overlijden.
    """

    meer_passende_woning = EindedetailredenReferentiedata(
        code="PAS",
        naam="Meer passende woning",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd vanwege verhuizing naar een meer passende woning.
    Bijvoorbeeld bij gezinsuitbreiding, leeftijdsgerelateerde aanpassingen,
    locatievoorkeur, financiële redenen of woonstijl.
    """

    persoonlijke_omstandigheden = EindedetailredenReferentiedata(
        code="PER",
        naam="Persoonlijke omstandigheden",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens persoonlijke omstandigheden.
    """

    regulier = EindedetailredenReferentiedata(
        code="REG",
        naam="Regulier",
        parent=Eindereden.opzegging,
    )
    """
    Er is geen bijzondere aanleiding voor het beëindigen van een overeenkomst, of de
    reden is niet bekend.
    """

    terugkoop = EindedetailredenReferentiedata(
        code="TER",
        naam="Terugkoop",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens terugkoop.
    """

    tijdelijke_overeenkomst = EindedetailredenReferentiedata(
        code="TIJ",
        naam="Tijdelijke overeenkomst",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens het einde van de looptijd.
    """

    verkoop = EindedetailredenReferentiedata(
        code="VER",
        naam="Verkoop",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens verkoop.
    """

    voorzieningen = EindedetailredenReferentiedata(
        code="VOO",
        naam="Voorzieningen",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd omdat de beschikbare voorzieningen in of rondom de
    woning niet voldoen aan de wensen of behoeften van de huurder. Dit kan
    bijvoorbeeld gaan om onvoldoende parkeergelegenheid, gebrek aan groen en
    recreatiemogelijkheden, of beperkte buurtvoorzieningen zoals winkels en openbaar
    vervoer.
    """

    werk_buiten_regio = EindedetailredenReferentiedata(
        code="WER",
        naam="Werk buiten regio",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens werk buiten de regio.
    """

    wijziging_tenaamstelling = EindedetailredenReferentiedata(
        code="WIJ",
        naam="Wijziging tenaamstelling",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd omdat de tenaamstelling is gewijzigd (en is vervangen
    door een nieuwe overeenkomst).
    """

    woningruil = EindedetailredenReferentiedata(
        code="WON",
        naam="Woningruil",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens woningruil.
    """
