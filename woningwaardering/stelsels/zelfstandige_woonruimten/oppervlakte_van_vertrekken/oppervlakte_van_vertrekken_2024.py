from decimal import ROUND_HALF_UP, Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)


def ruimte_is_overige_ruimte(ruimte: EenhedenRuimte) -> bool:
    """Check of de ruimte een overige ruimte is.

    Args:
        ruimte (EenhedenRuimte): een ruimte.

    Returns:
        bool: is de ruimte een overige ruimte.

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

        result = (
            ruimte.detail_soort.code != Ruimtedetailsoort.badkamer_en_of_toilet.code
            or ruimte.oppervlakte >= 0.64
        )
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

        result = ruimte.oppervlakte >= 4 or ruimte.detail_soort.code in [
            Ruimtedetailsoort.keuken.code,
            Ruimtedetailsoort.badkamer_en_of_toilet.code,
            Ruimtedetailsoort.badkamer.code,
            Ruimtedetailsoort.toiletruimte.code,
        ]
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
            bool: True als de zolder een vaste heeft, False otherwise.

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
        return True

    if not _min_0komma64m2_badkamer_en_of_toilet(ruimte):
        return True

    if not _min_4m2_exclusief_keuken_en_badkamer_en_of_toilet(ruimte):
        return True

    if not _zolder_heeft_vaste_trap(ruimte):
        return True

    return False


class OppervlakteVanVertrekken2024(Stelselgroepversie):
    @staticmethod
    def bereken(
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        for ruimte in eenheid.ruimten or []:
            logger.debug(f"Processsing ruimte: {ruimte.id}")
            if ruimte.oppervlakte is None:
                error_msg = f"Ruimte {ruimte.id} heeft geen oppervlakte"
                logger.error(error_msg)
                raise TypeError(error_msg)
            if ruimte.detail_soort is None:
                error_msg = f"Ruimte {ruimte.id} heeft geen detailsoort"
                logger.error(error_msg)
                raise TypeError(error_msg)
            if ruimte.detail_soort.code is None:
                error_msg = f"Ruimte {ruimte.id} heeft geen detailsoortcode"
                logger.error(error_msg)
                raise TypeError(error_msg)

            criterium_naam = ruimte.naam

            # Indien een toilet in een badruimte of doucheruimte is geplaatst, wordt de oppervlakte van die ruimte met 1m2 verminderd.
            if OppervlakteVanVertrekken2024.badruimte_met_toilet(ruimte):
                ruimte.oppervlakte = float(
                    Decimal(str(ruimte.oppervlakte)) - Decimal("1")
                )
                logger.debug(
                    "Toilet in badkamer gevonden. 1m2 in mindering gebracht van de oppervlakte van de ruimte."
                )

            # Van vaste kasten (kleiner dan 2m²) wordt de netto oppervlakte bepaald
            # en bij de oppervlakte van het betreffende vertrek opgeteld.
            # Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een
            # verkeersruimte, wordt niet gewaardeerd
            if ruimte.detail_soort.code not in [
                Ruimtedetailsoort.hal.code,
                Ruimtedetailsoort.overloop.code,
                Ruimtedetailsoort.entree.code,
                Ruimtedetailsoort.gang.code,
            ]:
                ruimte_kasten = [
                    verbonden_ruimte
                    for verbonden_ruimte in ruimte.verbonden_ruimten or []
                    if verbonden_ruimte.detail_soort is not None
                    and verbonden_ruimte.detail_soort.code
                    == Ruimtedetailsoort.kast.code
                    and verbonden_ruimte.oppervlakte is not None
                    and verbonden_ruimte.oppervlakte < 2.0
                ]

                aantal_ruimte_kasten = len(ruimte_kasten)

                if aantal_ruimte_kasten > 0:
                    ruimte.oppervlakte += float(
                        sum(
                            [
                                Decimal(ruimte_kast.oppervlakte)
                                for ruimte_kast in ruimte_kasten
                                if ruimte_kast.oppervlakte is not None
                            ]
                        )
                    )

                    if ruimte.inhoud is not None:
                        ruimte.inhoud += float(
                            sum(
                                [
                                    Decimal(ruimte_kast.inhoud)
                                    for ruimte_kast in ruimte_kasten
                                    if ruimte_kast.inhoud is not None
                                ]
                            )
                        )

                    logger.debug(
                        f"De netto oppervlakte van {aantal_ruimte_kasten} verbonden {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'} is opgeteld bij {ruimte.naam}"
                    )

                    criterium_naam = f"{ruimte.naam} + {aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'}"

            if ruimte_is_overige_ruimte(ruimte):
                continue

            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                    naam=criterium_naam,
                )
            )

            woningwaardering.aantal = float(
                Decimal(str(ruimte.oppervlakte)).quantize(
                    Decimal("0.01"), ROUND_HALF_UP
                )
            )
            logger.debug(
                f"Oppervlakte voor {ruimte.naam} van {ruimte.oppervlakte} is afgerond naar {woningwaardering.aantal}"
            )

            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.aantal))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.aantal is not None
            )
        ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")

        woningwaardering_groep.punten = float(punten)
        return woningwaardering_groep

    @staticmethod
    def badruimte_met_toilet(ruimte: EenhedenRuimte) -> bool:
        if ruimte.detail_soort is None:
            raise TypeError("ruimte.detail_soort is None")
        if any(
            bouwkundig_element.detail_soort is not None
            and bouwkundig_element.detail_soort.code
            == Ruimtedetailsoort.toiletruimte.code
            for bouwkundig_element in ruimte.bouwkundige_elementen or []
        ):
            logger.warning(
                f"{Ruimtedetailsoort.toiletruimte} gebruikt in plaats van {Bouwkundigelementdetailsoort.closetcombinatie}"
            )
        return (
            ruimte.detail_soort.code == Ruimtedetailsoort.badkamer_en_of_toilet.code
        ) or (
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


if __name__ == "__main__":
    f = open(
        "tests/data/input/zelfstandige_woonruimten/12006000004.json",
        "r+",
    )
    eenheid = EenhedenEenheid.model_validate_json(f.read())

    woningwaardering_resultaat = OppervlakteVanVertrekken2024.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
