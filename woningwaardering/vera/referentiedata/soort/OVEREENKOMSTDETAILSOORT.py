
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OVEREENKOMSTDETAILSOORT:

    bepaalde_tijd = Referentiedata(
        code="BEP",
        naam="Bepaalde tijd",
    )
    # bepaalde_tijd = ("BEP", "Bepaalde tijd")
    """
    Arbeidsovereenkomst voor bepaalde tijd.
    """

    bedrijfsonroerendgoed = Referentiedata(
        code="BOG",
        naam="Bedrijfsonroerendgoed",
    )
    # bedrijfsonroerendgoed = ("BOG", "Bedrijfsonroerendgoed")
    """
    Verhuur van vastgoed voor zakelijke doeleinden.
    """

    campuscontract = Referentiedata(
        code="CAM",
        naam="Campuscontract",
    )
    # campuscontract = ("CAM", "Campuscontract")
    """
    Een campuscontract is een huurovereenkomst die direct is gekoppeld aan een
    inschrijving bij een onderwijsinstelling. Bij beindiging inschrijving eindigt ook de
    overeenkomst.
    """

    flexcontract = Referentiedata(
        code="FLE",
        naam="Flexcontract",
    )
    # flexcontract = ("FLE", "Flexcontract")
    """
    Huurovereenkomst voor een flexwoning: de einddatum van de omgevingsvergunning die
    voor de woning is afgegeven is een opzeggrond voor de huurovereenkomst (artikel
    7:271 lid 4 BW).
    """

    jongerencontract = Referentiedata(
        code="JON",
        naam="Jongerencontract",
    )
    # jongerencontract = ("JON", "Jongerencontract")
    """
    Jongeren tussen 18 en 28 jaar kunnen een huurcontract voor vijf jaar krijgen voor
    een geschikte woning voor jongeren.
    """

    koopgarant = Referentiedata(
        code="KGA",
        naam="Koopgarant",
    )
    # koopgarant = ("KGA", "Koopgarant")
    """
    Verkoop van een woning tegen lagere prijs dan de marktwaarde en de garantie dat de
    corporatie of ontwikkelaar de woning binnen 3 maanden zal terugkopen indien gewenst.
    """

    mge_constructie = Referentiedata(
        code="MGE",
        naam="MGE constructie",
    )
    # mge_constructie = ("MGE", "MGE constructie")
    """
    Verkoop met Maatschappelijk Gebonden Eigendom.
    """

    nieuwsbrief = Referentiedata(
        code="NIE",
        naam="Nieuwsbrief",
    )
    # nieuwsbrief = ("NIE", "Nieuwsbrief")
    """
    Nieuwsbrief voor marketing doeleinden.
    """

    nul_uren_contract = Referentiedata(
        code="NUL",
        naam="Nul-uren contract",
    )
    # nul_uren_contract = ("NUL", "Nul-uren contract")
    """
    Nul-uren arbeidsovereenkomst
    """

    onbepaalde_tijd = Referentiedata(
        code="OBE",
        naam="Onbepaalde tijd",
    )
    # onbepaalde_tijd = ("OBE", "Onbepaalde tijd")
    """
    Arbeidsovereenkomst voor onbepaalde tijd
    """

    onbepaalde_tijd_contract = Referentiedata(
        code="ONB",
        naam="Onbepaalde tijd contract",
    )
    # onbepaalde_tijd_contract = ("ONB", "Onbepaalde tijd contract")
    """
    Regulier huurcontract zonder einddatum.
    """

    persoonlijke_woonkrant = Referentiedata(
        code="PER",
        naam="Persoonlijke woonkrant",
    )
    # persoonlijke_woonkrant = ("PER", "Persoonlijke woonkrant")
    """
    Nieuwsbrief met gepersonificeerd aanbod. (Digizine)
    """

    nieuwbouwinformatie = Referentiedata(
        code="PRO",
        naam="Nieuwbouwinformatie",
    )
    # nieuwbouwinformatie = ("PRO", "Nieuwbouwinformatie")
    """
    Abonnement of nieuwsbrief met informatie over nieuwbouw projecten en/of vastgoed
    ontwikkelingen.
    """

    shortstay = Referentiedata(
        code="SHS",
        naam="ShortStay",
    )
    # shortstay = ("SHS", "ShortStay")
    """
    Short stay is het tijdelijk wonen in een zelfstandige woning voor een periode van
    tenminste zeven nachten en maximaal zes maanden
    """

    tijdelijk_contract = Referentiedata(
        code="TIJ",
        naam="Tijdelijk contract",
    )
    # tijdelijk_contract = ("TIJ", "Tijdelijk contract")
    """
    Huurcontract voor bepaalde tijd.
    """

    te_woon_of_vrije_keuze = Referentiedata(
        code="TWO",
        naam="Te Woon / Vrije keuze",
    )
    # te_woon_of_vrije_keuze = ("TWO", "Te Woon / Vrije keuze")
    """
    De woning is zowel te huur als te koop.
    """

    is_onderdeel_uitpondproject = Referentiedata(
        code="UIT",
        naam="Is onderdeel uitpondproject",
    )
    # is_onderdeel_uitpondproject = ("UIT", "Is onderdeel uitpondproject")
    """
    Verkoop van voormalige huurwoning aan de voormalige huurder of een nieuwe eigenaar.
    """
