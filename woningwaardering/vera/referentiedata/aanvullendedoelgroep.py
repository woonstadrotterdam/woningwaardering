from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Aanvullendedoelgroep(Enum):
    buitenlandse_studenten = Referentiedata(
        code="BSTU",
        naam="Buitenlandse studenten",
        parent=Referentiedata(
            code="STU",
            naam="Studenten",
        ),
    )
    """
    Woonruimte is bestemd voor en/of huurder is een uit het buitenland afkomstige
    student aan een instelling voor hoger of wetenschappelijk onderwijs
    """

    ex_dak_en_thuislozen = Referentiedata(
        code="DAK",
        naam="ex-dak- en thuislozen",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een ex-dak- of thuisloze, eventueel met
    (behoefte aan) begeleiding.
    """

    personen_met_een_geringe_ergonomische_beperking = Referentiedata(
        code="GEB",
        naam="Personen met een Geringe Ergonomische Beperking",
    )
    """
    Woonruimte is bestemd voor mensen met een geringe ergonomische beperking. Ook wel
    GEB-woningen genoemd.
    """

    ex_gedetineerden = Referentiedata(
        code="GED",
        naam="ex-gedetineerden",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een ex-gedetineerde, eventueel met
    (behoefte aan) begeleiding.
    """

    ggz_patienten = Referentiedata(
        code="GGZ",
        naam="GGZ-Patiënten",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een zelfstandig wonende in behandeling
    bij en/of begeleid door een GGZ instelling.
    """

    kunstenaars = Referentiedata(
        code="KUN",
        naam="Kunstenaars",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een kunstenaar (de woonruimte is ook als
    atelier te gebruiken, of bij de woonruimte is een afzonderlijke atelierruimte
    beschikbaar).
    """

    lichamelijk_beperkten = Referentiedata(
        code="LIC",
        naam="Lichamelijk beperkten",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft een lichamelijke beperking
    (motorisch, zintuigelijk en/of chronisch fysiologisch van aard).
    """

    psychiatrische_patienten = Referentiedata(
        code="PSY",
        naam="(ex-) psychiatrische patiënten",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een (ex-) psychiatrische patiënt,
    eventueel met (behoefte aan) begeleiding.
    """

    skaeve_huse = Referentiedata(
        code="SKA",
        naam="Skaeve Huse",
    )
    """
    Woonruimte is bestemd voor en/of huurder zorgt voor zware overlast in de omgeving.
    Dit zijn bijvoorbeeld moeilijk te huisvesten drank- of drugsverslaafden.
    """

    statushouders = Referentiedata(
        code="STH",
        naam="Statushouders",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een als vluchteling erkende asielzoeker
    (statushouder of vergunninghouder)
    """

    verstandelijk_beperkten = Referentiedata(
        code="VBE",
        naam="Verstandelijk beperkten",
    )
    """
    Woonuimte is bestemd voor en/of huurder heeft een verstandelijke beperking.
    """

    verslaafden = Referentiedata(
        code="VER",
        naam="(ex)-verslaafden",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een (ex-) verslaafde, eventueel met
    (behoefte aan) begeleiding.
    """

    zorgindicatie = Referentiedata(
        code="ZIN",
        naam="Zorgindicatie",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft een zorgindicatie.
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
