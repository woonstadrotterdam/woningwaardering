from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DefectstatusReferentiedata(Referentiedata):
    pass


class Defectstatus(Referentiedatasoort):
    geinspecteerd = DefectstatusReferentiedata(
        code="INS",
        naam="Geinspecteerd",
    )

    gemeld = DefectstatusReferentiedata(
        code="MEL",
        naam="Gemeld",
    )
