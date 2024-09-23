from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Vragenlijstregelonderwerpsoort(Enum):
    aanbod = Referentiedata(
        code="AAN",
        naam="Aanbod",
    )
    """
    Vraag behoort bij onderwerp: aanbod
    """

    afrekening = Referentiedata(
        code="AFR",
        naam="Afrekening",
    )
    """
    Vraag behoort bij onderwerp: afrekening
    """

    afspraak = Referentiedata(
        code="AFS",
        naam="Afspraak",
    )
    """
    Vraag behoort bij onderwerp: afspraak
    """

    algemene_ruimte = Referentiedata(
        code="ALG",
        naam="Algemene ruimte",
    )
    """
    Vraag behoort bij onderwerp: algemene ruimte
    """

    behulpzaamheid = Referentiedata(
        code="BEH",
        naam="Behulpzaamheid",
    )
    """
    Vraag behoort bij onderwerp: behulpzaamheid
    """

    behulpzaamheid_aannemer = Referentiedata(
        code="BEA",
        naam="Behulpzaamheid aannemer",
    )
    """
    Vraag behoort bij onderwerp: behulpzaamheid aannemer
    """

    bel = Referentiedata(
        code="BEL",
        naam="BEL",
    )
    """
    Vraag behoort bij onderwerp: belofte
    """

    besluit = Referentiedata(
        code="BES",
        naam="Besluit",
    )
    """
    Vraag behoort bij onderwerp: besluit
    """

    buurt = Referentiedata(
        code="BUU",
        naam="Buurt",
    )
    """
    Vraag behoort bij onderwerp: buurt
    """

    buurt_motivatie = Referentiedata(
        code="BUM",
        naam="Buurt motivatie",
    )
    """
    Vraag behoort bij onderwerp: buurt motivatie
    """

    customereffortscore = Referentiedata(
        code="CES",
        naam="CustomerEffortScore",
    )
    """
    Vraag behoort bij onderwerp: Customer Effort Score
    """

    contact = Referentiedata(
        code="CON",
        naam="Contact",
    )
    """
    Vraag behoort bij contact: aanbod
    """

    deskundigheid = Referentiedata(
        code="DES",
        naam="Deskundigheid",
    )
    """
    Vraag behoort bij onderwerp: deskundigheid
    """

    dienstverlening = Referentiedata(
        code="DIE",
        naam="Dienstverlening",
    )
    """
    Vraag behoort bij onderwerp: dienstverlening
    """

    duidelijkheid = Referentiedata(
        code="DUI",
        naam="Duidelijkheid",
    )
    """
    Vraag behoort bij onderwerp: duidelijkheid
    """

    eindopname = Referentiedata(
        code="EIN",
        naam="Eindopname",
    )
    """
    Vraag behoort bij onderwerp: eindopname
    """

    gemak = Referentiedata(
        code="GEM",
        naam="Gemak",
    )
    """
    Vraag behoort bij onderwerp: gemak
    """

    informatie = Referentiedata(
        code="INF",
        naam="Informatie",
    )
    """
    Vraag behoort bij onderwerp: informatie
    """

    medewerker = Referentiedata(
        code="MED",
        naam="Medewerker",
    )
    """
    Vraag behoort bij onderwerp: medewerker
    """

    monteur = Referentiedata(
        code="MON",
        naam="Monteur",
    )
    """
    Vraag behoort bij onderwerp: monteur
    """

    netheid = Referentiedata(
        code="NET",
        naam="Netheid",
    )
    """
    Vraag behoort bij onderwerp: netheid
    """

    oplevering = Referentiedata(
        code="OLE",
        naam="Oplevering",
    )
    """
    Vraag behoort bij onderwerp: oplevering
    """

    oplossing = Referentiedata(
        code="OPL",
        naam="Oplossing",
    )
    """
    Vraag behoort bij onderwerp: oplossing
    """

    resultaat = Referentiedata(
        code="RES",
        naam="Resultaat",
    )
    """
    Vraag behoort bij onderwerp: resultaat
    """

    snelheid = Referentiedata(
        code="SNE",
        naam="Snelheid",
    )
    """
    Vraag behoort bij onderwerp: snelheid
    """

    staat = Referentiedata(
        code="STA",
        naam="Staat",
    )
    """
    Vraag behoort bij onderwerp: staat
    """

    termijn = Referentiedata(
        code="TER",
        naam="Termijn",
    )
    """
    Vraag behoort bij onderwerp: termijn
    """

    tijdstip = Referentiedata(
        code="TIJ",
        naam="Tijdstip",
    )
    """
    Vraag behoort bij onderwerp: tijdstip
    """

    uitleg = Referentiedata(
        code="UIT",
        naam="Uitleg",
    )
    """
    Vraag behoort bij onderwerp: uitleg
    """

    verloop = Referentiedata(
        code="VER",
        naam="Verloop",
    )
    """
    Vraag behoort bij onderwerp: verloop
    """

    vooropname = Referentiedata(
        code="VOO",
        naam="Vooropname",
    )
    """
    Vraag behoort bij onderwerp: vooropname
    """

    website = Referentiedata(
        code="WEB",
        naam="Website",
    )
    """
    Vraag behoort bij onderwerp: website
    """

    weten = Referentiedata(
        code="WET",
        naam="Weten",
    )
    """
    Vraag behoort bij onderwerp: weten
    """

    weten_aannemer = Referentiedata(
        code="WEA",
        naam="Weten aannemer",
    )
    """
    Vraag behoort bij onderwerp: weten aannemer
    """

    woning = Referentiedata(
        code="WON",
        naam="Woning",
    )
    """
    Vraag behoort bij onderwerp: woning
    """

    woning_motivatie = Referentiedata(
        code="WOM",
        naam="Woning motivatie",
    )
    """
    Vraag behoort bij onderwerp: woning motivatie
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
