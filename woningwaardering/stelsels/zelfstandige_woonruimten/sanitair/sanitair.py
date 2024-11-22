import warnings
from collections import Counter
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    _bouwkundige_elementen_naar_installaties,
    _waardeer_baden_en_douches,
    _waardeer_toiletten,
    _waardeer_wastafels,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
    Ruimtedetailsoort,
    Voorzieningsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Sanitair(Stelselgroep):
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
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        for ruimte in ruimten:
            woningwaardering_groep.woningwaarderingen.extend(
                Sanitair.genereer_woningwaarderingen(ruimte, self.stelselgroep)
            )

        totaal_punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )
        woningwaardering_groep.punten = float(totaal_punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte,
        stelselgroep: Woningwaarderingstelselgroep,
        stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if ruimte.detail_soort is None:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort."
            )
            return

        _bouwkundige_elementen_naar_installaties(ruimte)
        zelfstandige_woonruimte = (
            stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten
        )

        installaties = Counter(
            [installatie for installatie in ruimte.installaties or []]
        )

        yield from _waardeer_toiletten(ruimte)

        punten_sanitair = {
            Voorzieningsoort.wastafel.value: 1.0,
            Voorzieningsoort.meerpersoonswastafel.value: 1.5,
            Voorzieningsoort.douche.value: 4.0 if zelfstandige_woonruimte else 3.0,
            Voorzieningsoort.bad.value: 6.0 if zelfstandige_woonruimte else 5.0,
            Voorzieningsoort.bad_en_douche.value: 7.0
            if zelfstandige_woonruimte
            else 6.0,
        }

        yield from _waardeer_wastafels(ruimte, stelsel)

        baden_en_douches_waarderingen = list(
            _waardeer_baden_en_douches(ruimte, stelsel)
        )
        totaal_punten_bad_en_douche = Decimal(
            sum(
                woningwaardering.punten
                for woningwaardering in baden_en_douches_waarderingen
                if woningwaardering.punten is not None
            )
        )
        yield from baden_en_douches_waarderingen

        punten_voorzieningen = {
            Voorzieningsoort.bubbelfunctie_van_het_bad.value: 1.5,
            Voorzieningsoort.douchewand.value: 1.25,
            Voorzieningsoort.handdoekenradiator.value: 0.75,
            Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.value: 1,
            Voorzieningsoort.kastruimte.value: 0.75,
            Voorzieningsoort.stopcontact_bij_wastafel.value: 0.25,
            Voorzieningsoort.eenhandsmengkraan.value: 0.25,
            Voorzieningsoort.thermostatische_mengkraan.value: 0.5,
        }

        totaal_punten_voorzieningen = Decimal("0")

        totaal_aantal_wastafels = (
            installaties[Voorzieningsoort.wastafel.value]
            + installaties[Voorzieningsoort.meerpersoonswastafel.value]
        )

        if ruimte.detail_soort in [
            Ruimtedetailsoort.badkamer.value,
            Ruimtedetailsoort.badkamer_met_toilet.value,
            Ruimtedetailsoort.doucheruimte.value,
        ]:
            # Geen waardering voor extra voorzieningen indien er geen wastafel in de ruimte is
            if totaal_aantal_wastafels == 0:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen wastafel aanwezig in {ruimte.detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
                )
            # Geen waardering voor extra voorzieningen indien er geen douche of bad in de ruimte is
            elif totaal_punten_bad_en_douche == 0:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen bad of douche aanwezig in {ruimte.detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
                )
            elif totaal_aantal_wastafels > 0 and totaal_punten_bad_en_douche > 0:
                for installatie, aantal in installaties.items():
                    if installatie not in (
                        set(punten_voorzieningen)
                        | set(punten_sanitair)
                        | {
                            Voorzieningsoort.hangend_toilet.value,
                            Voorzieningsoort.staand_toilet.value,
                        }
                    ):
                        logger.info(
                            f"Installatie {installatie.naam} komt niet in aanmerking voor waardering"
                        )
                        continue

                    if installatie in punten_voorzieningen:
                        punten = utils.rond_af(
                            aantal * punten_voorzieningen[installatie], decimalen=2
                        )

                        totaal_punten_voorzieningen += punten

                        yield (
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - Voorzieningen: {installatie.naam}",
                                ),
                                punten=float(punten),
                                aantal=aantal,
                            )
                        )

                        if installatie == Voorzieningsoort.kastruimte.value:
                            maximum = Decimal("0.75")
                            correctie = min(maximum - punten, Decimal("0"))
                            if correctie < 0:
                                totaal_punten_voorzieningen += correctie

                                yield WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Voorzieningen: Max {maximum} punten voor {installatie.naam}"
                                    ),
                                    punten=float(correctie),
                                )

                        if (
                            installatie
                            == Voorzieningsoort.stopcontact_bij_wastafel.value
                        ):
                            correctie_aantal = (
                                totaal_aantal_wastafels * Decimal("2") - aantal
                            )
                            correctie = min(
                                correctie_aantal
                                * Decimal(punten_voorzieningen[installatie]),
                                Decimal("0"),
                            )
                            if correctie < 0:
                                totaal_punten_voorzieningen += correctie

                                yield WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Voorzieningen: Max 2 stopcontacten per wastafel"
                                    ),
                                    punten=float(correctie),
                                )

        maximering = min(
            utils.rond_af(totaal_punten_bad_en_douche - totaal_punten_voorzieningen, 2),
            Decimal("0"),
        )

        if maximering < 0:
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam} - Voorzieningen: Max verdubbeling punten bad en douche"
                ),
                punten=maximering,
            )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        instance=Sanitair(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )
