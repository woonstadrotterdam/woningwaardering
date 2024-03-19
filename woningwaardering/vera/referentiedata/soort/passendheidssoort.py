from vera.bvg.generated import Referentiedata


class Passendheidssoort:
    niet_passend = Referentiedata(
        code="NIE",
        naam="Niet passend",
    )
    """
    De toewijzing is niet-passend volgens de Woningwet (toewijzen betaalbare woning aan
    huishoudens met huurtoeslag). Om een niet-passende toewijzing nader te verantwoorden
    kan passendheiddetailsoort worden gebruikt.
    """

    passendheidtoets_niet_van_toepassing = Referentiedata(
        code="NVT",
        naam="Passendheidtoets niet van toepassing",
    )
    """
    De toewijzing valt buiten de regels van de passendheidstoets volgens de Woningwet,
    bijvoorbeeld omdat de woning niet tot de betaalbare woningvoorraad behoort
    """

    passend = Referentiedata(
        code="PAS",
        naam="Passend",
    )
    """
    De toewijzing is passend volgens de Woningwet (toewijzen betaalbare woning aan
    huishoudens met huurtoeslag)
    """
