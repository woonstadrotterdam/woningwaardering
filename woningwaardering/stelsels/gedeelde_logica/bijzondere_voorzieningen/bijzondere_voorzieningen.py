from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica.gemeenschappelijke_parkeerruimten import (
    wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten,
)
from woningwaardering.stelsels.utils import gedeeld_met_adressen
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Installatiesoort,
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import aantal_bouwkundige_elementen


def waardeer_bijzondere_voorzieningen(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroepen_zonder_opslag: list[WoningwaarderingstelselgroepReferentiedata],
    stelsel: WoningwaarderingstelselReferentiedata,
    uitgesloten_zorgwoning_grondslag_criterium_ids: list[str] | None = None,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat | None
    ) = None,
) -> list[WaarderingBuilder]:
    """Genereert de woningwaarderingen voor bijzondere voorzieningen.

    Args:
        peildatum (date): De peildatum.
        eenheid (EenhedenEenheid): De eenheid.
        stelselgroepen_zonder_opslag (list[WoningwaarderingstelselgroepReferentiedata]): De stelselgroepen die niet moeten worden opgehoogd met zorgwoning opslag.
        stelsel (WoningwaarderingstelselReferentiedata): Het woningwaarderingsstelsel.
        uitgesloten_zorgwoning_grondslag_criterium_ids (list[str] | None): De criterium-id's die niet meetellen in de zorgwoninggrondslag.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Het woningwaardering resultaat.

    Returns:
        list[WaarderingBuilder]: De aangemaakte woningwaarderingen.
    """
    woningwaarderingen = [
        _opslag_zorgwoning(
            peildatum,
            eenheid,
            stelselgroepen_zonder_opslag,
            stelsel,
            uitgesloten_zorgwoning_grondslag_criterium_ids,
            waarderingsgroep_builder,
            woningwaardering_resultaat,
        ),
        _aanbelfunctie_met_video_en_audioverbinding(eenheid, waarderingsgroep_builder),
    ]

    return [
        waardering for waardering in woningwaarderingen if waardering is not None
    ] + _prive_laadpaal(eenheid, stelsel, waarderingsgroep_builder)


def _opslag_zorgwoning(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroepen_zonder_opslag: list[WoningwaarderingstelselgroepReferentiedata],
    stelsel: WoningwaarderingstelselReferentiedata,
    uitgesloten_zorgwoning_grondslag_criterium_ids: list[str] | None,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    woningwaardering_resultaat: (
        WoningwaarderingResultatenWoningwaarderingResultaat | None
    ) = None,
) -> WaarderingBuilder | None:
    """Als sprake is van een zorgwoning, dan volgt er een opslag van 35% op het puntentotaal van
    de rubrieken 1 tot en met 11 (of 1 tot en met 10 voor onzelfstandige woonruimten) van het
    woningwaarderingsstelsel. Deze opslag wordt gedaan in de rubriek Bijzondere voorzieningen.

    Args:
        peildatum (date): De peildatum voor de berekening.
        eenheid (EenhedenEenheid): De eenheid die wordt gewaardeerd.
        stelselgroepen_zonder_opslag (list[WoningwaarderingstelselgroepReferentiedata]): Lijst van stelselgroepen die niet worden meegenomen in de opslag.
        stelsel (WoningwaarderingstelselReferentiedata): Het type woningwaarderingsstelsel.
        uitgesloten_zorgwoning_grondslag_criterium_ids (list[str] | None): De criterium-id's die niet meetellen in de zorgwoninggrondslag.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.
        woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None): Het bestaande waarderingsresultaat, indien aanwezig.

    Returns:
        WaarderingBuilder | None: De woningwaardering met 35% opslag als het een zorgwoning betreft, anders None.

    Raises:
        ValueError: Als het stelsel niet gelijk is aan zelfstandige woonruimten of onzelfstandige woonruimten.
    """
    if eenheid.doelgroep is None or (
        eenheid.doelgroep and eenheid.doelgroep != Doelgroep.zorg
    ):
        logger.debug(
            f"Eenheid ({eenheid.id}) is geen zorgwoning en krijgt dus geen zorgwoningopslag"
        )
        return None

    if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
        logger.warning(
            "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
        )
        if stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten:
            from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                ZelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = ZelfstandigeWoonruimten(
                peildatum=peildatum
            ).waardeer(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen,
            )

        elif stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten:
            from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
                OnzelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = OnzelfstandigeWoonruimten(
                peildatum=peildatum
            ).waardeer(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.bijzondere_voorzieningen,
            )
        else:
            raise ValueError(
                f"Invalid stelsel {stelsel}. Bijzondere voorzieningen zijn alleen gedefinieerd voor {Woningwaarderingstelsel.zelfstandige_woonruimten.naam} en {Woningwaarderingstelsel.onzelfstandige_woonruimten.naam}"
            )

    uitgesloten_criterium_ids = set(
        uitgesloten_zorgwoning_grondslag_criterium_ids or []
    )
    puntentotaal = sum(
        Decimal(str(groep.punten or "0")) or Decimal()
        for groep in woningwaardering_resultaat.groepen or []
        if (
            groep.punten
            and groep.criterium_groep
            and groep.criterium_groep.stelselgroep not in stelselgroepen_zonder_opslag
        )
    )

    if uitgesloten_criterium_ids:
        # Voor zelfstandige zorgwoningen telt rubriek 11.2 niet mee in de 35%-grondslag
        # (§2.12 voetnoot 13), dus trekken we die onderliggende criteria hier af.
        puntentotaal -= sum(
            (
                Decimal(str(waardering.punten))
                for groep in woningwaardering_resultaat.groepen or []
                for waardering in groep.woningwaarderingen or []
                if (
                    waardering.punten is not None
                    and waardering.criterium is not None
                    and waardering.criterium.id in uitgesloten_criterium_ids
                )
            ),
            start=Decimal("0"),
        )

    grondslag_label = (
        "1 tot en met 11.1" if uitgesloten_criterium_ids else "1 tot en met 11"
    )
    logger.info(
        f"Eenheid ({eenheid.id}): Puntentotaal van de rubrieken {grondslag_label} van het woningwaarderingsstelsel is {puntentotaal}"
    )

    verhoging = utils.rond_af_op_kwart(puntentotaal * Decimal("0.35"))

    logger.info(
        f"Eenheid ({eenheid.id}) is een zorgwoning: {verhoging} punten voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return waarderingsgroep_builder.met_onderliggend(
        id="zorgwoning_puntenverhoging",
        naam="Zorgwoning 35% puntenverhoging",
        punten=float(verhoging),
    )


def _aanbelfunctie_met_video_en_audioverbinding(
    eenheid: EenhedenEenheid,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> WaarderingBuilder | None:
    """Een aanbelfunctie met video- en audioverbinding waarbij de voordeur
    automatisch kan worden geopend vanuit de woning wordt gewaardeerd
    met 0,25 punt.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de opslag berekend wordt.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.

    Returns:
        WaarderingBuilder | None: De woningwaardering met 0,25 punt
        als de eenheid een aanbelfunctie met video en audio heeft, anders None.
    """
    if not any(
        installatie == Installatiesoort.aanbelfunctie_met_video_en_audioverbinding
        for ruimte in (eenheid.ruimten or [])
        for installatie in (ruimte.installaties or [])
    ):
        logger.debug(
            f"Eenheid ({eenheid.id}) heeft geen aanbelfunctie met video en audioverbinding"
        )
        return None

    logger.info(
        f"Eenheid ({eenheid.id}) heeft een aanbelfunctie met video en audioverbinding: 0.25 punt voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
    )

    return waarderingsgroep_builder.met_onderliggend(
        id="aanbelfunctie_met_video_en_audioverbinding",
        naam="Aanbelfunctie met video- en audioverbinding",
        punten=0.25,
    )


def _prive_laadpaal(
    eenheid: EenhedenEenheid,
    stelsel: WoningwaarderingstelselReferentiedata,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> list[WaarderingBuilder]:
    """Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik
    door de bewoners wordt gewaardeerd met 2 punten.

    Bij onzelfstandige woonruimten worden die punten gedeeld door het aantal
    onzelfstandige woonruimten dat toegang heeft (2.1.4 / 2.1.5). Laadpalen worden
    daarom per deler gegroepeerd, zodat elke groep onder een eigen
    gedeeld-met-criterium komt te hangen.

    Args:
        eenheid (EenhedenEenheid): De eenheid waarvoor de waardering berekend wordt.
        stelsel (WoningwaarderingstelselReferentiedata): Het woningwaarderingsstelsel.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.
    Returns:
        list[WaarderingBuilder]: Per deler een woningwaardering met de punten voor
        de laadpalen die met dat aantal onzelfstandige woonruimten gedeeld worden.
    """
    aantal_laadpalen_per_deler: defaultdict[int, int] = defaultdict(int)

    for ruimte in eenheid.ruimten or []:
        if gedeeld_met_adressen(ruimte):
            continue

        # 2.12.3 ONZ: "Als een gemeenschappelijke parkeerruimte een laadpaal heeft,
        # wordt voor de berekeningsmethode aangesloten bij rubriek 10." Omdat deze
        # package een specifieke parkeer-detailsoort altijd in rubriek 10 waardeert,
        # ook wanneer die privé is (zie 2.8.3 en 2.10.2), is het criterium hier niet
        # of de parkeerplek een "gemeenschappelijke parkeerruimte" is in de zin van
        # 2.10.2, maar of rubriek 10 de punten daadwerkelijk toekent. Rubriek 10 kent
        # de laadpaalpunten immers zelf toe (2.10.5); zonder deze uitzondering zou
        # dezelfde laadpaal twee keer punten opleveren. Krijgt de parkeerplek daar
        # niets (bijv. een carport < 12 m², 2.10.3), dan geldt de algemene regel van
        # 2.12.3 en houdt de laadpaal hier zijn 2 punten.
        if (
            stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten
            and wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(ruimte)
        ):
            continue

        aantal_laadpalen_in_ruimte = aantal_bouwkundige_elementen(
            ruimte, Bouwkundigelementdetailsoort.laadpaal
        )
        if aantal_laadpalen_in_ruimte == 0:
            continue

        deler = 1
        if stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten:
            deler = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1

        aantal_laadpalen_per_deler[deler] += aantal_laadpalen_in_ruimte

    if not aantal_laadpalen_per_deler:
        logger.debug(f"Eenheid ({eenheid.id}) heeft geen privé laadpaal")
        return []

    waarderingen = []

    for deler, aantal_laadpalen in sorted(aantal_laadpalen_per_deler.items()):
        punten_afgerond = utils.rond_af(
            Decimal(aantal_laadpalen) * Decimal("2") / Decimal(deler), decimalen=2
        )

        logger.info(
            f"Eenheid ({eenheid.id}) heeft {aantal_laadpalen} {'laadpaal' if aantal_laadpalen == 1 else 'laadpalen'} gedeeld met {deler} {'onzelfstandige woonruimte' if deler == 1 else 'onzelfstandige woonruimten'}: {punten_afgerond} punten voor {Woningwaarderingstelselgroep.bijzondere_voorzieningen.naam}"
        )

        gedeeld_met_laag = waarderingsgroep_builder.gedeeld_met(
            aantal_onzelfstandige_woonruimten=deler,
        )

        waarderingen.append(
            gedeeld_met_laag.met_onderliggend(
                id="laadpalen",
                naam="Laadpalen",
                meeteenheid=Meeteenheid.stuks,
                aantal=aantal_laadpalen,
                punten=float(punten_afgerond),
            )
        )

    return waarderingen
