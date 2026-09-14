import warnings

import pytest

from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
    Referentiedata,
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


def maak_ruimte(
    soort,
    detail_soort,
    oppervlakte,
    *,
    naam="Ruimte",
    id="Space_1",
    gedeeld_met_aantal_adressen=None,
):
    return EenhedenRuimte(
        id=id,
        naam=naam,
        soort=soort,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        gedeeld_met_aantal_adressen=gedeeld_met_aantal_adressen,
    )


def classificeer(ruimte, *, verwacht_soort_warning: bool = False):
    """Classificeer en toets de soort-mismatch-warning zonder de error-filter.

    De package promoveert `UserWarning` tot error. Binnen deze helper zetten we
    dat terug naar `always`, zodat we zowel het resultaat als de warning kunnen
    toetsen.
    """
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", UserWarning)
        resultaat = classificeer_ruimte(ruimte)

    soort_warnings = [
        w
        for w in caught
        if issubclass(w.category, UserWarning) and "aangeleverd als" in str(w.message)
    ]
    if verwacht_soort_warning:
        assert soort_warnings, "Verwachte UserWarning omdat soort ≠ classificatie"
    else:
        assert not soort_warnings, (
            f"Geen soort-mismatch-warning verwacht, kreeg: "
            f"{[str(w.message) for w in soort_warnings]}"
        )
    return resultaat


@pytest.mark.parametrize(
    "oppervlakte,bouwkundige_elementen,verwacht,verwacht_soort_warning",
    [
        # 2.2.1.3: een zoldervertrek voldoet aan de afwerkingseisen en gaat er op grond
        # van de detailsoort van uit dat er een vaste trap is. Vanaf 4 m² is het een
        # vertrek, ook wanneer de trap niet apart gemodelleerd is.
        (10, [], Ruimtesoort.vertrek, False),
        (10, [TRAP], Ruimtesoort.vertrek, False),
        (4, [TRAP], Ruimtesoort.vertrek, False),
        # Een vlizotrap weerspreekt de vaste trap uit de detailsoort: geen vertrek, maar
        # wel bereikbaar en daarmee een overige ruimte. `soort=vertrek` is de VERA-parent
        # van `zoldervertrek` → geen warning.
        (10, [VLIZOTRAP], Ruimtesoort.overige_ruimten, False),
        # Een expliciete vaste trap wint van een vlizotrap.
        (10, [TRAP, VLIZOTRAP], Ruimtesoort.vertrek, False),
        # 2.2.1.2: onder de 4 m² valt de zolder terug op de eisen van een overige
        # ruimte, net als andere vertrekken die de minimale oppervlakte niet halen.
        (3.99, [TRAP], Ruimtesoort.overige_ruimten, False),
        (2, [TRAP], Ruimtesoort.overige_ruimten, False),
        # Onder de 2 m² voldoet de zolder aan geen van beide rubrieken. Geen warning:
        # dat is dezelfde soort drempel als de 4 m²-fallback.
        (1.99, [TRAP], None, False),
        (1.99, [VLIZOTRAP], None, False),
        (1.99, [], None, False),
    ],
)
def test_classificeer_ruimte_zoldervertrek_als_vertrek_aangeleverd(
    oppervlakte, bouwkundige_elementen, verwacht, verwacht_soort_warning
):
    ruimte = maak_zolder(
        Ruimtesoort.vertrek,
        oppervlakte,
        bouwkundige_elementen,
        detail_soort=Ruimtedetailsoort.zoldervertrek,
    )

    assert (
        classificeer(ruimte, verwacht_soort_warning=verwacht_soort_warning) == verwacht
    )


@pytest.mark.parametrize(
    "oppervlakte,bouwkundige_elementen,verwacht,verwacht_soort_warning",
    [
        (10, [], Ruimtesoort.overige_ruimten, True),
        (10, [TRAP], Ruimtesoort.overige_ruimten, True),
        (10, [VLIZOTRAP], Ruimtesoort.overige_ruimten, True),
        (4, [TRAP], Ruimtesoort.overige_ruimten, True),
        (2, [TRAP], Ruimtesoort.overige_ruimten, False),
        (1.99, [TRAP], None, False),
    ],
)
def test_classificeer_ruimte_zolder_als_vertrek_aangeleverd_wordt_overige_ruimte(
    oppervlakte, bouwkundige_elementen, verwacht, verwacht_soort_warning
):
    """2.2.1.3: een `zolder` voldoet volgens VERA niet aan de afwerkingseisen.

    De VERA-definitie van `zolder` is een ruimte "die qua oppervlakte en stahoogte
    geschikt is om als vertrek te worden gekwalificeerd, maar die niet voldoet aan de
    afwerkingseisen". Daarmee is niet voldaan aan de eis dat het dak beschoten is, dus
    een `zolder` kan nooit als vertrek worden gewaardeerd — ook niet met een vaste trap
    en ruim voldoende oppervlakte. Vanaf 4 m² is dat geen 4 m²-fallback, dus warning.
    """
    ruimte = maak_zolder(Ruimtesoort.vertrek, oppervlakte, bouwkundige_elementen)

    assert (
        classificeer(ruimte, verwacht_soort_warning=verwacht_soort_warning) == verwacht
    )


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

    assert classificeer(ruimte) == verwacht


def test_classificeer_ruimte_zoldervertrek_als_vertrek_zonder_trap_element_waarschuwt_niet():
    """De detailsoort draagt de trap: een ontbrekend trap-element is geen incomplete input."""
    ruimte = maak_zolder(
        Ruimtesoort.vertrek,
        10,
        [],
        detail_soort=Ruimtedetailsoort.zoldervertrek,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("error", UserWarning)
        assert classificeer_ruimte(ruimte) == Ruimtesoort.vertrek


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

    assert classificeer(ruimte) == Ruimtesoort.overige_ruimten




def test_classificeer_ruimte_garage_gedeeld_als_overige_is_none_zonder_warning():
    """VERA-parent van garage is overige ruimte: gedeeld is geen foute input."""
    ruimte = maak_ruimte(
        Ruimtesoort.overige_ruimten,
        Ruimtedetailsoort.garage,
        20,
        naam="Garage",
        gedeeld_met_aantal_adressen=4,
    )
    assert classificeer(ruimte) is None


def test_classificeer_ruimte_garage_gedeeld_als_vertrek_is_vertrek():
    ruimte = maak_ruimte(
        Ruimtesoort.vertrek,
        Ruimtedetailsoort.garage,
        20,
        naam="Garage",
        gedeeld_met_aantal_adressen=4,
    )
    assert classificeer(ruimte) == Ruimtesoort.vertrek


@pytest.mark.parametrize(
    "detail_soort",
    [
        Ruimtedetailsoort.gang,
        Ruimtedetailsoort.hal,
        Ruimtedetailsoort.overloop,
        Ruimtedetailsoort.entree,
        Ruimtedetailsoort.trappenhuis,
        Ruimtedetailsoort.galerij,
        Ruimtedetailsoort.liftschacht,
    ],
)
def test_classificeer_ruimte_verkeersruimte_detailsoort_dwingt_categorie(detail_soort):
    ruimte = maak_ruimte(Ruimtesoort.vertrek, detail_soort, 4.5, naam="Gang")
    assert (
        classificeer(ruimte, verwacht_soort_warning=True) == Ruimtesoort.verkeersruimte
    )


def test_classificeer_ruimte_verkeersruimte_met_passende_soort_waarschuwt_niet():
    ruimte = maak_ruimte(
        Ruimtesoort.verkeersruimte, Ruimtedetailsoort.gang, 4.5, naam="Gang"
    )
    assert classificeer(ruimte) == Ruimtesoort.verkeersruimte


def test_classificeer_ruimte_keuken_als_overige_ruimte_is_vertrek_met_warning():
    ruimte = maak_ruimte(
        Ruimtesoort.overige_ruimten, Ruimtedetailsoort.keuken, 6, naam="Keuken"
    )
    assert classificeer(ruimte, verwacht_soort_warning=True) == Ruimtesoort.vertrek


def test_classificeer_ruimte_keuken_als_vertrek_waarschuwt_niet():
    ruimte = maak_ruimte(
        Ruimtesoort.vertrek, Ruimtedetailsoort.keuken, 6, naam="Keuken"
    )
    assert classificeer(ruimte) == Ruimtesoort.vertrek


@pytest.mark.parametrize(
    "detail_soort",
    [
        Ruimtedetailsoort.schacht,
        Ruimtedetailsoort.kast,
        Ruimtedetailsoort.meterruimte,
        Ruimtedetailsoort.technische_ruimte,
        Ruimtedetailsoort.vliering,
    ],
)
@pytest.mark.parametrize(
    "soort",
    [Ruimtesoort.vertrek, Ruimtesoort.overige_ruimten],
)
def test_classificeer_ruimte_niet_op_allowlist_is_none_zonder_warning(
    detail_soort, soort
):
    ruimte = maak_ruimte(soort, detail_soort, 4.2, naam=detail_soort.naam)
    assert classificeer(ruimte) is None


@pytest.mark.parametrize(
    "detail_soort",
    [
        Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
        Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage,
        Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex,
        Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
    ],
)
@pytest.mark.parametrize(
    "soort",
    [Ruimtesoort.vertrek, Ruimtesoort.overige_ruimten],
)
def test_classificeer_ruimte_parkeertype_nooit_vertrek_of_overige(detail_soort, soort):
    ruimte = maak_ruimte(soort, detail_soort, 12, naam="Parkeerplek")
    assert classificeer(ruimte) is None


def test_classificeer_ruimte_parkeertype_als_gemeenschappelijk_waarschuwt_niet():
    """Parkeer-types in rubriek 10 hebben vaak `soort=GEM`; dat is geen rubriek 1/2-claim."""
    ruimte = maak_ruimte(
        Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen,
        Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
        12,
        naam="Parkeerplek",
    )
    assert classificeer(ruimte) is None


def test_classificeer_ruimte_toiletruimte_json_zonder_parent_waarschuwt_niet():
    """JSON vult `parent` niet; de VERA-parent-schildregel zoekt het enumlid op code."""
    ruimte = EenhedenRuimte(
        id="Space_1",
        naam="Toiletruimte",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Referentiedata(code="TOI", naam="Toiletruimte"),
        oppervlakte=2.5,
    )
    assert classificeer(ruimte) == Ruimtesoort.overige_ruimten


def test_classificeer_ruimte_balkon_als_vertrek_is_buitenruimte_met_warning():
    ruimte = maak_ruimte(
        Ruimtesoort.vertrek, Ruimtedetailsoort.balkon, 6, naam="Balkon"
    )
    assert classificeer(ruimte, verwacht_soort_warning=True) == Ruimtesoort.buitenruimte
