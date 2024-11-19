import warnings
from typing import Iterator

from woningwaardering.stelsels import stelsel
from woningwaardering.stelsels.utils import gedeeld_met_onzelfstandige_woonruimten
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)
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


def waardeer_aanrecht(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    for element in ruimte.bouwkundige_elementen or []:
        if not element.detail_soort or not element.detail_soort.code:
            warnings.warn(
                f"Bouwkundig element {element.id} heeft geen detailsoort.code en kan daardoor niet gewaardeerd worden.",
                UserWarning,
            )
            continue
        if element.detail_soort.code == Bouwkundigelementdetailsoort.aanrecht.code:
            if not element.lengte:
                warnings.warn(
                    f"{Bouwkundigelementdetailsoort.aanrecht.naam} {element.id} heeft geen lengte en kan daardoor niet gewaardeerd worden.",
                    UserWarning,
                )
                continue
            if element.lengte < 1000:
                aanrecht_punten = 0
            elif (
                element.lengte >= 2000
                and (
                    (  # zelfstandige keuken met aanrecht boven 2000mm is 7 punten
                        not gedeeld_met_onzelfstandige_woonruimten(ruimte)
                    )
                    or (  # onzelfstandige keuken met aanrecht tussen 2000mm en 3000mm is 7 punten
                        gedeeld_met_onzelfstandige_woonruimten(ruimte)
                        and element.lengte <= 3000
                    )
                )
            ):
                aanrecht_punten = 7
            elif (
                element.lengte > 3000
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
            ):
                aanrecht_punten = 13
            elif (
                element.lengte > 3000
                and stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten
            ):
                aanrecht_punten = 10

            else:
                aanrecht_punten = 4
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam}: Lengte {element.naam.lower() if element.naam else 'aanrecht'}",
                    meeteenheid=Meeteenheid.millimeter.value,
                ),
                punten=aanrecht_punten,
                aantal=element.lengte,
            )
