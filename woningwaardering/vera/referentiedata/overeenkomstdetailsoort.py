from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.overeenkomstsoort import (
    Overeenkomstsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OvereenkomstdetailsoortReferentiedata(Referentiedata):
    pass


class Overeenkomstdetailsoort(Referentiedatasoort):
    bepaalde_tijd = OvereenkomstdetailsoortReferentiedata(
        code="BEP",
        naam="Bepaalde tijd",
        parent=Overeenkomstsoort.arbeid,
    )
    """
    Arbeidsovereenkomst voor bepaalde tijd.
    """

    bedrijfsonroerendgoed = OvereenkomstdetailsoortReferentiedata(
        code="BOG",
        naam="Bedrijfsonroerendgoed",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Verhuur van vastgoed voor zakelijke doeleinden.
    """

    campuscontract = OvereenkomstdetailsoortReferentiedata(
        code="CAM",
        naam="Campuscontract",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Een campuscontract is een huurovereenkomst die direct is gekoppeld aan een
    inschrijving bij een onderwijsinstelling. Bij beeindiging inschrijving eindigt
    ook de overeenkomst.
    """

    flexcontract = OvereenkomstdetailsoortReferentiedata(
        code="FLE",
        naam="Flexcontract",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Huurovereenkomst voor een flexwoning: de einddatum van de omgevingsvergunning die
    voor de woning is afgegeven is een opzeggrond voor de huurovereenkomst (artikel
    7:271 lid 4 BW).
    """

    jongerencontract = OvereenkomstdetailsoortReferentiedata(
        code="JON",
        naam="Jongerencontract",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Jongeren tussen 18 en 28 jaar kunnen een huurcontract voor vijf jaar krijgen voor
    een geschikte woning voor jongeren.
    """

    koopgarant = OvereenkomstdetailsoortReferentiedata(
        code="KGA",
        naam="Koopgarant",
        parent=Overeenkomstsoort.koopovereenkomst,
    )
    """
    Verkoop van een woning tegen lagere prijs dan de marktwaarde en de garantie dat de
    corporatie of ontwikkelaar de woning binnen 3 maanden zal terugkopen indien
    gewenst.
    """

    mge_constructie = OvereenkomstdetailsoortReferentiedata(
        code="MGE",
        naam="MGE constructie",
        parent=Overeenkomstsoort.koopovereenkomst,
    )
    """
    Verkoop met Maatschappelijk Gebonden Eigendom.
    """

    nieuwsbrief = OvereenkomstdetailsoortReferentiedata(
        code="NIE",
        naam="Nieuwsbrief",
        parent=Overeenkomstsoort.serviceovereenkomst,
    )
    """
    Nieuwsbrief voor marketing doeleinden.
    """

    nul_uren_contract = OvereenkomstdetailsoortReferentiedata(
        code="NUL",
        naam="Nul-uren contract",
        parent=Overeenkomstsoort.arbeid,
    )
    """
    Nul-uren arbeidsovereenkomst
    """

    onbepaalde_tijd = OvereenkomstdetailsoortReferentiedata(
        code="OBE",
        naam="Onbepaalde tijd",
        parent=Overeenkomstsoort.arbeid,
    )
    """
    Arbeidsovereenkomst voor onbepaalde tijd
    """

    onbepaalde_tijd_contract = OvereenkomstdetailsoortReferentiedata(
        code="ONB",
        naam="Onbepaalde tijd contract",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Regulier huurcontract zonder einddatum.
    """

    persoonlijke_woonkrant = OvereenkomstdetailsoortReferentiedata(
        code="PER",
        naam="Persoonlijke woonkrant",
        parent=Overeenkomstsoort.serviceovereenkomst,
    )
    """
    Nieuwsbrief met gepersonificeerd aanbod. (Digizine)
    """

    nieuwbouwinformatie = OvereenkomstdetailsoortReferentiedata(
        code="PRO",
        naam="Nieuwbouwinformatie",
        parent=Overeenkomstsoort.serviceovereenkomst,
    )
    """
    Abonnement of nieuwsbrief met informatie over nieuwbouw projecten en/of vastgoed
    ontwikkelingen.
    """

    shortstay = OvereenkomstdetailsoortReferentiedata(
        code="SHS",
        naam="ShortStay",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Short stay is het tijdelijk wonen in een zelfstandige woning voor een periode van
    tenminste zeven nachten en maximaal zes maanden
    """

    tijdelijk_contract = OvereenkomstdetailsoortReferentiedata(
        code="TIJ",
        naam="Tijdelijk contract",
        parent=Overeenkomstsoort.huurovereenkomst,
    )
    """
    Huurcontract voor bepaalde tijd.
    """

    te_woon_en_of_vrije_keuze = OvereenkomstdetailsoortReferentiedata(
        code="TWO",
        naam="Te Woon / Vrije keuze",
    )
    """
    De woning is zowel te huur als te koop.
    """

    is_onderdeel_uitpondproject = OvereenkomstdetailsoortReferentiedata(
        code="UIT",
        naam="Is onderdeel uitpondproject",
        parent=Overeenkomstsoort.koopovereenkomst,
    )
    """
    Verkoop van voormalige huurwoning aan de voormalige huurder of een nieuwe eigenaar.
    """

    inhuurovereenkomst_plaatsvervangend = OvereenkomstdetailsoortReferentiedata(
        code="INP",
        naam="Inhuurovereenkomst plaatsvervangend",
        parent=Overeenkomstsoort.arbeid,
    )
    """
    Een inhuurovereenkomst plaatsvervangend is een contract waarbij een werknemer
    tijdelijk wordt ingehuurd om de taken van een afwezige medewerker over te nemen.
    """

    inhuurovereenkomst_boven_formatie = OvereenkomstdetailsoortReferentiedata(
        code="INB",
        naam="Inhuurovereenkomst boven formatie",
        parent=Overeenkomstsoort.arbeid,
    )
    """
    Een inhuurovereenkomst boven formatie is een contract waarbij een werknemer
    tijdelijk wordt ingehuurd voor extra capaciteit bovenop de bestaande
    personeelsformatie.
    """

    inhuurovereenkomst_structureel = OvereenkomstdetailsoortReferentiedata(
        code="INS",
        naam="Inhuurovereenkomst structureel",
        parent=Overeenkomstsoort.arbeid,
    )
    """
    Een overeenkomst waarin de rechten en plichten van een externe kracht, zoals een
    zzp-er of freelancer, voor een langere periode worden vastgelegd om continuïteit
    en duidelijkheid te waarborgen.
    """
