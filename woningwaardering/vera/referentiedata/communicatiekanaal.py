from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class CommunicatiekanaalReferentiedata(Referentiedata):
    pass


class Communicatiekanaal(Referentiedatasoort):
    whatsapp = CommunicatiekanaalReferentiedata(
        code="APP",
        naam="Whatsapp",
    )

    balie = CommunicatiekanaalReferentiedata(
        code="BAL",
        naam="Balie",
    )

    huisbezoek = CommunicatiekanaalReferentiedata(
        code="BEZ",
        naam="Huisbezoek",
    )

    brief = CommunicatiekanaalReferentiedata(
        code="BRI",
        naam="Brief",
    )

    e_mail = CommunicatiekanaalReferentiedata(
        code="EMA",
        naam="E-mail",
    )

    inspectie = CommunicatiekanaalReferentiedata(
        code="INS",
        naam="Inspectie",
    )

    internet_en_of_klantportaal = CommunicatiekanaalReferentiedata(
        code="INT",
        naam="Internet / klantportaal",
    )

    sms = CommunicatiekanaalReferentiedata(
        code="SMS",
        naam="SMS",
    )

    telefoon = CommunicatiekanaalReferentiedata(
        code="TEL",
        naam="Telefoon",
    )
