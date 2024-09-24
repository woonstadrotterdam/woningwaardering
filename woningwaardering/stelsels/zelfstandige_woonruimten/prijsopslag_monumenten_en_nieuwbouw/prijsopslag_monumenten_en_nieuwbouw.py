import warnings
from datetime import date
from decimal import Decimal

from dateutil.relativedelta import relativedelta
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
            warnings.warn(
                f"Eenheid {eenheid.id}: 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            utils.update_eenheid_monumenten(eenheid)

        if any(
            monument.code == Eenheidmonument.rijksmonument.code
            for monument in eenheid.monumenten or []
        ):
            datum_afsluiten_huurovereenkomst = eenheid.datum_afsluiten_huurovereenkomst
            if datum_afsluiten_huurovereenkomst is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.",
                    UserWarning,
                )
                logger.warning(
                    f"Eenheid {eenheid.id}: Voor de waardering van dit rijksmonument wordt de peildatum {self.peildatum} gebruikt in plaats van de datum van de afsluiting van de huurovereenkomst."
                )
                datum_afsluiten_huurovereenkomst = self.peildatum

            woningwaardering = WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Rijksmonument",
                ),
            )

            if datum_afsluiten_huurovereenkomst >= date(2024, 7, 1):
                logger.info(
                    f"Eenheid {eenheid.id} is een rijksmonument en wordt gewaardeerd met een opslagpercentage van 35% op de maximale huurprijs voor de stelselgroep {self.stelselgroep.naam}."
                )
                woningwaardering.opslagpercentage = 0.35
            else:
                logger.info(
                    f"Eenheid {eenheid.id} is een rijksmonument en wordt gewaardeerd met een 50 punten voor de stelselgroep {self.stelselgroep.naam}."
                )
                woningwaardering.punten = 50.0

            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        if any(
            monument.code
            in [
                Eenheidmonument.gemeentelijk_monument.code,
                Eenheidmonument.provinciaal_monument.code,
            ]
            for monument in eenheid.monumenten or []
        ):
            logger.info(
                f"Eenheid {eenheid.id} is gemeentelijk of provinciaal monument en wordt gewaardeerd met een opslagpercentage van 15% op de maximale huurprijs voor de stelselgroep {self.stelselgroep.naam}."
            )
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
                Eenheidmonument.rijksmonument.code,
                Eenheidmonument.gemeentelijk_monument.code,
                Eenheidmonument.provinciaal_monument.code,
            ]
            for monument in eenheid.monumenten or []
        ):
            if eenheid.bouwjaar is None:
                warnings.warn(
                    f"Eenheid {eenheid.id}: 'bouwjaar' is niet gespecificeerd.",
                    UserWarning,
                )
            elif eenheid.bouwjaar < 1965:
                logger.info(
                    f"Eenheid {eenheid.id} behoort tot een beschermd stads- of dorpsgezicht en wordt gewaardeerd met een opslagpercentage van 5% op de maximale huurprijs voor de stelselgroep {self.stelselgroep.naam}."
                )
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Beschermd stads- of dorpsgezicht",
                        ),
                        opslagpercentage=0.05,
                    )
                )
            else:
                logger.info(
                    f"Eenheid {eenheid.id} behoort tot een beschermd stads- of dorpsgezicht, maar is niet gebouwd voor 1965. Er wordt geen opslagpercentage toegepast."
                )

        if (
            eenheid.begin_bouwdatum is not None
            and eenheid.begin_bouwdatum < date(2028, 1, 1)
            and eenheid.in_exploitatiedatum is not None
            and eenheid.in_exploitatiedatum
            > date(
                2024, 7, 1
            )  # TODO: https://github.com/woonstadrotterdam/woningwaardering/issues/105
            and eenheid.in_exploitatiedatum > self.peildatum - relativedelta(years=20)
        ):
            if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
                logger.warning(
                    "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
                )
                from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                    ZelfstandigeWoonruimten,
                )

                woningwaardering_resultaat = ZelfstandigeWoonruimten(
                    peildatum=self.peildatum
                ).bereken(eenheid, negeer_stelselgroep=PrijsopslagMonumentenEnNieuwbouw)

            puntentotaal = (
                woningwaardering_resultaat is not None
                and Stelsel.bereken_puntentotaal(woningwaardering_resultaat)
                or None
            )

            if puntentotaal is not None and 144 <= puntentotaal <= 186:
                logger.info(
                    f"Eenheid {eenheid.id} is een nieuwbouw en wordt gewaardeerd met een opslagpercentage van 10% op de maximale huurprijs voor de stelselgroep {self.stelselgroep.naam}."
                )

                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Nieuwbouw",
                        ),
                        opslagpercentage=0.1,
                    )
                )
            else:
                logger.info(
                    f"Eenheid {eenheid.id} is een nieuwbouw maar valt buiten het puntenbereik om in aanmerking te komen voor een opslagpercentage voor de stelselgroep {self.stelselgroep.naam}."
                )

        opslagpercentage = Decimal(
            sum(
                Decimal(str(woningwaardering.opslagpercentage))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.opslagpercentage is not None
            )
        )

        woningwaardering_groep.opslagpercentage = float(opslagpercentage)
        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep


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
