from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Ruimtesoort(Enum):
    buitenruimte = Referentiedata(
        code="BTR",
        naam="Buitenruimte",
    )
    """
    Een buitenruimte is een ruimte die volgens de woningwaardering als (privé)
    buitenruimte wordt gezien. Nader te specificeren met ruimtedetailsoort.
    """

    gemeenschappelijke_ruimten_en_voorzieningen = Referentiedata(
        code="GEM",
        naam="Gemeenschappelijke ruimten en voorzieningen",
    )
    """
    Een gemeenschappelijk ruimte of voorziening is een ruimte die volgens de
    woningwaardering als gemeenschappelijke ruimte of voorziening wordt gezien
    """

    overige_ruimtes = Referentiedata(
        code="OVR",
        naam="Overige ruimtes",
    )
    """
    Een ruimte die geen buitenruimte is, en die geen vertrek is volgens de definitie van
    de woningwaardering. Nader te specificeren met ruimtedetailsoort.
    """

    vertrek = Referentiedata(
        code="VTK",
        naam="Vertrek",
    )
    """
    Een vertrek is een ruimte die volgens de woningwaardering als vertrek wordt gezien
    (Beleidsboek waarderingsstelsel zelfstandige woonruimte)
    """

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
