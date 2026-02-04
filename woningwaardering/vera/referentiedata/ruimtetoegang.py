from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RuimtetoegangReferentiedata(Referentiedata):
    pass


class Ruimtetoegang(Referentiedatasoort):
    afsluitbaar = RuimtetoegangReferentiedata(
        code="ADS",
        naam="Afsluitbaar",
    )
    """
    De ruimte is fysiek afsluitbaar, bijvoorbeeld met een sleutel, pas of tag. Toegang
    moet actief worden verleend of geregeld.
    """

    collectieve_ruimte = RuimtetoegangReferentiedata(
        code="COR",
        naam="Collectieve ruimte",
    )
    """
    Een ruimte die gedeeld wordt door meerdere verblijfsobjecten binnen een complex,
    maar zelf geen zelfstandig verhuurd object is. De ruimte is doorgaans bereikbaar
    zonder dat bewoners aanwezig hoeven te zijn (bijv. via een complexloper of
    algemene toegang). Voorbeelden: fietsenstalling, containerruimte, technische
    ruimte.
    """

    gedeelde_ruimte = RuimtetoegangReferentiedata(
        code="GER",
        naam="Gedeelde ruimte",
    )
    """
    Een ruimte die gedeeld wordt door meerdere huurders binnen één verblijfsobject.
    Toegang verloopt via het privédeel van het verblijfsobject. Bewoners moeten
    aanwezig zijn of toegang verlenen.
    """

    gemeenschappelijke_ruimte = RuimtetoegangReferentiedata(
        code="GEM",
        naam="Gemeenschappelijke ruimte",
    )
    """
    Een ruimte waarvan meerdere verblijfsobjecten gezamenlijk exclusief gebruiksrecht
    hebben. Vaak bereikbaar vanuit een gedeeld deel van het gebouw, niet openbaar,
    maar zonder dat individuele toestemming per bewoner vereist is. Bijvoorbeeld een
    gezamenlijke ontmoetingsruimte of binnentuin voor bewoners van hetzelfde
    complex.
    """

    publiektoegankelijk = RuimtetoegangReferentiedata(
        code="PUT",
        naam="Publiektoegankelijk",
    )
    """
    De ruimte is vrij toegankelijk voor iedereen, ook zonder sleutel of toestemming.
    Bijvoorbeeld een open galerij of publieke tuin.
    """

    vluchtroute = RuimtetoegangReferentiedata(
        code="VLU",
        naam="Vluchtroute",
    )
    """
    De ruimte of doorgang maakt deel uit van een nood- of vluchtroute en moet te allen
    tijde toegankelijk zijn conform veiligheidsvoorschriften.
    """
