from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Boekingdetailsoort(Enum):
    aanmaning = Referentiedata(
        code="AAN",
        naam="Aanmaning",
    )
    """
    Boeking voor het verzoek tot betalen aan een huurder of debiteur van een of meer
    openstaande achterstallige vorderingen, dan wel de ontvangst naar aanleiding
    daarvan.
    """

    afboeking = Referentiedata(
        code="AFB",
        naam="Afboeking",
    )
    """
    Boeking voor afboeken van het totale saldo van een openstaande vordering.
    """

    bank = Referentiedata(
        code="BAN",
        naam="Bank",
    )
    """
    Boeking voor  een ontvangst of uitbetaling die via een bankrekening is ontvangen of
    uitgevoerd.
    """

    betalingsregeling = Referentiedata(
        code="BET",
        naam="Betalingsregeling",
    )
    """
    Boeking die het totaalbedrag van een betaalafspraak vertegenwoordigt, die is gemaakt
    voor een of meer openstaande vorderingen.
    """

    borg = Referentiedata(
        code="BOR",
        naam="Borg",
    )
    """
    Boeking van een door een huurder aan een verhuurder te betalen bedrag als onderpand
    ter dekking voor mogelijke kosten voor toekomstig herstel van schade dan wel de
    ontvangst of uitbetaling daarvan.
    """

    betalingsregelingtermijn = Referentiedata(
        code="BRT",
        naam="Betalingsregelingtermijn",
    )
    """
    Boeking van een periodiek te ontvangen of ontvangen betaling naar aanleiding van een
    met een huurder of debiteur afgesproken betalingsregeling.
    """

    creditnota = Referentiedata(
        code="CRE",
        naam="Creditnota",
    )
    """
    Boeking voor het geheel of gedeeltelijk corrigeren van een debiteurenfactuur.
    """

    eindafrekening = Referentiedata(
        code="EIN",
        naam="Eindafrekening",
    )
    """
    Boeking voor een verzamelnota van alle openstaande vorderingen en schulden van een
    vertrekkende huurder, dan wel de ontvangst of uitbetaling naar aanleiding
    daarvan.
    """

    eerste_verhuurnota = Referentiedata(
        code="EVN",
        naam="Eerste verhuurnota",
    )
    """
    Boeking voor een verzamelnota van de eerste maandhuur en eventueel bijkomende kosten
    voor een nieuwe huurder, dan wel de ontvangst naar aanleiding daarvan.
    """

    factuur = Referentiedata(
        code="FAC",
        naam="Factuur",
    )
    """
    Boeking van een vordering voor een geleverde dienst of product door een corporatie
    anders dan de verhuur van een eenheid of object, dan wel een ontvangst naar
    aanleiding daarvan.
    """

    prolongatie = Referentiedata(
        code="PRO",
        naam="Prolongatie",
    )
    """
    Boeking van een vordering of ontvangst naar aanleiding van de maandelijkse
    huurprolongatie.
    """

    storno = Referentiedata(
        code="STO",
        naam="Storno",
    )
    """
    Boeking van de terugboeking van een uitgevoerde incasso, op verzoek van een huurder
    of doordat deze niet kan worden uitgevoerd door de bank.
    """

    terugbetaling = Referentiedata(
        code="TER",
        naam="Terugbetaling",
    )
    """
    Boeking van de betaling aan een huurder of derde van een teveel of ten onrechte
    betaald bedrag.
    """

    voucher = Referentiedata(
        code="VOU",
        naam="Voucher",
    )
    """
    Boeking van toename of afname van een saldo binnen een spaarsysteem, die huurders
    kunnen inwisselen bij de corporatie of soms ook bij ondernemers in de buurt.
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
