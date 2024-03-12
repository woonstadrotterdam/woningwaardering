
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class CREDITEURSOORT:

    crediteur_gemeente = Referentiedata(
        code="CGM",
        naam="Crediteur gemeente",
    )
    # crediteur_gemeente = ("CGM", "Crediteur gemeente")

    crediteur_leningen_kredietinstelling = Referentiedata(
        code="CKI",
        naam="Crediteur leningen kredietinstelling",
    )
    # crediteur_leningen_kredietinstelling = ("CKI", "Crediteur leningen kredietinstelling")

    crediteur_leningen_overheid = Referentiedata(
        code="CLO",
        naam="Crediteur leningen overheid",
    )
    # crediteur_leningen_overheid = ("CLO", "Crediteur leningen overheid")
    """
    Aanduiding van de soort grootboekrekening. Administraties kunnen verschillen in
    indeling en detaillering. De referentiedata wordt gevormd door het
    ReferentieGrootboekSchema (RGS) zoals gepubliceerd op
    https://www.referentiegrootboekschema.nl/kbase?field_category_target_id=27
    (Kennisbank).
    """

    crediteur_overheid = Referentiedata(
        code="COH",
        naam="Crediteur overheid",
    )
    # crediteur_overheid = ("COH", "Crediteur overheid")

    handelscrediteur = Referentiedata(
        code="HCr",
        naam="Handelscrediteur",
    )
    # handelscrediteur = ("HCr", "Handelscrediteur")
