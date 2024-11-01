import warnings
from collections import Counter, namedtuple
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.voorzieningsoort import Voorzieningsoort
from woningwaardering.vera.utils import get_bouwkundige_elementen


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
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
                stelselgroep=Woningwaarderingstelselgroep.sanitair.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []
        woningwaarderingen_voor_gedeeld = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden < 2
        ]
        # * tot een maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer.
        # Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt dit maximum niet voor maximaal één ruimte.
        # Dat betekent dat er voor adressen met acht of meer onzelfstandige woonruimten maximaal één ruimte mag zijn,
        # naast de badkamer, met meer dan één wastafel die voor waardering in aanmerking kom
        MaxCount = namedtuple("MaxCount", ["aantal_wastafels", "ruimte"])

        # Initialize with zero counts and no rooms
        max_wastafels = MaxCount(0, None)
        max_meerpersoonswastafels = MaxCount(0, None)

        for ruimte in ruimten:
            woningwaarderingen = list(
                Sanitair.genereer_woningwaarderingen(ruimte, self.stelselgroep)
            )
            # zoek het maximum aantal wastafels in een ruimte m.u.v. badkamer
            if ruimte.detail_soort not in [
                Ruimtedetailsoort.badkamer.value,
                Ruimtedetailsoort.badkamer_met_toilet.value,
                Ruimtedetailsoort.doucheruimte.value,
            ]:
                aantal_wastafels = sum(
                    [
                        woningwaardering.aantal
                        for woningwaardering in woningwaarderingen
                        if f"{ruimte.naam} - {Voorzieningsoort.wastafel.naam}"
                        in woningwaardering.criterium.naam
                        and Voorzieningsoort.meerpersoonswastafel.naam
                        not in woningwaardering.criterium.naam
                    ]
                )
                if aantal_wastafels > max_wastafels.aantal_wastafels:
                    max_wastafels = MaxCount(aantal_wastafels, ruimte)

                aantal_meerpersoonswastafels = sum(
                    [
                        woningwaardering.aantal
                        for woningwaardering in woningwaarderingen
                        if f"{ruimte.naam} - {Voorzieningsoort.meerpersoonswastafel.naam}"
                        in woningwaardering.criterium.naam
                    ]
                )
                if (
                    aantal_meerpersoonswastafels
                    > max_meerpersoonswastafels.aantal_wastafels
                ):
                    max_meerpersoonswastafels = MaxCount(
                        aantal_meerpersoonswastafels, ruimte
                    )
            woningwaarderingen_voor_gedeeld.append((ruimte, woningwaarderingen))

        # pas maximering toe voor wastafels en meerpersoonswastafels m.u.v. één ruimte,
        # de ruimte met de meeste wastafels/meerpersoonswastafels.
        for ruimte, woningwaarderingen in woningwaarderingen_voor_gedeeld:
            if max_wastafels.ruimte != ruimte:
                for woningwaardering in woningwaarderingen:
                    if (
                        f"{ruimte.naam} - {Voorzieningsoort.wastafel.naam}"
                        in woningwaardering.criterium.naam
                        and Voorzieningsoort.meerpersoonswastafel.naam
                        not in woningwaardering.criterium.naam
                        and woningwaardering.aantal > 1
                    ):
                        woningwaarderingen_voor_gedeeld.append(
                            (
                                ruimte,
                                WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Max 1 punt voor {Voorzieningsoort.wastafel.naam}",
                                    ),
                                    punten=utils.rond_af(
                                        1 - woningwaardering.aantal * 1,
                                        decimalen=2,
                                    ),
                                ),
                            )
                        )
            if max_meerpersoonswastafels.ruimte != ruimte:
                for woningwaardering in woningwaarderingen:
                    if (
                        f"{ruimte.naam} - {Voorzieningsoort.meerpersoonswastafel.naam}"
                        in woningwaardering.criterium.naam
                        and woningwaardering.aantal > 1
                    ):
                        woningwaarderingen_voor_gedeeld.append(
                            (
                                ruimte,
                                WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Max 1,5 punt voor {Voorzieningsoort.meerpersoonswastafel.naam}",
                                    ),
                                    punten=utils.rond_af(
                                        1.5 - woningwaardering.aantal * 1.5,
                                        decimalen=2,
                                    ),
                                ),
                            )
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
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.sanitair.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte,
        stelselgroep: Woningwaarderingstelselgroep,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if ruimte.detail_soort is None:
            warnings.warn(f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen detailsoort.")
            return

        ruimte.installaties = ruimte.installaties or []

        # Backwards compatibiliteit voor bouwkundige elementen
        for mapping in {
            Bouwkundigelementdetailsoort.wastafel: Voorzieningsoort.wastafel,
            Bouwkundigelementdetailsoort.douche: Voorzieningsoort.douche,
            Bouwkundigelementdetailsoort.bad: Voorzieningsoort.bad,
            Bouwkundigelementdetailsoort.kast: Voorzieningsoort.kastruimte,
            Bouwkundigelementdetailsoort.closetcombinatie: Voorzieningsoort.staand_toilet,
        }.items():
            bouwkundige_elementen = list(get_bouwkundige_elementen(ruimte, mapping[0]))
            if bouwkundige_elementen:
                warnings.warn(
                    f"Ruimte {ruimte.naam} ({ruimte.id}) heeft een {mapping[0].naam} als bouwkundig element. Voor een correcte waardering dient dit als installatie in de ruimte gespecificeerd te worden."
                )
                logger.info(
                    f"Ruimte {ruimte.naam} ({ruimte.id}): {mapping[0].naam} wordt als {mapping[1].naam} toegevoegd aan installaties"
                )
                ruimte.installaties.extend(
                    [mapping[1].value for _ in bouwkundige_elementen]
                )

        installaties = Counter([installatie for installatie in ruimte.installaties])

        mapping_toilet = {
            Ruimtedetailsoort.toiletruimte.value: {
                Voorzieningsoort.hangend_toilet.value: 3.75,
                Voorzieningsoort.staand_toilet.value: 3.0,
            },
            Ruimtedetailsoort.badkamer.value: {
                Voorzieningsoort.hangend_toilet.value: 2.75,
                Voorzieningsoort.staand_toilet.value: 2.0,
            },
            Ruimtedetailsoort.badkamer_met_toilet.value: {
                Voorzieningsoort.hangend_toilet.value: 2.75,
                Voorzieningsoort.staand_toilet.value: 2.0,
            },
        }

        # Toiletten buiten toiletruimten en badkamers komen niet in aanmerking voor waardering.
        if ruimte.detail_soort in [
            Ruimtedetailsoort.toiletruimte.value,
            Ruimtedetailsoort.badkamer.value,
            Ruimtedetailsoort.badkamer_met_toilet.value,
            Ruimtedetailsoort.doucheruimte.value,
        ]:
            for toiletsoort in [
                Voorzieningsoort.hangend_toilet.value,
                Voorzieningsoort.staand_toilet.value,
            ]:
                aantal_toiletten = installaties[toiletsoort]

                if aantal_toiletten > 0:
                    yield (
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - {toiletsoort.naam}",
                            ),
                            punten=float(
                                utils.rond_af(
                                    mapping_toilet[ruimte.detail_soort][toiletsoort]
                                    * aantal_toiletten,
                                    decimalen=2,
                                )
                            ),
                            aantal=aantal_toiletten,
                        )
                    )

        punten_sanitair = {
            Voorzieningsoort.wastafel.value: 1.0,
            Voorzieningsoort.meerpersoonswastafel.value: 1.5,
            Voorzieningsoort.douche.value: 3.0,
            Voorzieningsoort.bad.value: 5.0,
            Voorzieningsoort.bad_en_douche.value: 6.0,
        }

        totaal_aantal_wastafels = 0

        for wastafelsoort in [
            Voorzieningsoort.wastafel,
            Voorzieningsoort.meerpersoonswastafel,
        ]:
            aantal_wastafels = installaties[wastafelsoort.value]

            # Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 m,
            # voldoet dus niet aan de eis van 1 m en wordt daarom niet als aanrecht gewaardeerd,
            # maar als wastafel.
            aantal_spoelbakken = 0
            if (
                wastafelsoort == Voorzieningsoort.wastafel
                and ruimte.detail_soort.code
                in [
                    Ruimtedetailsoort.keuken.code,
                    Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]
            ):
                for element in ruimte.bouwkundige_elementen or []:
                    if (
                        element.detail_soort
                        and element.detail_soort.code
                        == Bouwkundigelementdetailsoort.aanrecht.code
                    ):
                        if element.lengte is not None and element.lengte < 1000:
                            logger.info(
                                f"Ruimte {ruimte.naam} ({ruimte.id}): aanrecht < 1m wordt als wastafel gewaardeerd."
                            )
                            yield WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - {wastafelsoort.naam} (spoelbak in aanrecht < 1m)"
                                ),
                                punten=float(punten_sanitair[wastafelsoort.value]),
                                aantal=1,
                            )
                            aantal_spoelbakken += 1

            totaal_aantal_wastafels += aantal_wastafels

            punten_per_wastafel = Decimal(str(punten_sanitair[wastafelsoort.value]))

            punten_voor_wastafels = utils.rond_af(
                (aantal_wastafels + aantal_spoelbakken) * punten_per_wastafel,
                decimalen=2,
            )

            if aantal_wastafels > 0:
                yield (
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam} - {wastafelsoort.naam}"
                        ),
                        punten=float(
                            utils.rond_af(
                                aantal_wastafels * punten_per_wastafel,
                                decimalen=2,
                            )
                        ),
                        aantal=aantal_wastafels,
                    )
                )

                # Wastafels worden gewaardeerd tot een maximum van 1 punt,
                # meerpersoonswastafels tot een maximum van 1,5 punt,
                # per vertrek of overige ruimte, m.u.v. de badkamer.
                if (
                    punten_voor_wastafels > punten_per_wastafel
                    and ruimte.detail_soort
                    not in [
                        Ruimtedetailsoort.badkamer.value,
                        Ruimtedetailsoort.badkamer_met_toilet.value,
                        Ruimtedetailsoort.doucheruimte.value,
                    ]
                ):
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}): {punten_voor_wastafels} punten voor {wastafelsoort.naam} in {ruimte.detail_soort.naam}. Correctie wordt toegepast ivm maximaal {punten_per_wastafel} punt."
                    )
                    yield (
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - Max {punten_per_wastafel} punt voor {wastafelsoort.naam}",
                            ),
                            punten=utils.rond_af(
                                punten_per_wastafel - punten_voor_wastafels,
                                decimalen=2,
                            ),
                        )
                    )

        totaal_punten_bad_en_douche = Decimal("0")

        aantal_douches = installaties[Voorzieningsoort.douche.value]
        aantal_baden = installaties[Voorzieningsoort.bad.value]

        aantal_bad_en_douches = min(aantal_douches, aantal_baden)

        if aantal_bad_en_douches > 0:
            punten = utils.rond_af(
                aantal_bad_en_douches
                * punten_sanitair[Voorzieningsoort.bad_en_douche.value],
                decimalen=2,
            )

            totaal_punten_bad_en_douche += punten

            yield (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {Voorzieningsoort.bad_en_douche.naam}"
                    ),
                    punten=float(punten),
                    aantal=aantal_bad_en_douches,
                )
            )

        for voorzieningsoort in [
            Voorzieningsoort.bad,
            Voorzieningsoort.douche,
        ]:
            aantal = installaties[voorzieningsoort.value] - aantal_bad_en_douches
            if aantal > 0:
                punten = utils.rond_af(
                    aantal * punten_sanitair[voorzieningsoort.value], 2
                )

                totaal_punten_bad_en_douche += punten

                yield (
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam} - {voorzieningsoort.naam}"
                        ),
                        punten=float(punten),
                        aantal=aantal,
                    )
                )

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

        if ruimte.detail_soort in [
            Ruimtedetailsoort.badkamer.value,
            Ruimtedetailsoort.badkamer_met_toilet.value,
            Ruimtedetailsoort.doucheruimte.value,
        ]:
            for installatie, aantal in installaties.items():
                if installatie not in (
                    punten_voorzieningen
                    | punten_sanitair
                    | mapping_toilet[Ruimtedetailsoort.toiletruimte.value]
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

                    if installatie == Voorzieningsoort.stopcontact_bij_wastafel.value:
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
    logger.enable("woningwaardering")
    warnings.simplefilter("default", UserWarning)

    sanitair = Sanitair()
    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[sanitair.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    stelselgroep = Sanitair()
    with open(
        "tests/data/generiek/input/37101000032.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[stelselgroep.bereken(eenheid)]
    )

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)
