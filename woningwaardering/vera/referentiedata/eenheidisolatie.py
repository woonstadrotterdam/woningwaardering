from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidisolatieReferentiedata(Referentiedata):
    pass


class Eenheidisolatie(Referentiedatasoort):
    dakisolatie = EenheidisolatieReferentiedata(
        code="DAK",
        naam="Dakisolatie",
    )

    normaal_dubbelglas = EenheidisolatieReferentiedata(
        code="DGL",
        naam="Normaal dubbelglas",
    )
    """
    Dubbel glas waarbij de spouw tussen de glasplaten is gevuld met droge lucht.
    """

    hr_glas = EenheidisolatieReferentiedata(
        code="HR",
        naam="HR-glas",
    )
    """
    Dit is dubbelglas met een isolatiecoating op de ramen. De spouw is ook gevuld met
    droge lucht.
    """

    hr1 = EenheidisolatieReferentiedata(
        code="HR1",
        naam="HR+ glas",
    )
    """
    Dit is een verbeterde versie van HR-glas, met een dikkere coating en een smallere
    spouw.
    """

    hr2 = EenheidisolatieReferentiedata(
        code="HR2",
        naam="HR++ glas",
    )
    """
    Dit is dubbelglas heeft een spouw die gevuld is met gas, meestal argon.
    """

    hr3 = EenheidisolatieReferentiedata(
        code="HR3",
        naam="HR+++ glas",
    )
    """
    Dit is driedubbel glas met twee spouwen gevuld met gas.
    """

    eco_bouw = EenheidisolatieReferentiedata(
        code="ECO",
        naam="Eco-bouw",
    )
    """
    Ecologische, duurzame bouw
    """

    gedeeltelijk_dubbel_glas = EenheidisolatieReferentiedata(
        code="GDG",
        naam="Gedeeltelijk dubbel glas",
    )

    toekomstklaar = EenheidisolatieReferentiedata(
        code="TOE",
        naam="Toekomstklaar",
    )
    """
    Het betreft woningen die aan de isolatiestandaard voldoen, zie https://www.rvo.nl/on
    derwerpen/wetten-en-regels-gebouwen/standaard-streefwaarden-woningisolatie
    """

    vergaand_geisoleerd = EenheidisolatieReferentiedata(
        code="VER",
        naam="Vergaand geïsoleerd",
    )
    """
    De woning is vergaand geïsoleerd of geschikt voor verwarmen met maximaal 50 graden.
    De woning is wat betreft isolatie gereed voor verwarmen met een lage temperatuur
    bron.
    """

    gereed_voor_aansluiting_op_mt_warmtenet = EenheidisolatieReferentiedata(
        code="GER",
        naam="Gereed voor aansluiting op MT-warmtenet",
    )
    """
    Woning die qua isolatie geschikt is voor aansluiting op een MT-warmtenet en waarbij
    ook voorzien is dat deze woning in de toekomst wordt aangesloten op een
    MT-warmtenet of een HT-net dat op termijn naar MT gaat.
    """

    muurisolatie = EenheidisolatieReferentiedata(
        code="MUU",
        naam="Muurisolatie",
    )

    vloerisolatie = EenheidisolatieReferentiedata(
        code="VLO",
        naam="Vloerisolatie",
    )

    volledig_geisoleerd = EenheidisolatieReferentiedata(
        code="VOL",
        naam="Volledig geïsoleerd",
    )
