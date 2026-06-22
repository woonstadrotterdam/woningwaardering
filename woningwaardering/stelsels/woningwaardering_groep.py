from __future__ import annotations

from decimal import Decimal
from typing import Any

from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.vera.bvg.generated import (
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    WoningwaarderingstelselgroepReferentiedata,
)


class Waardering:
    """Keten-handle voor een uitgegeven waardering (output-element).

    Een ``Waardering`` is een dunne handle om een ``CriteriumId`` plus de
    ``woningwaarderingen``-lijst van de groep. Elke ``met_onderliggend(...)`` voegt
    een onderliggende waardering toe aan die lijst en geeft een nieuwe ``Waardering``
    terug zodat je daar weer onder kunt ketenen.

    Structurele criteria (alleen ``naam``, geen ``punten``/``aantal``) worden
    uitgesteld tot er een onderliggend criterium onder wordt gehangen.
    Waardecriteria (``punten`` of ``aantal``) worden direct uitgegeven.

    Let op: dit is de keten-handle, niet het VERA-model
    ``WoningwaarderingResultatenWoningwaardering`` (dat wordt intern aangemaakt en
    aan de groep toegevoegd).
    """

    __slots__ = (
        "_criterium_id",
        "_woningwaarderingen",
        "_bovenliggende_waardering",
        "_uitgestelde_waardering",
    )

    def __init__(
        self,
        criterium_id: CriteriumId,
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
        *,
        bovenliggende_waardering: Waardering | None = None,
        uitgestelde_waardering: dict[str, Any] | None = None,
    ) -> None:
        self._criterium_id = criterium_id
        self._woningwaarderingen = woningwaarderingen
        self._bovenliggende_waardering = bovenliggende_waardering
        self._uitgestelde_waardering = uitgestelde_waardering

    def _materialiseer(self) -> None:
        if self._uitgestelde_waardering is None:
            return
        if self._bovenliggende_waardering is not None:
            self._bovenliggende_waardering._materialiseer()
        uitgesteld, self._uitgestelde_waardering = self._uitgestelde_waardering, None
        self._woningwaarderingen.append(self._criterium_id.met_waardering(**uitgesteld))

    def met_onderliggend(
        self,
        criteriumid_toevoeging: str,
        *,
        naam: str | None = None,
        punten: float | Decimal | None = None,
        aantal: float | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
    ) -> Waardering:
        """Voegt een onderliggende waardering toe en geeft een handle daarop terug."""
        self._materialiseer()
        onderliggend = self._criterium_id.met_onderliggend(criteriumid_toevoeging)
        handle = Waardering(
            onderliggend,
            self._woningwaarderingen,
            bovenliggende_waardering=self,
            uitgestelde_waardering={
                "naam": naam,
                "punten": punten,
                "aantal": aantal,
                "meeteenheid": meeteenheid,
            },
        )
        if punten is not None or aantal is not None:
            handle._materialiseer()
        return handle

    def met_gedeeld_met_criterium(
        self,
        aantal: int,
        soort: GedeeldMetSoort | None = None,
        *,
        naam: str,
    ) -> Waardering:
        """Structureel gedeeld_met_criterium onder dit criterium (uitgesteld)."""
        onderliggend = self._criterium_id.gedeeld_met_criterium(aantal, soort)
        return Waardering(
            onderliggend,
            self._woningwaarderingen,
            bovenliggende_waardering=self,
            uitgestelde_waardering={
                "naam": naam,
                "punten": None,
                "aantal": None,
                "meeteenheid": None,
            },
        )


class WoningwaarderingGroep(WoningwaarderingResultatenWoningwaarderingGroep):
    """Woningwaarderinggroep met een keten-API zodat waarderingen niet handmatig
    aan ``woningwaarderingen`` hoeven te worden toegevoegd.

    De groep zelf is de niet-uitgegeven root (het stelselgroepcriterium staat in
    ``criteriumGroep``). ``met_onderliggend(...)`` voegt daarom een top-level
    waardering toe (direct onder het stelselgroepcriterium).
    """

    woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering]

    def __init__(
        self,
        *,
        stelsel: WoningwaarderingstelselReferentiedata,
        stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    ) -> None:
        super().__init__(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=stelsel,
                stelselgroep=stelselgroep,
            ),
            woningwaarderingen=[],
        )

    def _stelselgroep_waardering(self) -> Waardering:
        if self.criterium_groep is None or self.criterium_groep.stelselgroep is None:
            raise ValueError("criterium_groep.stelselgroep is verplicht")
        if self.woningwaarderingen is None:
            self.woningwaarderingen = []
        stelselgroep = self.criterium_groep.stelselgroep
        if not isinstance(stelselgroep, WoningwaarderingstelselgroepReferentiedata):
            raise TypeError(
                "stelselgroep moet WoningwaarderingstelselgroepReferentiedata zijn"
            )
        return Waardering(
            CriteriumId.voor_stelselgroep(stelselgroep), self.woningwaarderingen
        )

    def met_onderliggend(
        self,
        criteriumid_toevoeging: str,
        *,
        naam: str | None = None,
        punten: float | Decimal | None = None,
        aantal: float | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
    ) -> Waardering:
        """Voegt een top-level waardering toe (onder het stelselgroepcriterium) en
        geeft een handle daarop terug."""
        return self._stelselgroep_waardering().met_onderliggend(
            criteriumid_toevoeging,
            naam=naam,
            punten=punten,
            aantal=aantal,
            meeteenheid=meeteenheid,
        )

    def met_gedeeld_met_criterium(
        self,
        aantal: int,
        soort: GedeeldMetSoort | None = None,
        *,
        naam: str,
    ) -> Waardering:
        """Structureel gedeeld_met_criterium onder het stelselgroepcriterium."""
        return self._stelselgroep_waardering().met_gedeeld_met_criterium(
            aantal, soort, naam=naam
        )
