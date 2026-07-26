from decimal import Decimal

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    adres_met_8_of_meer_onzelfstandige_woonruimten,
    maximeer_wastafels,
    waardeer_sanitair,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _waardeer_ruimten(
    ruimten: list[EenhedenRuimte],
    *,
    stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
) -> list[tuple[EenhedenRuimte, object, list]]:
    adres_met_8 = adres_met_8_of_meer_onzelfstandige_woonruimten(ruimten)
    waarderingsgroep_builder = WaarderingsgroepBuilder(
        stelsel, Woningwaarderingstelselgroep.sanitair
    )
    ruimte_waarderingen = []

    for ruimte in ruimten:
        waarderingen = waardeer_sanitair(
            ruimte,
            stelsel,
            waarderingsgroep_builder=waarderingsgroep_builder,
            adres_met_8_of_meer_onzelfstandige_woonruimten=adres_met_8,
        )
        if waarderingen:
            ruimte_waarderingen.append((ruimte, waarderingen[0], waarderingen))

    maximeer_wastafels(ruimte_waarderingen)
    return ruimte_waarderingen


def _totaal_punten(waarderingen: list) -> Decimal:
    return sum(Decimal(str(w.punten)) for w in waarderingen if w.punten is not None)


def _heeft_maximering(waarderingen: list, segment: str) -> bool:
    return any(w.segment == f"max_punten_{segment}" for w in waarderingen)


def test_spoelbakken_in_korte_aanrechten_worden_gemaximeerd_op_1_punt():
    # Spoelbakken in aanrechten korter dan 1 m, zonder installatie-wastafel.
    ruimte = EenhedenRuimte(
        id="keuken",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.keuken,
        naam="Keuken",
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                id="aanrecht_1",
                naam="Aanrecht",
                soort=Bouwkundigelementsoort.voorziening,
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=800,
            ),
            BouwkundigElementenBouwkundigElement(
                id="aanrecht_2",
                naam="Aanrecht",
                soort=Bouwkundigelementsoort.voorziening,
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=900,
            ),
        ],
    )

    _, _, waarderingen = _waardeer_ruimten([ruimte])[0]

    assert _totaal_punten(waarderingen) == Decimal("1")
    assert _heeft_maximering(waarderingen, Installatiesoort.wastafel.name)


def test_badkamer_wordt_niet_gemaximeerd_bij_adres_met_8_onzelfstandige_woonruimten():
    # Badkamers blijven uitgezonderd van het wastafelmaximum.
    badkamer = EenhedenRuimte(
        id="badkamer",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.badkamer,
        naam="Badkamer",
        gedeeld_met_aantal_onzelfstandige_woonruimten=8,
        installaties=[
            Installatiesoort.wastafel,
            Installatiesoort.wastafel,
            Installatiesoort.douche,
        ],
    )
    slaapkamer = EenhedenRuimte(
        id="slaapkamer",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        naam="Slaapkamer",
        gedeeld_met_aantal_onzelfstandige_woonruimten=8,
        installaties=[
            Installatiesoort.wastafel,
            Installatiesoort.wastafel,
            Installatiesoort.wastafel,
        ],
    )

    ruimte_waarderingen = _waardeer_ruimten(
        [badkamer, slaapkamer],
        stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    badkamer_waarderingen = next(
        waarderingen
        for ruimte, _, waarderingen in ruimte_waarderingen
        if ruimte.id == "badkamer"
    )

    assert not _heeft_maximering(badkamer_waarderingen, Installatiesoort.wastafel.name)
    assert _totaal_punten(badkamer_waarderingen) == Decimal("5")


def test_8_plus_uitzondering_blijft_als_max_ruimte_prive_is():
    # De privéruimte met de meeste wastafels blijft vrijgesteld.
    slaapkamer = EenhedenRuimte(
        id="slaapkamer",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        naam="Slaapkamer",
        installaties=[
            Installatiesoort.wastafel,
            Installatiesoort.wastafel,
            Installatiesoort.wastafel,
        ],
    )
    bergruimte = EenhedenRuimte(
        id="bergruimte",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.bergruimte,
        naam="Bergruimte",
        gedeeld_met_aantal_onzelfstandige_woonruimten=8,
        installaties=[
            Installatiesoort.wastafel,
            Installatiesoort.wastafel,
        ],
    )

    ruimte_waarderingen = _waardeer_ruimten(
        [slaapkamer, bergruimte],
        stelsel=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    waarderingen_per_ruimte = {
        ruimte.id: waarderingen for ruimte, _, waarderingen in ruimte_waarderingen
    }

    assert _totaal_punten(waarderingen_per_ruimte["slaapkamer"]) == Decimal("3")
    assert _totaal_punten(waarderingen_per_ruimte["bergruimte"]) == Decimal("1")
    assert not _heeft_maximering(
        waarderingen_per_ruimte["slaapkamer"], Installatiesoort.wastafel.name
    )
    assert _heeft_maximering(
        waarderingen_per_ruimte["bergruimte"], Installatiesoort.wastafel.name
    )
