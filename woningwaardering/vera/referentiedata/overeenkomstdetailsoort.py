from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Overeenkomstdetailsoort(Enum):
    bepaalde_tijd = Referentiedata(
        code="BEP",
        naam="Bepaalde tijd",
        parent=Referentiedata(
            code="ARB",
            naam="Arbeid",
        ),
    )
    """
    Arbeidsovereenkomst voor bepaalde tijd.
    """

    bedrijfsonroerendgoed = Referentiedata(
        code="BOG",
        naam="Bedrijfsonroerendgoed",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
    )
    """
    Verhuur van vastgoed voor zakelijke doeleinden.
    """

    campuscontract = Referentiedata(
        code="CAM",
        naam="Campuscontract",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
    )
    """
    Een campuscontract is een huurovereenkomst die direct is gekoppeld aan een
    inschrijving bij een onderwijsinstelling. Bij beeindiging inschrijving eindigt
    ook de overeenkomst.
    """

    flexcontract = Referentiedata(
        code="FLE",
        naam="Flexcontract",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
    )
    """
    Huurovereenkomst voor een flexwoning: de einddatum van de omgevingsvergunning die
    voor de woning is afgegeven is een opzeggrond voor de huurovereenkomst (artikel
    7:271 lid 4 BW).
    """

    jongerencontract = Referentiedata(
        code="JON",
        naam="Jongerencontract",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
    )
    """
    Jongeren tussen 18 en 28 jaar kunnen een huurcontract voor vijf jaar krijgen voor
    een geschikte woning voor jongeren.
    """

    koopgarant = Referentiedata(
        code="KGA",
        naam="Koopgarant",
        parent=Referentiedata(
            code="KOO",
            naam="Koopovereenkomst",
        ),
    )
    """
    Verkoop van een woning tegen lagere prijs dan de marktwaarde en de garantie dat de
    corporatie of ontwikkelaar de woning binnen 3 maanden zal terugkopen indien
    gewenst.
    """

    mge_constructie = Referentiedata(
        code="MGE",
        naam="MGE constructie",
        parent=Referentiedata(
            code="KOO",
            naam="Koopovereenkomst",
        ),
    )
    """
    Verkoop met Maatschappelijk Gebonden Eigendom.
    """

    nieuwsbrief = Referentiedata(
        code="NIE",
        naam="Nieuwsbrief",
        parent=Referentiedata(
            code="SER",
            naam="Serviceovereenkomst",
        ),
    )
    """
    Nieuwsbrief voor marketing doeleinden.
    """

    nul_uren_contract = Referentiedata(
        code="NUL",
        naam="Nul-uren contract",
        parent=Referentiedata(
            code="ARB",
            naam="Arbeid",
        ),
    )
    """
    Nul-uren arbeidsovereenkomst
    """

    onbepaalde_tijd = Referentiedata(
        code="OBE",
        naam="Onbepaalde tijd",
        parent=Referentiedata(
            code="ARB",
            naam="Arbeid",
        ),
    )
    """
    Arbeidsovereenkomst voor onbepaalde tijd
    """

    onbepaalde_tijd_contract = Referentiedata(
        code="ONB",
        naam="Onbepaalde tijd contract",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
    )
    """
    Regulier huurcontract zonder einddatum.
    """

    persoonlijke_woonkrant = Referentiedata(
        code="PER",
        naam="Persoonlijke woonkrant",
        parent=Referentiedata(
            code="SER",
            naam="Serviceovereenkomst",
        ),
    )
    """
    Nieuwsbrief met gepersonificeerd aanbod. (Digizine)
    """

    nieuwbouwinformatie = Referentiedata(
        code="PRO",
        naam="Nieuwbouwinformatie",
        parent=Referentiedata(
            code="SER",
            naam="Serviceovereenkomst",
        ),
    )
    """
    Abonnement of nieuwsbrief met informatie over nieuwbouw projecten en/of vastgoed
    ontwikkelingen.
    """

    shortstay = Referentiedata(
        code="SHS",
        naam="ShortStay",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
    )
    """
    Short stay is het tijdelijk wonen in een zelfstandige woning voor een periode van
    tenminste zeven nachten en maximaal zes maanden
    """

    tijdelijk_contract = Referentiedata(
        code="TIJ",
        naam="Tijdelijk contract",
        parent=Referentiedata(
            code="HUU",
            naam="Huurovereenkomst",
        ),
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
        parent=Referentiedata(
            code="KOO",
            naam="Koopovereenkomst",
        ),
    )
    """
    Verkoop van voormalige huurwoning aan de voormalige huurder of een nieuwe eigenaar.
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
