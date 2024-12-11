from typing import Iterator

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    BouwkundigelementdetailsoortReferentiedata,
)


def get_bouwkundige_elementen(
    ruimte: EenhedenRuimte,
    *bouwkundigelementdetailsoort: BouwkundigelementdetailsoortReferentiedata,
) -> Iterator[BouwkundigElementenBouwkundigElement]:
    """
    Haalt de lijst met bouwkundige elementen met de gegeven detailsoorten in de ruimte op.

    Args:
        ruimte (EenhedenRuimte): Een ruimte met bouwkundige elementen
        *bouwkundigelementdetailsoort (BouwkundigelementdetailsoortReferentiedata): De soort bouwkundige elementen die opgehaald moeten worden.

    Returns:
        Iterator[BouwkundigElementenBouwkundigElement]: Een iterator van bouwkundige elementen.
    """
    return (
        element
        for element in ruimte.bouwkundige_elementen or []
        if element.detail_soort in bouwkundigelementdetailsoort
    )


def get_bouwkundige_elementen_detailsoort(
    ruimte: EenhedenRuimte,
) -> Iterator[Referentiedata]:
    """
    Haalt de lijst met detailsoorten van bouwkundige elementen in de ruimte op.

    Args:
        ruimte (EenhedenRuimte): Een ruimte met bouwkundige elementen

    Returns:
        Iterator[Referentiedata]: Een iterator van de detailsoorten van de bouwkundige elementen.
    """
    return (
        element.detail_soort
        for element in ruimte.bouwkundige_elementen or []
        if element.detail_soort is not None
    )


def heeft_bouwkundig_element(
    ruimte: EenhedenRuimte,
    *bouwkundigelementdetailsoort: BouwkundigelementdetailsoortReferentiedata,
) -> bool:
    """
    Controleert of een ruimte een specifiek bouwkundig element bevat.

    Args:
        ruimte (EenhedenRuimte): De ruimte waarin gecontroleerd moet worden.
        *bouwkundigelementdetailsoort (BouwkundigelementdetailsoortReferentiedata): De bouwkundige elementen waarop gecontroleerd moet worden.

    Returns:
        bool: True als de ruimte alle opgegeven bouwkundige elementen bevat, anders False.
    """
    ruimte_bouwkundige_elementen_detailsoorten = get_bouwkundige_elementen_detailsoort(
        ruimte
    )

    return set(bouwkundigelementdetailsoort).issubset(
        ruimte_bouwkundige_elementen_detailsoorten
    )


def aantal_bouwkundige_elementen(
    ruimte: EenhedenRuimte,
    *bouwkundigelementdetailsoort: BouwkundigelementdetailsoortReferentiedata,
) -> int:
    """
    Telt (de combinatie van) het aantal bouwkundige elementen in een ruimte dat overeenkomt met het opgegeven bouwkundige element.

    Args:
        ruimte (EenhedenRuimte): De ruimte waarin geteld moet worden.
        *bouwkundigelementdetailsoort (BouwkundigelementdetailsoortReferentiedata): De bouwkundige elementen die geteld moeten worden.

    Returns:
        int: Het aantal bouwkundige elementen in de ruimte dat overeenkomt met de opgegeven bouwkundige elementen.
    """
    if len(bouwkundigelementdetailsoort) > 1:
        return min(
            aantal_bouwkundige_elementen(ruimte, detailsoort)
            for detailsoort in bouwkundigelementdetailsoort
        )

    ruimte_bouwkundige_elementen_detailsoorten = get_bouwkundige_elementen_detailsoort(
        ruimte
    )

    return len(
        list(
            detailsoort
            for detailsoort in ruimte_bouwkundige_elementen_detailsoorten
            if detailsoort in bouwkundigelementdetailsoort
        )
    )
