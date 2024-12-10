from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PassendheidssoortReferentiedata(Referentiedata):
    pass


class Passendheidssoort(Referentiedatasoort):
    niet_passend = PassendheidssoortReferentiedata(
        code="NIE",
        naam="Niet passend",
    )
    """
    De toewijzing is niet-passend volgens de Woningwet (toewijzen betaalbare woning aan
    huishoudens met huurtoeslag). Om een niet-passende toewijzing nader te
    verantwoorden kan passendheiddetailsoort worden gebruikt.
    """

    passendheidtoets_niet_van_toepassing = PassendheidssoortReferentiedata(
        code="NVT",
        naam="Passendheidtoets niet van toepassing",
    )
    """
    De toewijzing valt buiten de regels van de passendheidstoets volgens de Woningwet,
    bijvoorbeeld omdat de woning niet tot de betaalbare woningvoorraad behoort
    """

    passend = PassendheidssoortReferentiedata(
        code="PAS",
        naam="Passend",
    )
    """
    De toewijzing is passend volgens de Woningwet (toewijzen betaalbare woning aan
    huishoudens met huurtoeslag)
    """
