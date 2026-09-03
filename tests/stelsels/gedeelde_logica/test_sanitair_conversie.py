from collections import Counter

import pytest

from woningwaardering.stelsels.gedeelde_logica.sanitair.sanitair import (
    converteer_bouwkundige_elementen_naar_installaties,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import Sanitair
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    BouwkundigelementdetailsoortReferentiedata,
    Bouwkundigelementsoort,
    Installatiesoort,
    InstallatiesoortReferentiedata,
    Ruimtedetailsoort,
    Ruimtesoort,
)


def _badkamer(
    bouwkundige_elementen: list[BouwkundigelementdetailsoortReferentiedata],
    installaties: list[InstallatiesoortReferentiedata] | None = None,
) -> EenhedenEenheid:
    ruimte = EenhedenRuimte(
        id="badkamer",
        naam="Badkamer",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.badkamer,
        oppervlakte=6.0,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                id=f"element_{index}",
                soort=Bouwkundigelementsoort.voorziening,
                detail_soort=detail_soort,
            )
            for index, detail_soort in enumerate(bouwkundige_elementen)
        ],
        installaties=list(installaties or []),
    )
    return EenhedenEenheid(id="eenheid", ruimten=[ruimte])


def _installaties(eenheid: EenhedenEenheid) -> Counter[Referentiedata]:
    assert eenheid.ruimten is not None
    return Counter(eenheid.ruimten[0].installaties or [])


def test_bouwkundig_element_wordt_als_installatie_meegeteld():
    eenheid = _badkamer([Bouwkundigelementdetailsoort.wastafel])

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[Installatiesoort.wastafel] == 1


def test_elk_bouwkundig_element_telt_afzonderlijk_mee():
    eenheid = _badkamer(
        [Bouwkundigelementdetailsoort.wastafel, Bouwkundigelementdetailsoort.wastafel]
    )

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[Installatiesoort.wastafel] == 2


def test_wastafel_en_fontein_tellen_beide_als_wastafel():
    # Een fonteintje wordt volgens 2.6.1 als wastafel gewaardeerd. Een fontein naast
    # een wastafel mag daarom niet wegvallen tegen de wastafel-installatie die we
    # zelf uit het wastafel-element hebben afgeleid.
    eenheid = _badkamer(
        [Bouwkundigelementdetailsoort.wastafel, Bouwkundigelementdetailsoort.fontein]
    )

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[Installatiesoort.wastafel] == 2


def test_dubbel_gemodelleerde_voorziening_telt_een_keer():
    # VERA staat toe dat dezelfde wastafel zowel als bouwkundig element als als
    # installatie wordt meegegeven. Zonder identiteitskoppeling houden we het
    # hoogste van beide aantallen aan, zodat de voorziening niet dubbel telt.
    eenheid = _badkamer(
        [Bouwkundigelementdetailsoort.wastafel], [Installatiesoort.wastafel]
    )

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[Installatiesoort.wastafel] == 1


def test_meegegeven_installatie_onderdrukt_extra_bouwkundige_elementen_niet():
    eenheid = _badkamer(
        [Bouwkundigelementdetailsoort.wastafel, Bouwkundigelementdetailsoort.wastafel],
        [Installatiesoort.wastafel],
    )

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[Installatiesoort.wastafel] == 2


def test_meer_installaties_dan_bouwkundige_elementen_blijft_ongewijzigd():
    eenheid = _badkamer(
        [Bouwkundigelementdetailsoort.wastafel],
        [Installatiesoort.wastafel, Installatiesoort.wastafel],
    )

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[Installatiesoort.wastafel] == 2


@pytest.mark.parametrize(
    "detail_soort, installatiesoort",
    [
        (Bouwkundigelementdetailsoort.douche, Installatiesoort.douche),
        (Bouwkundigelementdetailsoort.bad, Installatiesoort.bad),
        (Bouwkundigelementdetailsoort.kast, Installatiesoort.kastruimte),
        (
            Bouwkundigelementdetailsoort.closetcombinatie,
            Installatiesoort.staand_toilet,
        ),
        (Bouwkundigelementdetailsoort.fontein, Installatiesoort.wastafel),
    ],
)
def test_elk_gemapt_bouwkundig_element_levert_de_juiste_installatie(
    detail_soort, installatiesoort
):
    eenheid = _badkamer([detail_soort])

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid)[installatiesoort] == 1


def test_niet_gemapt_bouwkundig_element_levert_geen_installatie():
    eenheid = _badkamer([Bouwkundigelementdetailsoort.aanrecht])

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid).total() == 0


def test_conversie_is_idempotent():
    # Meerdere stelselgroepen roepen de conversie aan op dezelfde eenheid. Het
    # resultaat mag daardoor niet stapelen.
    eenheid = _badkamer(
        [
            Bouwkundigelementdetailsoort.wastafel,
            Bouwkundigelementdetailsoort.fontein,
            Bouwkundigelementdetailsoort.douche,
        ],
        [Installatiesoort.wastafel],
    )

    converteer_bouwkundige_elementen_naar_installaties(eenheid)
    na_eerste_aanroep = _installaties(eenheid)

    converteer_bouwkundige_elementen_naar_installaties(eenheid)
    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert _installaties(eenheid) == na_eerste_aanroep


def test_bouwkundige_elementen_blijven_behouden():
    # De conversie vult installaties aan en verwijdert niets: een bouwkundig element
    # draagt gegevens (id, afmetingen) die een installatiesoort niet kan bevatten.
    eenheid = _badkamer([Bouwkundigelementdetailsoort.wastafel])
    assert eenheid.ruimten is not None

    converteer_bouwkundige_elementen_naar_installaties(eenheid)

    assert [
        element.detail_soort
        for element in eenheid.ruimten[0].bouwkundige_elementen or []
    ] == [Bouwkundigelementdetailsoort.wastafel]


def test_wastafel_en_fontein_leveren_samen_twee_wastafelpunten(peildatum):
    # Ketentest: 1 punt per wastafel in een badkamer, dus een wastafel naast een
    # fontein levert 2 punten voor wastafels.
    eenheid = _badkamer(
        [
            Bouwkundigelementdetailsoort.wastafel,
            Bouwkundigelementdetailsoort.fontein,
            Bouwkundigelementdetailsoort.douche,
        ]
    )

    groep = Sanitair(peildatum=peildatum).waardeer(eenheid)

    punten_per_criterium = {
        waardering.criterium.id: (waardering.aantal, waardering.punten)
        for waardering in groep.woningwaarderingen or []
    }
    assert punten_per_criterium["sanitair__badkamer__wastafel"] == (2.0, 2.0)
    assert punten_per_criterium["sanitair__badkamer__douche"] == (1.0, 4.0)
    assert groep.punten == 6.0
