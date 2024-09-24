from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidmonument(Enum):
    beschermd_dorpsgezicht = Referentiedata(
        code="DOR",
        naam="Beschermd dorpsgezicht",
    )
    """
    Bij ontwikkelingen binnen een stads- of dorpsgezicht moet rekening gehouden met de
    cultuurhistorische waarde. Elk beschermd gebied heeft hiervoor een eigen
    bestemmingsplan. Vergeleken met een gewoon bestemmingsplan is het
    gedetailleerder en gelden er strengere regels, zowel voor de bebouwde als voor
    de onbebouwde ruimte. Bovendien is voor een aantal bouwactiviteiten een
    vergunning nodig.
    """

    gemeentelijk_monument = Referentiedata(
        code="GEM",
        naam="Gemeentelijk monument",
    )
    """
    Een gemeente kan besluiten een bijzonder pand op de gemeentelijke monumentenlijst te
    zetten. Dit gebeurt als een pand geen nationale betekenis heeft, maar wel van
    plaatselijk of regionaal belang is.
    """

    provinciaal_monument = Referentiedata(
        code="PRO",
        naam="Provinciaal monument",
    )
    """
    Niet alleen panden, maar ook dijken, grenspalen en gemeente-overschrijdende objecten
    kunnen deel uitmaken van een provinciale monumentenlijst. De lijst wordt
    samengesteld door de Provinciale Staten van de provincie. Als een pand op de
    lijst staat, betekent het dat het pand bescherming geniet vanuit de provincie.
    Bovendien dient de lijst als basis voor eventuele subsidietoezeggingen.
    Noord-Holland en Drenthe zijn de enige provincies die provinciale monumenten
    hebben aangewezen.
    """

    rijksmonument = Referentiedata(
        code="RIJ",
        naam="Rijksmonument",
    )
    """
    Rijksmonumenten zijn gebouwen of andere objecten die om hun nationale
    cultuurhistorische waarde door de rijksoverheid zijn aangewezen als beschermd
    monument.
    """

    beschermd_stadsgezicht = Referentiedata(
        code="STA",
        naam="Beschermd stadsgezicht",
    )
    """
    Bij ontwikkelingen binnen een stads- of dorpsgezicht moet rekening gehouden met de
    cultuurhistorische waarde. Elk beschermd gebied heeft hiervoor een eigen
    bestemmingsplan. Vergeleken met een gewoon bestemmingsplan is het
    gedetailleerder en gelden er strengere regels, zowel voor de bebouwde als voor
    de onbebouwde ruimte. Bovendien is voor een aantal bouwactiviteiten een
    vergunning nodig.
    """

    werelderfgoed = Referentiedata(
        code="WER",
        naam="Werelderfgoed",
    )
    """
    Werelderfgoederen zijn culturele of natuurlijke monumenten die mondiaal gezien
    uitzonderlijk en onvervangbaar zijn. Alleen als een monument is ingeschreven op
    de Werelderfgoedlijst van UNESCO mag het de titel Werelderfgoed dragen.
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
