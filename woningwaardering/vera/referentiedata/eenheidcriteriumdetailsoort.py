from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidcriteriumdetailsoort(Enum):
    beroep = Referentiedata(
        code="BER",
        naam="Beroep",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens een bijzonder beroep in de regio onderwijs, zorg of politie
    """

    dakloos = Referentiedata(
        code="DAK",
        naam="(Bijna) dakloos",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    dakloos / calamiteit /brand onbewoonbaar / uitzetting / terugkeer uit buitenland
    """

    doelgroep = Referentiedata(
        code="DOE",
        naam="Doelgroep",
        parent=Referentiedata(
            code="GRO",
            naam="Groep",
        ),
    )
    """
    Behoren tot een doelgroep. Bijv. gezin, student, senioren etc.
    """

    gedupeerd = Referentiedata(
        code="DUP",
        naam="Gedupeerd",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens dupering van woningzoekende bij woningaanbieding
    """

    economisch = Referentiedata(
        code="ECO",
        naam="Economisch",
        parent=Referentiedata(
            code="BIN",
            naam="Binding",
        ),
    )
    """
    Economische binding
    """

    ex_gedetineerd = Referentiedata(
        code="EXD",
        naam="ex-gedetineerd",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens het vrijkomen uit detentie
    """

    financieel = Referentiedata(
        code="FIN",
        naam="Financieel",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens financiele problemen
    """

    gelijkvloers = Referentiedata(
        code="GEL",
        naam="Gelijkvloers",
        parent=Referentiedata(
            code="IND",
            naam="Indicatie",
        ),
    )
    """
    Indicatie voor een gelijkvloerse woning
    """

    geweld_bedreiging_en_of_overlast = Referentiedata(
        code="GEW",
        naam="Geweld bedreiging / overlast",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens overlast uit de omgeving of bedreiging.
    """

    herhuisvesting = Referentiedata(
        code="HUI",
        naam="Herhuisvesting",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens (langdurige) renovatie, nieuwbouw of sloop
    """

    kern = Referentiedata(
        code="KRN",
        naam="Kern",
        parent=Referentiedata(
            code="BIN",
            naam="Binding",
        ),
    )
    """
    Kernbinding
    """

    maatschappelijk = Referentiedata(
        code="MAA",
        naam="Maatschappelijk",
        parent=Referentiedata(
            code="BIN",
            naam="Binding",
        ),
    )
    """
    Maatschappelijke binding
    """

    mantelzorg = Referentiedata(
        code="MAN",
        naam="Mantelzorg",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens het ontvangen of geven van mantelzorg
    """

    medisch = Referentiedata(
        code="MED",
        naam="Medisch",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie voor een aangepaste woning op medische gronden
    """

    regio = Referentiedata(
        code="REG",
        naam="Regio",
        parent=Referentiedata(
            code="BIN",
            naam="Binding",
        ),
    )
    """
    Regionale of regio binding
    """

    relationeel = Referentiedata(
        code="REL",
        naam="Relationeel",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Echtscheiding / verbroken relatie / gezinsproblemen /zwangerschap
    """

    rollatorgeschikt = Referentiedata(
        code="ROL",
        naam="Rollatorgeschikt",
        parent=Referentiedata(
            code="IND",
            naam="Indicatie",
        ),
    )
    """
    Indicatie voor een rollatorgeschikte woning
    """

    rolstoelgeschikt = Referentiedata(
        code="RST",
        naam="Rolstoelgeschikt",
        parent=Referentiedata(
            code="IND",
            naam="Indicatie",
        ),
    )
    """
    Indicatie voor een rolstoelgeschikte woning
    """

    servicewoning = Referentiedata(
        code="SER",
        naam="Servicewoning",
        parent=Referentiedata(
            code="IND",
            naam="Indicatie",
        ),
    )
    """
    Woningen bij een zorginstelling of verpleegcentrum.
    """

    sociaal = Referentiedata(
        code="SOC",
        naam="Sociaal",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    De woonsituatie is levensontwrichtend of levensbedreigend voor een of meer
    gezinsleden.
    """

    statushouder = Referentiedata(
        code="STA",
        naam="Statushouder",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens het verkrijgen van een verblijfsstatus
    """

    uitstroom_maatschappelijke_instelling = Referentiedata(
        code="UIT",
        naam="Uitstroom maatschappelijke instelling",
        parent=Referentiedata(
            code="URG",
            naam="Urgentie",
        ),
    )
    """
    Urgentie wegens het uitstromen bij een maatschappelijke instelling
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
