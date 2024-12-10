from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OrganisatievormReferentiedata(Referentiedata):
    pass


class Organisatievorm(Referentiedatasoort):
    buitenlandse_rechtsvorm = OrganisatievormReferentiedata(
        code="BUI",
        naam="Buitenlandse rechtsvorm",
    )
    """
    Buitenlandse rechtsvorm  (Handelsregisterwet: art 5,d)
    """

    besloten_vennootschap_met_beperkte_aansprakelijkheid = (
        OrganisatievormReferentiedata(
            code="BV",
            naam="Besloten vennootschap met beperkte aansprakelijkheid",
        )
    )
    """
    Besloten vennootschap met beperkte aansprakelijkheid (BV)  (Handelsregisterwet: art
    5,a)
    """

    cooperatie = OrganisatievormReferentiedata(
        code="COO",
        naam="Coöperatie",
    )
    """
    Coöperatie  (Handelsregisterwet: art 5,a)
    """

    commanditaire_vennootschap = OrganisatievormReferentiedata(
        code="CV",
        naam="Commanditaire vennootschap",
    )
    """
    Commanditaire vennootschap (cv)  (Handelsregisterwet: art 5,a)
    """

    europees_economisch_samenwerkingsverband = OrganisatievormReferentiedata(
        code="EES",
        naam="Europees Economisch Samenwerkingsverband",
    )
    """
    Europees Economisch Samenwerkingsverband  (Handelsregisterwet: art 5,c)
    """

    eenmanszaak = OrganisatievormReferentiedata(
        code="EZ",
        naam="Eenmanszaak",
    )
    """
    Eenmanszaak  (Handelsregisterwet: art 5,b)
    """

    kerkgenootschap = OrganisatievormReferentiedata(
        code="KERK",
        naam="Kerkgenootschap",
    )
    """
    Kerkgenootschap (Handelsregisterwet: art 1, e)
    """

    maatschap = OrganisatievormReferentiedata(
        code="MTS",
        naam="Maatschap",
    )
    """
    Maatschap  (Handelsregisterwet: art 5,a)
    """

    naamloze_vennootschap = OrganisatievormReferentiedata(
        code="NV",
        naam="Naamloze vennootschap",
    )
    """
    Naamloze vennootschap (NV) (Handelsregisterwet: art 5,a)
    """

    overige_rechtsvorm = OrganisatievormReferentiedata(
        code="OVE",
        naam="Overige rechtsvorm",
    )
    """
    Conform  (Handelsregisterwet: art 5,e)
    """

    onderlinge_waarborgmaatschappij = OrganisatievormReferentiedata(
        code="OW",
        naam="Onderlinge waarborgmaatschappij",
    )
    """
    Onderlinge waarborgmaatschappij  (Handelsregisterwet: art 5,a)
    """

    publiekrechterlijke_rechtspersoon = OrganisatievormReferentiedata(
        code="PUB",
        naam="Publiekrechterlijke rechtspersoon",
    )
    """
    Publiekrechterlijke rechtspersoon (Handelsregisterwet: art 1, d)
    """

    rederij = OrganisatievormReferentiedata(
        code="RED",
        naam="Rederij",
    )
    """
    Rederij  (Handelsregisterwet: art 5,a)
    """

    europese_cooperatieve_vennootschap = OrganisatievormReferentiedata(
        code="SCE",
        naam="Europese coöperatieve vennootschap",
    )
    """
    Europese coöperatieve vennootschap (SCE) (Handelsregisterwet: art 5,c)
    """

    europese_naamloze_vennootschap = OrganisatievormReferentiedata(
        code="SE",
        naam="Europese naamloze vennootschap",
    )
    """
    Europese naamloze vennootschap (SE)  (Handelsregisterwet: art 5,c)
    """

    stichting = OrganisatievormReferentiedata(
        code="STI",
        naam="Stichting",
    )
    """
    Stichting (Handelsregisterwet: art 5,a)
    """

    vereniging = OrganisatievormReferentiedata(
        code="VER",
        naam="Vereniging",
    )
    """
    Vereniging  (Handelsregisterwet: art 5,a)
    """

    vennootschap_onder_firma = OrganisatievormReferentiedata(
        code="VOF",
        naam="Vennootschap onder firma",
    )
    """
    Vennootschap onder firma (vof) (Handelsregisterwet: art 5,a)
    """

    vereniging_van_eigenaars = OrganisatievormReferentiedata(
        code="VVE",
        naam="Vereniging van eigenaars",
    )
    """
    Vereniging van eigenaars (Handelsregisterwet: art 6, 1, b)
    """
