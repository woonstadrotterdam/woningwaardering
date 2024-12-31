from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RuimtesoortReferentiedata(Referentiedata):
    pass


class Ruimtesoort(Referentiedatasoort):
    buitenruimte = RuimtesoortReferentiedata(
        code="BTR",
        naam="Buitenruimte",
    )
    """
    Een buitenruimte is een ruimte die volgens de woningwaardering als (privé)
    buitenruimte wordt gezien. Nader te specificeren met ruimtedetailsoort.
    """

    gemeenschappelijke_ruimten_en_voorzieningen = RuimtesoortReferentiedata(
        code="GEM",
        naam="Gemeenschappelijke ruimten en voorzieningen",
    )
    """
    Een gemeenschappelijk ruimte of voorziening is een ruimte die volgens de
    woningwaardering als gemeenschappelijke ruimte of voorziening wordt gezien
    """

    overige_ruimten = RuimtesoortReferentiedata(
        code="OVR",
        naam="Overige ruimten",
    )
    """
    Een ruimte die geen buitenruimte is, en die geen vertrek is volgens de definitie van
    de woningwaardering. Nader te specificeren met ruimtedetailsoort.
    """

    vertrek = RuimtesoortReferentiedata(
        code="VTK",
        naam="Vertrek",
    )
    """
    Een vertrek is een ruimte die volgens de woningwaardering als vertrek wordt gezien
    (Beleidsboek waarderingsstelsel zelfstandige woonruimte)
    """

    verkeersruimte = RuimtesoortReferentiedata(
        code="VRK",
        naam="Verkeersruimte",
    )
    """
    Een verkeersruimte is een ruimte die wordt gebruikt om toegang te krijgen tot andere
    vertrekken.
    """

    parkeergelegenheid = RuimtesoortReferentiedata(
        code="PAR",
        naam="Parkeergelegenheid",
    )
    """
    (UITBREIDING) Een locatie die speciaal is ingericht voor het parkeren van
    voertuigen. Dit kan variëren van een eenvoudige parkeerplaats op straat tot
    uitgebreide faciliteiten zoals parkeerterreinen en parkeergarages.
    Parkeergelegenheden bieden gemarkeerde plaatsen waar voertuigen veilig kunnen
    worden geparkeerd, en ze kunnen openbaar of privé zijn. De term
    "parkeergelegenheid" omvat alle vormen van parkeerinfrastructuur die zijn
    ontworpen om voertuigen tijdelijk of langdurig te stallen.
    """
