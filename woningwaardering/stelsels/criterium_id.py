from enum import Enum

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    WoningwaarderingstelselgroepReferentiedata,
)


class GedeeldMetSoort(Enum):
    adressen = "adressen"
    onzelfstandige_woonruimten = "onzelfstandige_woonruimten"


class CriteriumId:
    def __init__(
        self,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        ruimte_id: str | None = None,
        criterium: str = "",
        gedeeld_met_aantal: int | None = None,
        gedeeld_met_soort: GedeeldMetSoort | None = None,
        is_totaal: bool = False,
        stelsel: WoningwaarderingstelselReferentiedata | None = None,
    ):
        self.stelselgroep = stelselgroep
        self.ruimte_id = ruimte_id
        self.criterium = criterium
        self.gedeeld_met_aantal = gedeeld_met_aantal
        self.gedeeld_met_soort = gedeeld_met_soort
        self.is_totaal = is_totaal
        self.stelsel = stelsel

    @classmethod
    def blad_ruimte(
        cls,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        ruimte_id: str | None,
        *,
        stelsel: WoningwaarderingstelselReferentiedata | None = None,
    ) -> "CriteriumId":
        """Bladregel gekoppeld aan een ruimte (geen ``totaal``-segment)."""
        return cls(stelselgroep=stelselgroep, ruimte_id=ruimte_id, stelsel=stelsel)

    @classmethod
    def blad_criterium(
        cls,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        criterium: str,
        *,
        ruimte_id: str | None = None,
        stelsel: WoningwaarderingstelselReferentiedata | None = None,
    ) -> "CriteriumId":
        """Bladregel op eenheids- of rubriekniveau (label, factor, correctie, …)."""
        return cls(
            stelselgroep=stelselgroep,
            ruimte_id=ruimte_id,
            criterium=criterium,
            stelsel=stelsel,
        )

    @classmethod
    def totaal_deel(
        cls,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        gedeeld_met_aantal: int,
        gedeeld_met_soort: GedeeldMetSoort | None = None,
        *,
        stelsel: WoningwaarderingstelselReferentiedata | None = None,
    ) -> "CriteriumId":
        """Aggregaat op deel-dimensie (privé / gedeeld met N)."""
        return cls(
            stelselgroep=stelselgroep,
            is_totaal=True,
            gedeeld_met_aantal=gedeeld_met_aantal,
            gedeeld_met_soort=gedeeld_met_soort,
            stelsel=stelsel,
        )

    @classmethod
    def totaal_subgroep(
        cls,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
        subgroep_segment: str,
        gedeeld_met_aantal: int,
        gedeeld_met_soort: GedeeldMetSoort | None = None,
        *,
        stelsel: WoningwaarderingstelselReferentiedata | None = None,
    ) -> "CriteriumId":
        """Aggregaat voor een benoemde subgroep (bv. verkoeling) inclusief bucket."""
        return cls(
            stelselgroep=stelselgroep,
            criterium=subgroep_segment,
            is_totaal=True,
            gedeeld_met_aantal=gedeeld_met_aantal,
            gedeeld_met_soort=gedeeld_met_soort,
            stelsel=stelsel,
        )

    def _gebruik_prive_bucket(self) -> bool:
        """Of segment ``prive`` in het id hoort (onz. altijd bij aantal ≤ 1; zelfstandig niet)."""
        if self.stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten:
            return False
        return True

    def __str__(self) -> str:
        """Genereert de criterium id string."""
        onderdelen = [self.stelselgroep.name]

        if self.ruimte_id is not None:
            onderdelen.append(self.ruimte_id)

        if self.is_totaal:
            onderdelen.append("totaal")

        if self.criterium:
            onderdelen.append(self.criterium)

        if self.gedeeld_met_aantal:
            if self.gedeeld_met_aantal <= 1:
                if self._gebruik_prive_bucket():
                    onderdelen.append("prive")
            else:
                onderdelen.extend(["gedeeld_met", str(self.gedeeld_met_aantal)])
                if self.gedeeld_met_soort:
                    onderdelen.append(self.gedeeld_met_soort.value)

        return "__".join(onderdelen).strip("__")


def criterium_segment_na_totaal(criterium_id: str) -> str | None:
    """
    Het ``criterium``-segment direct na ``totaal``, indien aanwezig.

    Retourneert ``None`` bij totalen zonder subgroep-segment (alleen bucket).
    """
    parts = criterium_id.split("__")
    try:
        totaal_index = parts.index("totaal")
    except ValueError:
        return None
    if totaal_index + 1 >= len(parts):
        return None
    volgend = parts[totaal_index + 1]
    if volgend in ("gedeeld_met", "prive"):
        return None
    return volgend


def naam_uit_subgroep_criterium_id(criterium_id: str) -> str:
    """Weergavenaam van een subgroep uit een criterium-id (segment na ``totaal``)."""
    criterium = criterium_segment_na_totaal(criterium_id)
    if criterium is None:
        parts = criterium_id.split("__")
        criterium = parts[-1]
    return criterium.replace("_", " ").capitalize()


def validate_criterium_ids_in_groep(
    woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
) -> list[str]:
    """
    Controleert invarianten voor criterium-id's in een stelselgroep-output.

    Args:
        woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep):
            Output van één stelselgroep.

    Returns:
        list[str]: Foutmeldingen; leeg indien alles geldig is.
    """
    fouten: list[str] = []
    waarderingen = woningwaardering_groep.woningwaarderingen or []
    ids: dict[str, int] = {}

    for waardering in waarderingen:
        if waardering.criterium is None or not waardering.criterium.id:
            continue
        cid = waardering.criterium.id
        ids[cid] = ids.get(cid, 0) + 1

    for cid, count in ids.items():
        if count > 1:
            fouten.append(f"Dubbel criterium.id: {cid!r} ({count}x)")

    id_set = set(ids)
    for waardering in waarderingen:
        if waardering.criterium is None:
            continue
        parent = waardering.criterium.bovenliggende_criterium
        if parent is None or not parent.id:
            continue
        if parent.id not in id_set:
            fouten.append(
                f"bovenliggendeCriterium {parent.id!r} bestaat niet als output-regel"
            )
        if waardering.criterium.id == parent.id:
            fouten.append(
                f"Criterium {waardering.criterium.id!r} verwijst naar zichzelf als parent"
            )

    # Acyclic check (diepte beperkt tot aantal regels in één groep)
    for start in waarderingen:
        if start.criterium is None or not start.criterium.id:
            continue
        bezocht: set[str] = set()
        huidig_id: str | None = start.criterium.id
        while huidig_id:
            if huidig_id in bezocht:
                fouten.append(
                    f"Cyclische bovenliggendeCriterium-keten bij {huidig_id!r}"
                )
                break
            bezocht.add(huidig_id)
            parent_id = _parent_id_voor_criterium(waarderingen, huidig_id)
            huidig_id = parent_id

    return fouten


def _parent_id_voor_criterium(
    waarderingen: list[WoningwaarderingResultatenWoningwaardering],
    criterium_id: str,
) -> str | None:
    for waardering in waarderingen:
        if waardering.criterium and waardering.criterium.id == criterium_id:
            parent = waardering.criterium.bovenliggende_criterium
            return parent.id if parent else None
    return None
