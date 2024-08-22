import warnings
from functools import wraps
from typing import Callable

from loguru import logger

from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element


def classificeer_ruimte_dec(
    func: Callable[[EenhedenRuimte], Ruimtesoort | None],
) -> Callable[[EenhedenRuimte], Ruimtesoort | None]:
    """Logt de classificatie van de ruimte volgens het Woningwaarderingstelsel voor zelfstandige woonruimten."""

    @wraps(func)
    def wrapper(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
        ruimtesoort = func(ruimte)
        if ruimtesoort is not None:
            logger.debug(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is geclassificeerd als een {ruimtesoort.naam if ruimtesoort.naam else ruimtesoort.code}"
            )
        else:
            logger.debug(
                f"Ruimte {ruimte.naam} ({ruimte.id}) kan niet worden geclassificeerd als een ruimtesoort binnen {Woningwaarderingstelsel.zelfstandige_woonruimten.naam}"
            )
        return ruimtesoort

    return wrapper


@classificeer_ruimte_dec
def classificeer_ruimte(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
    """
    Classificeert de ruimte volgens het Woningwaarderingstelsel juli 2024 voor zelfstandige woonruimten.

    Args:
        ruimte (EenhedenRuimte): De ruimte die geclassificeerd moet worden.

    Returns:
        Ruimtesoort | None: De classificatie van de ruimte volgens het Woningwaarderingstelsel.
            Geeft `None` terug als de ruimte niet kan worden gewaardeerd.
    """
    if ruimte.oppervlakte is None:
        warning_msg = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte en kan daardoor niet geclassificeerd worden."
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.soort is None:
        warning_msg = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen soort en kan daardoor niet geclassificeerd worden."
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.detail_soort is None:
        warning_msg = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort en kan daardoor niet geclassificeerd worden."
        warnings.warn(warning_msg, UserWarning)
        return None

    # Keuken, badkamer en doucheruimte worden altijd gewaardeerd als vertrek
    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.keuken.code,
        Ruimtedetailsoort.badkamer.code,
        Ruimtedetailsoort.doucheruimte.code,
    ]:
        return Ruimtesoort.vertrek

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.woonkamer.code,
        Ruimtedetailsoort.woon_en_of_slaapkamer.code,
        Ruimtedetailsoort.woonkamer_en_of_keuken.code,
        Ruimtedetailsoort.slaapkamer.code,
        Ruimtedetailsoort.badkamer_met_toilet.code,
        Ruimtedetailsoort.overig_vertrek.code,
        Ruimtedetailsoort.bijkeuken.code,
        Ruimtedetailsoort.berging.code,
        Ruimtedetailsoort.wasruimte.code,
        Ruimtedetailsoort.garage.code,
        Ruimtedetailsoort.kelder.code,
        # Ruimtedetailsoort.schuur.code # niet mogelijk want schuur en schacht zelfde code zie: https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/116 en https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/92
    ] or (
        ruimte.detail_soort.naam
        and ruimte.detail_soort.naam == Ruimtedetailsoort.schuur.naam
    ):
        if ruimte.soort.code == Ruimtesoort.vertrek.code and ruimte.oppervlakte >= 4:
            return Ruimtesoort.vertrek
        if (
            ruimte.soort.code == Ruimtesoort.overige_ruimten.code
            and ruimte.oppervlakte >= 2
        ):
            return Ruimtesoort.overige_ruimten

    if ruimte.detail_soort.code == Ruimtedetailsoort.toiletruimte.code:
        if (
            ruimte.soort.code == Ruimtesoort.overige_ruimten.code
            and ruimte.oppervlakte >= 2
        ):
            return Ruimtesoort.overige_ruimten

    if ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
        if ruimte.soort.code == Ruimtesoort.vertrek.code:
            if (
                heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)
                and ruimte.oppervlakte >= 4
            ):
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft een vaste trap: Ruimte wordt gewaardeerd als {Ruimtesoort.vertrek.naam}."
                )
                return Ruimtesoort.vertrek

            else:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen vaste trap gevonden: Ruimte wordt niet gewaardeerd als {ruimte.soort.naam}."
                )

        if ruimte.soort.code == Ruimtesoort.overige_ruimten.code:
            if (
                heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap)
                or heeft_bouwkundig_element(
                    ruimte, Bouwkundigelementdetailsoort.vlizotrap
                )
            ) and ruimte.oppervlakte >= 2:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft een trap: Ruimte wordt gewaardeerd als {Ruimtesoort.overige_ruimten.naam}."
                )
                return Ruimtesoort.overige_ruimten

            else:
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen trap: Ruimte wordt niet gewaardeerd als {Ruimtesoort.overige_ruimten.naam}."
                )

    return None


def voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte: EenhedenRuimte) -> str:
    """
    Deze functie voegt de oppervlakte van kasten toe aan een ruimte en retourneert de naam van de ruimte inclusief het aantal kasten.

    Args:
        ruimte (EenhedenRuimte): De ruimte waar kasten aan toegevoegd moeten worden.

    Returns:
        str: De naam van de ruimte inclusief het aantal toegevoegde kasten.
    """

    criterium_naam = ruimte.naam or "Naamloze ruimte"

    if ruimte.detail_soort is None or ruimte.detail_soort.code is None:
        message = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        warnings.warn(message, UserWarning)
        return criterium_naam

    if ruimte.oppervlakte is None:
        message = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        warnings.warn(message, UserWarning)
        return criterium_naam

    # Van vaste kasten wordt de netto oppervlakte bepaald
    # en bij de oppervlakte van de betreffende ruimte opgeteld.
    # Een kast waarvan de deur uitkomt op een
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
            and verbonden_ruimte.detail_soort.code == Ruimtedetailsoort.kast.code
        ]

        aantal_ruimte_kasten = len(ruimte_kasten)

        if aantal_ruimte_kasten > 0:
            ruimte.oppervlakte += sum(
                [
                    ruimte_kast.oppervlakte
                    for ruimte_kast in ruimte_kasten
                    if ruimte_kast.oppervlakte is not None
                ]
            )

            if ruimte.inhoud is not None:
                ruimte.inhoud += sum(
                    [
                        ruimte_kast.inhoud
                        for ruimte_kast in ruimte_kasten
                        if ruimte_kast.inhoud is not None
                    ]
                )

            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}): de netto oppervlakte van {aantal_ruimte_kasten} verbonden {'kast' if aantal_ruimte_kasten == 1 else 'kasten'} is erbij opgeteld."
            )

            criterium_naam = f"{ruimte.naam} + {aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'}"
    return criterium_naam
