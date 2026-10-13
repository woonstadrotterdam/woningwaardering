"""Functies voor testinput: VERA-objecten met standaardwaarden.

Wat een beleidsregel raakt geeft de test zelf mee; de rest krijgt hier een
standaardwaarde. Zie docs/voor-ontwikkelaars/testing.md.
"""

from collections.abc import Sequence

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    BouwkundigelementdetailsoortReferentiedata,
    InstallatiesoortReferentiedata,
    Ruimtedetailsoort,
    RuimtedetailsoortReferentiedata,
    RuimtesoortReferentiedata,
)


def ruimte(
    detail_soort: RuimtedetailsoortReferentiedata,
    *installaties: InstallatiesoortReferentiedata,
    elementen: Sequence[BouwkundigElementenBouwkundigElement] = (),
    naam: str | None = None,
    oppervlakte: float = 10.0,
    soort: RuimtesoortReferentiedata | None = None,
    verbonden_ruimten: Sequence[EenhedenRuimte] = (),
    gedeeld_met_aantal_onzelfstandige_woonruimten: int | None = None,
    gedeeld_met_aantal_adressen: int | None = None,
    verwarmd: bool | None = None,
    verkoeld: bool | None = None,
    lengte_mm: int | None = None,
    breedte_mm: int | None = None,
    hoogte_mm: int | None = None,
    aantal: int | None = None,
) -> EenhedenRuimte:
    """Maak een ruimte; de naam volgt uit de detailsoort en de id uit de naam.

    Nummer de ruimten met `naam` wanneer een eenheid meer ruimten van dezelfde
    detailsoort heeft: "Badkamer1", "Badkamer2".

    De soort volgt uit de detailsoort. Geef `soort` mee wanneer de ruimte met
    een andere ruimtesoort is aangeleverd, zoals een schuur als vertrek.

    Zonder `gedeeld_met_aantal_onzelfstandige_woonruimten` is de ruimte privé.
    Zonder `gedeeld_met_aantal_adressen` is ze niet met andere adressen gedeeld.

    Zonder `verwarmd` is de ruimte niet verwarmd, zonder `verkoeld` heeft ze
    geen verkoelingsfunctie.

    Zonder `lengte_mm`, `breedte_mm` en `hoogte_mm` heeft de ruimte geen
    afmetingen, alleen een oppervlakte.

    Zonder `aantal` is de ruimte één parkeerplek. Geef `aantal` mee wanneer de
    ruimte voor meer dan één parkeerplek van dezelfde soort staat.
    """
    naam = naam or detail_soort.naam or ""
    nieuwe_ruimte = EenhedenRuimte(
        id=naam.lower().replace(" ", "_"),
        naam=naam,
        soort=soort or detail_soort.parent,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        installaties=list(installaties) or None,
        bouwkundige_elementen=list(elementen) or None,
        verbonden_ruimten=list(verbonden_ruimten) or None,
        gedeeld_met_aantal_onzelfstandige_woonruimten=(
            gedeeld_met_aantal_onzelfstandige_woonruimten
        ),
        gedeeld_met_aantal_adressen=gedeeld_met_aantal_adressen,
        verwarmd=verwarmd,
        verkoeld=verkoeld,
        lengte=lengte_mm,
        breedte=breedte_mm,
        hoogte=hoogte_mm,
    )
    # Het model geeft `aantal` zelf de standaardwaarde 1; alleen een meegegeven
    # aantal komt in de input van de test.
    if aantal is not None:
        nieuwe_ruimte.aantal = aantal
    return nieuwe_ruimte


def badkamer(
    *installaties: InstallatiesoortReferentiedata,
    elementen: Sequence[BouwkundigElementenBouwkundigElement] = (),
    naam: str | None = None,
) -> EenhedenRuimte:
    return ruimte(
        Ruimtedetailsoort.badkamer, *installaties, elementen=elementen, naam=naam
    )


def element(
    detail_soort: BouwkundigelementdetailsoortReferentiedata,
    *,
    id: str | None = None,
    lengte_mm: int | None = None,
) -> BouwkundigElementenBouwkundigElement:
    """Maak een bouwkundig element; id en naam volgen uit de detailsoort."""
    naam = detail_soort.naam or ""
    return BouwkundigElementenBouwkundigElement(
        id=id or naam.lower().replace(" ", "_"),
        naam=naam,
        soort=detail_soort.parent,
        detail_soort=detail_soort,
        lengte=lengte_mm,
    )


def elementen(
    *detail_soorten: BouwkundigelementdetailsoortReferentiedata,
) -> list[BouwkundigElementenBouwkundigElement]:
    """Maak een bouwkundig element per detailsoort, elk met een eigen id."""
    return [
        element(detail_soort, id=f"element_{nummer}")
        for nummer, detail_soort in enumerate(detail_soorten, start=1)
    ]


def aanrecht(
    lengte_mm: int, *, id: str = "aanrecht"
) -> BouwkundigElementenBouwkundigElement:
    return element(Bouwkundigelementdetailsoort.aanrecht, id=id, lengte_mm=lengte_mm)
