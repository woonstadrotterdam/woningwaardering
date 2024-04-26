from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Crediteursoort(Enum):
    crediteur_gemeente = Referentiedata(
        code="CGM",
        naam="Crediteur gemeente",
    )
    """
    Verwijst naar een entiteit of persoon aan wie de gemeente geld verschuldigd is. Dit
    kan bijvoorbeeld gebeuren wanneer de gemeente diensten heeft ontvangen of
    contracten heeft afgesloten met externe partijen, zoals leveranciers, aannemers
    of dienstverleners, en deze partijen nog betalingen moeten ontvangen van de
    gemeente. Een crediteur gemeente vertegenwoordigt dus iemand die een openstaande
    vordering heeft op de gemeente en die recht heeft op betaling voor geleverde
    goederen of diensten.
    """

    crediteur_leningen_kredietinstelling = Referentiedata(
        code="CKI",
        naam="Crediteur leningen kredietinstelling",
    )
    """
    Verwijst naar een entiteit, meestal een financiële instelling zoals een bank, die
    leningen verstrekt aan een andere partij, zoals een individu, bedrijf of
    overheid. In deze context is de kredietinstelling de crediteur, omdat zij geld
    lenen aan de partij die de lening aanvraagt. De partij die de lening ontvangt,
    wordt de debiteur genoemd. De crediteur leningen kredietinstelling heeft het
    recht om het geleende bedrag terug te vorderen, meestal met rente, volgens de
    voorwaarden van de leningsovereenkomst die tussen beide partijen is gesloten.
    """

    crediteur_leningen_overheid = Referentiedata(
        code="CLO",
        naam="Crediteur leningen overheid",
    )
    """
    Verwijst naar een crediteur of schuldeiser die leningen verstrekt aan de overheid.
    In dit geval leent de overheid geld van de crediteur, met de belofte om het
    bedrag op een later tijdstip terug te betalen, meestal met rente. Deze leningen
    kunnen worden verstrekt door verschillende entiteiten, waaronder andere
    overheden, internationale organisaties, financiële instellingen of particuliere
    investeerders. De overheid kan leningen aangaan om tekorten in de begroting aan
    te vullen, infrastructurele projecten te financieren of andere overheidsuitgaven
    te dekken.
    """

    crediteur_overheid = Referentiedata(
        code="COH",
        naam="Crediteur overheid",
    )
    """
    Verwijst naar een entiteit, persoon of organisatie die geld verschuldigd is aan de
    overheid. Dit kan bijvoorbeeld gebeuren wanneer een bedrijf belastingen
    verschuldigd is aan de overheid, wanneer individuen boetes moeten betalen, of
    wanneer andere overheidsdiensten of overheidsgerelateerde entiteiten betalingen
    verschuldigd zijn aan de overheid. In wezen is een crediteur overheid iemand die
    een schuld heeft aan de overheid en verplicht is deze schuld op een bepaald
    moment terug te betalen.
    """

    handelscrediteur = Referentiedata(
        code="HCR",
        naam="Handelscrediteur",
    )
    """
    Een persoon of entiteit aan wie een bedrijf geld verschuldigd is voor goederen of
    diensten die zijn geleverd als onderdeel van de normale bedrijfsvoering. Dit kan
    bijvoorbeeld een leverancier zijn van grondstoffen, goederen of diensten die op
    krediet worden geleverd. Handelscrediteuren zijn een vorm van kortlopende
    schulden op de balans van een bedrijf en vertegenwoordigen de openstaande
    betalingen die het bedrijf aan zijn leveranciers moet voldoen. Het is een
    belangrijk onderdeel van het werkkapitaalbeheer van een bedrijf en een aspect
    van het crediteurenbeheer.
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
