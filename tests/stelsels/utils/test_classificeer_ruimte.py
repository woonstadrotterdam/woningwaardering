import warnings

import pytest

from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)

TRAP = BouwkundigElementenBouwkundigElement(
    soort=Bouwkundigelementsoort.voorziening,
    detail_soort=Bouwkundigelementdetailsoort.trap,
)
VLIZOTRAP = BouwkundigElementenBouwkundigElement(
    soort=Bouwkundigelementsoort.voorziening,
    detail_soort=Bouwkundigelementdetailsoort.vlizotrap,
)


def maak_zolder(
    soort,
    oppervlakte,
    bouwkundige_elementen=None,
    detail_soort=Ruimtedetailsoort.zolder,
):
    return EenhedenRuimte(
        id="Space_1",
        naam="Zolder",
        soort=soort,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        bouwkundige_elementen=bouwkundige_elementen or [],
    )


@pytest.mark.parametrize(
    "oppervlakte,bouwkundige_elementen,verwacht",
    [
        # 2.2.1.3: een zoldervertrek voldoet aan de afwerkingseisen en gaat er op grond
        # van de detailsoort van uit dat er een vaste trap is. Vanaf 4 m² is het een
        # vertrek, ook wanneer de trap niet apart gemodelleerd is.
        (10, [], Ruimtesoort.vertrek),
        (10, [TRAP], Ruimtesoort.vertrek),
        (4, [TRAP], Ruimtesoort.vertrek),
        # Een vlizotrap weerspreekt de vaste trap uit de detailsoort: geen vertrek, maar
        # wel bereikbaar en daarmee een overige ruimte.
        (10, [VLIZOTRAP], Ruimtesoort.overige_ruimten),
        # Een expliciete vaste trap wint van een vlizotrap.
        (10, [TRAP, VLIZOTRAP], Ruimtesoort.vertrek),
        # 2.2.1.2: onder de 4 m² valt de zolder terug op de eisen van een overige
        # ruimte, net als andere vertrekken die de minimale oppervlakte niet halen.
        (3.99, [TRAP], Ruimtesoort.overige_ruimten),
        (2, [TRAP], Ruimtesoort.overige_ruimten),
        # Onder de 2 m² voldoet de zolder aan geen van beide rubrieken.
        (1.99, [TRAP], None),
        (1.99, [VLIZOTRAP], None),
        (1.99, [], None),
    ],
)
def test_classificeer_ruimte_zoldervertrek_als_vertrek_aangeleverd(
    oppervlakte, bouwkundige_elementen, verwacht
):
    ruimte = maak_zolder(
        Ruimtesoort.vertrek,
        oppervlakte,
        bouwkundige_elementen,
        detail_soort=Ruimtedetailsoort.zoldervertrek,
    )

    assert classificeer_ruimte(ruimte) == verwacht


@pytest.mark.parametrize(
    "oppervlakte,bouwkundige_elementen,verwacht",
    [
        (10, [], Ruimtesoort.overige_ruimten),
        (10, [TRAP], Ruimtesoort.overige_ruimten),
        (10, [VLIZOTRAP], Ruimtesoort.overige_ruimten),
        (4, [TRAP], Ruimtesoort.overige_ruimten),
        (2, [TRAP], Ruimtesoort.overige_ruimten),
        (1.99, [TRAP], None),
    ],
)
def test_classificeer_ruimte_zolder_als_vertrek_aangeleverd_wordt_overige_ruimte(
    oppervlakte, bouwkundige_elementen, verwacht
):
    """2.2.1.3: een `zolder` voldoet volgens VERA niet aan de afwerkingseisen.

    De VERA-definitie van `zolder` is een ruimte "die qua oppervlakte en stahoogte
    geschikt is om als vertrek te worden gekwalificeerd, maar die niet voldoet aan de
    afwerkingseisen". Daarmee is niet voldaan aan de eis dat het dak beschoten is, dus
    een `zolder` kan nooit als vertrek worden gewaardeerd — ook niet met een vaste trap
    en ruim voldoende oppervlakte.
    """
    ruimte = maak_zolder(Ruimtesoort.vertrek, oppervlakte, bouwkundige_elementen)

    assert classificeer_ruimte(ruimte) == verwacht


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
@pytest.mark.parametrize(
    "oppervlakte,bouwkundige_elementen,verwacht",
    [
        (10, [], Ruimtesoort.overige_ruimten),
        (10, [TRAP], Ruimtesoort.overige_ruimten),
        (10, [VLIZOTRAP], Ruimtesoort.overige_ruimten),
        (2, [VLIZOTRAP], Ruimtesoort.overige_ruimten),
        (1.99, [TRAP], None),
    ],
)
def test_classificeer_ruimte_zolder_als_overige_ruimte_aangeleverd(
    detail_soort, oppervlakte, bouwkundige_elementen, verwacht
):
    ruimte = maak_zolder(
        Ruimtesoort.overige_ruimten,
        oppervlakte,
        bouwkundige_elementen,
        detail_soort=detail_soort,
    )

    assert classificeer_ruimte(ruimte) == verwacht


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
@pytest.mark.parametrize("soort", [Ruimtesoort.vertrek, Ruimtesoort.overige_ruimten])
@pytest.mark.parametrize("bouwkundige_elementen", [[], [TRAP], [VLIZOTRAP]])
def test_classificeer_ruimte_zolder_waarschuwt_niet(
    detail_soort, soort, bouwkundige_elementen
):
    """De detailsoort draagt de trap: een ontbrekend trap-element is geen incomplete input."""
    ruimte = maak_zolder(soort, 10, bouwkundige_elementen, detail_soort=detail_soort)

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        assert classificeer_ruimte(ruimte) is not None


def test_classificeer_ruimte_zoldervertrek_als_overige_ruimte_wordt_nooit_vertrek():
    """De aangeleverde ruimtesoort is leidend: een overige ruimte wordt nooit opgewaardeerd.

    2.2.1.2: "Een ruimte dient `Ruimtesoort` `vertrek` te hebben om in aanmerking te
    komen voor een waardering in de rubriek 'Oppervlakte van vertrekken'."
    """
    ruimte = maak_zolder(
        Ruimtesoort.overige_ruimten,
        10,
        [TRAP],
        detail_soort=Ruimtedetailsoort.zoldervertrek,
    )

    assert classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
