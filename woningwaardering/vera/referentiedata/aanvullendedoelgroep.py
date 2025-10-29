from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.doelgroep import (
    Doelgroep,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AanvullendedoelgroepReferentiedata(Referentiedata):
    pass


class Aanvullendedoelgroep(Referentiedatasoort):
    buitenlandse_studenten = AanvullendedoelgroepReferentiedata(
        code="BSTU",
        naam="Buitenlandse studenten",
        parent=Doelgroep.studenten,
    )
    """
    Woonruimte is bestemd voor en/of huurder is een uit het buitenland afkomstige
    student aan een instelling voor hoger of wetenschappelijk onderwijs
    """

    ex_dak_en_thuislozen = AanvullendedoelgroepReferentiedata(
        code="DAK",
        naam="ex-dak- en thuislozen",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een ex-dak- of thuisloze, eventueel met
    (behoefte aan) begeleiding.
    """

    personen_met_een_geringe_ergonomische_beperking = (
        AanvullendedoelgroepReferentiedata(
            code="GEB",
            naam="Personen met een Geringe Ergonomische Beperking",
        )
    )
    """
    Woonruimte is bestemd voor mensen met een geringe ergonomische beperking. Ook wel
    GEB-woningen genoemd.
    """

    ex_gedetineerden = AanvullendedoelgroepReferentiedata(
        code="GED",
        naam="ex-gedetineerden",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een ex-gedetineerde, eventueel met
    (behoefte aan) begeleiding.
    """

    ggz_patienten = AanvullendedoelgroepReferentiedata(
        code="GGZ",
        naam="GGZ-Patiënten",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een zelfstandig wonende in behandeling
    bij en/of begeleid door een GGZ instelling.
    """

    kunstenaars = AanvullendedoelgroepReferentiedata(
        code="KUN",
        naam="Kunstenaars",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een kunstenaar (de woonruimte is ook als
    atelier te gebruiken, of bij de woonruimte is een afzonderlijke atelierruimte
    beschikbaar).
    """

    lichamelijk_beperkten = AanvullendedoelgroepReferentiedata(
        code="LIC",
        naam="Lichamelijk beperkten",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft een lichamelijke beperking
    (motorisch, zintuigelijk en/of chronisch fysiologisch van aard).
    """

    psychiatrische_patienten = AanvullendedoelgroepReferentiedata(
        code="PSY",
        naam="(ex-) psychiatrische patiënten",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een (ex-) psychiatrische patiënt,
    eventueel met (behoefte aan) begeleiding.
    """

    skaeve_huse = AanvullendedoelgroepReferentiedata(
        code="SKA",
        naam="Skaeve Huse",
    )
    """
    Woonruimte is bestemd voor en/of huurder zorgt voor zware overlast in de omgeving.
    Dit zijn bijvoorbeeld moeilijk te huisvesten drank- of drugsverslaafden.
    """

    statushouders = AanvullendedoelgroepReferentiedata(
        code="STH",
        naam="Statushouders",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een als vluchteling erkende asielzoeker
    (statushouder of vergunninghouder)
    """

    verstandelijk_beperkten = AanvullendedoelgroepReferentiedata(
        code="VBE",
        naam="Verstandelijk beperkten",
    )
    """
    Woonuimte is bestemd voor en/of huurder heeft een verstandelijke beperking.
    """

    verslaafden = AanvullendedoelgroepReferentiedata(
        code="VER",
        naam="(ex)-verslaafden",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een (ex-) verslaafde, eventueel met
    (behoefte aan) begeleiding.
    """

    zorgindicatie = AanvullendedoelgroepReferentiedata(
        code="ZIN",
        naam="Zorgindicatie",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft een zorgindicatie.
    """
