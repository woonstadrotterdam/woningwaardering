"""Builders die tijdens een ``waardeer()``-aanroep een woningwaarderingsgroep opbouwen.

De builders werken via compositie: ze houden de waarderingen-in-opbouw bij met
hun onderlinge bovenliggende/onderliggende-relaties en produceren pas bij
:meth:`WaarderingsgroepBouwer.bouw` kale VERA-objecten
(``WoningwaarderingResultatenWoningwaarderingGroep`` met platte
``woningwaarderingen``). De output blijft daardoor zuiver VERA; de builders zelf
lekken niet in het resultaat.

De hiërarchie tussen waarderingen is in VERA een platte lijst met
``bovenliggende_criterium``-verwijzingen. ``bouw()`` loopt alle waarderingen af
(elke bovenliggende vóór wat eronder hangt) en zet die verwijzingen.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Iterator

from woningwaardering.stelsels.criterium import (
    GedeeldMetSoort,
    naam_gedeeld_met_groep,
)
from woningwaardering.vera.bvg.generated import (
    Referentiedata,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
)


class WaarderingBouwer:
    """Een waardering-in-opbouw die een ``WoningwaarderingResultatenWoningwaardering`` representeert.

    Een waardering kent zijn eigen id-segment, zijn bovenliggende en zijn
    onderliggende waarderingen. De volledige criterium-id (pad-id) en de
    ``bovenliggende_criterium``-verwijzing worden pas afgeleid uit de
    bouwer-hiërarchie (via ``criterium_id`` / ``bovenliggende_id``), zodat het
    verplaatsen van een waardering geen id-herberekening vergt. ``punten``,
    ``aantal``, ``naam`` en ``meeteenheid`` mogen na creatie nog aangepast worden
    (bijvoorbeeld voor een deler-correctie).
    """

    def __init__(
        self,
        *,
        segment: str,
        naam: str,
        bovenliggende: "WaarderingBouwer | WaarderingsgroepBouwer",
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
        opslagpercentage: float | None = None,
    ) -> None:
        self._segment = segment
        self.naam = naam
        self.punten = punten
        self.aantal = aantal
        self.meeteenheid = meeteenheid
        self.opslagpercentage = opslagpercentage
        self._bovenliggende = bovenliggende
        self._onderliggende: list[WaarderingBouwer] = []

    @property
    def segment(self) -> str:
        """Het eigen id-segment van deze waardering (het laatste deel van de criterium-id)."""
        return self._segment

    @property
    def bovenliggende(self) -> "WaarderingBouwer | WaarderingsgroepBouwer":
        """De bovenliggende bouwer of groep waaronder deze waardering hangt."""
        return self._bovenliggende

    @property
    def criterium_id(self) -> str:
        """De volledige criterium-id (pad-id), afgeleid uit de bouwer-hiërarchie."""
        return f"{self._bovenliggende._id_prefix}__{self._segment}"

    @property
    def _id_prefix(self) -> str:
        return self.criterium_id

    def maak_onderliggende(
        self,
        *,
        id: str | None,
        naam: str | None,
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
    ) -> "WaarderingBouwer":
        """Maak een onderliggende waardering en hang die onder deze waardering.

        De volledige criterium-id wordt ``{deze.criterium_id}__{id}`` en
        ``bovenliggende_criterium`` verwijst naar deze waardering.
        """
        return _voeg_onderliggende_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
            punten=punten,
            aantal=aantal,
            meeteenheid=meeteenheid,
        )

    def verplaats_naar(
        self, nieuwe_bovenliggende: "WaarderingBouwer | WaarderingsgroepBouwer"
    ) -> "WaarderingBouwer":
        """Verplaats deze waardering (met alles eronder) naar onder ``nieuwe_bovenliggende``.

        De waardering wordt losgekoppeld van haar huidige bovenliggende en onder
        ``nieuwe_bovenliggende`` gehangen; haar criterium-id (en die van alles
        eronder) verandert vanzelf mee, omdat die uit de hiërarchie wordt afgeleid.
        """
        self._loskoppelen()
        self._bovenliggende = nieuwe_bovenliggende
        nieuwe_bovenliggende._onderliggende.append(self)
        return self

    def gedeeld_met(
        self,
        *,
        aantal: int,
        soort: GedeeldMetSoort,
    ) -> "WaarderingBouwer":
        """Geef de (gededupliceerde) gedeeld-met/``prive``-waardering onder deze waardering."""
        return _voeg_gedeeld_met_toe(
            self,
            aantal=aantal,
            soort=soort,
        )

    def verwijder(self) -> None:
        """Koppel deze waardering (en wat eronder hangt) los van zijn bovenliggende (voor het bouw-dan-weggooien-patroon)."""
        self._loskoppelen()

    def _loskoppelen(self) -> None:
        self._bovenliggende._onderliggende.remove(self)

    @property
    def is_leeg(self) -> bool:
        """Of deze waardering (nog) geen onderliggende waarderingen heeft."""
        return not self._onderliggende

    @property
    def bovenliggende_id(self) -> str | None:
        """De criterium-id van het bovenliggende criterium (``None`` als direct onder de groep)."""
        if isinstance(self._bovenliggende, WaarderingBouwer):
            return self._bovenliggende.criterium_id
        return None

    def _zelf_en_onderliggende(self) -> Iterator["WaarderingBouwer"]:
        yield self
        for onderliggende in self._onderliggende:
            yield from onderliggende._zelf_en_onderliggende()

    def _naar_waardering(self) -> WoningwaarderingResultatenWoningwaardering:
        # De hiërarchie tussen waarderingen wordt in VERA vastgelegd via
        # ``bovenliggende_criterium`` (en spiegelt het id-pad). Voor waarderingen
        # direct onder de groep is er geen bovenliggend criterium.
        bovenliggende_id = self.bovenliggende_id
        criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
            naam=self.naam or "",
            id=self.criterium_id,
            meeteenheid=self.meeteenheid,
        )
        if bovenliggende_id is not None:
            criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                id=bovenliggende_id
            )
        waardering = WoningwaarderingResultatenWoningwaardering(
            criterium=criterium,
            punten=float(self.punten) if self.punten is not None else None,
            aantal=float(self.aantal) if self.aantal is not None else None,
        )
        if self.opslagpercentage is not None:
            waardering.opslagpercentage = self.opslagpercentage
        return waardering


class WaarderingsgroepBouwer:
    """Verzamelt de waarderingen van één stelselgroep en bouwt daar het VERA-resultaat uit.

    Hang waarderingen onder de groep met :meth:`maak_onderliggende` en gedeeld-met-
    criteria met :meth:`gedeeld_met` (dat een al bestaande laag hergebruikt). Sluit
    af met :meth:`bouw`, dat de ``WoningwaarderingResultatenWoningwaarderingGroep``
    oplevert.
    """

    def __init__(
        self,
        stelsel: Referentiedata,
        stelselgroep: Referentiedata,
    ) -> None:
        self.stelsel = stelsel
        self.stelselgroep = stelselgroep
        self._onderliggende: list[WaarderingBouwer] = []

    def maak_onderliggende(
        self,
        *,
        id: str | None,
        naam: str | None,
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
    ) -> WaarderingBouwer:
        """Maak een waardering direct onder de groep (zonder ``bovenliggende_criterium``)."""
        return _voeg_onderliggende_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
            punten=punten,
            aantal=aantal,
            meeteenheid=meeteenheid,
        )

    def gedeeld_met(
        self,
        *,
        aantal: int,
        soort: GedeeldMetSoort,
    ) -> WaarderingBouwer:
        """Geef de (gededupliceerde) gedeeld-met/``prive``-waardering direct onder de groep."""
        return _voeg_gedeeld_met_toe(
            self,
            aantal=aantal,
            soort=soort,
        )

    def gedeeld_met_laag(
        self,
        *,
        aantal_eenheden: int,
        aantal_onzelfstandige_woonruimten: int = 1,
    ) -> WaarderingBouwer:
        """Geef de gedeeld-met-laag voor adressen en optioneel onzelfstandige woonruimten.

        Bij gedeelde gemeenschappelijke ruimten ontstaat een hiërarchie van
        gedeeld-met-criteria: eerst (indien van toepassing) gedeeld met
        onzelfstandige woonruimten, daarna gedeeld met adressen. Bij geen
        deling op beide niveaus wordt een enkele ``prive``-waardering teruggegeven.
        """
        onz_laag = None
        if aantal_onzelfstandige_woonruimten > 1:
            onz_laag = self.gedeeld_met(
                aantal=aantal_onzelfstandige_woonruimten,
                soort=GedeeldMetSoort.onzelfstandige_woonruimten,
            )

        if aantal_onzelfstandige_woonruimten < 2 and aantal_eenheden < 2:
            return self.gedeeld_met(
                aantal=1,
                soort=GedeeldMetSoort.adressen,
            )
        if aantal_eenheden > 1:
            tussen_bouwer: WaarderingsgroepBouwer | WaarderingBouwer = (
                onz_laag if onz_laag is not None else self
            )
            return tussen_bouwer.gedeeld_met(
                aantal=aantal_eenheden,
                soort=GedeeldMetSoort.adressen,
            )
        return onz_laag or self.gedeeld_met(
            aantal=1,
            soort=GedeeldMetSoort.adressen,
        )

    def alle_waarderingen(self) -> Iterator[WaarderingBouwer]:
        """Loop door alle tot nu toe opgebouwde waarderingen (elke bovenliggende vóór wat eronder hangt)."""
        for onderliggende in self._onderliggende:
            yield from onderliggende._zelf_en_onderliggende()

    def bouw(self) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """Bouw de VERA-woningwaarderingsgroep uit de opgebouwde hiërarchie.

        De boom wordt platgeslagen tot een lijst ``woningwaarderingen`` (elke
        bovenliggende komt vóór zijn onderliggende) en de groepspunten worden
        gesommeerd.
        """
        from woningwaardering.stelsels.utils import som_punten_waarderingen

        groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )
        groep.woningwaarderingen = [
            waardering._naar_waardering() for waardering in self.alle_waarderingen()
        ]
        groep.punten = som_punten_waarderingen(groep.woningwaarderingen)
        return groep

    @property
    def _id_prefix(self) -> str:
        if self.stelselgroep is None or self.stelselgroep.name is None:
            raise ValueError(
                "De groep heeft geen stelselgroep met naam om de id-prefix uit af te leiden."
            )
        return self.stelselgroep.name


def _voeg_onderliggende_toe(
    waarderingsgroep_bouwer: WaarderingBouwer | WaarderingsgroepBouwer,
    *,
    segment: str,
    naam: str,
    punten: float | Decimal | None,
    aantal: float | int | Decimal | None,
    meeteenheid: Referentiedata | None,
) -> WaarderingBouwer:
    onderliggende = WaarderingBouwer(
        segment=segment,
        naam=naam,
        bovenliggende=waarderingsgroep_bouwer,
        punten=punten,
        aantal=aantal,
        meeteenheid=meeteenheid,
    )
    waarderingsgroep_bouwer._onderliggende.append(onderliggende)
    return onderliggende


def _voeg_gedeeld_met_toe(
    waarderingsgroep_bouwer: WaarderingBouwer | WaarderingsgroepBouwer,
    *,
    aantal: int,
    soort: GedeeldMetSoort,
) -> WaarderingBouwer:
    if aantal <= 1:
        segment = "prive"
        naam = naam_gedeeld_met_groep(1)
    else:
        segment = f"gedeeld_met_{aantal}_{soort.value}"
        naam = naam_gedeeld_met_groep(aantal, soort=soort)

    # Hergebruik de gedeeld-met-laag als die er onder deze bovenliggende al is.
    for bestaand in waarderingsgroep_bouwer._onderliggende:
        if bestaand._segment == segment:
            return bestaand

    onderliggende = WaarderingBouwer(
        segment=segment,
        naam=naam,
        bovenliggende=waarderingsgroep_bouwer,
    )
    waarderingsgroep_bouwer._onderliggende.append(onderliggende)
    return onderliggende
