"""Tests voor de gedeelde parkeerregels (rubriek 8, 10 en 12).

De regelset staat beschreven in https://github.com/woonstadrotterdam/woningwaardering/issues/381:
één stroom voor zelfstandige en onzelfstandige woonruimten, waarbij alleen de
deler verschilt.
"""

from decimal import Decimal
from itertools import product

import pytest

from tests.peildatum import REFERENTIE_PEILDATUM
from woningwaardering.stelsels.gedeelde_logica.parkeerruimten import (
    is_gemeenschappelijke_parkeerruimte,
    is_kerntype_parkeerruimte,
    is_overige_parkeerruimte,
    wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.bijzondere_voorzieningen import (
    BijzondereVoorzieningen as BijzondereVoorzieningenOnz,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.buitenruimten import (
    Buitenruimten as BuitenruimtenOnz,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten as GemeenschappelijkeParkeerruimtenOnz,
)
from woningwaardering.stelsels.utils import deler, is_prive
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen import (
    BijzondereVoorzieningen as BijzondereVoorzieningenZel,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.buitenruimten import (
    Buitenruimten as BuitenruimtenZel,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten as GemeenschappelijkeParkeerruimtenZel,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)

KERNTYPEN = [
    Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage,
    Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage,
    Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,
]

OVERIGE_PARKEERRUIMTEN = [
    Ruimtedetailsoort.carport,
    Ruimtedetailsoort.parkeerplaats,
]

RUBRIEK_8 = "buitenruimten"
RUBRIEK_10 = "gemeenschappelijke_parkeerruimten"
RUBRIEK_12 = "bijzondere_voorzieningen"

STELSELGROEP_CLASSES = {
    "zelfstandige_woonruimten": {
        RUBRIEK_8: BuitenruimtenZel,
        RUBRIEK_10: GemeenschappelijkeParkeerruimtenZel,
        RUBRIEK_12: BijzondereVoorzieningenZel,
    },
    "onzelfstandige_woonruimten": {
        RUBRIEK_8: BuitenruimtenOnz,
        RUBRIEK_10: GemeenschappelijkeParkeerruimtenOnz,
        RUBRIEK_12: BijzondereVoorzieningenOnz,
    },
}


def maak_parkeerruimte(
    detailsoort,
    *,
    oppervlakte: float = 15.0,
    aantal_adressen: int = 1,
    aantal_onzelfstandige_woonruimten: int = 1,
    met_laadpaal: bool = False,
) -> EenhedenRuimte:
    """Maak een parkeerruimte volgens de VERA-standaard."""
    ruimte = EenhedenRuimte(
        id="parkeerruimte",
        naam=detailsoort.naam,
        soort=(
            Ruimtesoort.buitenruimte
            if detailsoort in OVERIGE_PARKEERRUIMTEN
            else Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen
        ),
        detailSoort=detailsoort,
        oppervlakte=oppervlakte,
        lengte=5.0,
        breedte=oppervlakte / 5.0,
        aantal=1,
        gedeeldMetAantalAdressen=aantal_adressen,
        gedeeldMetAantalOnzelfstandigeWoonruimten=aantal_onzelfstandige_woonruimten,
    )
    if met_laadpaal:
        ruimte.bouwkundige_elementen = [
            BouwkundigElementenBouwkundigElement(
                id="laadpaal_1",
                naam="Laadpaal",
                detailSoort=Bouwkundigelementdetailsoort.laadpaal,
            )
        ]
    return ruimte


def maak_referentie_tuin() -> EenhedenRuimte:
    """Een privé-tuin die in elke variant gelijk blijft.

    Hiermee blijven de aanwezigheidspunten en de aftrek voor 'geen buitenruimten'
    in rubriek 8 constant, zodat het verschil tussen twee varianten precies de
    bijdrage van de parkeerruimte of de laadpaal is.
    """
    return EenhedenRuimte(
        id="referentie_tuin",
        naam="Tuin",
        soort=Ruimtesoort.buitenruimte,
        detailSoort=Ruimtedetailsoort.tuin,
        oppervlakte=20.0,
        lengte=5.0,
        breedte=4.0,
        gedeeldMetAantalAdressen=1,
        gedeeldMetAantalOnzelfstandigeWoonruimten=1,
    )


def maak_eenheid(*ruimten: EenhedenRuimte) -> EenhedenEenheid:
    return EenhedenEenheid(id="parkeer_eenheid", ruimten=list(ruimten))


def som_punten(stelsel: str, rubriek: str, eenheid: EenhedenEenheid) -> Decimal:
    """Som de punten van alle waarderingen in een stelselgroep, vóór kwartafronding.

    De waardering 'Afronding op kwartpunten' telt niet mee: die zou het verschil
    tussen twee varianten vertroebelen.
    """
    stelselgroep = STELSELGROEP_CLASSES[stelsel][rubriek](
        peildatum=REFERENTIE_PEILDATUM
    )
    groep = stelselgroep.waardeer(eenheid)
    return sum(
        (
            Decimal(str(waardering.punten))
            for waardering in groep.woningwaarderingen or []
            if waardering.punten is not None
            and waardering.criterium is not None
            and not (waardering.criterium.id or "").endswith(
                "__afronding_op_kwartpunten"
            )
        ),
        start=Decimal("0"),
    )


# --- Privé of gemeenschappelijk -------------------------------------------------


@pytest.mark.parametrize(
    "aantal_adressen, aantal_onzelfstandige_woonruimten, verwacht_prive",
    [
        (1, 1, True),
        (0, 0, True),
        (None, None, True),
        (2, 1, False),
        (1, 2, False),
        (3, 4, False),
    ],
)
def test_is_prive(
    aantal_adressen, aantal_onzelfstandige_woonruimten, verwacht_prive
) -> None:
    ruimte = maak_parkeerruimte(
        Ruimtedetailsoort.carport,
        aantal_adressen=aantal_adressen,
        aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
    )
    assert is_prive(ruimte) is verwacht_prive
    assert is_gemeenschappelijke_parkeerruimte(ruimte) is not verwacht_prive


@pytest.mark.parametrize("detailsoort", KERNTYPEN)
def test_is_kerntype_parkeerruimte(detailsoort) -> None:
    assert is_kerntype_parkeerruimte(detailsoort) is True
    assert is_overige_parkeerruimte(detailsoort) is False


@pytest.mark.parametrize("detailsoort", OVERIGE_PARKEERRUIMTEN)
def test_is_overige_parkeerruimte(detailsoort) -> None:
    assert is_overige_parkeerruimte(detailsoort) is True
    assert is_kerntype_parkeerruimte(detailsoort) is False


def test_deler() -> None:
    ruimte = maak_parkeerruimte(
        Ruimtedetailsoort.carport,
        aantal_adressen=3,
        aantal_onzelfstandige_woonruimten=4,
    )
    assert deler(ruimte) == Decimal("12")


@pytest.mark.parametrize("detailsoort", KERNTYPEN)
def test_wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten_kerntypen(
    detailsoort,
) -> None:
    """Kerntypen staan altijd in een gemeenschappelijke parkeergelegenheid (regel 1)."""
    prive = maak_parkeerruimte(detailsoort)
    gemeenschappelijk = maak_parkeerruimte(detailsoort, aantal_adressen=3)
    assert wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(prive) is True
    assert (
        wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(gemeenschappelijk)
        is True
    )


@pytest.mark.parametrize("detailsoort", OVERIGE_PARKEERRUIMTEN)
def test_wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten_overige(
    detailsoort,
) -> None:
    """Overige parkeerruimten gaan privé naar rubriek 8, gemeenschappelijk naar 10 (regel 2)."""
    prive = maak_parkeerruimte(detailsoort)
    gemeenschappelijk = maak_parkeerruimte(detailsoort, aantal_adressen=3)
    gedeeld_met_onzelfstandig = maak_parkeerruimte(
        detailsoort, aantal_onzelfstandige_woonruimten=4
    )
    assert wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(prive) is False
    assert (
        wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(gemeenschappelijk)
        is True
    )
    assert (
        wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(
            gedeeld_met_onzelfstandig
        )
        is True
    )


# --- Geen dubbeltelling over de rubrieken heen ----------------------------------

DETAILSOORTEN = KERNTYPEN + OVERIGE_PARKEERRUIMTEN
OPPERVLAKTEN = [10.0, 12.0, 15.0]
AANTALLEN_ADRESSEN = [1, 3]
AANTALLEN_ONZELFSTANDIGE_WOONRUIMTEN = [1, 4]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("stelsel", sorted(STELSELGROEP_CLASSES))
@pytest.mark.parametrize(
    "detailsoort, oppervlakte, aantal_adressen, aantal_onzelfstandige_woonruimten",
    list(
        product(
            DETAILSOORTEN,
            OPPERVLAKTEN,
            AANTALLEN_ADRESSEN,
            AANTALLEN_ONZELFSTANDIGE_WOONRUIMTEN,
        )
    ),
)
def test_parkeerruimte_en_laadpaal_krijgen_in_hoogstens_een_rubriek_punten(
    stelsel,
    detailsoort,
    oppervlakte,
    aantal_adressen,
    aantal_onzelfstandige_woonruimten,
) -> None:
    """Regel 5: een parkeerruimte en een laadpaal worden nooit dubbel gewaardeerd.

    De bijdrage van de parkeerruimte is het verschil tussen een eenheid mét en
    zónder die parkeerruimte; de bijdrage van de laadpaal het verschil tussen
    dezelfde parkeerruimte mét en zónder laadpaal.
    """
    zonder_parkeerruimte = maak_eenheid(maak_referentie_tuin())
    parkeerruimte = maak_parkeerruimte(
        detailsoort,
        oppervlakte=oppervlakte,
        aantal_adressen=aantal_adressen,
        aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
    )
    met_parkeerruimte = maak_eenheid(maak_referentie_tuin(), parkeerruimte)
    met_laadpaal = maak_eenheid(
        maak_referentie_tuin(),
        maak_parkeerruimte(
            detailsoort,
            oppervlakte=oppervlakte,
            aantal_adressen=aantal_adressen,
            aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
            met_laadpaal=True,
        ),
    )

    punten_ruimte = {}
    punten_laadpaal = {}
    for rubriek in (RUBRIEK_8, RUBRIEK_10, RUBRIEK_12):
        basis = som_punten(stelsel, rubriek, zonder_parkeerruimte)
        met_ruimte = som_punten(stelsel, rubriek, met_parkeerruimte)
        met_paal = som_punten(stelsel, rubriek, met_laadpaal)
        punten_ruimte[rubriek] = met_ruimte - basis
        punten_laadpaal[rubriek] = met_paal - met_ruimte

    rubrieken_met_ruimtepunten = [
        rubriek for rubriek, punten in punten_ruimte.items() if punten != 0
    ]
    rubrieken_met_laadpaalpunten = [
        rubriek for rubriek, punten in punten_laadpaal.items() if punten != 0
    ]

    assert len(rubrieken_met_ruimtepunten) <= 1, (
        f"{detailsoort.naam} ({oppervlakte}m2, {aantal_adressen} adressen, "
        f"{aantal_onzelfstandige_woonruimten} onzelfstandige woonruimten) krijgt punten "
        f"in meerdere rubrieken: {punten_ruimte}"
    )
    assert len(rubrieken_met_laadpaalpunten) <= 1, (
        f"De laadpaal bij {detailsoort.naam} ({oppervlakte}m2, {aantal_adressen} adressen, "
        f"{aantal_onzelfstandige_woonruimten} onzelfstandige woonruimten) krijgt punten "
        f"in meerdere rubrieken: {punten_laadpaal}"
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("stelsel", sorted(STELSELGROEP_CLASSES))
@pytest.mark.parametrize(
    "detailsoort, oppervlakte, aantal_adressen, aantal_onzelfstandige_woonruimten",
    list(
        product(
            DETAILSOORTEN,
            OPPERVLAKTEN,
            AANTALLEN_ADRESSEN,
            AANTALLEN_ONZELFSTANDIGE_WOONRUIMTEN,
        )
    ),
)
def test_laadpaal_krijgt_altijd_punten(
    stelsel,
    detailsoort,
    oppervlakte,
    aantal_adressen,
    aantal_onzelfstandige_woonruimten,
) -> None:
    """Regel 4: de laadpaal wordt in rubriek 10 óf in rubriek 12 gewaardeerd.

    Er is dus altijd precies één rubriek waarin de laadpaal punten oplevert.
    """
    zonder_laadpaal = maak_eenheid(
        maak_referentie_tuin(),
        maak_parkeerruimte(
            detailsoort,
            oppervlakte=oppervlakte,
            aantal_adressen=aantal_adressen,
            aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
        ),
    )
    met_laadpaal = maak_eenheid(
        maak_referentie_tuin(),
        maak_parkeerruimte(
            detailsoort,
            oppervlakte=oppervlakte,
            aantal_adressen=aantal_adressen,
            aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
            met_laadpaal=True,
        ),
    )

    verwachte_punten = Decimal("2") / Decimal(
        aantal_adressen * aantal_onzelfstandige_woonruimten
    )
    winst = {
        rubriek: som_punten(stelsel, rubriek, met_laadpaal)
        - som_punten(stelsel, rubriek, zonder_laadpaal)
        for rubriek in (RUBRIEK_8, RUBRIEK_10, RUBRIEK_12)
    }

    # De waardering wordt op twee decimalen afgerond (2 / 3 wordt 0,67).
    assert float(sum(winst.values())) == pytest.approx(
        float(verwachte_punten), abs=0.005
    ), f"Laadpaal levert {winst} op, verwacht {verwachte_punten} in precies één rubriek"
