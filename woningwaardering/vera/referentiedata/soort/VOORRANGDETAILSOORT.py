
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VOORRANGDETAILSOORT:

    beroep = Referentiedata(
        code="BER",
        naam="Beroep",
    )
    # beroep = ("BER", "Beroep")
    """
    Ugrentie wegens een bijzonder beroep in de regio onderwijs, zorg of politie
    """

    dakloos = Referentiedata(
        code="DAK",
        naam="(Bijna) dakloos",
    )
    # dakloos = ("DAK", "(Bijna) dakloos")
    """
    dakloos / calamiteit /brand onbewoonbaar / uitzetting / terugkeer uit buitenland
    """

    gedupeerd = Referentiedata(
        code="DUP",
        naam="Gedupeerd",
    )
    # gedupeerd = ("DUP", "Gedupeerd")
    """
    Urgentie wegens dupering van woningzoekende bij woningaanbieding
    """

    economisch = Referentiedata(
        code="ECO",
        naam="Economisch",
    )
    # economisch = ("ECO", "Economisch")
    """
    Economische binding
    """

    ex_gedetineerd = Referentiedata(
        code="EXD",
        naam="ex-gedetineerd",
    )
    # ex_gedetineerd = ("EXD", "ex-gedetineerd")
    """
    Urgentie wegens het vrijkomen uit detentie
    """

    financieel = Referentiedata(
        code="FIN",
        naam="Financieel",
    )
    # financieel = ("FIN", "Financieel")
    """
    Urgentie wegens financiele problemen
    """

    gelijkvloers = Referentiedata(
        code="GEL",
        naam="Gelijkvloers",
    )
    # gelijkvloers = ("GEL", "Gelijkvloers")
    """
    Indicatie voor een gelijkvloerse woning
    """

    geweld_bedreiging_of_overlast = Referentiedata(
        code="GEW",
        naam="Geweld bedreiging / overlast",
    )
    # geweld_bedreiging_of_overlast = ("GEW", "Geweld bedreiging / overlast")
    """
    Urgentie wegens overlast uit de omgeving of bedreiging.
    """

    herhuisvesting = Referentiedata(
        code="HUI",
        naam="Herhuisvesting",
    )
    # herhuisvesting = ("HUI", "Herhuisvesting")
    """
    Urgentie wegens (langdurige) renovatie, nieuwbouw of sloop
    """

    kern = Referentiedata(
        code="KRN",
        naam="Kern",
    )
    # kern = ("KRN", "Kern")
    """
    Kernbinding
    """

    maatschappelijk = Referentiedata(
        code="MAA",
        naam="Maatschappelijk",
    )
    # maatschappelijk = ("MAA", "Maatschappelijk")
    """
    Maatschappelijke binding
    """

    mantelzorg = Referentiedata(
        code="MAN",
        naam="Mantelzorg",
    )
    # mantelzorg = ("MAN", "Mantelzorg")
    """
    Urgentie wegens het ontvangen of geven van mantelzorg
    """

    medisch = Referentiedata(
        code="MED",
        naam="Medisch",
    )
    # medisch = ("MED", "Medisch")
    """
    Urgentie voor een aangepaste woning op medische gronden
    """

    regio = Referentiedata(
        code="REG",
        naam="Regio",
    )
    # regio = ("REG", "Regio")
    """
    Regionale of regio binding
    """

    relationeel = Referentiedata(
        code="REL",
        naam="Relationeel",
    )
    # relationeel = ("REL", "Relationeel")
    """
    Echtscheiding / verbroken relatie / gezinsproblemen /zwangerschap
    """

    rollatorgeschikt = Referentiedata(
        code="ROL",
        naam="Rollatorgeschikt",
    )
    # rollatorgeschikt = ("ROL", "Rollatorgeschikt")
    """
    Indicatie voor een rollatorgeschikte woning
    """

    rolstoelgeschikt = Referentiedata(
        code="RST",
        naam="Rolstoelgeschikt",
    )
    # rolstoelgeschikt = ("RST", "Rolstoelgeschikt")
    """
    Indicatie voor een rolstoelgeschikte woning
    """

    servicewoning = Referentiedata(
        code="SER",
        naam="Servicewoning",
    )
    # servicewoning = ("SER", "Servicewoning")
    """
    Woningen bij een zorginstelling of verpleegcentrum.
    """

    sociaal = Referentiedata(
        code="SOC",
        naam="Sociaal",
    )
    # sociaal = ("SOC", "Sociaal")
    """
    De woonsituatie is levensontwrichtend of levensbedreigend voor een of meer
    gezinsleden.
    """

    statushouder = Referentiedata(
        code="STA",
        naam="Statushouder",
    )
    # statushouder = ("STA", "Statushouder")
    """
    Urgentie wegens het verkrijgen van een verblijfsstatus
    """

    uitstroom_maatschappelijke_instelling = Referentiedata(
        code="UIT",
        naam="uitstroom maatschappelijke instelling",
    )
    # uitstroom_maatschappelijke_instelling = ("UIT", "uitstroom maatschappelijke instelling")
    """
    Urgentie wegens het uitstromen bij een maatschappelijke instelling
    """
