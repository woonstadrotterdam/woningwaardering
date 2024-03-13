from woningwaardering.vera.bvg.models import Referentiedata


class MEDEWERKERSOORT:
    in_dienst = Referentiedata(
        code="DIE",
        naam="in dienst",
    )

    meewerkende_partner = Referentiedata(
        code="FAM",
        naam="meewerkende partner",
    )

    inhuur_zzp_of_payroll_of_detachering = Referentiedata(
        code="INH",
        naam="inhuur: zzp / payroll / detachering",
    )

    oproepkracht = Referentiedata(
        code="OPR",
        naam="oproepkracht",
    )

    stagair = Referentiedata(
        code="STA",
        naam="stagair",
    )
