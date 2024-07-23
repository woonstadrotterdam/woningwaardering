from functools import wraps
from typing import Callable
import warnings

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
from woningwaardering.vera.utils import badruimte_met_toilet, heeft_bouwkundig_element


def classificeer_ruimte_dec(
    func: Callable[[EenhedenRuimte], Ruimtesoort | None],
) -> Callable[[EenhedenRuimte], Ruimtesoort | None]:
    """Logt de classificatie van de ruimte volgens het Woningwaarderingstelsel voor zelfstandige woonruimten."""

    @wraps(func)
    def wrapper(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
        ruimtesoort = func(ruimte)
        if ruimtesoort is not None:
            logger.debug(
                f"Ruimte {ruimte.naam} ({ruimte.id}) is geklassificeerd als een {ruimtesoort.naam if ruimtesoort.naam else ruimtesoort.code}"
            )
        else:
            logger.debug(
                f"Ruimte {ruimte.naam} ({ruimte.id}) kan niet worden geklassificeerd als een ruimtesoort binnen {Woningwaarderingstelsel.zelfstandige_woonruimten.naam}"
            )
        return ruimtesoort

    return wrapper


@classificeer_ruimte_dec
def classificeer_ruimte(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
    """
    Classificeert de ruimte volgens het Woningwaarderingstelsel voor zelfstandige woonruimten.

    Args:
        ruimte (EenhedenRuimte): De ruimte die geclassificeerd moet worden.

    Returns:
        Ruimtesoort | None: De classificatie van de ruimte volgens het Woningwaarderingstelsel.
            Geeft `None` terug als de ruimte niet kan worden gewaardeerd.
    """
    if ruimte.oppervlakte is None:
        warning_msg = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}."
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.soort is None or ruimte.soort.code is None:
        warning_msg = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen soort en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}."
        warnings.warn(warning_msg, UserWarning)
        return None

    if ruimte.detail_soort is None:
        warning_msg = f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}."
        warnings.warn(warning_msg, UserWarning)
        return None

    if (
        ruimte.soort.code == Ruimtesoort.buitenruimte.code
        or ruimte.detail_soort.code
        in [
            Ruimtedetailsoort.gemeenschappelijke_tuin.code,
            Ruimtedetailsoort.gemeenschappelijk_dakterras_gda.code,
            Ruimtedetailsoort.achtertuin.code,
            Ruimtedetailsoort.voortuin.code,
            Ruimtedetailsoort.balkon.code,
            Ruimtedetailsoort.atrium_en_of_patio.code,
            Ruimtedetailsoort.loggia.code,
            Ruimtedetailsoort.dakterras.code,
            Ruimtedetailsoort.terras.code,
            Ruimtedetailsoort.tuin_rondom.code,
            Ruimtedetailsoort.tuin.code,
        ]  # ruimten die ondanks potentieel verkeerde parent toch zeker een buitenruimte zijn
    ):
        return Ruimtesoort.buitenruimte

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.woonkamer.code,
        Ruimtedetailsoort.woon_en_of_slaapkamer.code,
        Ruimtedetailsoort.woonkamer_en_of_keuken.code,
        Ruimtedetailsoort.slaapkamer.code,
        Ruimtedetailsoort.overig_vertrek.code,
    ]:
        if ruimte.oppervlakte >= 4:
            return Ruimtesoort.vertrek
        elif ruimte.oppervlakte >= 2:
            return Ruimtesoort.overige_ruimten

    if ruimte.detail_soort.code == Ruimtedetailsoort.keuken.code:
        return Ruimtesoort.vertrek

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.badkamer_met_toilet.code,
        Ruimtedetailsoort.badkamer.code,
        Ruimtedetailsoort.doucheruimte.code,
    ]:
        if badruimte_met_toilet(ruimte) and ruimte.oppervlakte < 0.64:
            return None
        else:
            return Ruimtesoort.vertrek

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.bijkeuken.code,
        Ruimtedetailsoort.berging.code,
        Ruimtedetailsoort.wasruimte.code,
        Ruimtedetailsoort.garage.code,
        Ruimtedetailsoort.kelder.code,
        # Ruimtedetailsoort.schuur.code # niet mogelijk want schuur en schacht zelfde code zie: https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/116 en https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/92
    ] or (
        ruimte.detail_soort.naam
        and ruimte.detail_soort.naam == Ruimtedetailsoort.schuur.naam
    ):  # zie hierboven i.v.m. limitaties schuur.code
        if ruimte.oppervlakte >= 2:
            return Ruimtesoort.overige_ruimten
        else:
            return None

    if ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
        if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap):
            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}): vaste trap gevonden. Ruimte wordt gewaardeerd als {ruimte.soort.naam}."
            )
            if (
                ruimte.soort.code == Ruimtesoort.vertrek.code
                and ruimte.oppervlakte >= 4
            ):
                return Ruimtesoort.vertrek
            elif ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimten
            else:
                return None
        elif heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.vlizotrap):
            logger.info(
                f"Ruimte {ruimte.naam} ({ruimte.id}): vlizotrap gevonden. Ruimte wordt gewaardeerd als {Ruimtesoort.overige_ruimten}."
            )
            if ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimten
            else:
                return None

        logger.info(
            f"Ruimte {ruimte.naam} ({ruimte.id}): geen trap gevonden. Ruimte wordt niet gewaardeerd binnen {Woningwaarderingstelsel.zelfstandige_woonruimten}."
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
            and verbonden_ruimte.detail_soort.code == Ruimtedetailsoort.kast.code
            and verbonden_ruimte.oppervlakte is not None
            and verbonden_ruimte.oppervlakte < 2.0
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
