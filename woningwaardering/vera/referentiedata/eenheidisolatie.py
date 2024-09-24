from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidisolatie(Enum):
    dakisolatie = Referentiedata(
        code="DAK",
        naam="Dakisolatie",
    )

    normaal_dubbelglas = Referentiedata(
        code="DGL",
        naam="Normaal dubbelglas",
    )
    """
    Dubbel glas waarbij de spouw tussen de glasplaten is gevuld met droge lucht.
    """

    hr_glas = Referentiedata(
        code="HR",
        naam="HR-glas",
    )
    """
    Dit is dubbelglas met een isolatiecoating op de ramen. De spouw is ook gevuld met
    droge lucht.
    """

    hr1 = Referentiedata(
        code="HR1",
        naam="HR+ glas",
    )
    """
    Dit is een verbeterde versie van HR-glas, met een dikkere coating en een smallere
    spouw.
    """

    hr2 = Referentiedata(
        code="HR2",
        naam="HR++ glas",
    )
    """
    Dit is dubbelglas heeft een spouw die gevuld is met gas, meestal argon.
    """

    hr3 = Referentiedata(
        code="HR3",
        naam="HR+++ glas",
    )
    """
    Dit is driedubbel glas met twee spouwen gevuld met gas.
    """

    eco_bouw = Referentiedata(
        code="ECO",
        naam="Eco-bouw",
    )
    """
    Ecologische, duurzame bouw
    """

    gedeeltelijk_dubbel_glas = Referentiedata(
        code="GDG",
        naam="Gedeeltelijk dubbel glas",
    )

    toekomstklaar = Referentiedata(
        code="TOE",
        naam="Toekomstklaar",
    )
    """
    Het betreft woningen die aan de isolatiestandaard voldoen, zie https://www.rvo.nl/on
    derwerpen/wetten-en-regels-gebouwen/standaard-streefwaarden-woningisolatie
    """

    vergaand_geisoleerd = Referentiedata(
        code="VER",
        naam="Vergaand geïsoleerd",
    )
    """
    De woning is vergaand geïsoleerd of geschikt voor verwarmen met maximaal 50 graden.
    De woning is wat betreft isolatie gereed voor verwarmen met een lage temperatuur
    bron.
    """

    gereed_voor_aansluiting_op_mt_warmtenet = Referentiedata(
        code="GER",
        naam="Gereed voor aansluiting op MT-warmtenet",
    )
    """
    Woning die qua isolatie geschikt is voor aansluiting op een MT-warmtenet en waarbij
    ook voorzien is dat deze woning in de toekomst wordt aangesloten op een
    MT-warmtenet of een HT-net dat op termijn naar MT gaat.
    """

    muurisolatie = Referentiedata(
        code="MUU",
        naam="Muurisolatie",
    )

    vloerisolatie = Referentiedata(
        code="VLO",
        naam="Vloerisolatie",
    )

    volledig_geisoleerd = Referentiedata(
        code="VOL",
        naam="Volledig geïsoleerd",
    )

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
