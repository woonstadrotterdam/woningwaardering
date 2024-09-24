from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Organisatievorm(Enum):
    buitenlandse_rechtsvorm = Referentiedata(
        code="BUI",
        naam="Buitenlandse rechtsvorm",
    )
    """
    Buitenlandse rechtsvorm  (Handelsregisterwet: art 5,d)
    """

    besloten_vennootschap_met_beperkte_aansprakelijkheid = Referentiedata(
        code="BV",
        naam="Besloten vennootschap met beperkte aansprakelijkheid",
    )
    """
    Besloten vennootschap met beperkte aansprakelijkheid (BV)  (Handelsregisterwet: art
    5,a)
    """

    cooperatie = Referentiedata(
        code="COO",
        naam="Coöperatie",
    )
    """
    Coöperatie  (Handelsregisterwet: art 5,a)
    """

    commanditaire_vennootschap = Referentiedata(
        code="CV",
        naam="Commanditaire vennootschap",
    )
    """
    Commanditaire vennootschap (cv)  (Handelsregisterwet: art 5,a)
    """

    europees_economisch_samenwerkingsverband = Referentiedata(
        code="EES",
        naam="Europees Economisch Samenwerkingsverband",
    )
    """
    Europees Economisch Samenwerkingsverband  (Handelsregisterwet: art 5,c)
    """

    eenmanszaak = Referentiedata(
        code="EZ",
        naam="Eenmanszaak",
    )
    """
    Eenmanszaak  (Handelsregisterwet: art 5,b)
    """

    kerkgenootschap = Referentiedata(
        code="KERK",
        naam="Kerkgenootschap",
    )
    """
    Kerkgenootschap (Handelsregisterwet: art 1, e)
    """

    maatschap = Referentiedata(
        code="MTS",
        naam="Maatschap",
    )
    """
    Maatschap  (Handelsregisterwet: art 5,a)
    """

    naamloze_vennootschap = Referentiedata(
        code="NV",
        naam="Naamloze vennootschap",
    )
    """
    Naamloze vennootschap (NV) (Handelsregisterwet: art 5,a)
    """

    overige_rechtsvorm = Referentiedata(
        code="OVE",
        naam="Overige rechtsvorm",
    )
    """
    Conform  (Handelsregisterwet: art 5,e)
    """

    onderlinge_waarborgmaatschappij = Referentiedata(
        code="OW",
        naam="Onderlinge waarborgmaatschappij",
    )
    """
    Onderlinge waarborgmaatschappij  (Handelsregisterwet: art 5,a)
    """

    publiekrechterlijke_rechtspersoon = Referentiedata(
        code="PUB",
        naam="Publiekrechterlijke rechtspersoon",
    )
    """
    Publiekrechterlijke rechtspersoon (Handelsregisterwet: art 1, d)
    """

    rederij = Referentiedata(
        code="RED",
        naam="Rederij",
    )
    """
    Rederij  (Handelsregisterwet: art 5,a)
    """

    europese_cooperatieve_vennootschap = Referentiedata(
        code="SCE",
        naam="Europese coöperatieve vennootschap",
    )
    """
    Europese coöperatieve vennootschap (SCE) (Handelsregisterwet: art 5,c)
    """

    europese_naamloze_vennootschap = Referentiedata(
        code="SE",
        naam="Europese naamloze vennootschap",
    )
    """
    Europese naamloze vennootschap (SE)  (Handelsregisterwet: art 5,c)
    """

    stichting = Referentiedata(
        code="STI",
        naam="Stichting",
    )
    """
    Stichting (Handelsregisterwet: art 5,a)
    """

    vereniging = Referentiedata(
        code="VER",
        naam="Vereniging",
    )
    """
    Vereniging  (Handelsregisterwet: art 5,a)
    """

    vennootschap_onder_firma = Referentiedata(
        code="VOF",
        naam="Vennootschap onder firma",
    )
    """
    Vennootschap onder firma (vof) (Handelsregisterwet: art 5,a)
    """

    vereniging_van_eigenaars = Referentiedata(
        code="VVE",
        naam="Vereniging van eigenaars",
    )
    """
    Vereniging van eigenaars (Handelsregisterwet: art 6, 1, b)
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
