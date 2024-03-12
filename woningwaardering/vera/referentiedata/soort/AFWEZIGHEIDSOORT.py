
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AFWEZIGHEIDSOORT:

    adoptieverlof = Referentiedata(
        code="ADO",
        naam="Adoptieverlof",
    )
    # adoptieverlof = ("ADO", "Adoptieverlof")

    bijzonder_verlof = Referentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
    )
    # bijzonder_verlof = ("BIJ", "Bijzonder verlof")

    calamiteitenverlof = Referentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
    )
    # calamiteitenverlof = ("CAL", "Calamiteitenverlof")

    geschorst = Referentiedata(
        code="GES",
        naam="Geschorst",
    )
    # geschorst = ("GES", "Geschorst")

    non_actief = Referentiedata(
        code="NON",
        naam="Non-actief",
    )
    # non_actief = ("NON", "Non-actief")

    onbetaald_verlof = Referentiedata(
        code="ONB",
        naam="Onbetaald verlof",
    )
    # onbetaald_verlof = ("ONB", "Onbetaald verlof")

    ouderschapsverlof = Referentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
    )
    # ouderschapsverlof = ("OUD", "Ouderschapsverlof")

    verlof_regulier = Referentiedata(
        code="VER",
        naam="Verlof (regulier)",
    )
    # verlof_regulier = ("VER", "Verlof (regulier)")

    ziek = Referentiedata(
        code="ZIE",
        naam="Ziek",
    )
    # ziek = ("ZIE", "Ziek")

    zorgverlof = Referentiedata(
        code="ZOR",
        naam="Zorgverlof",
    )
    # zorgverlof = ("ZOR", "Zorgverlof")

    zwangerschapsverlof = Referentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
    )
    # zwangerschapsverlof = ("ZWA", "Zwangerschapsverlof")
