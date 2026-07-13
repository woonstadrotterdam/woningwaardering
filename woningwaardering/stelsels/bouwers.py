"""Builders die tijdens een ``waardeer()``-aanroep een woningwaarderingsgroep opbouwen.

De builders werken via compositie: ze houden de waarderingen-in-opbouw bij met
hun onderlinge bovenliggende/onderliggende-relaties en produceren pas bij
:meth:`WaarderingsgroepBouwer.bouw` kale VERA-objecten
(``WoningwaarderingResultatenWoningwaarderingGroep`` met platte
``woningwaarderingen``). De output blijft daardoor zuiver VERA; de builders zelf
lekken niet in het resultaat.

Gebruik :meth:`gedeeld_met` voor gedeeld-met/``prive``-lagen, :meth:`categorie`
voor structurele tussenlagen (sanitair, keuken, …) en :meth:`maak_onderliggende`
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

    naam: str
    punten: float | Decimal | None
    aantal: float | int | Decimal | None
    meeteenheid: Referentiedata | None
    opslagpercentage: float | None
    _segment: str
    _bovenliggende: "WaarderingBouwer | WaarderingsgroepBouwer"
    _actief: bool
    _kinderen: list["WaarderingBouwer"]

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
        self._bovenliggende = bovenliggende
        self._actief = False
        self._kinderen = []
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

    @property
    def _actieve_kinderen(self) -> list["WaarderingBouwer"]:
        actief = [kind for kind in self._kinderen if kind._actief]
        eigen = [kind for kind in actief if not _is_gedeeld_met_segment(kind._segment)]
        gedeeld = [kind for kind in actief if _is_gedeeld_met_segment(kind._segment)]
        return [*eigen, *gedeeld]

    def categorie(
        self,
        *,
        id: str | None,
        naam: str | None,
    ) -> "WaarderingBouwer":
        """Geef een (lazy) categorie-onderlaag onder deze waardering.

        De categorie wordt pas actief bij het eerste kind of bij het zetten van
        ``punten``, ``aantal`` of ``opslagpercentage``.

        Een bestaande categorie met hetzelfde id-segment wordt teruggegeven in
        plaats van een nieuwe aan te maken.
        """
        return _voeg_categorie_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
        )

    def maak_onderliggende(
        self,
        *,
        id: str | None,
        naam: str | None,
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
        hergebruik: bool = False,
    ) -> "WaarderingBouwer":
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
        self, nieuwe_bovenliggende: "WaarderingBouwer | WaarderingsgroepBouwer"
    ) -> "WaarderingBouwer":
        """Verplaats deze waardering (met alles eronder) naar onder ``nieuwe_bovenliggende``.

        De waardering wordt losgekoppeld van haar huidige bovenliggende en onder
        ``nieuwe_bovenliggende`` gehangen; haar criterium-id (en die van alles
        eronder) verandert vanzelf mee, omdat die uit de hiërarchie wordt afgeleid.
        """
        self._loskoppelen()
        self._bovenliggende = nieuwe_bovenliggende
        nieuwe_bovenliggende._kinderen.append(self)
        self._actief = True
        return self

    def gedeeld_met(
        self,
        *,
        aantal_adressen: int = 1,
        aantal_onzelfstandige_woonruimten: int = 1,
    ) -> "WaarderingBouwer":
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
            isinstance(bovenliggende, WaarderingBouwer)
            and bovenliggende._actief
            and not bovenliggende._actieve_kinderen
        ):
            bovenliggende.verwijder()

    def _activeer(self) -> None:
        """Maak deze lazy waardering actief (en activeer pending bovenliggenden)."""
        if self._actief:
            return
        bovenliggende = self._bovenliggende
        if isinstance(bovenliggende, WaarderingBouwer):
            bovenliggende._activeer()
        self._actief = True

    def _loskoppelen(self) -> None:
        bovenliggende = self._bovenliggende
        if self in bovenliggende._kinderen:
            bovenliggende._kinderen.remove(self)
        self._actief = False

    @property
    def bovenliggende_id(self) -> str | None:
        """De criterium-id van het bovenliggende criterium (``None`` als direct onder de groep)."""
        if isinstance(self._bovenliggende, WaarderingBouwer):
            return self._bovenliggende.criterium_id
        return None

    def _zelf_en_onderliggende(self) -> Iterator["WaarderingBouwer"]:
        yield self
        for onderliggende in self._actieve_kinderen:
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

    Hang inhoudelijke waarderingen onder de groep met :meth:`maak_onderliggende`,
    gedeeld-met-criteria met :meth:`gedeeld_met` en structurele categorieën met
    :meth:`categorie`. Sluit af met :meth:`bouw`.
    """

    stelsel: Referentiedata
    stelselgroep: Referentiedata
    _kinderen: list[WaarderingBouwer]

    def __init__(
        self,
        stelsel: Referentiedata,
        stelselgroep: Referentiedata,
    ) -> None:
        self.stelsel = stelsel
        self.stelselgroep = stelselgroep
        self._kinderen = []

    @property
    def _actieve_kinderen(self) -> list[WaarderingBouwer]:
        return [kind for kind in self._kinderen if kind._actief]

    def categorie(
        self,
        *,
        id: str | None,
        naam: str | None,
    ) -> WaarderingBouwer:
        """Geef een (lazy) categorie direct onder de groep.

        De categorie wordt pas actief bij het eerste kind of bij het zetten van
        ``punten``, ``aantal`` of ``opslagpercentage``.

        Een bestaande categorie met hetzelfde id-segment wordt teruggegeven in
        plaats van een nieuwe aan te maken.
        """
        return _voeg_categorie_toe(
            self,
            segment=id or "onbekend",
            naam=naam or "",
        )

    def maak_onderliggende(
        self,
        *,
        id: str | None,
        naam: str | None,
        punten: float | Decimal | None = None,
        aantal: float | int | Decimal | None = None,
        meeteenheid: Referentiedata | None = None,
        hergebruik: bool = False,
    ) -> WaarderingBouwer:
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
    ) -> WaarderingBouwer:
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

    def alle_waarderingen(self) -> Iterator[WaarderingBouwer]:
        """Loop door alle tot nu toe opgebouwde waarderingen (elke bovenliggende vóór wat eronder hangt)."""
        for onderliggende in self._actieve_kinderen:
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
            for onderliggende in self._actieve_kinderen
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
    waarderingsgroep_bouwer: WaarderingBouwer | WaarderingsgroepBouwer,
    *,
    segment: str,
    naam: str,
    punten: float | Decimal | None,
    aantal: float | int | Decimal | None,
    meeteenheid: Referentiedata | None,
    hergebruik: bool = False,
) -> WaarderingBouwer:
    if hergebruik:
        for bestaand in waarderingsgroep_bouwer._kinderen:
            if bestaand._actief and bestaand._segment == segment:
                return bestaand
    onderliggende = WaarderingBouwer(
        segment=segment,
        naam=naam,
        bovenliggende=waarderingsgroep_bouwer,
        punten=punten,
        aantal=aantal,
        meeteenheid=meeteenheid,
    )
    onderliggende._actief = True
    waarderingsgroep_bouwer._kinderen.append(onderliggende)
    return onderliggende


def _voeg_categorie_toe(
    parent: WaarderingBouwer | WaarderingsgroepBouwer,
    *,
    segment: str,
    naam: str,
) -> WaarderingBouwer:
    for bestaand in parent._kinderen:
        if bestaand._segment == segment:
            return bestaand
    categorie = WaarderingBouwer(
        segment=segment,
        naam=naam,
        bovenliggende=parent,
    )
    parent._kinderen.append(categorie)
    return categorie


def _gedeeld_met_lagen(
    bouwer: WaarderingBouwer | WaarderingsgroepBouwer,
    *,
    aantal_adressen: int,
    aantal_onzelfstandige_woonruimten: int,
) -> WaarderingBouwer:
    onz_laag = None
    if aantal_onzelfstandige_woonruimten > 1:
        onz_laag = _voeg_gedeeld_met_toe(
            bouwer,
            aantal=aantal_onzelfstandige_woonruimten,
            soort=GedeeldMetSoort.onzelfstandige_woonruimten,
        )

    if aantal_onzelfstandige_woonruimten < 2 and aantal_adressen < 2:
        return _voeg_gedeeld_met_toe(
            bouwer,
            aantal=1,
            soort=GedeeldMetSoort.adressen,
        )
    if aantal_adressen > 1:
        tussen_bouwer: WaarderingsgroepBouwer | WaarderingBouwer = (
            onz_laag if onz_laag is not None else bouwer
        )
        return _voeg_gedeeld_met_toe(
            tussen_bouwer,
            aantal=aantal_adressen,
            soort=GedeeldMetSoort.adressen,
        )
    return onz_laag or _voeg_gedeeld_met_toe(
        bouwer,
        aantal=1,
        soort=GedeeldMetSoort.adressen,
    )


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

    for bestaand in waarderingsgroep_bouwer._kinderen:
        if bestaand._segment == segment:
            return bestaand

    onderliggende = WaarderingBouwer(
        segment=segment,
        naam=naam,
        bovenliggende=waarderingsgroep_bouwer,
    )
    waarderingsgroep_bouwer._kinderen.append(onderliggende)
    return onderliggende
