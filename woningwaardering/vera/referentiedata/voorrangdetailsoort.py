from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.voorrangsoort import (
    Voorrangsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VoorrangdetailsoortReferentiedata(Referentiedata):
    pass


class Voorrangdetailsoort(Referentiedatasoort):
    beroep = VoorrangdetailsoortReferentiedata(
        code="BER",
        naam="Beroep",
        parent=Voorrangsoort.urgentie,
    )
    """
    Ugrentie wegens een bijzonder beroep in de regio onderwijs, zorg of politie
    """

    dakloos = VoorrangdetailsoortReferentiedata(
        code="DAK",
        naam="(Bijna) dakloos",
        parent=Voorrangsoort.urgentie,
    )
    """
    dakloos / calamiteit /brand onbewoonbaar / uitzetting / terugkeer uit buitenland
    """

    gedupeerd = VoorrangdetailsoortReferentiedata(
        code="DUP",
        naam="Gedupeerd",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens dupering van woningzoekende bij woningaanbieding
    """

    economisch = VoorrangdetailsoortReferentiedata(
        code="ECO",
        naam="Economisch",
        parent=Voorrangsoort.binding,
    )
    """
    Economische binding
    """

    ex_gedetineerd = VoorrangdetailsoortReferentiedata(
        code="EXD",
        naam="ex-gedetineerd",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het vrijkomen uit detentie
    """

    financieel = VoorrangdetailsoortReferentiedata(
        code="FIN",
        naam="Financieel",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens financiele problemen
    """

    gelijkvloers = VoorrangdetailsoortReferentiedata(
        code="GEL",
        naam="Gelijkvloers",
        parent=Voorrangsoort.indicatie,
    )
    """
    Indicatie voor een gelijkvloerse woning
    """

    geweld_bedreiging_en_of_overlast = VoorrangdetailsoortReferentiedata(
        code="GEW",
        naam="Geweld bedreiging / overlast",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens overlast uit de omgeving of bedreiging.
    """

    herhuisvesting = VoorrangdetailsoortReferentiedata(
        code="HUI",
        naam="Herhuisvesting",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens (langdurige) renovatie, nieuwbouw of sloop
    """

    kern = VoorrangdetailsoortReferentiedata(
        code="KRN",
        naam="Kern",
        parent=Voorrangsoort.binding,
    )
    """
    Kernbinding
    """

    maatschappelijk = VoorrangdetailsoortReferentiedata(
        code="MAA",
        naam="Maatschappelijk",
        parent=Voorrangsoort.binding,
    )
    """
    Maatschappelijke binding
    """

    mantelzorg = VoorrangdetailsoortReferentiedata(
        code="MAN",
        naam="Mantelzorg",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het ontvangen of geven van mantelzorg
    """

    medisch = VoorrangdetailsoortReferentiedata(
        code="MED",
        naam="Medisch",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie voor een aangepaste woning op medische gronden
    """

    regio = VoorrangdetailsoortReferentiedata(
        code="REG",
        naam="Regio",
        parent=Voorrangsoort.binding,
    )
    """
    Regionale of regio binding
    """

    relationeel = VoorrangdetailsoortReferentiedata(
        code="REL",
        naam="Relationeel",
        parent=Voorrangsoort.urgentie,
    )
    """
    Echtscheiding / verbroken relatie / gezinsproblemen /zwangerschap
    """

    rollatorgeschikt = VoorrangdetailsoortReferentiedata(
        code="ROL",
        naam="Rollatorgeschikt",
        parent=Voorrangsoort.indicatie,
    )
    """
    Indicatie voor een rollatorgeschikte woning
    """

    rolstoelgeschikt = VoorrangdetailsoortReferentiedata(
        code="RST",
        naam="Rolstoelgeschikt",
        parent=Voorrangsoort.indicatie,
    )
    """
    Indicatie voor een rolstoelgeschikte woning
    """

    servicewoning = VoorrangdetailsoortReferentiedata(
        code="SER",
        naam="Servicewoning",
        parent=Voorrangsoort.indicatie,
    )
    """
    Woningen bij een zorginstelling of verpleegcentrum.
    """

    sociaal = VoorrangdetailsoortReferentiedata(
        code="SOC",
        naam="Sociaal",
        parent=Voorrangsoort.urgentie,
    )
    """
    De woonsituatie is levensontwrichtend of levensbedreigend voor een of meer
    gezinsleden.
    """

    statushouder = VoorrangdetailsoortReferentiedata(
        code="STA",
        naam="Statushouder",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het verkrijgen van een verblijfsstatus
    """

    uitstroom_maatschappelijke_instelling = VoorrangdetailsoortReferentiedata(
        code="UIT",
        naam="uitstroom maatschappelijke instelling",
        parent=Voorrangsoort.urgentie,
    )
    """
    Urgentie wegens het uitstromen bij een maatschappelijke instelling
    """
