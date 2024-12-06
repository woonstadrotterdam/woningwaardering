from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.voorrangsoort import Voorrangsoort
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Voorrangdetailsoort(Referentiedatasoort):
    beroep = Referentiedata(
        code="BER",
        naam="Beroep",
        parent=Voorrangsoort.urgentie,
    )
    """
    Ugrentie wegens een bijzonder beroep in de regio onderwijs, zorg of politie
    """

    dakloos = Referentiedata(
        code="DAK",
        naam="(Bijna) dakloos",
        parent=Voorrangsoort.urgentie,
    )
    """
    dakloos / calamiteit /brand onbewoonbaar / uitzetting / terugkeer uit buitenland
    """

    gedupeerd = Referentiedata(
        code="DUP",
        naam="Gedupeerd",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens dupering van woningzoekende bij woningaanbieding
    """

    economisch = Referentiedata(
        code="ECO",
        naam="Economisch",
        parent=Voorrangsoort.binding,
    )
    """
    Economische binding
    """

    ex_gedetineerd = Referentiedata(
        code="EXD",
        naam="ex-gedetineerd",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het vrijkomen uit detentie
    """

    financieel = Referentiedata(
        code="FIN",
        naam="Financieel",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens financiele problemen
    """

    gelijkvloers = Referentiedata(
        code="GEL",
        naam="Gelijkvloers",
        parent=Voorrangsoort.indicatie,
    )
    """
    Indicatie voor een gelijkvloerse woning
    """

    geweld_bedreiging_en_of_overlast = Referentiedata(
        code="GEW",
        naam="Geweld bedreiging / overlast",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens overlast uit de omgeving of bedreiging.
    """

    herhuisvesting = Referentiedata(
        code="HUI",
        naam="Herhuisvesting",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens (langdurige) renovatie, nieuwbouw of sloop
    """

    kern = Referentiedata(
        code="KRN",
        naam="Kern",
        parent=Voorrangsoort.binding,
    )
    """
    Kernbinding
    """

    maatschappelijk = Referentiedata(
        code="MAA",
        naam="Maatschappelijk",
        parent=Voorrangsoort.binding,
    )
    """
    Maatschappelijke binding
    """

    mantelzorg = Referentiedata(
        code="MAN",
        naam="Mantelzorg",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het ontvangen of geven van mantelzorg
    """

    medisch = Referentiedata(
        code="MED",
        naam="Medisch",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie voor een aangepaste woning op medische gronden
    """

    regio = Referentiedata(
        code="REG",
        naam="Regio",
        parent=Voorrangsoort.binding,
    )
    """
    Regionale of regio binding
    """

    relationeel = Referentiedata(
        code="REL",
        naam="Relationeel",
        parent=Voorrangsoort.urgentie,
    )
    """
    Echtscheiding / verbroken relatie / gezinsproblemen /zwangerschap
    """

    rollatorgeschikt = Referentiedata(
        code="ROL",
        naam="Rollatorgeschikt",
        parent=Voorrangsoort.indicatie,
    )
    """
    Indicatie voor een rollatorgeschikte woning
    """

    rolstoelgeschikt = Referentiedata(
        code="RST",
        naam="Rolstoelgeschikt",
        parent=Voorrangsoort.indicatie,
    )
    """
    Indicatie voor een rolstoelgeschikte woning
    """

    servicewoning = Referentiedata(
        code="SER",
        naam="Servicewoning",
        parent=Voorrangsoort.indicatie,
    )
    """
    Woningen bij een zorginstelling of verpleegcentrum.
    """

    sociaal = Referentiedata(
        code="SOC",
        naam="Sociaal",
        parent=Voorrangsoort.urgentie,
    )
    """
    De woonsituatie is levensontwrichtend of levensbedreigend voor een of meer
    gezinsleden.
    """

    statushouder = Referentiedata(
        code="STA",
        naam="Statushouder",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het verkrijgen van een verblijfsstatus
    """

    uitstroom_maatschappelijke_instelling = Referentiedata(
        code="UIT",
        naam="uitstroom maatschappelijke instelling",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het uitstromen bij een maatschappelijke instelling
    """
