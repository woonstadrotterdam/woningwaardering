from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EnergieprestatievergoedingsoortReferentiedata(Referentiedata):
    pass


class Energieprestatievergoedingsoort(Referentiedatasoort):
    epv_basis = EnergieprestatievergoedingsoortReferentiedata(
        code="BAS",
        naam="EPV Basis",
    )
    """
    De maximale EPV geldt voor: een woning die ten minste duurzame energie levert voor
    het volledige gebouwgebonden gebruik (EGW) of een woning die ten minste duurzame
    energie levert voor het volledige gebouwgebonden deel (MGW).
    """

    epv_hoogwaardig = EnergieprestatievergoedingsoortReferentiedata(
        code="HOO",
        naam="EPV Hoogwaardig",
    )
    """
    De maximale EPV geldt voor: een woning die ten minste duurzame energie levert voor
    het volledige gebouwgebonden deel én ten minste 2100 kWh/jaar voor het
    gebruikersgebonden deel (EGW) of een woning die ten minste duurzame energie
    levert voor het volledige gebouwgebonden deel én 530 kWh/jaar voor het
    gebruikersgebonden deel (MGW).
    """
