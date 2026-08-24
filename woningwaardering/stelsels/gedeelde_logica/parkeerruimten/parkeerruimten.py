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
    Ruimtedetailsoort,
)

# 2.10.3 Punten per soort parkeerplek
# | Type I: parkeerplek in een afgesloten parkeergarage behorende tot een complex | 9 |
# | Type II: parkeerplek buiten behorende tot het complex of de woning met dak    | 6 |
# | Type III: parkeerplek buiten behorende tot het complex of de woning zonder dak| 4 |
TYPE_I = "Type I"
TYPE_II = "Type II"
TYPE_III = "Type III"

PARKEERTYPE_PUNTEN: dict[str, Decimal] = {
    TYPE_I: Decimal("9.0"),
    TYPE_II: Decimal("6.0"),
    TYPE_III: Decimal("4.0"),
}

# Kerntypen: de detailsoorten die één-op-één een Type I/II/III-parkeerplek zijn.
# Zij staan altijd in een gemeenschappelijke parkeergelegenheid en worden daarom
# altijd in rubriek 10 gewaardeerd, ook wanneer de plek zelf privé is.
KERNTYPE_PARKEERTYPE: dict[Referentiedata, str] = {
    Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage: TYPE_I,
    Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage: TYPE_II,
    Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex: TYPE_III,
}

# Overige parkeerruimten: privé horen zij in rubriek 8, gemeenschappelijk in
# rubriek 10. Een gemeenschappelijke carport telt daar als Type II, een
# gemeenschappelijke parkeerplaats als Type III (met een UserWarning, omdat
# `parkeerplaats` een privé-detailsoort is).
OVERIGE_PARKEERTYPE: dict[Referentiedata, str] = {
    Ruimtedetailsoort.carport: TYPE_II,
    Ruimtedetailsoort.parkeerplaats: TYPE_III,
}

# Deze parkeergelegenheden zijn vervallen en worden vervangen door de kerntypen:
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


def is_kerntype_parkeerruimte(detail_soort: Referentiedata | None) -> bool:
    """Of de detailsoort een kerntype (`PIP`, `PUP`, `PBC`) is.

    Kerntypen staan altijd in een gemeenschappelijke parkeergelegenheid en
    worden daarom altijd in rubriek 10 gewaardeerd, privé of gemeenschappelijk.
    """
    return detail_soort in KERNTYPE_PARKEERTYPE


def is_overige_parkeerruimte(detail_soort: Referentiedata | None) -> bool:
    """Of de detailsoort een overige parkeerruimte (`carport`, `parkeerplaats`) is.

    Deze gaan privé naar rubriek 8 en gemeenschappelijk naar rubriek 10.
    """
    return detail_soort in OVERIGE_PARKEERTYPE


def is_parkeerruimte(detail_soort: Referentiedata | None) -> bool:
    """Of de detailsoort onder de parkeerregels valt."""
    return is_kerntype_parkeerruimte(detail_soort) or is_overige_parkeerruimte(
        detail_soort
    )


def is_gemeenschappelijke_parkeerruimte(ruimte: EenhedenRuimte) -> bool:
    """Of de parkeerruimte gemeenschappelijk is.

    Gemeenschappelijk betekent dat het aantal adressen en/of het aantal
    onzelfstandige woonruimten groter is dan 1. Privé is het spiegelbeeld
    daarvan: ``utils.is_prive``.

    De deler die bij deze indeling hoort is ``utils.deler``: het aantal adressen
    maal het aantal onzelfstandige woonruimten (2.10.4 Rekenmethode).
    """
    return not is_prive(ruimte)


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
    return KERNTYPE_PARKEERTYPE.get(detail_soort) or OVERIGE_PARKEERTYPE.get(
        detail_soort
    )


def wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(
    ruimte: EenhedenRuimte,
) -> bool:
    """Of de ruimte in rubriek 10 hoort (los van de 12 m²-eis).

    Kerntypen horen er altijd in; overige parkeerruimten alleen wanneer ze
    gemeenschappelijk zijn. Overige ruimtedetailsoorten vallen buiten de
    parkeerregels.
    """
    if is_kerntype_parkeerruimte(ruimte.detail_soort):
        return True
    if is_overige_parkeerruimte(ruimte.detail_soort):
        return is_gemeenschappelijke_parkeerruimte(ruimte)
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
    """
    return wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(
        ruimte
    ) and voldoet_aan_oppervlakte_eis(ruimte)
