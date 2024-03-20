from decimal import ROUND_HALF_UP, BasicContext, Decimal, setcontext
from woningwaardering.vera.referentiedata.soort import (
    Meeteenheid,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Ruimtesoort,
    Woningwaarderingstelselgroep,
)

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

# Set context for all calculations to avoid rounding errors
# See https://docs.python.org/3/library/decimal.html#rounding
setcontext(BasicContext)


def bereken_vertrekken(
    eenheid: EenhedenEenheid,
    woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> WoningwaarderingResultatenWoningwaarderingGroep:
    woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
        criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
            stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
        )
    )

    woningwaardering_groep.woningwaarderingen = []

    for ruimte in eenheid.ruimten or []:
        if ruimte.soort == Ruimtesoort.vertrek and ruimte.detail_soort is not None:
            if ruimte.detail_soort.code not in [
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
            ]:
                print(
                    f"{ruimte.detail_soort.naam} {ruimte.detail_soort.code} komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
                )
                continue

            if ruimte.oppervlakte is not None and ruimte.oppervlakte < 4:
                print(
                    f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 4 vierkante meter"
                )
                continue

            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                    # stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
                    naam=ruimte.naam,
                )
            )

            if ruimte.oppervlakte is not None:
                woningwaardering.aantal = float(
                    Decimal(ruimte.oppervlakte).quantize(Decimal("0.01"), ROUND_HALF_UP)
                )

            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

    punten = Decimal(
        sum(
            Decimal(woningwaardering.aantal)
            for woningwaardering in woningwaardering_groep.woningwaarderingen or []
            if woningwaardering.aantal is not None
        )
    ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("1")

    woningwaardering_groep.punten = float(punten)
    return woningwaardering_groep


def bereken_overige_ruimten(
    eenheid: EenhedenEenheid,
    woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> WoningwaarderingResultatenWoningwaarderingGroep:
    woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
        criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
            stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
            stelselgroep=Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
        ),
    )

    woningwaardering_groep.woningwaarderingen = []

    for ruimte in eenheid.ruimten or []:
        if (
            ruimte.soort == Ruimtesoort.overige_ruimtes
            and ruimte.detail_soort is not None
        ):
            if ruimte.detail_soort.code not in [
                Ruimtedetailsoort.bijkeuken.code,
                Ruimtedetailsoort.berging.code,
                Ruimtedetailsoort.wasruimte.code,
                Ruimtedetailsoort.garage.code,
                Ruimtedetailsoort.zolder.code,
                Ruimtedetailsoort.kelder.code,
                Ruimtedetailsoort.parkeerplaats.code,
                # Deze vertrekken kunnen als overige ruimte tellen
                # wanneer ze niet aan bepaalde voorwaarden voldoen:
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
            ]:
                print(
                    f"{ruimte.detail_soort.naam} {ruimte.detail_soort.code} komt niet in aanmerking voor een puntenwaardering onder {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam}"
                )
                continue

            if ruimte.oppervlakte is not None and ruimte.oppervlakte < 2:
                print(
                    f"{ruimte.naam} {ruimte.detail_soort.code} is kleiner dan 2 vierkante meter"
                )
                continue

            woningwaardering = WoningwaarderingResultatenWoningwaardering()

            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                    # stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
                    naam=ruimte.naam,
                )
            )

            if ruimte.oppervlakte is not None:
                woningwaardering.aantal = float(
                    Decimal(ruimte.oppervlakte).quantize(Decimal("0.01"), ROUND_HALF_UP)
                )

            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

    punten = Decimal(
        sum(
            Decimal(woningwaardering.aantal)
            for woningwaardering in (woningwaardering_groep.woningwaarderingen or [])
            if woningwaardering.aantal is not None
        )
    ).quantize(Decimal("1"), ROUND_HALF_UP) * Decimal("0.75")

    woningwaardering_groep.punten = float(punten)
    return woningwaardering_groep


f = open("./woningwaardering/41164000002.json", "r+")

eenheid = EenhedenEenheid.model_validate_json(f.read())

woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()

woningwaardering_resultaat.groepen = []

woningwaardering_resultaat.groepen.append(
    bereken_vertrekken(eenheid, woningwaardering_resultaat)
)
woningwaardering_resultaat.groepen.append(
    bereken_overige_ruimten(eenheid, woningwaardering_resultaat)
)

woningwaardering_resultaat.punten = sum(
    woningwaardering_groep.punten
    for woningwaardering_groep in woningwaardering_resultaat.groepen or []
    if woningwaardering_groep.punten is not None
)

print(
    woningwaardering_resultaat.model_dump_json(
        by_alias=True, exclude_unset=True, indent=2
    )
)
