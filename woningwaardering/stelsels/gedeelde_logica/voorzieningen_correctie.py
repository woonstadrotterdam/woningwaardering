"""
Module voor het automatisch toevoegen van missende voorzieningen om woningwaardering mogelijk te maken
bij incomplete of ontbrekende data.

Deze module voegt automatisch essentiële voorzieningen toe zoals:
- Toilet in toiletruimte zonder toilet
- Aanrecht in keuken zonder aanrecht
- Standaard lengte aan aanrecht zonder lengte
- Wastafel in badkamer zonder wastafel
- Douche in badkamer zonder douche of bad
"""

from loguru import logger

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    InstallatiesoortReferentiedata,
    Ruimtedetailsoort,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen


# Helper functies
def _heeft_toilet(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of een ruimte al een toilet heeft (als installatie of bouwkundig element).

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren

    Returns:
        bool: True als de ruimte een toilet heeft, anders False
    """
    # Check installaties
    if ruimte.installaties:
        toilet_installatie_types = [
            Installatiesoort.hangend_toilet,
            Installatiesoort.staand_toilet,
        ]
        if any(
            installatie in toilet_installatie_types
            for installatie in ruimte.installaties
        ):
            return True

    # Check bouwkundige elementen
    if ruimte.bouwkundige_elementen:
        toilet_bouwkundig_types = [
            Bouwkundigelementdetailsoort.closetcombinatie,
        ]
        toilet_elementen = get_bouwkundige_elementen(ruimte, *toilet_bouwkundig_types)
        if len(list(toilet_elementen)) > 0:
            return True

    return False


def _heeft_aanrecht(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of een ruimte al een aanrecht heeft.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren

    Returns:
        bool: True als de ruimte een aanrecht heeft, anders False
    """
    if not ruimte.bouwkundige_elementen:
        return False

    aanrechten = get_bouwkundige_elementen(
        ruimte, Bouwkundigelementdetailsoort.aanrecht
    )

    return len(list(aanrechten)) > 0


def _heeft_wastafel(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of een ruimte al een wastafel heeft (als installatie of bouwkundig element).

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren

    Returns:
        bool: True als de ruimte een wastafel heeft, anders False
    """
    # Check installaties
    if ruimte.installaties:
        wastafel_installatie_types = [
            Installatiesoort.wastafel,
            Installatiesoort.meerpersoonswastafel,
        ]
        if any(
            installatie in wastafel_installatie_types
            for installatie in ruimte.installaties
        ):
            return True

    # Check bouwkundige elementen
    if ruimte.bouwkundige_elementen:
        wastafel_bouwkundig_types = [
            Bouwkundigelementdetailsoort.wastafel,
        ]
        wastafel_elementen = get_bouwkundige_elementen(
            ruimte, *wastafel_bouwkundig_types
        )
        if len(list(wastafel_elementen)) > 0:
            return True

    return False


def _heeft_douche_of_bad(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of een ruimte al een douche of bad heeft.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren

    Returns:
        bool: True als de ruimte een douche of bad heeft, anders False
    """
    # Check installaties
    if ruimte.installaties:
        douche_bad_installatie_types = [
            Installatiesoort.douche,
            Installatiesoort.bad,
            Installatiesoort.bad_en_douche,
            Installatiesoort.drempelloze_inrijdouche,
        ]
        if any(
            installatie in douche_bad_installatie_types
            for installatie in ruimte.installaties
        ):
            return True

    # Check bouwkundige elementen
    if ruimte.bouwkundige_elementen:
        douche_bad_bouwkundig_types = [
            Bouwkundigelementdetailsoort.douche,
            Bouwkundigelementdetailsoort.bad,
        ]
        douche_bad_elementen = get_bouwkundige_elementen(
            ruimte, *douche_bad_bouwkundig_types
        )
        if len(list(douche_bad_elementen)) > 0:
            return True

    return False


def _corrigeer_toilet(
    ruimte: EenhedenRuimte, toilet_type: InstallatiesoortReferentiedata
) -> None:
    """
    Zorgt ervoor dat een toiletruimte een toilet heeft.

    Args:
        ruimte (EenhedenRuimte): De toiletruimte om te controleren
        toilet_type (InstallatiesoortReferentiedata): Het type toilet om toe te voegen
    """
    if _heeft_toilet(ruimte):
        return

    # Initialiseer installaties lijst als deze niet bestaat
    if ruimte.installaties is None:
        ruimte.installaties = []

    # Voeg toilet toe
    ruimte.installaties.append(toilet_type)

    logger.info(
        f"Automatisch toegevoegd: {toilet_type.naam} aan ruimte '{ruimte.naam}' ({ruimte.id}) "
        f"van type {ruimte.detail_soort.naam if ruimte.detail_soort else 'onbekend'}"
    )


def _corrigeer_aanrecht(ruimte: EenhedenRuimte, standaard_lengte: int) -> None:
    """
    Zorgt ervoor dat een keuken een aanrecht heeft.

    Args:
        ruimte (EenhedenRuimte): De keuken om te controleren
        standaard_lengte (int): Lengte van het aanrecht in mm
    """
    if _heeft_aanrecht(ruimte):
        return

    # Initialiseer bouwkundige elementen lijst als deze niet bestaat
    if ruimte.bouwkundige_elementen is None:
        ruimte.bouwkundige_elementen = []

    # Creëer nieuw aanrecht
    nieuw_aanrecht = BouwkundigElementenBouwkundigElement(
        id=f"Aanrecht_{ruimte.id}",
        naam="Aanrecht",
        detail_soort=Bouwkundigelementdetailsoort.aanrecht,
        lengte=standaard_lengte,
    )

    # Voeg aanrecht toe
    ruimte.bouwkundige_elementen.append(nieuw_aanrecht)

    logger.info(
        f"Automatisch toegevoegd: Aanrecht ({standaard_lengte}mm) aan ruimte '{ruimte.naam}' ({ruimte.id}) "
        f"van type {ruimte.detail_soort.naam if ruimte.detail_soort else 'onbekend'}"
    )


def _corrigeer_aanrecht_lengte(ruimte: EenhedenRuimte, standaard_lengte: int) -> None:
    """
    Zorgt ervoor dat aanrechten een lengte hebben.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren
        standaard_lengte (int): Standaard lengte in mm
    """
    if not ruimte.bouwkundige_elementen:
        return

    for element in ruimte.bouwkundige_elementen:
        if (
            element.detail_soort == Bouwkundigelementdetailsoort.aanrecht
            and element.lengte is None
        ):
            element.lengte = standaard_lengte

            logger.info(
                f"Automatisch toegevoegd: Lengte ({standaard_lengte}mm) aan aanrecht '{element.naam or element.id}' "
                f"in ruimte '{ruimte.naam}' ({ruimte.id})"
            )


def _corrigeer_wastafel(ruimte: EenhedenRuimte) -> None:
    """
    Zorgt ervoor dat een badkamer een wastafel heeft.

    Args:
        ruimte (EenhedenRuimte): De badkamer om te controleren
    """
    if _heeft_wastafel(ruimte):
        return

    # Initialiseer installaties lijst als deze niet bestaat
    if ruimte.installaties is None:
        ruimte.installaties = []

    # Voeg wastafel toe
    ruimte.installaties.append(Installatiesoort.wastafel)

    logger.info(
        f"Automatisch toegevoegd: Wastafel aan ruimte '{ruimte.naam}' ({ruimte.id}) "
        f"van type {ruimte.detail_soort.naam if ruimte.detail_soort else 'onbekend'}"
    )


def _corrigeer_douche(ruimte: EenhedenRuimte) -> None:
    """
    Zorgt ervoor dat een badkamer een douche heeft indien geen douche of bad aanwezig.

    Args:
        ruimte (EenhedenRuimte): De badkamer om te controleren
    """
    if _heeft_douche_of_bad(ruimte):
        return

    # Initialiseer installaties lijst als deze niet bestaat
    if ruimte.installaties is None:
        ruimte.installaties = []

    # Voeg douche toe
    ruimte.installaties.append(Installatiesoort.douche)

    logger.info(
        f"Automatisch toegevoegd: Douche aan ruimte '{ruimte.naam}' ({ruimte.id}) "
        f"van type {ruimte.detail_soort.naam if ruimte.detail_soort else 'onbekend'}"
    )


def corrigeer_afwezigheid_toilet(
    eenheid: EenhedenEenheid,
    standaard_toilet_type: InstallatiesoortReferentiedata,
) -> None:
    """
    Zorgt ervoor dat een eenheid ten minste één toilet heeft.

    - Voegt toilet toe aan toiletruimte of badkamer_met_toilet indien ontbrekend.
    - Als geen toilet gevonden, voegt toe aan badkamer (fallback).

    Args:
        eenheid (EenhedenEenheid): De eenheid om te controleren en eventueel aan te vullen
        standaard_toilet_type (InstallatiesoortReferentiedata): Het type toilet om toe te voegen
    """
    if not eenheid.ruimten:
        return

    heeft_toilet = False

    # Voeg toilet toe aan ruimten die een toilet zouden moeten hebben indien geen toilet aanwezig is
    for ruimte in eenheid.ruimten:
        if _heeft_toilet(ruimte):
            heeft_toilet = True
            continue

        if ruimte.detail_soort in [
            Ruimtedetailsoort.toiletruimte,
            Ruimtedetailsoort.badkamer_met_toilet,
        ]:
            _corrigeer_toilet(ruimte, standaard_toilet_type)
            heeft_toilet = True

    if heeft_toilet:
        return

    # Eenheid heeft geen specifieke ruimte voor een toilet, dus zoek een badkamer om het toilet aan toe te voegen
    for ruimte in eenheid.ruimten:
        if ruimte.detail_soort == Ruimtedetailsoort.badkamer:
            _corrigeer_toilet(ruimte, standaard_toilet_type)
            return


def corrigeer_afwezigheid_aanrecht(
    eenheid: EenhedenEenheid,
    standaard_aanrecht_lengte: int,
) -> None:
    """
    Zorgt ervoor dat een eenheid ten minste één aanrecht heeft.

    - Voegt aanrecht toe aan keuken, woonkamer_en_of_keuken, of
    woon_en_of_slaapkamer_en_of_keuken indien ontbrekend.
    - Als geen aanrecht gevonden, voegt toe aan woonkamer (fallback).

    Args:
        eenheid (EenhedenEenheid): De eenheid om te controleren en eventueel aan te vullen
        standaard_aanrecht_lengte (int): Lengte van het aanrecht in millimeters
    """
    if not eenheid.ruimten:
        return

    heeft_aanrecht = False

    # Voeg aanrecht toe aan ruimten die een aanrecht zouden moeten hebben indien geen aanrecht aanwezig is
    for ruimte in eenheid.ruimten:
        if _heeft_aanrecht(ruimte):
            heeft_aanrecht = True
            continue

        if ruimte.detail_soort in [
            Ruimtedetailsoort.keuken,
            Ruimtedetailsoort.woonkamer_en_of_keuken,
            Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken,
        ]:
            _corrigeer_aanrecht(ruimte, standaard_aanrecht_lengte)
            heeft_aanrecht = True

    if heeft_aanrecht:
        return

    # Eenheid heeft geen specifieke ruimte voor een aanrecht, dus zoek een woonkamer om het aanrecht aan toe te voegen
    for ruimte in eenheid.ruimten:
        if ruimte.detail_soort == Ruimtedetailsoort.woonkamer:
            _corrigeer_aanrecht(ruimte, standaard_aanrecht_lengte)
            return


# Hoofdfunctie
def corrigeer_voorzieningen_eenheid(
    eenheid: EenhedenEenheid,
    *,
    standaard_aanrecht_lengte: int = 1000,
    standaard_toilet_type: InstallatiesoortReferentiedata = Installatiesoort.staand_toilet,
) -> None:
    """
    Voegt automatisch missende essentiële voorzieningen toe aan een eenheid.

    Args:
        eenheid (EenhedenEenheid): De eenheid om te controleren en aan te vullen
        standaard_aanrecht_lengte (int): Standaard lengte in mm voor aanrechten zonder lengte
        standaard_toilet_type (InstallatiesoortReferentiedata): Type toilet om toe te voegen in toiletruimtes
    """

    if not eenheid.ruimten:
        logger.debug(
            f"Eenheid {eenheid.id} heeft geen ruimten, overslaan auto-toevoegen voorzieningen"
        )
        return

    for ruimte in eenheid.ruimten:
        if not ruimte.detail_soort:
            continue

        # Zorg voor wastafel en douche in badkamer
        if ruimte.detail_soort in [
            Ruimtedetailsoort.badkamer,
            Ruimtedetailsoort.badkamer_met_toilet,
        ]:
            _corrigeer_wastafel(ruimte)
            _corrigeer_douche(ruimte)

        # Zorg voor aanrecht lengte.
        # Geen check op ruimte detailsoort omdat een aanrecht in verschillende soorten ruimten kan voorkomen.
        _corrigeer_aanrecht_lengte(ruimte, standaard_aanrecht_lengte)

    corrigeer_afwezigheid_toilet(eenheid, standaard_toilet_type)
    corrigeer_afwezigheid_aanrecht(eenheid, standaard_aanrecht_lengte)
