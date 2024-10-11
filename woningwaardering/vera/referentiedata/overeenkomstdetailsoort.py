from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.overeenkomstsoort import Overeenkomstsoort


class Overeenkomstdetailsoort(Enum):
    bepaalde_tijd = Referentiedata(
        code="BEP",
        naam="Bepaalde tijd",
        parent=Overeenkomstsoort.arbeid.value,
    )
    """
    Arbeidsovereenkomst voor bepaalde tijd.
    """

    bedrijfsonroerendgoed = Referentiedata(
        code="BOG",
        naam="Bedrijfsonroerendgoed",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Verhuur van vastgoed voor zakelijke doeleinden.
    """

    campuscontract = Referentiedata(
        code="CAM",
        naam="Campuscontract",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Een campuscontract is een huurovereenkomst die direct is gekoppeld aan een
    inschrijving bij een onderwijsinstelling. Bij beeindiging inschrijving eindigt
    ook de overeenkomst.
    """

    flexcontract = Referentiedata(
        code="FLE",
        naam="Flexcontract",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Huurovereenkomst voor een flexwoning: de einddatum van de omgevingsvergunning die
    voor de woning is afgegeven is een opzeggrond voor de huurovereenkomst (artikel
    7:271 lid 4 BW).
    """

    jongerencontract = Referentiedata(
        code="JON",
        naam="Jongerencontract",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Jongeren tussen 18 en 28 jaar kunnen een huurcontract voor vijf jaar krijgen voor
    een geschikte woning voor jongeren.
    """

    koopgarant = Referentiedata(
        code="KGA",
        naam="Koopgarant",
        parent=Overeenkomstsoort.koopovereenkomst.value,
    )
    """
    Verkoop van een woning tegen lagere prijs dan de marktwaarde en de garantie dat de
    corporatie of ontwikkelaar de woning binnen 3 maanden zal terugkopen indien
    gewenst.
    """

    mge_constructie = Referentiedata(
        code="MGE",
        naam="MGE constructie",
        parent=Overeenkomstsoort.koopovereenkomst.value,
    )
    """
    Verkoop met Maatschappelijk Gebonden Eigendom.
    """

    nieuwsbrief = Referentiedata(
        code="NIE",
        naam="Nieuwsbrief",
        parent=Overeenkomstsoort.serviceovereenkomst.value,
    )
    """
    Nieuwsbrief voor marketing doeleinden.
    """

    nul_uren_contract = Referentiedata(
        code="NUL",
        naam="Nul-uren contract",
        parent=Overeenkomstsoort.arbeid.value,
    )
    """
    Nul-uren arbeidsovereenkomst
    """

    onbepaalde_tijd = Referentiedata(
        code="OBE",
        naam="Onbepaalde tijd",
        parent=Overeenkomstsoort.arbeid.value,
    )
    """
    Arbeidsovereenkomst voor onbepaalde tijd
    """

    onbepaalde_tijd_contract = Referentiedata(
        code="ONB",
        naam="Onbepaalde tijd contract",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Regulier huurcontract zonder einddatum.
    """

    persoonlijke_woonkrant = Referentiedata(
        code="PER",
        naam="Persoonlijke woonkrant",
        parent=Overeenkomstsoort.serviceovereenkomst.value,
    )
    """
    Nieuwsbrief met gepersonificeerd aanbod. (Digizine)
    """

    nieuwbouwinformatie = Referentiedata(
        code="PRO",
        naam="Nieuwbouwinformatie",
        parent=Overeenkomstsoort.serviceovereenkomst.value,
    )
    """
    Abonnement of nieuwsbrief met informatie over nieuwbouw projecten en/of vastgoed
    ontwikkelingen.
    """

    shortstay = Referentiedata(
        code="SHS",
        naam="ShortStay",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Short stay is het tijdelijk wonen in een zelfstandige woning voor een periode van
    tenminste zeven nachten en maximaal zes maanden
    """

    tijdelijk_contract = Referentiedata(
        code="TIJ",
        naam="Tijdelijk contract",
        parent=Overeenkomstsoort.huurovereenkomst.value,
    )
    """
    Huurcontract voor bepaalde tijd.
    """

    te_woon_en_of_vrije_keuze = Referentiedata(
        code="TWO",
        naam="Te Woon / Vrije keuze",
    )
    """
    De woning is zowel te huur als te koop.
    """

    is_onderdeel_uitpondproject = Referentiedata(
        code="UIT",
        naam="Is onderdeel uitpondproject",
        parent=Overeenkomstsoort.koopovereenkomst.value,
    )
    """
    Verkoop van voormalige huurwoning aan de voormalige huurder of een nieuwe eigenaar.
    """

    inhuurovereenkomst_plaatsvervangend = Referentiedata(
        code="INP",
        naam="Inhuurovereenkomst plaatsvervangend",
        parent=Overeenkomstsoort.arbeid.value,
    )
    """
    Een inhuurovereenkomst plaatsvervangend is een contract waarbij een werknemer
    tijdelijk wordt ingehuurd om de taken van een afwezige medewerker over te nemen.
    """

    inhuurovereenkomst_boven_formatie = Referentiedata(
        code="INB",
        naam="Inhuurovereenkomst boven formatie",
        parent=Overeenkomstsoort.arbeid.value,
    )
    """
    Een inhuurovereenkomst boven formatie is een contract waarbij een werknemer
    tijdelijk wordt ingehuurd voor extra capaciteit bovenop de bestaande
    personeelsformatie.
    """

    inhuurovereenkomst_structureel = Referentiedata(
        code="INS",
        naam="Inhuurovereenkomst structureel",
        parent=Overeenkomstsoort.arbeid.value,
    )
    """
    Een overeenkomst waarin de rechten en plichten van een externe kracht, zoals een
    zzp-er of freelancer, voor een langere periode worden vastgelegd om continuïteit
    en duidelijkheid te waarborgen.
    """

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
