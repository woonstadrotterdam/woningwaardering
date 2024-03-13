from woningwaardering.vera.bvg.models import Referentiedata


class COMMUNICATIEKANAAL:
    whatsapp = Referentiedata(
        code="APP",
        naam="Whatsapp",
    )

    balie = Referentiedata(
        code="BAL",
        naam="Balie",
    )

    huisbezoek = Referentiedata(
        code="BEZ",
        naam="Huisbezoek",
    )

    brief = Referentiedata(
        code="BRI",
        naam="Brief",
    )

    e_mail = Referentiedata(
        code="EMA",
        naam="E-mail",
    )

    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )

    internet_of_klantportaal = Referentiedata(
        code="INT",
        naam="Internet / klantportaal",
    )

    sms = Referentiedata(
        code="SMS",
        naam="SMS",
    )

    telefoon = Referentiedata(
        code="TEL",
        naam="Telefoon",
    )
