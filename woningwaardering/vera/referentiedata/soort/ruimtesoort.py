from vera.referentiedata.models import Referentiedata


class Ruimtesoort:
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
