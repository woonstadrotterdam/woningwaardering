import warnings

from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen


def is_keuken(ruimte: EenhedenRuimte) -> bool:
    aanrecht_aantal = len(
        [
            aanrecht
            for aanrecht in get_bouwkundige_elementen(
                ruimte, Bouwkundigelementdetailsoort.aanrecht
            )
            if aanrecht.lengte and aanrecht.lengte >= 1000
        ]
    )

    if not ruimte.detail_soort:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort",
            UserWarning,
        )
        return False

    if not ruimte.detail_soort.code:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort.code",
            UserWarning,
        )
        return False

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.keuken.code,
        Ruimtedetailsoort.woonkamer_en_of_keuken.code,
    ]:
        if aanrecht_aantal == 0:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor stelselgroep {Woningwaarderingstelselgroep.keuken.naam}.",
                UserWarning,
            )
            return False  # ruimte is een keuken maar heeft geen valide aanrecht en mag dus niet als keuken gewaardeerd worden
        return True  # ruimte is een keuken met een valide aanrecht
    if ruimte.detail_soort.code not in [
        Ruimtedetailsoort.woonkamer.code,
        Ruimtedetailsoort.woon_en_of_slaapkamer.code,
        Ruimtedetailsoort.slaapkamer.code,
    ]:
        return False  # ruimte is geen ruimte dat een keuken zou kunnen zijn met een aanrecht erin

    if aanrecht_aantal == 0:  # ruimte is geen keuken want heeft geen valide aanrecht
        return False

    return True  # ruimte is een impliciete keuken vanwege een valide aanrecht
