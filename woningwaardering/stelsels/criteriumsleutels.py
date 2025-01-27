from enum import Enum

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)


class CriteriumSleutels(Enum):
    verkoeling_en_verwarming__totaal__verwarmde_overige_en_verkeersruimten = (
        WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Verwarmde overige- en verkeersruimten",
            id=str(
                CriteriumId(
                    stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming,
                    criterium="verwarmde_overige_en_verkeersruimten",
                    is_totaal=True,
                )
            ),
        )
    )
    verkoeling_en_verwarming__totaal__verkoelde_en_verwarmde_vertrekken = (
        WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Verkoelde en verwarmde vertrekken",
            id=str(
                CriteriumId(
                    stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming,
                    criterium="verkoelde_en_verwarmde_vertrekken",
                    is_totaal=True,
                )
            ),
        )
    )
    verkoeling_en_verwarming__totaal__open_keuken = (
        WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Open keuken",
            id=str(
                CriteriumId(
                    stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming,
                    criterium="open_keuken",
                    is_totaal=True,
                )
            ),
        )
    )
    verkoeling_en_verwarming__totaal__verwarmde_vertrekken = (
        WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Verwarmde vertrekken",
            id=str(
                CriteriumId(
                    stelselgroep=Woningwaarderingstelselgroep.verkoeling_en_verwarming,
                    criterium="verwarmde_vertrekken",
                    is_totaal=True,
                )
            ),
        )
    )
