from pathlib import Path

from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    bepaal_wastafel_uitzonderingsruimte,
    waardeer_sanitair,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    Sanitair,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Installatiesoort,
    Ruimtedetailsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

INPUT = (
    Path(__file__).parents[2]
    / "data/onzelfstandige_woonruimten/stelselgroepen/sanitair/input/maximering_wastafels_8_onz_gunstigste_ruimte.json"
)
PRIVE_INPUT = (
    Path(__file__).parents[2]
    / "data/onzelfstandige_woonruimten/stelselgroepen/sanitair/input/8_onzelfstandige_woonruimten_prive_wastafels.json"
)
SPOELBAKKEN_INPUT = (
    Path(__file__).parents[2]
    / "data/onzelfstandige_woonruimten/stelselgroepen/sanitair/input/spoelbakken_8_onzelfstandige_woonruimten.json"
)


def _lees_eenheid(pad: Path) -> EenhedenEenheid:
    with pad.open() as f:
        return EenhedenEenheid.model_validate_json(f.read())


def _maximeringsregels_per_ruimte(
    ruimte_waarderingen: list,
) -> dict[str, list[str]]:
    per_ruimte: dict[str, list[str]] = {}
    for ruimte, ruimte_criterium, waarderingen in ruimte_waarderingen:
        maximeringen = [
            waardering.naam or ""
            for waardering in waarderingen
            if waardering.bovenliggende is ruimte_criterium
            and (waardering.naam or "").startswith("Max")
        ]
        per_ruimte[ruimte.id] = maximeringen
    return per_ruimte


def test_wastafelmaximering_stelt_precies_een_uitzonderingsruimte_vrij():
    eenheid = _lees_eenheid(INPUT)

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)
    assert uitzonderingsruimte is not None
    assert uitzonderingsruimte.id == "bergruimte_meerpersoons"

    waarderingsgroep_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.onzelfstandige_woonruimten,
        Woningwaarderingstelselgroep.sanitair,
    )

    ruimte_waarderingen = []
    for ruimte in eenheid.ruimten or []:
        gedeeld_met = waarderingsgroep_builder.gedeeld_met(
            aantal_onzelfstandige_woonruimten=(
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            ),
        )
        waarderingen = waardeer_sanitair(
            ruimte,
            Woningwaarderingstelsel.onzelfstandige_woonruimten,
            waarderingsgroep_builder=gedeeld_met,
            deler=1,
            wastafel_uitzonderingsruimte=uitzonderingsruimte,
        )
        if not waarderingen:
            continue
        ruimte_waarderingen.append((ruimte, waarderingen[0], waarderingen))

    maximeringen = _maximeringsregels_per_ruimte(ruimte_waarderingen)
    vrijgestelde_ruimten = [
        ruimte_id for ruimte_id, regels in maximeringen.items() if not regels
    ]
    gemaximeerde_ruimten = [
        ruimte_id for ruimte_id, regels in maximeringen.items() if regels
    ]

    assert vrijgestelde_ruimten == ["bergruimte_meerpersoons"]
    assert gemaximeerde_ruimten == ["woonkamer_wastafels"]
    assert maximeringen["woonkamer_wastafels"] == ["Maximering voor Wastafel"]


def test_adresdrempel_maakt_prive_ruimte_kandidaat():
    eenheid = _lees_eenheid(PRIVE_INPUT)

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is not None
    assert uitzonderingsruimte.id == "slaapkamer"


def test_uitzonderingsruimte_kan_in_beide_stelselgroepen_vallen():
    eenheid = _lees_eenheid(INPUT)
    assert eenheid.ruimten is not None
    ruimte_op_adres, ruimte_gedeeld_met_adressen = eenheid.ruimten
    ruimte_gedeeld_met_adressen.gedeeld_met_aantal_adressen = 2

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)
    assert uitzonderingsruimte is ruimte_op_adres

    assert ruimte_gedeeld_met_adressen.installaties is not None
    ruimte_gedeeld_met_adressen.installaties.append(
        Installatiesoort.meerpersoonswastafel
    )

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)
    assert uitzonderingsruimte is ruimte_gedeeld_met_adressen


def test_beide_stelselgroepen_gebruiken_dezelfde_uitzonderingsruimte():
    eenheid = _lees_eenheid(INPUT)
    assert eenheid.ruimten is not None
    _, ruimte_gedeeld_met_adressen = eenheid.ruimten
    ruimte_gedeeld_met_adressen.gedeeld_met_aantal_adressen = 2
    ruimte_gedeeld_met_adressen.oppervlakte = 10
    assert ruimte_gedeeld_met_adressen.installaties is not None
    ruimte_gedeeld_met_adressen.installaties.append(
        Installatiesoort.meerpersoonswastafel
    )

    sanitair = Sanitair().waardeer(eenheid)
    gemeenschappelijke_binnenruimten = (
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen().waardeer(eenheid)
    )

    sanitair_maximeringen = [
        waardering
        for waardering in sanitair.woningwaarderingen or []
        if "max_punten" in waardering.criterium.id
    ]
    gemeenschappelijke_maximeringen = [
        waardering
        for waardering in gemeenschappelijke_binnenruimten.woningwaarderingen or []
        if "max_punten" in waardering.criterium.id
    ]
    assert len(sanitair_maximeringen) == 1
    assert gemeenschappelijke_maximeringen == []


def test_zorgwoning_sluit_ruimte_gedeeld_met_adressen_uit():
    eenheid = _lees_eenheid(INPUT)
    assert eenheid.ruimten is not None
    ruimte_op_adres, ruimte_gedeeld_met_adressen = eenheid.ruimten
    ruimte_gedeeld_met_adressen.gedeeld_met_aantal_adressen = 2
    assert ruimte_gedeeld_met_adressen.installaties is not None
    ruimte_gedeeld_met_adressen.installaties.append(
        Installatiesoort.meerpersoonswastafel
    )
    eenheid.doelgroep = Doelgroep.zorg

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is ruimte_op_adres


def test_korte_aanrechten_tellen_mee_bij_selectie():
    eenheid = _lees_eenheid(SPOELBAKKEN_INPUT)
    assert eenheid.ruimten is not None
    bergruimte = eenheid.ruimten[1]
    bergruimte.installaties = [Installatiesoort.wastafel]

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is eenheid.ruimten[0]


def test_korte_aanrechten_in_woon_slaap_keuken_tellen_mee():
    eenheid = _lees_eenheid(SPOELBAKKEN_INPUT)
    assert eenheid.ruimten is not None
    keuken = eenheid.ruimten[0]
    keuken.detail_soort = Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken
    eenheid.ruimten[1].installaties = [Installatiesoort.wastafel]

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is keuken
