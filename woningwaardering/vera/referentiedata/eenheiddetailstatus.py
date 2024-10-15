from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eenheidstatus import Eenheidstatus


class Eenheiddetailstatus(Enum):
    verhuurd_antikraak = Referentiedata(
        code="ANT",
        naam="Verhuurd antikraak",
        parent=Eenheidstatus.verhuurd.value,
    )
    """
    De eenheid wordt verhuurd onder de voorwaarden van anti-kraak
    """

    bouwplannen = Referentiedata(
        code="BOU",
        naam="Bouwplannen",
        parent=Eenheidstatus.in_ontwikkeling.value,
    )
    """
    Eenheid is in ontwikkeling, nog in de planfase
    """

    bruikleen = Referentiedata(
        code="BRU",
        naam="Bruikleen",
        parent=Eenheidstatus.verhuurd.value,
    )
    """
    De eenheid wordt verhuurd onder een bruikleen constructie
    """

    wacht_op_energie_prestatie_advies = Referentiedata(
        code="EPA",
        naam="Wacht op Energie Prestatie Advies",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    Frictieleegstand, ontstaan doordat er nog gewacht wordt op de afgifte van een EPA
    label
    """

    mutatie = Referentiedata(
        code="MUT",
        naam="Mutatie",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    Frictieleegstand wegens mutatieonderhoud. De eenheid is in exploitatie, maar niet
    verhuurd. Aansluitende verhuur is niet mogelijk omdat eerst nog onderhoud in de
    woning plaatsvindt.
    """

    wacht_op_nieuwe_huurder_niet_regulier = Referentiedata(
        code="NIB",
        naam="Wacht op nieuwe huurder - niet-regulier",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    Frictieleegstand, ontstaan doordat er nog geen nieuwe huurder is gevonden, waarbij
    geldt dat er sprake is van een niet-regulier toewijzingsproces of een
    niet-reguliere beoogd huurder. Het betreft de leegstand vanaf het moment waarop
    de woning klaar is voor verhuur (nadat eventueel mutatieonderhoud is afgerond)
    totdat de overeenkomst met een nieuwe, niet-reguliere, huurder ingaat.
    """

    nieuwbouw = Referentiedata(
        code="NIE",
        naam="Nieuwbouw",
        parent=Eenheidstatus.in_ontwikkeling.value,
    )
    """
    Eenheid is in ontwikkeling, realisatie-/bouwfase is gestart
    """

    wacht_op_nieuwe_huurder_regulier = Referentiedata(
        code="NIH",
        naam="Wacht op nieuwe huurder - regulier",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    Frictieleegstand, ontstaan doordat er nog geen nieuwe huurder is gevonden, zonder
    dat daar een speciale oorzaak voor is (het reguliere matching proces duurt
    langer dan gewenst). Het betreft de leegstand vanaf het moment waarop de woning
    klaar is voor verhuur (nadat eventueel mutatieonderhoud is afgerond) totdat de
    overeenkomst met een nieuwe huurder ingaat.
    """

    oplevering = Referentiedata(
        code="OPL",
        naam="Oplevering",
        parent=Eenheidstatus.in_ontwikkeling.value,
    )
    """
    Eenheid is in ontwikkeling, klaar voor oplevering
    """

    verhuurd_permanent = Referentiedata(
        code="PER",
        naam="Verhuurd permanent",
        parent=Eenheidstatus.verhuurd.value,
    )
    """
    Doorlopend contract of voor onbepaalde tijd.
    """

    projectleegstand = Referentiedata(
        code="PRO",
        naam="Projectleegstand",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    Leegstand doordat de eenheid deel uitmaakt van een onderhouds- of renovatieproject,
    waarbij de eenheid niet uit exploitatie wordt genomen
    """

    structurele_leegstand = Referentiedata(
        code="STR",
        naam="Structurele leegstand",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    (Verwachte) Langdurige frictieleegstand, doordat vraag en aanbod niet op elkaar
    aansluiten
    """

    verhuurd_tijdelijk = Referentiedata(
        code="TIJD",
        naam="Verhuurd tijdelijk",
        parent=Eenheidstatus.verhuurd.value,
    )
    """
    Huurcontract met beperkte looptijd (anders dan anti-kraak of onder een bruikleen
    constructie)
    """

    verkoop = Referentiedata(
        code="VEK",
        naam="Verkoop",
        parent=Eenheidstatus.leegstand.value,
    )
    """
    Leegstand omdat de eenheid op korte termijn verkocht zal worden, maar nog wel in
    exploitatie is.
    """

    vergunning_verleend = Referentiedata(
        code="VER",
        naam="Vergunning verleend",
        parent=Eenheidstatus.in_ontwikkeling.value,
    )
    """
    Eenheid is in ontwikkeling, bouwvergunning is verleend
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
