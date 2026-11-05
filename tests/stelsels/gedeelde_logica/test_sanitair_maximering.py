from tests.input import aanrecht
from tests.input import ruimte as maak_ruimte
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
    Bouwkundigelementdetailsoort,
    Doelgroep,
    Installatiesoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def _eenheid_met_wastafels_en_meerpersoonswastafels() -> EenhedenEenheid:
    """Maak een eenheid met twee ruimten die elk met 8 onzelfstandige woonruimten worden gedeeld.

    De woonkamer heeft drie wastafels, de berging drie meerpersoonswastafels.
    """
    return EenhedenEenheid(
        ruimten=[
            maak_ruimte(
                Ruimtedetailsoort.woonkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                naam="woonkamer_wastafels",
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
            maak_ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                Installatiesoort.meerpersoonswastafel,
                naam="bergruimte_meerpersoons",
                soort=Ruimtesoort.vertrek,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )


def _eenheid_met_prive_wastafels() -> EenhedenEenheid:
    """Maak een eenheid met een privéslaapkamer en een berging gedeeld met 8 onzelfstandige woonruimten.

    De slaapkamer heeft drie wastafels, de berging twee.
    """
    return EenhedenEenheid(
        ruimten=[
            maak_ruimte(
                Ruimtedetailsoort.slaapkamer,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
            ),
            maak_ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                soort=Ruimtesoort.vertrek,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )


def _eenheid_met_korte_aanrechten() -> EenhedenEenheid:
    """Maak een eenheid met een keuken en een berging, elk gedeeld met 8 onzelfstandige woonruimten.

    De keuken heeft twee aanrechten korter dan 1 m, de berging drie wastafels.
    """
    return EenhedenEenheid(
        ruimten=[
            maak_ruimte(
                Ruimtedetailsoort.keuken,
                elementen=[
                    aanrecht(800, id="aanrecht_1"),
                    aanrecht(900, id="aanrecht_2"),
                ],
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
            maak_ruimte(
                Ruimtedetailsoort.berging,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                Installatiesoort.wastafel,
                soort=Ruimtesoort.vertrek,
                gedeeld_met_aantal_onzelfstandige_woonruimten=8,
            ),
        ]
    )


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
    eenheid = _eenheid_met_wastafels_en_meerpersoonswastafels()

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
    eenheid = _eenheid_met_prive_wastafels()

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is not None
    assert uitzonderingsruimte.id == "slaapkamer"


def test_uitzonderingsruimte_kan_in_beide_stelselgroepen_vallen():
    eenheid = _eenheid_met_wastafels_en_meerpersoonswastafels()
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
    eenheid = _eenheid_met_wastafels_en_meerpersoonswastafels()
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
    eenheid = _eenheid_met_wastafels_en_meerpersoonswastafels()
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


def test_spoelbak_in_kort_aanrecht_telt_mee_bij_selectie():
    eenheid = _eenheid_met_korte_aanrechten()
    assert eenheid.ruimten is not None
    keuken, bergruimte = eenheid.ruimten
    keuken.installaties = [Installatiesoort.wastafel]
    bergruimte.installaties = [Installatiesoort.wastafel]
    eenheid.ruimten = [bergruimte, keuken]

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is keuken


def test_spoelbak_in_kort_aanrecht_in_woon_slaap_keuken_telt_mee():
    eenheid = _eenheid_met_korte_aanrechten()
    assert eenheid.ruimten is not None
    keuken, bergruimte = eenheid.ruimten
    keuken.detail_soort = Ruimtedetailsoort.woon_en_of_slaapkamer_en_of_keuken
    keuken.installaties = [Installatiesoort.wastafel]
    bergruimte.installaties = [Installatiesoort.wastafel]
    eenheid.ruimten = [bergruimte, keuken]

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is keuken


def test_meerdere_korte_aanrechten_tellen_als_een_wastafel_bij_selectie():
    eenheid = _eenheid_met_korte_aanrechten()
    assert eenheid.ruimten is not None
    keuken, bergruimte = eenheid.ruimten
    bergruimte.installaties = [Installatiesoort.wastafel, Installatiesoort.wastafel]

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is bergruimte


def test_kort_aanrechtdeel_naast_aanrecht_vanaf_1m_telt_niet_mee_bij_selectie():
    eenheid = EenhedenEenheid.model_validate(
        {
            "ruimten": [
                {
                    "id": "keuken_met_kort_aanrechtdeel",
                    "soort": Ruimtesoort.vertrek,
                    "detailSoort": Ruimtedetailsoort.keuken,
                    "gedeeldMetAantalOnzelfstandigeWoonruimten": 8,
                    "installaties": [Installatiesoort.wastafel],
                    "bouwkundigeElementen": [
                        {
                            "id": "aanrecht_kort",
                            "detailSoort": Bouwkundigelementdetailsoort.aanrecht,
                            "lengte": 800,
                        },
                        {
                            "id": "aanrecht_lang",
                            "detailSoort": Bouwkundigelementdetailsoort.aanrecht,
                            "lengte": 1200,
                        },
                    ],
                },
                {
                    "id": "keuken_met_twee_wastafels",
                    "soort": Ruimtesoort.vertrek,
                    "detailSoort": Ruimtedetailsoort.keuken,
                    "gedeeldMetAantalOnzelfstandigeWoonruimten": 8,
                    "installaties": [
                        Installatiesoort.wastafel,
                        Installatiesoort.wastafel,
                    ],
                },
            ]
        }
    )

    uitzonderingsruimte = bepaal_wastafel_uitzonderingsruimte(eenheid)

    assert uitzonderingsruimte is not None
    assert uitzonderingsruimte.id == "keuken_met_twee_wastafels"
