import warnings

from loguru import logger

from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.voorzieningsoort import Voorzieningsoort
from woningwaardering.vera.utils import get_bouwkundige_elementen


def _bouwkundige_elementen_naar_installaties(ruimte: EenhedenRuimte):
    ruimte.installaties = ruimte.installaties or []
    # Backwards compatibiliteit voor bouwkundige elementen
    for mapping in {
        Bouwkundigelementdetailsoort.wastafel: Voorzieningsoort.wastafel,
        Bouwkundigelementdetailsoort.douche: Voorzieningsoort.douche,
        Bouwkundigelementdetailsoort.bad: Voorzieningsoort.bad,
        Bouwkundigelementdetailsoort.kast: Voorzieningsoort.kastruimte,
        Bouwkundigelementdetailsoort.closetcombinatie: Voorzieningsoort.staand_toilet,
    }.items():
        bouwkundige_elementen = list(get_bouwkundige_elementen(ruimte, mapping[0]))
        if bouwkundige_elementen:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een {mapping[0].naam} als bouwkundig element. Voor een correcte waardering dient dit als installatie in de ruimte gespecificeerd te worden."
            )
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {mapping[0].naam} wordt als {mapping[1].naam} toegevoegd aan installaties"
            )
            ruimte.installaties.extend(
                [mapping[1].value for _ in bouwkundige_elementen]
            )
