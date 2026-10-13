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
) -> EenhedenRuimte:
    """Maak een ruimte; de naam volgt uit de detailsoort en de id uit de naam.

    Nummer de ruimten met `naam` wanneer een eenheid meer ruimten van dezelfde
    detailsoort heeft: "Badkamer1", "Badkamer2".

    De soort volgt uit de detailsoort. Geef `soort` mee wanneer de ruimte met
    een andere ruimtesoort is aangeleverd, zoals een schuur als vertrek.
    """
    naam = naam or detail_soort.naam or ""
    return EenhedenRuimte(
        id=naam.lower().replace(" ", "_"),
        naam=naam,
        soort=soort or detail_soort.parent,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        installaties=list(installaties) or None,
        bouwkundige_elementen=list(elementen) or None,
        verbonden_ruimten=list(verbonden_ruimten) or None,
    )


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
