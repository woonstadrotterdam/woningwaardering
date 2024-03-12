
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MEDEWERKERSOORT:

    in_dienst = Referentiedata(
        code="DIE",
        naam="in dienst",
    )
    # in_dienst = ("DIE", "in dienst")

    meewerkende_partner = Referentiedata(
        code="FAM",
        naam="meewerkende partner",
    )
    # meewerkende_partner = ("FAM", "meewerkende partner")

    inhuur_zzp_of_payroll_of_detachering = Referentiedata(
        code="INH",
        naam="inhuur: zzp / payroll / detachering",
    )
    # inhuur_zzp_of_payroll_of_detachering = ("INH", "inhuur: zzp / payroll / detachering")

    oproepkracht = Referentiedata(
        code="OPR",
        naam="oproepkracht",
    )
    # oproepkracht = ("OPR", "oproepkracht")

    stagair = Referentiedata(
        code="STA",
        naam="stagair",
    )
    # stagair = ("STA", "stagair")
