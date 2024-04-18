from loguru import logger

from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import badruimte_met_toilet


def vertrek_telt_als_vertrek(ruimte: EenhedenRuimte) -> bool:
    """Check of een vertrek voldoet aan de voorwaarden om mee te tellen als vertrek onder de oppervlakte van vertrekken.

    Args:
        ruimte (EenhedenRuimte): een ruimte.

    Returns:
        bool: True als de ruimte mee telt als vertrek voor oppervlakte van vertrekken, anders False.

    Raises:
        TypeError: als de ruimte geen soort en/of detailsoort(-code) en/of oppervlakte heeft.
    """

    def _vertrek_detailsoort(ruimte: EenhedenRuimte) -> bool:
        """Een ruimte telt mogelijk als vertrek indien de ruimte een van de volgende detailsoort is:
        - woonkamer
        - woonkamer en of slaapkamer
        - keuken
        - overig vertrek
        - badkamer
        - badkamer en of toilet
        - doucheruimte
        - zolder
        - slaapkamer

        Args:
            ruimte (EenhedenRuimte): een ruimte

        Returns:
            bool: voldoet de ruimte aan het detailsoort om een vertrek te kunnen zijn.

        Raises:
            TypeError: als de ruimte geen soort en/of detailsoort(-code) heeft.
        """
        if (
            ruimte.detail_soort is None
            or ruimte.detail_soort.code is None
            or ruimte.soort is None
        ):
            error_msg = f"{ruimte.id} heeft geen soort en/of detailsoort(-code)"
            logger.error(error_msg)
            raise TypeError(error_msg)

        if ruimte.soort.code != Ruimtesoort.vertrek.code:
            return False

        result = ruimte.detail_soort.code in [
            Ruimtedetailsoort.woonkamer.code,
            Ruimtedetailsoort.woon_en_of_slaapkamer.code,
            Ruimtedetailsoort.woonkamer_en_of_keuken.code,
            Ruimtedetailsoort.keuken.code,
            Ruimtedetailsoort.overig_vertrek.code,
            Ruimtedetailsoort.badkamer.code,
            Ruimtedetailsoort.badkamer_en_of_toilet.code,
            Ruimtedetailsoort.doucheruimte.code,
            Ruimtedetailsoort.zolder.code,
            Ruimtedetailsoort.slaapkamer.code,
        ]
        if result is False:
            logger.warning(
                f"{ruimte.id} {ruimte.detail_soort.naam} {ruimte.detail_soort.code} komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
            )
        return result

    def _min_0komma64m2_badkamer_en_of_toilet(ruimte: EenhedenRuimte) -> bool:
        """Voor gecombineerde bad-/doucheruimte met toilet geldt een minimale oppervlakte van 0,64 m².

        Args:
            ruimte (EenhedenRuimte): een ruimte.

        Returns:
            bool: voldoet de ruimte aan de eis

        Raises:
            TypeError: als de ruimte geen detailsoort(-code) en/of oppervlakte heeft.
        """
        if (
            ruimte.oppervlakte is None
            or ruimte.detail_soort is None
            or ruimte.detail_soort.code is None
        ):
            error_msg = f"{ruimte.id} heeft geen detailsoort(-code) en/of oppervlakte"
            logger.error(error_msg)
            raise TypeError(error_msg)

        if not badruimte_met_toilet(ruimte):
            return True

        result = ruimte.oppervlakte >= 0.64

        if result is False:
            logger.warning(
                f"{ruimte.id} {ruimte.naam} {ruimte.detail_soort} is kleiner dan 0.64 vierkante meter ({ruimte.oppervlakte}) en krijgt daarom geen punten onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
            )
        return result

    def _min_4m2_exclusief_keuken_en_badkamer_en_of_toilet(
        ruimte: EenhedenRuimte,
    ) -> bool:
        """Een ruimte moet minimaal 4m2 zijn om te tellen als vertrek. De eisen van minimaal 4m2 gelden niet voor de keuken en badkamer en/of toilet.

        Args:
            ruimte (EenhedenRuimte): een ruimte.

        Returns:
            bool: voldoet de ruimte aan de eis

        Raises:
            TypeError: als de ruimte geen detailsoort(-code) en/of oppervlakte heeft.
        """
        if (
            ruimte.oppervlakte is None
            or ruimte.detail_soort is None
            or ruimte.detail_soort.code is None
        ):
            error_msg = f"{ruimte.id} heeft geen detailsoort(-code) en/of oppervlakte"
            logger.error(error_msg)
            raise TypeError(error_msg)

        if ruimte.detail_soort.code in [
            Ruimtedetailsoort.keuken.code,
            Ruimtedetailsoort.badkamer_en_of_toilet.code,
            Ruimtedetailsoort.badkamer.code,
            Ruimtedetailsoort.doucheruimte.code,
        ]:
            return True

        result = ruimte.oppervlakte >= 4

        if result is False:
            logger.warning(
                f"{ruimte.id} {ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 4 vierkante meter ({ruimte.oppervlakte}) en krijgt daarom geen punten onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
            )
        return result

    def _zolder_heeft_vaste_trap(ruimte: EenhedenRuimte) -> bool:
        """Check of een zolder een vaste trap heeft.

        Args:
            ruimte (EenhedenRuimte): Het vertrek om te checken.

        Returns:
            bool: True als de zolder een vaste trap heeft, anders False.

        Raises:
            TypeError: als de ruimte geen detailsoort heeft.
        """
        if ruimte.detail_soort is None:
            error_msg = f"{ruimte.id} heeft geen detailsoort"
            logger.error(error_msg)
            raise TypeError(error_msg)

        if ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
            vaste_trap = [
                element.detail_soort
                for element in ruimte.bouwkundige_elementen or []
                if element.detail_soort
                and element.detail_soort.code == Bouwkundigelementdetailsoort.trap.code
            ]
            if not vaste_trap:
                logger.warning(
                    f"Geen vaste trap gevonden in {ruimte.naam} ({ruimte.id}): telt niet mee onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
                )
                return False
            logger.warning(
                f"Vaste trap gevonden in {ruimte.naam} ({ruimte.id}): telt mee onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
            )
        return True

    if ruimte.soort is None or ruimte.detail_soort is None:
        error_msg = f"Ruimte {ruimte.id} heeft geen soort en/of detailsoort en kan daardoor niet meegerekend worden onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
        logger.error(error_msg)
        raise TypeError(error_msg)

    if not _vertrek_detailsoort(ruimte):
        return False

    if not _min_0komma64m2_badkamer_en_of_toilet(ruimte):
        return False

    if not _min_4m2_exclusief_keuken_en_badkamer_en_of_toilet(ruimte):
        return False

    if not _zolder_heeft_vaste_trap(ruimte):
        return False

    return True
