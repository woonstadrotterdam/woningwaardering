from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eenheidcriteriumsoort import (
    Eenheidcriteriumsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidcriteriumdetailsoortReferentiedata(Referentiedata):
    pass


class Eenheidcriteriumdetailsoort(Referentiedatasoort):
    beroep = EenheidcriteriumdetailsoortReferentiedata(
        code="BER",
        naam="Beroep",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens een bijzonder beroep in de regio onderwijs, zorg of politie
    """

    dakloos = EenheidcriteriumdetailsoortReferentiedata(
        code="DAK",
        naam="(Bijna) dakloos",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    dakloos / calamiteit /brand onbewoonbaar / uitzetting / terugkeer uit buitenland
    """

    doelgroep = EenheidcriteriumdetailsoortReferentiedata(
        code="DOE",
        naam="Doelgroep",
        parent=Eenheidcriteriumsoort.groep,
    )
    """
    Behoren tot een doelgroep. Bijv. gezin, student, senioren etc.
    """

    gedupeerd = EenheidcriteriumdetailsoortReferentiedata(
        code="DUP",
        naam="Gedupeerd",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens dupering van woningzoekende bij woningaanbieding
    """

    economisch = EenheidcriteriumdetailsoortReferentiedata(
        code="ECO",
        naam="Economisch",
        parent=Eenheidcriteriumsoort.binding,
    )
    """
    Economische binding
    """

    ex_gedetineerd = EenheidcriteriumdetailsoortReferentiedata(
        code="EXD",
        naam="ex-gedetineerd",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens het vrijkomen uit detentie
    """

    financieel = EenheidcriteriumdetailsoortReferentiedata(
        code="FIN",
        naam="Financieel",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens financiele problemen
    """

    gelijkvloers = EenheidcriteriumdetailsoortReferentiedata(
        code="GEL",
        naam="Gelijkvloers",
        parent=Eenheidcriteriumsoort.indicatie,
    )
    """
    Indicatie voor een gelijkvloerse woning
    """

    geweld_bedreiging_en_of_overlast = EenheidcriteriumdetailsoortReferentiedata(
        code="GEW",
        naam="Geweld bedreiging / overlast",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens overlast uit de omgeving of bedreiging.
    """

    herhuisvesting = EenheidcriteriumdetailsoortReferentiedata(
        code="HUI",
        naam="Herhuisvesting",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens (langdurige) renovatie, nieuwbouw of sloop
    """

    kern = EenheidcriteriumdetailsoortReferentiedata(
        code="KRN",
        naam="Kern",
        parent=Eenheidcriteriumsoort.binding,
    )
    """
    Kernbinding
    """

    maatschappelijk = EenheidcriteriumdetailsoortReferentiedata(
        code="MAA",
        naam="Maatschappelijk",
        parent=Eenheidcriteriumsoort.binding,
    )
    """
    Maatschappelijke binding
    """

    mantelzorg = EenheidcriteriumdetailsoortReferentiedata(
        code="MAN",
        naam="Mantelzorg",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens het ontvangen of geven van mantelzorg
    """

    medisch = EenheidcriteriumdetailsoortReferentiedata(
        code="MED",
        naam="Medisch",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie voor een aangepaste woning op medische gronden
    """

    regio = EenheidcriteriumdetailsoortReferentiedata(
        code="REG",
        naam="Regio",
        parent=Eenheidcriteriumsoort.binding,
    )
    """
    Regionale of regio binding
    """

    relationeel = EenheidcriteriumdetailsoortReferentiedata(
        code="REL",
        naam="Relationeel",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Echtscheiding / verbroken relatie / gezinsproblemen /zwangerschap
    """

    rollatorgeschikt = EenheidcriteriumdetailsoortReferentiedata(
        code="ROL",
        naam="Rollatorgeschikt",
        parent=Eenheidcriteriumsoort.indicatie,
    )
    """
    Indicatie voor een rollatorgeschikte woning
    """

    rolstoelgeschikt = EenheidcriteriumdetailsoortReferentiedata(
        code="RST",
        naam="Rolstoelgeschikt",
        parent=Eenheidcriteriumsoort.indicatie,
    )
    """
    Indicatie voor een rolstoelgeschikte woning
    """

    servicewoning = EenheidcriteriumdetailsoortReferentiedata(
        code="SER",
        naam="Servicewoning",
        parent=Eenheidcriteriumsoort.indicatie,
    )
    """
    Woningen bij een zorginstelling of verpleegcentrum.
    """

    sociaal = EenheidcriteriumdetailsoortReferentiedata(
        code="SOC",
        naam="Sociaal",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    De woonsituatie is levensontwrichtend of levensbedreigend voor een of meer
    gezinsleden.
    """

    statushouder = EenheidcriteriumdetailsoortReferentiedata(
        code="STA",
        naam="Statushouder",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens het verkrijgen van een verblijfsstatus
    """

    uitstroom_maatschappelijke_instelling = EenheidcriteriumdetailsoortReferentiedata(
        code="UIT",
        naam="Uitstroom maatschappelijke instelling",
        parent=Eenheidcriteriumsoort.urgentie,
    )
    """
    Urgentie wegens het uitstromen bij een maatschappelijke instelling
    """
