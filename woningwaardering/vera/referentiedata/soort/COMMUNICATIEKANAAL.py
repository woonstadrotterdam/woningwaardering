
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class COMMUNICATIEKANAAL:

    whatsapp = Referentiedata(
        code="APP",
        naam="Whatsapp",
    )
    # whatsapp = ("APP", "Whatsapp")

    balie = Referentiedata(
        code="BAL",
        naam="Balie",
    )
    # balie = ("BAL", "Balie")

    huisbezoek = Referentiedata(
        code="BEZ",
        naam="Huisbezoek",
    )
    # huisbezoek = ("BEZ", "Huisbezoek")

    brief = Referentiedata(
        code="BRI",
        naam="Brief",
    )
    # brief = ("BRI", "Brief")

    e_mail = Referentiedata(
        code="EMA",
        naam="E-mail",
    )
    # e_mail = ("EMA", "E-mail")

    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )
    # inspectie = ("INS", "Inspectie")

    internet_of_klantportaal = Referentiedata(
        code="INT",
        naam="Internet / klantportaal",
    )
    # internet_of_klantportaal = ("INT", "Internet / klantportaal")

    sms = Referentiedata(
        code="SMS",
        naam="SMS",
    )
    # sms = ("SMS", "SMS")

    telefoon = Referentiedata(
        code="TEL",
        naam="Telefoon",
    )
    # telefoon = ("TEL", "Telefoon")
