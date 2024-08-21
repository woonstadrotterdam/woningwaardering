import warnings
from datetime import date
from decimal import Decimal

from dateutil.relativedelta import relativedelta
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    PriveBuitenruimten,
    Keuken,
    Sanitair,
    Energieprestatie,
    Verwarming,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument


class PrijsopslagMonumentenEnNieuwbouw(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = (
            Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw
        )

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
            warnings.warn(f"Eenheid {eenheid.id}: Monumenten is None.", UserWarning)
            logger.info(
                f"Eenheid {eenheid.id}: De api van cultureelerfgoed wordt geraadpleegd voor monumenten."
            )
            utils.update_eenheid_monumenten(eenheid)

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
            and eenheid.in_exploitatiedatum > self.peildatum - relativedelta(years=20)
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

        stelselgroepen = [
            OppervlakteVanVertrekken(peildatum=self.peildatum),
            OppervlakteVanOverigeRuimten(peildatum=self.peildatum),
            Verwarming(peildatum=self.peildatum),
            Energieprestatie(peildatum=self.peildatum),
            Sanitair(peildatum=self.peildatum),
            Keuken(peildatum=self.peildatum),
            PriveBuitenruimten(peildatum=self.peildatum),
        ]

        for stelselgroep in stelselgroepen:
            if (
                stelselgroep.stelselgroep
                == Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw
            ):
                continue

            woningwaardering_groep = stelselgroep.bereken(
                eenheid, woningwaardering_resultaat
            )
            woningwaardering_resultaat.groepen.append(woningwaardering_groep)

        return woningwaardering_resultaat


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumentenEnNieuwbouw()
    with open(
        "tests/data/zelfstandige_woonruimten/input/23109000031.json", "r+"
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

        woningwaardering_resultaat = prijsopslag_monumenten_en_nieuwbouw.bereken(
            eenheid
        )

        print(
            woningwaardering_resultaat.model_dump_json(
                by_alias=True, indent=2, exclude_none=True
            )
        )

        tabel = utils.naar_tabel(woningwaardering_resultaat)

        print(tabel)
