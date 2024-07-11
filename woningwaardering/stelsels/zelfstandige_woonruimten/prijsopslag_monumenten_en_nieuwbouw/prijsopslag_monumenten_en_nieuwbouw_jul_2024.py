from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import Stelsel
from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import update_eenheid_monumenten
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    PrijsopslagMonumentenEnNieuwbouw,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class PrijsopslagMonumentenEnNieuwbouwJul2024(Stelselgroepversie):
    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if eenheid.monumenten is None:
            logger.info(
                f"Monumenten is None voor eenheid {eenheid.id}. De api van cultureelerfgoed wordt geraadpleegd."
            )

            update_eenheid_monumenten(eenheid)

        if any(
            monument.code == Eenheidmonument.rijksmonument.code
            for monument in eenheid.monumenten or []
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Rijksmonument",
                    ),
                    opslagpercentage=0.35,
                )
            )

        if any(
            monument.code
            in [
                Eenheidmonument.gemeentelijk_monument.code,
                Eenheidmonument.provinciaal_monument.code,
            ]
            for monument in eenheid.monumenten or []
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Gemeentelijk of provinciaal monument",
                    ),
                    opslagpercentage=0.15,
                )
            )

        if any(
            monument.code
            in [
                Eenheidmonument.beschermd_dorpsgezicht.code,
                Eenheidmonument.beschermd_stadsgezicht.code,
            ]
            for monument in eenheid.monumenten or []
        ) and not any(
            monument.code
            in [
                Eenheidmonument.gemeentelijk_monument.code,
                Eenheidmonument.provinciaal_monument.code,
                Eenheidmonument.rijksmonument.code,
            ]
            for monument in eenheid.monumenten or []
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Beschermd stads- of dorpsgezicht",
                    ),
                    opslagpercentage=0.05,
                )
            )

        if (
            eenheid.begin_bouwdatum is not None
            and eenheid.begin_bouwdatum < date(2028, 1, 1)
            and eenheid.in_exploitatiedatum is not None
            and eenheid.in_exploitatiedatum > date(2024, 7, 1)
        ):
            if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
                logger.warning(
                    "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
                )
                woningwaardering_resultaat = self._bereken_woningwaarderingresultaat(
                    eenheid
                )

            puntentotaal = (
                woningwaardering_resultaat is not None
                and Stelsel.bereken_puntentotaal(woningwaardering_resultaat)
                or None
            )

            if puntentotaal is not None and 144 <= puntentotaal <= 186:
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Nieuwbouw",
                        ),
                        opslagpercentage=0.1,
                    )
                )

        opslagpercentage = Decimal(
            sum(
                Decimal(str(woningwaardering.opslagpercentage))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.opslagpercentage is not None
            )
        )

        woningwaardering_groep.opslagpercentage = float(opslagpercentage)
        return woningwaardering_groep

    def _bereken_woningwaarderingresultaat(
        self, eenheid: EenhedenEenheid
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        Berekent de woningwaardering resultaten voor de eenheid voor alle stelselgroepen behalve stelselgroep Prijsopslag monumenten en nieuwbouw.

        Args:
            eenheid (EenhedenEenheid): de eenheid waarvoor de woningwaardering wordt berekend.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: de woningwaardering resultaten.
        """

        woningwaardering_resultaat = (
            WoningwaarderingResultatenWoningwaarderingResultaat()
        )
        woningwaardering_resultaat.stelsel = (
            Woningwaarderingstelsel.zelfstandige_woonruimten.value
        )
        woningwaardering_resultaat.groepen = []

        geldige_stelselgroepen = Stelsel.select_geldige_stelselgroepen(
            self.peildatum, Woningwaarderingstelsel.zelfstandige_woonruimten
        )

        prijsopslag_monumenten_en_nieuwbouw_stelselgroep = (
            PrijsopslagMonumentenEnNieuwbouw().stelselgroep
        )

        for stelselgroep in geldige_stelselgroepen:
            if (
                stelselgroep.stelselgroep
                == prijsopslag_monumenten_en_nieuwbouw_stelselgroep
            ):
                continue

            woningwaardering_groep = stelselgroep.bereken(
                eenheid, woningwaardering_resultaat
            )
            woningwaardering_resultaat.groepen.append(woningwaardering_groep)

        return woningwaardering_resultaat
