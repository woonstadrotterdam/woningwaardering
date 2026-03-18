from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectrolsoortReferentiedata(Referentiedata):
    pass


class Projectrolsoort(Referentiedatasoort):
    interne_rol = ProjectrolsoortReferentiedata(
        code="INT",
        naam="Interne rol",
    )
    """
    Rol vervuld door iemand binnen de eigen organisatie.
    """

    externe_rol = ProjectrolsoortReferentiedata(
        code="EXT",
        naam="Externe rol",
    )
    """
    Rol vervuld door een externe partij.
    """
