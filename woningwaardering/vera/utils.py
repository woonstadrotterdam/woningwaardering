from loguru import logger

from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
)


def badruimte_met_toilet(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of de gegeven `ruimte` een badkamer met een toilet is of een doucheruimte met een toilet.

    Args:
        ruimte (EenhedenRuimte): Het ruimte-object om te controleren.

    Returns:
        bool: True als de ruimte een badkamer met een toilet is of een doucheruimte met een toilet, anders False.

    Raises:
        TypeError: Als de ruimte geen detailsoort heeft.
    """
    if ruimte.detail_soort is None:
        error_msg = f"{ruimte.id}: ruimte.detail_soort is None"
        logger.error(error_msg)
        raise TypeError(error_msg)
    if any(
        bouwkundig_element.detail_soort is not None
        and bouwkundig_element.detail_soort.code == Ruimtedetailsoort.toiletruimte.code
        for bouwkundig_element in ruimte.bouwkundige_elementen or []
    ):
        logger.warning(
            f"{Ruimtedetailsoort.toiletruimte} gebruikt in plaats van {Bouwkundigelementdetailsoort.closetcombinatie}"
        )
    return (ruimte.detail_soort.code == Ruimtedetailsoort.badkamer_met_toilet.code) or (
        ruimte.detail_soort.code
        in [Ruimtedetailsoort.doucheruimte.code, Ruimtedetailsoort.badkamer.code]
        and any(
            bouwkundig_element.detail_soort is not None
            and bouwkundig_element.detail_soort.code
            in [
                Bouwkundigelementdetailsoort.closetcombinatie.code,
                Ruimtedetailsoort.toiletruimte.code,  # Foutief, maar vaak gebruikt
            ]
            for bouwkundig_element in ruimte.bouwkundige_elementen or []
        )
    )
