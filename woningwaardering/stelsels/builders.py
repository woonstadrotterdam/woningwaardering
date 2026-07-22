"""Builders die tijdens een ``waardeer()``-aanroep een woningwaarderingsgroep opbouwen.

De builders houden de hiërarchie bij met hun bovenliggende- en
onderliggende-relaties. Pas bij :meth:`WaarderingsgroepBuilder.bouw` ontstaat
een ``WoningwaarderingResultatenWoningwaarderingGroep`` met een platte lijst
``woningwaarderingen``.

Gebruik :meth:`gedeeld_met` voor gedeeld-met/``prive``-lagen, :meth:`categorie`
voor structurele tussenlagen (sanitair, keuken, …) en :meth:`met_onderliggend`
voor inhoudelijke waarderingen. Gedeeld-met-lagen en categorieën worden pas actief
(in de output) zodra er inhoud of waarde aan wordt toegevoegd.

De hiërarchie tussen waarderingen is in VERA een platte lijst met
``bovenliggende_criterium``-verwijzingen. ``bouw()`` loopt alle actieve
waarderingen af (elke bovenliggende vóór wat eronder hangt) en zet die
verwijzingen.
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


class WaarderingBuilder:
    """Een waardering-in-opbouw die een ``WoningwaarderingResultatenWoningwaardering`` representeert.

    Een waardering kent zijn eigen id-segment, zijn bovenliggende en zijn
    onderliggende waarderingen. De volledige criterium-id (pad-id) en de
    ``bovenliggende_criterium``-verwijzing worden pas afgeleid uit de
    builder-hiërarchie (via ``criterium_id`` / ``bovenliggende_id``), zodat het
    verplaatsen van een waardering geen id-herberekening vergt. ``punten``,
    ``aantal``, ``naam`` en ``meeteenheid`` mogen na creatie nog aangepast worden
    (bijvoorbeeld voor een deler-correctie).
    """

    naam: str
    punten: float | Decimal | None
    aantal: float | int | Decimal | None
    meeteenheid: Referentiedata | None
    opslagpercentage: float | None
    _segment: str
    _bovenliggende: "WaarderingBuilder | WaarderingsgroepBuilder"
    _actief: bool
    _onderliggende: list["WaarderingBuilder"]

    def __init__(
        self,
        *,
        segment: str,
        naam: str,
        bovenliggende: "WaarderingBuilder | WaarderingsgroepBuilder",
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
        opslagpercentage: float | None = None,
    ) -> None:
        self._bovenliggende = bovenliggende
        self._actief = False
        self._onderliggende = []
        self._segment = segment
        self.naam = naam
        self.meeteenheid = meeteenheid
        self.punten = punten
        self.aantal = aantal
        self.opslagpercentage = opslagpercentage

    def __setattr__(self, name: str, value: object) -> None:
        object.__setattr__(self, name, value)
        if (
            name in ("punten", "aantal", "opslagpercentage")
            and value is not None
            and not self._actief
        ):
            self._activeer()

    @property
    def segment(self) -> str:
        """Het eigen id-segment van deze waardering (het laatste deel van de criterium-id)."""
        return self._segment

    @property
    def bovenliggende(self) -> "WaarderingBuilder | WaarderingsgroepBuilder":
        """De bovenliggende builder of groep waaronder deze waardering hangt."""
        return self._bovenliggende

    @property
    def criterium_id(self) -> str:
        """De volledige criterium-id (pad-id), afgeleid uit de builder-hiërarchie."""
        return f"{self._bovenliggende._id_prefix}__{self._segment}"

    @property
    def _id_prefix(self) -> str:
        return self.criterium_id

    @property
    def _actieve_onderliggende(self) -> list["WaarderingBuilder"]:
        actief = [
            waardering for waardering in self._onderliggende if waardering._actief
        ]
        eigen = [
            waardering
            for waardering in actief
            if not _is_gedeeld_met_segment(waardering._segment)
        ]
        gedeeld = [
            waardering
            for waardering in actief
            if _is_gedeeld_met_segment(waardering._segment)
        ]
        return [*eigen, *gedeeld]

    def categorie(
        self,
        *,
        id: str | None,
        naam: str | None,
    ) -> "WaarderingBuilder":
        """Geef een (lazy) categorie-onderlaag onder deze waardering.

        De categorie wordt pas actief bij de eerste onderliggende of bij het zetten van
        ``punten``, ``aantal`` of ``opslagpercentage``.

        Een bestaande categorie met hetzelfde id-segment wordt teruggegeven in
        plaats van een nieuwe aan te maken.
        """
        return _voeg_categorie_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
        )

    def met_onderliggend(
        self,
        *,
        id: str | None,
        naam: str | None,
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
        hergebruik: bool = False,
    ) -> "WaarderingBuilder":
        """Maak een onderliggende waardering en hang die onder deze waardering.

        De volledige criterium-id wordt ``{deze.criterium_id}__{id}`` en
        ``bovenliggende_criterium`` verwijst naar deze waardering.

        Met ``hergebruik=True`` wordt een bestaande onderliggende met hetzelfde
        id-segment teruggegeven in plaats van een nieuwe aan te maken.
        """
        self._activeer()
        return _voeg_onderliggende_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
            punten=punten,
            aantal=aantal,
            meeteenheid=meeteenheid,
            hergebruik=hergebruik,
        )

    def verplaats_naar(
        self, nieuwe_bovenliggende: "WaarderingBuilder | WaarderingsgroepBuilder"
    ) -> "WaarderingBuilder":
        """Verplaats deze waardering (met alles eronder) naar onder ``nieuwe_bovenliggende``.

        De waardering wordt losgekoppeld van haar huidige bovenliggende en onder
        ``nieuwe_bovenliggende`` gehangen; haar criterium-id (en die van alles
        eronder) verandert vanzelf mee, omdat die uit de hiërarchie wordt afgeleid.
        """
        self._loskoppelen()
        self._bovenliggende = nieuwe_bovenliggende
        nieuwe_bovenliggende._onderliggende.append(self)
        self._actief = True
        return self

    def gedeeld_met(
        self,
        *,
        aantal_adressen: int = 1,
        aantal_onzelfstandige_woonruimten: int = 1,
    ) -> "WaarderingBuilder":
        """Geef de (gededupliceerde) gedeeld-met/``prive``-waardering onder deze waardering.

        Bij gedeelde gemeenschappelijke ruimten ontstaat een hiërarchie van
        gedeeld-met-criteria: eerst (indien van toepassing) gedeeld met
        onzelfstandige woonruimten, daarna gedeeld met adressen. Bij geen
        deling op beide niveaus wordt een enkele ``prive``-waardering teruggegeven.
        """
        return _gedeeld_met_lagen(
            self,
            aantal_adressen=aantal_adressen,
            aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
        )

    def verwijder(self) -> None:
        """Koppel deze waardering (en wat eronder hangt) los van zijn bovenliggende (voor het bouw-dan-weggooien-patroon)."""
        bovenliggende = self._bovenliggende
        self._loskoppelen()
        if (
            isinstance(bovenliggende, WaarderingBuilder)
            and bovenliggende._actief
            and not bovenliggende._actieve_onderliggende
        ):
            bovenliggende.verwijder()

    def _activeer(self) -> None:
        """Maak deze lazy waardering actief (en activeer pending bovenliggenden)."""
        if self._actief:
            return
        bovenliggende = self._bovenliggende
        if isinstance(bovenliggende, WaarderingBuilder):
            bovenliggende._activeer()
        self._actief = True

    def _loskoppelen(self) -> None:
        bovenliggende = self._bovenliggende
        if self in bovenliggende._onderliggende:
            bovenliggende._onderliggende.remove(self)
        self._actief = False

    @property
    def bovenliggende_id(self) -> str | None:
        """De criterium-id van het bovenliggende criterium (``None`` als direct onder de groep)."""
        if isinstance(self._bovenliggende, WaarderingBuilder):
            return self._bovenliggende.criterium_id
        return None

    def _zelf_en_onderliggende(self) -> Iterator["WaarderingBuilder"]:
        yield self
        for onderliggende in self._actieve_onderliggende:
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


class WaarderingsgroepBuilder:
    """Verzamelt de waarderingen van één stelselgroep en bouwt daar het VERA-resultaat uit.

    Hang inhoudelijke waarderingen onder de groep met :meth:`met_onderliggend`,
    gedeeld-met-criteria met :meth:`gedeeld_met` en structurele categorieën met
    :meth:`categorie`. Sluit af met :meth:`bouw`.
    """

    stelsel: Referentiedata
    stelselgroep: Referentiedata
    _onderliggende: list[WaarderingBuilder]

    def __init__(
        self,
        stelsel: Referentiedata,
        stelselgroep: Referentiedata,
    ) -> None:
        self.stelsel = stelsel
        self.stelselgroep = stelselgroep
        self._onderliggende = []

    @property
    def _actieve_onderliggende(self) -> list[WaarderingBuilder]:
        return [waardering for waardering in self._onderliggende if waardering._actief]

    def categorie(
        self,
        *,
        id: str | None,
        naam: str | None,
    ) -> WaarderingBuilder:
        """Geef een (lazy) categorie direct onder de groep.

        De categorie wordt pas actief bij de eerste onderliggende of bij het zetten van
        ``punten``, ``aantal`` of ``opslagpercentage``.

        Een bestaande categorie met hetzelfde id-segment wordt teruggegeven in
        plaats van een nieuwe aan te maken.
        """
        return _voeg_categorie_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
        )

    def met_onderliggend(
        self,
        *,
        id: str | None,
        naam: str | None,
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
        hergebruik: bool = False,
    ) -> WaarderingBuilder:
        """Maak een waardering direct onder de groep (zonder ``bovenliggende_criterium``).

        Met ``hergebruik=True`` wordt een bestaande onderliggende met hetzelfde
        id-segment teruggegeven in plaats van een nieuwe aan te maken.
        """
        return _voeg_onderliggende_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
            punten=punten,
            aantal=aantal,
            meeteenheid=meeteenheid,
            hergebruik=hergebruik,
        )

    def gedeeld_met(
        self,
        *,
        aantal_adressen: int = 1,
        aantal_onzelfstandige_woonruimten: int = 1,
    ) -> WaarderingBuilder:
        """Geef de gedeeld-met/``prive``-waardering direct onder de groep.

        Bij gedeelde gemeenschappelijke ruimten ontstaat een hiërarchie van
        gedeeld-met-criteria: eerst (indien van toepassing) gedeeld met
        onzelfstandige woonruimten, daarna gedeeld met adressen. Bij geen
        deling op beide niveaus wordt een enkele ``prive``-waardering teruggegeven.
        """
        return _gedeeld_met_lagen(
            self,
            aantal_adressen=aantal_adressen,
            aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
        )

    def alle_waarderingen(self) -> Iterator[WaarderingBuilder]:
        """Loop door alle tot nu toe opgebouwde waarderingen (elke bovenliggende vóór wat eronder hangt)."""
        for onderliggende in self._actieve_onderliggende:
            yield from onderliggende._zelf_en_onderliggende()

    def bouw(self) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """Bouw de VERA-woningwaarderingsgroep uit de opgebouwde hiërarchie.

        De boom wordt doorlopen (elke bovenliggende vóór zijn onderliggende) en
        de groepspunten worden gesommeerd.
        """
        from woningwaardering.stelsels.utils import som_punten_waarderingen

        groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )
        groep.woningwaarderingen = [
            waardering._naar_waardering()
            for onderliggende in self._actieve_onderliggende
            for waardering in onderliggende._zelf_en_onderliggende()
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


def _is_gedeeld_met_segment(segment: str) -> bool:
    return segment == "prive" or segment.startswith("gedeeld_met_")


def _voeg_onderliggende_toe(
    waarderingsgroep_builder: WaarderingBuilder | WaarderingsgroepBuilder,
    *,
    segment: str,
    naam: str,
    punten: float | Decimal | None,
    aantal: float | int | Decimal | None,
    meeteenheid: Referentiedata | None,
    hergebruik: bool = False,
) -> WaarderingBuilder:
    if hergebruik:
        for bestaand in waarderingsgroep_builder._onderliggende:
            if bestaand._actief and bestaand._segment == segment:
                return bestaand
    onderliggende = WaarderingBuilder(
        segment=segment,
        naam=naam,
        bovenliggende=waarderingsgroep_builder,
        punten=punten,
        aantal=aantal,
        meeteenheid=meeteenheid,
    )
    onderliggende._actief = True
    waarderingsgroep_builder._onderliggende.append(onderliggende)
    return onderliggende


def _voeg_categorie_toe(
    parent: WaarderingBuilder | WaarderingsgroepBuilder,
    *,
    segment: str,
    naam: str,
) -> WaarderingBuilder:
    for bestaand in parent._onderliggende:
        if bestaand._segment == segment:
            return bestaand
    categorie = WaarderingBuilder(
        segment=segment,
        naam=naam,
        bovenliggende=parent,
    )
    parent._onderliggende.append(categorie)
    return categorie


def _gedeeld_met_lagen(
    builder: WaarderingBuilder | WaarderingsgroepBuilder,
    *,
    aantal_adressen: int,
    aantal_onzelfstandige_woonruimten: int,
) -> WaarderingBuilder:
    onz_laag = None
    if aantal_onzelfstandige_woonruimten > 1:
        onz_laag = _voeg_gedeeld_met_toe(
            builder,
            aantal=aantal_onzelfstandige_woonruimten,
            soort=GedeeldMetSoort.onzelfstandige_woonruimten,
        )

    if aantal_onzelfstandige_woonruimten < 2 and aantal_adressen < 2:
        return _voeg_gedeeld_met_toe(
            builder,
            aantal=1,
            soort=GedeeldMetSoort.adressen,
        )
    if aantal_adressen > 1:
        tussen_builder: WaarderingsgroepBuilder | WaarderingBuilder = (
            onz_laag if onz_laag is not None else builder
        )
        return _voeg_gedeeld_met_toe(
            tussen_builder,
            aantal=aantal_adressen,
            soort=GedeeldMetSoort.adressen,
        )
    return onz_laag or _voeg_gedeeld_met_toe(
        builder,
        aantal=1,
        soort=GedeeldMetSoort.adressen,
    )


def _voeg_gedeeld_met_toe(
    waarderingsgroep_builder: WaarderingBuilder | WaarderingsgroepBuilder,
    *,
    aantal: int,
    soort: GedeeldMetSoort,
) -> WaarderingBuilder:
    if aantal <= 1:
        segment = "prive"
        naam = naam_gedeeld_met_groep(1)
    else:
        segment = f"gedeeld_met_{aantal}_{soort.value}"
        naam = naam_gedeeld_met_groep(aantal, soort=soort)

    for bestaand in waarderingsgroep_builder._onderliggende:
        if bestaand._segment == segment:
            return bestaand

    onderliggende = WaarderingBuilder(
        segment=segment,
        naam=naam,
        bovenliggende=waarderingsgroep_builder,
    )
    waarderingsgroep_builder._onderliggende.append(onderliggende)
    return onderliggende
