from woningwaardering.vera.bvg.models import Referentiedata


class ENERGIEPRESTATIEVERGOEDINGSOORT:
    epv_basis = Referentiedata(
        code="BAS",
        naam="EPV Basis",
    )
    """
    De maximale EPV geldt voor: een woning die ten minste duurzame energie levert voor
    het volledige gebouwgebonden gebruik (EGW) of een woning die ten minste duurzame
    energie levert voor het volledige gebouwgebonden deel (MGW).
    """

    epv_hoogwaardig = Referentiedata(
        code="HOO",
        naam="EPV Hoogwaardig",
    )
    """
    De maximale EPV geldt voor: een woning die ten minste duurzame energie levert voor
    het volledige gebouwgebonden deel én ten minste 2100 kWh/jaar voor het
    gebruikersgebonden deel (EGW) of een woning die ten minste duurzame energie levert
    voor het volledige gebouwgebonden deel én 530 kWh/jaar voor het gebruikersgebonden
    deel (MGW).
    """
