from loguru import logger

from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)
from woningwaardering.vera.utils import badruimte_met_toilet, heeft_bouwkundig_element


def classificeer_ruimte(ruimte: EenhedenRuimte) -> Ruimtesoort | None:
    """
    Classificeert de ruimte volgens het Woningwaarderingstelsel voor zelfstandige woonruimten.

    Args:
        ruimte (EenhedenRuimte): De ruimte die geclassificeerd moet worden.

    Returns:
        Ruimtesoort | None: De classificatie van de ruimte volgens het Woningwaarderingstelsel.
            Geeft `None` terug als de ruimte niet kan worden gewaardeerd.

    Raises:
        TypeError: Als de ruimte ontbrekende informatie heeft, zoals oppervlakte, soort of detailsoort.
    """
    if ruimte.oppervlakte is None:
        error_msg = f"ruimte {ruimte.id} heeft geen oppervlakte en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        raise TypeError(error_msg)

    if ruimte.soort is None or ruimte.soort.code is None:
        error_msg = f"ruimte {ruimte.id} heeft geen soort en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        raise TypeError(error_msg)

    if ruimte.detail_soort is None:
        error_msg = f"ruimte {ruimte.id} heeft geen detailsoort en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        raise TypeError(error_msg)

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
            return Ruimtesoort.overige_ruimtes

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
        Ruimtedetailsoort.parkeerplaats.code,
    ]:
        if ruimte.oppervlakte >= 2:
            return Ruimtesoort.overige_ruimtes
        else:
            return None

    if ruimte.detail_soort.code == Ruimtedetailsoort.zolder.code:
        if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.trap.code):
            logger.debug(
                f"Vaste trap gevonden in {ruimte.naam} ({ruimte.id}): wordt gewaardeerd als {ruimte.soort.naam}"
            )
            if (
                ruimte.soort.code == Ruimtesoort.vertrek.code
                and ruimte.oppervlakte >= 4
            ):
                return Ruimtesoort.vertrek
            elif ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimtes
            else:
                return None
        elif heeft_bouwkundig_element(
            ruimte, Bouwkundigelementdetailsoort.vlizotrap.code
        ):
            logger.debug(
                f"Vlizo trap gevonden in {ruimte.naam} ({ruimte.id}): wordt gewaardeerd als {Ruimtesoort.overige_ruimtes}"
            )
            if ruimte.oppervlakte >= 2:
                return Ruimtesoort.overige_ruimtes
            else:
                return None

        logger.debug(
            f"Geen trap gevonden in {ruimte.naam} ({ruimte.id}): wordt niet gewaardeerd binnen {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        )
    return None


def voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte: EenhedenRuimte) -> str:
    """
    Deze functie voegt de oppervlakte van kasten toe aan een ruimte en retourneert de naam van de ruimte inclusief het aantal kasten.

    Args:
        ruimte (EenhedenRuimte): De ruimte waar kasten aan toegevoegd moeten worden.

    Returns:
        str: De naam van de ruimte inclusief het aantal toegevoegde kasten.

    Raises:
        TypeError: Als de ruimte ontbrekende informatie heeft, zoals oppervlakte of detailsoort.
    """
    if ruimte.detail_soort is None or ruimte.detail_soort.code is None:
        error_msg = f"ruimte {ruimte.id} heeft geen detailsoort en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        raise TypeError(error_msg)

    if ruimte.oppervlakte is None:
        error_msg = f"ruimte {ruimte.id} heeft geen oppervlakte en kan daardoor niet gewaardeerd worden voor {Woningwaarderingstelsel.zelfstandige_woonruimten}"
        raise TypeError(error_msg)

    criterium_naam = ruimte.naam or "Naamloze ruimte"

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

            logger.debug(
                f"De netto oppervlakte van {aantal_ruimte_kasten} verbonden {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'} is opgeteld bij {ruimte.naam}"
            )

            criterium_naam = f"{ruimte.naam} + {aantal_ruimte_kasten} {aantal_ruimte_kasten == 1 and 'kast' or 'kasten'}"
    return criterium_naam
