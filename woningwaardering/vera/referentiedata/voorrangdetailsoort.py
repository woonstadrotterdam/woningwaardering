from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.voorrangsoort import Voorrangsoort


class Voorrangdetailsoort(Enum):
    beroep = Referentiedata(
        code="BER",
        naam="Beroep",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Ugrentie wegens een bijzonder beroep in de regio onderwijs, zorg of politie
    """

    dakloos = Referentiedata(
        code="DAK",
        naam="(Bijna) dakloos",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    dakloos / calamiteit /brand onbewoonbaar / uitzetting / terugkeer uit buitenland
    """

    gedupeerd = Referentiedata(
        code="DUP",
        naam="Gedupeerd",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens dupering van woningzoekende bij woningaanbieding
    """

    economisch = Referentiedata(
        code="ECO",
        naam="Economisch",
        parent=Voorrangsoort.binding.value,
    )
    """
    Economische binding
    """

    ex_gedetineerd = Referentiedata(
        code="EXD",
        naam="ex-gedetineerd",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens het vrijkomen uit detentie
    """

    financieel = Referentiedata(
        code="FIN",
        naam="Financieel",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens financiele problemen
    """

    gelijkvloers = Referentiedata(
        code="GEL",
        naam="Gelijkvloers",
        parent=Voorrangsoort.indicatie.value,
    )
    """
    Indicatie voor een gelijkvloerse woning
    """

    geweld_bedreiging_en_of_overlast = Referentiedata(
        code="GEW",
        naam="Geweld bedreiging / overlast",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens overlast uit de omgeving of bedreiging.
    """

    herhuisvesting = Referentiedata(
        code="HUI",
        naam="Herhuisvesting",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens (langdurige) renovatie, nieuwbouw of sloop
    """

    kern = Referentiedata(
        code="KRN",
        naam="Kern",
        parent=Voorrangsoort.binding.value,
    )
    """
    Kernbinding
    """

    maatschappelijk = Referentiedata(
        code="MAA",
        naam="Maatschappelijk",
        parent=Voorrangsoort.binding.value,
    )
    """
    Maatschappelijke binding
    """

    mantelzorg = Referentiedata(
        code="MAN",
        naam="Mantelzorg",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens het ontvangen of geven van mantelzorg
    """

    medisch = Referentiedata(
        code="MED",
        naam="Medisch",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie voor een aangepaste woning op medische gronden
    """

    regio = Referentiedata(
        code="REG",
        naam="Regio",
        parent=Voorrangsoort.binding.value,
    )
    """
    Regionale of regio binding
    """

    relationeel = Referentiedata(
        code="REL",
        naam="Relationeel",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Echtscheiding / verbroken relatie / gezinsproblemen /zwangerschap
    """

    rollatorgeschikt = Referentiedata(
        code="ROL",
        naam="Rollatorgeschikt",
        parent=Voorrangsoort.indicatie.value,
    )
    """
    Indicatie voor een rollatorgeschikte woning
    """

    rolstoelgeschikt = Referentiedata(
        code="RST",
        naam="Rolstoelgeschikt",
        parent=Voorrangsoort.indicatie.value,
    )
    """
    Indicatie voor een rolstoelgeschikte woning
    """

    servicewoning = Referentiedata(
        code="SER",
        naam="Servicewoning",
        parent=Voorrangsoort.indicatie.value,
    )
    """
    Woningen bij een zorginstelling of verpleegcentrum.
    """

    sociaal = Referentiedata(
        code="SOC",
        naam="Sociaal",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    De woonsituatie is levensontwrichtend of levensbedreigend voor een of meer
    gezinsleden.
    """

    statushouder = Referentiedata(
        code="STA",
        naam="Statushouder",
        parent=Voorrangsoort.urgentie.value,
    )
    """
    Urgentie wegens het verkrijgen van een verblijfsstatus
    """

    uitstroom_maatschappelijke_instelling = Referentiedata(
        code="UIT",
        naam="uitstroom maatschappelijke instelling",
        parent=Voorrangsoort.urgentie.value,
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
