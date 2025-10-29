from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MedewerkersoortReferentiedata(Referentiedata):
    pass


class Medewerkersoort(Referentiedatasoort):
    in_dienst = MedewerkersoortReferentiedata(
        code="DIE",
        naam="In dienst",
    )

    meewerkende_partner = MedewerkersoortReferentiedata(
        code="FAM",
        naam="Meewerkende partner",
    )

    inhuur_zzp_en_of_payroll_en_of_detachering = MedewerkersoortReferentiedata(
        code="INH",
        naam="Inhuur: zzp / payroll / detachering",
    )
    """
    Een inhuurkracht is een werknemer die tijdelijk wordt ingehuurd door een organisatie
    om specifieke taken of projecten uit te voeren. Inhuurkrachten zijn meestal niet
    in vaste dienst bij de organisatie en kunnen ingehuurd worden via een
    uitzendbureau, zelfstandige, zelfstandige via een payrol-organisatie of een
    detacheringsbureau.
    """

    oproepkracht = MedewerkersoortReferentiedata(
        code="OPR",
        naam="Oproepkracht",
    )

    stagair = MedewerkersoortReferentiedata(
        code="STA",
        naam="Stagair",
    )
    """
    Een stagiair is een student of pas afgestudeerde die een tijdelijke werkperiode bij
    een organisatie doorbrengt om praktische ervaring op te doen in een specifiek
    vakgebied. Deze stage kan deel uitmaken van hun opleiding of bedoeld zijn om
    werkervaring op te doen en hun vaardigheden in de praktijk te ontwikkelen.
    """

    trainee = MedewerkersoortReferentiedata(
        code="TRA",
        naam="Trainee",
    )
    """
    Een trainee is een persoon die net is afgestudeerd of aan het begin van zijn of haar
    carrière staat en een gestructureerd opleidingsprogramma volgt binnen een
    organisatie. Dit programma is bedoeld om hen de vaardigheden, kennis en ervaring
    te geven die nodig zijn om succesvol te zijn in een specifieke rol of sector.
    """
