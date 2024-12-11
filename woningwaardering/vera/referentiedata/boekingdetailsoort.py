from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BoekingdetailsoortReferentiedata(Referentiedata):
    pass


class Boekingdetailsoort(Referentiedatasoort):
    aanmaning = BoekingdetailsoortReferentiedata(
        code="AAN",
        naam="Aanmaning",
    )
    """
    Boeking voor het verzoek tot betalen aan een huurder of debiteur van een of meer
    openstaande achterstallige vorderingen, dan wel de ontvangst naar aanleiding
    daarvan.
    """

    afboeking = BoekingdetailsoortReferentiedata(
        code="AFB",
        naam="Afboeking",
    )
    """
    Boeking voor afboeken van het totale saldo van een openstaande vordering.
    """

    bank = BoekingdetailsoortReferentiedata(
        code="BAN",
        naam="Bank",
    )
    """
    Boeking voor  een ontvangst of uitbetaling die via een bankrekening is ontvangen of
    uitgevoerd.
    """

    betalingsregeling = BoekingdetailsoortReferentiedata(
        code="BET",
        naam="Betalingsregeling",
    )
    """
    Boeking die het totaalbedrag van een betaalafspraak vertegenwoordigt, die is gemaakt
    voor een of meer openstaande vorderingen.
    """

    borg = BoekingdetailsoortReferentiedata(
        code="BOR",
        naam="Borg",
    )
    """
    Boeking van een door een huurder aan een verhuurder te betalen bedrag als onderpand
    ter dekking voor mogelijke kosten voor toekomstig herstel van schade dan wel de
    ontvangst of uitbetaling daarvan.
    """

    betalingsregelingtermijn = BoekingdetailsoortReferentiedata(
        code="BRT",
        naam="Betalingsregelingtermijn",
    )
    """
    Boeking van een periodiek te ontvangen of ontvangen betaling naar aanleiding van een
    met een huurder of debiteur afgesproken betalingsregeling.
    """

    creditnota = BoekingdetailsoortReferentiedata(
        code="CRE",
        naam="Creditnota",
    )
    """
    Boeking voor het geheel of gedeeltelijk corrigeren van een debiteurenfactuur.
    """

    eindafrekening = BoekingdetailsoortReferentiedata(
        code="EIN",
        naam="Eindafrekening",
    )
    """
    Boeking voor een verzamelnota van alle openstaande vorderingen en schulden van een
    vertrekkende huurder, dan wel de ontvangst of uitbetaling naar aanleiding
    daarvan.
    """

    eerste_verhuurnota = BoekingdetailsoortReferentiedata(
        code="EVN",
        naam="Eerste verhuurnota",
    )
    """
    Boeking voor een verzamelnota van de eerste maandhuur en eventueel bijkomende kosten
    voor een nieuwe huurder, dan wel de ontvangst naar aanleiding daarvan.
    """

    factuur = BoekingdetailsoortReferentiedata(
        code="FAC",
        naam="Factuur",
    )
    """
    Boeking van een vordering voor een geleverde dienst of product door een corporatie
    anders dan de verhuur van een eenheid of object, dan wel een ontvangst naar
    aanleiding daarvan.
    """

    prolongatie = BoekingdetailsoortReferentiedata(
        code="PRO",
        naam="Prolongatie",
    )
    """
    Boeking van een vordering of ontvangst naar aanleiding van de maandelijkse
    huurprolongatie.
    """

    storno = BoekingdetailsoortReferentiedata(
        code="STO",
        naam="Storno",
    )
    """
    Boeking van de terugboeking van een uitgevoerde incasso, op verzoek van een huurder
    of doordat deze niet kan worden uitgevoerd door de bank.
    """

    terugbetaling = BoekingdetailsoortReferentiedata(
        code="TER",
        naam="Terugbetaling",
    )
    """
    Boeking van de betaling aan een huurder of derde van een teveel of ten onrechte
    betaald bedrag.
    """

    voucher = BoekingdetailsoortReferentiedata(
        code="VOU",
        naam="Voucher",
    )
    """
    Boeking van toename of afname van een saldo binnen een spaarsysteem, die huurders
    kunnen inwisselen bij de corporatie of soms ook bij ondernemers in de buurt.
    """
