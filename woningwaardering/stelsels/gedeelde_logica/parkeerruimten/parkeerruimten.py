"""Eén regelset voor parkeerruimten en de laadpalen daarop.

Deze module bepaalt op één plek of een parkeerruimte privé of gemeenschappelijk
is, in welke rubriek zij thuishoort en met welke deler zij wordt gewaardeerd.
Rubriek 8 (Buitenruimten), rubriek 10 (Gemeenschappelijke parkeerruimten) en
rubriek 12 (Bijzondere voorzieningen) gebruiken deze functies, zodat een
parkeerruimte en een laadpaal nooit in meer dan één rubriek punten krijgen.

De regels gelden voor zelfstandige én onzelfstandige woonruimten; alleen de
deler verschilt (bij zelfstandige woonruimten is het aantal onzelfstandige
woonruimten 1).

Dit is de VERA-kant van de beleidsregels; zie de implementatietoelichtingen
bij §2.8, §2.10 en §2.12 voor de herkomst per regel.
"""

from decimal import Decimal

from woningwaardering.stelsels.utils import is_prive
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
)
from woningwaardering.vera.utils import aantal_bouwkundige_elementen

# 2.10.3 Punten per soort parkeerplek
# | Type I: een parkeerplek in een afgesloten parkeergarage behorende tot een complex | 9 |
# | Type II: een parkeerplek buiten behorende tot het complex of de woning met dak    | 6 |
# | Type III: een parkeerplek buiten behorende tot het complex of de woning zonder dak| 4 |
TYPE_I = "Type I"
TYPE_II = "Type II"
TYPE_III = "Type III"

PARKEERTYPE_PUNTEN: dict[str, Decimal] = {
    TYPE_I: Decimal("9.0"),
    TYPE_II: Decimal("6.0"),
    TYPE_III: Decimal("4.0"),
}

# `PIP`, `PUP`, `PBD`, `PBC`: altijd GPA (rubriek 10), ook wanneer de plek aan
# één adres is toegewezen.
#
# Het type volgt de wettekst: bepalend is of de plek in een afgesloten
# parkeergarage ligt (Type I) en anders of zij een dak heeft (Type II) of niet
# (Type III). In- of uitpandig maakt voor het type niets uit, en daarom leveren
# `PIP` en `PUP` allebei Type I; `carport` en `parkeerplaats` gaan privé naar BUI of gemeenschappelijk
# naar GPA (zie `PARKEERTYPE_BUI_OF_GPA`).
PARKEERTYPE_ALTIJD_GPA: dict[Referentiedata, str] = {
    Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage: TYPE_I,
    Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage: TYPE_I,
    Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex: TYPE_II,
    Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex: TYPE_III,
}

# `carport` en `parkeerplaats`: privé BUI (rubriek 8), gemeenschappelijk GPA
# (rubriek 10). Een gemeenschappelijke carport telt daar als Type II (2.10.3:
# "hieronder telt een carport"), een gemeenschappelijke parkeerplaats als Type
# III (met een UserWarning, omdat `parkeerplaats` een privé-detailsoort is).
PARKEERTYPE_BUI_OF_GPA: dict[Referentiedata, str] = {
    Ruimtedetailsoort.carport: TYPE_II,
    Ruimtedetailsoort.parkeerplaats: TYPE_III,
}

# Deze parkeergelegenheden zijn vervallen en worden vervangen door de
# Type-detailsoorten:
# https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/110#issuecomment-2190641829
VERVALLEN_PARKEERGARAGE_DETAILSOORTEN: list[Referentiedata] = [
    Ruimtedetailsoort.open_parkeergarage_niet_specifieke_plek,
    Ruimtedetailsoort.open_parkeergarage_specifieke_plek,
    Ruimtedetailsoort.parkeergarage_niet_specifieke_plek,
    Ruimtedetailsoort.specifieke_parkeerplek_in_parkeergarage,
]

# 2.10.3 Een parkeerplek is een afgebakend vak en heeft een oppervlakte van
# minimaal 12 m² waarin een gangbare personenauto in zijn geheel past.
MINIMALE_OPPERVLAKTE_PARKEERVAK = 12.0

# 2.10.5 / 2.12.3 Laadpalen: 2 punten per laadpaal.
PUNTEN_PER_LAADPAAL = Decimal("2.0")


def hoort_altijd_in_gemeenschappelijke_parkeerruimten(
    detail_soort: Referentiedata | None,
) -> bool:
    """Of de detailsoort een Type I/II/III-detailsoort is (`PIP`, `PUP`, `PBD`, `PBC`).

    Zij worden altijd in rubriek 10 gewaardeerd, privé of gemeenschappelijk.
    """
    return detail_soort in PARKEERTYPE_ALTIJD_GPA


def hoort_prive_in_buitenruimten(detail_soort: Referentiedata | None) -> bool:
    """Of de detailsoort een VERA-buitenruimte is (`carport` of `parkeerplaats`).

    Zij gaan privé naar rubriek 8 en gemeenschappelijk naar rubriek 10.
    """
    return detail_soort in PARKEERTYPE_BUI_OF_GPA


def is_parkeerruimte(detail_soort: Referentiedata | None) -> bool:
    """Of de detailsoort onder de parkeerregels valt."""
    return hoort_altijd_in_gemeenschappelijke_parkeerruimten(
        detail_soort
    ) or hoort_prive_in_buitenruimten(detail_soort)


def parkeertype(ruimte: EenhedenRuimte) -> str | None:
    """Het Type I/II/III waarmee de ruimte in rubriek 10 wordt gewaardeerd.

    Geeft ``None`` als de ruimte niet in rubriek 10 thuishoort.
    """
    detail_soort = ruimte.detail_soort
    if (
        detail_soort is None
        or not wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(ruimte)
    ):
        return None
    return PARKEERTYPE_ALTIJD_GPA.get(detail_soort) or PARKEERTYPE_BUI_OF_GPA.get(
        detail_soort
    )


def wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(
    ruimte: EenhedenRuimte,
) -> bool:
    """Of de ruimte in rubriek 10 hoort (los van de 12 m²-eis).

    Type-detailsoorten (`PIP`, `PUP`, `PBD`, `PBC`) horen er altijd in;
    `carport` en `parkeerplaats` alleen wanneer ze gemeenschappelijk zijn.
    Overige ruimtedetailsoorten vallen buiten de parkeerregels.
    """
    if hoort_altijd_in_gemeenschappelijke_parkeerruimten(ruimte.detail_soort):
        return True
    if hoort_prive_in_buitenruimten(ruimte.detail_soort):
        return not is_prive(ruimte)
    return False


def voldoet_aan_oppervlakte_eis(ruimte: EenhedenRuimte) -> bool:
    """Of de parkeerruimte aan de 12 m²-eis van rubriek 10 voldoet.

    Een ontbrekende oppervlakte telt als 'voldoet niet'.
    """
    return (
        ruimte.oppervlakte is not None
        and ruimte.oppervlakte >= MINIMALE_OPPERVLAKTE_PARKEERVAK
    )


def krijgt_punten_in_gemeenschappelijke_parkeerruimten(ruimte: EenhedenRuimte) -> bool:
    """Of de ruimte in rubriek 10 daadwerkelijk punten krijgt.

    Dit bepaalt tevens waar de laadpaal wordt gewaardeerd: in rubriek 10 als de
    ruimte daar punten krijgt, anders in rubriek 12.

    Ontbreekt ``gedeeld_met_aantal_adressen``, dan wordt de deler als 1 gelezen
    (niet gedeeld), gelijk aan ``utils.deler``.
    """
    return wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(
        ruimte
    ) and voldoet_aan_oppervlakte_eis(ruimte)


def aantal_laadpalen(ruimte: EenhedenRuimte) -> int:
    """Het aantal laadpalen bij een ruimte, over alle parkeerplekken van die ruimte.

    ``Eenhedenruimte.aantal`` geeft aan hoeveel identieke parkeerplekken de
    ruimte vertegenwoordigt; de laadpalen worden per plek geteld. Rubriek 10 en
    rubriek 12 gebruiken dezelfde telling, zodat een plek niet meer of minder
    laadpaalpunten krijgt door in een andere rubriek te vallen.
    """
    return aantal_bouwkundige_elementen(
        ruimte, Bouwkundigelementdetailsoort.laadpaal
    ) * int(ruimte.aantal or 1)
