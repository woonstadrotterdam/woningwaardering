from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AfwezigheidsoortReferentiedata(Referentiedata):
    pass


class Afwezigheidsoort(Referentiedatasoort):
    adoptieverlof = AfwezigheidsoortReferentiedata(
        code="ADO",
        naam="Adoptieverlof",
    )

    bijzonder_verlof = AfwezigheidsoortReferentiedata(
        code="BIJ",
        naam="Bijzonder verlof",
    )

    calamiteitenverlof = AfwezigheidsoortReferentiedata(
        code="CAL",
        naam="Calamiteitenverlof",
    )

    geschorst = AfwezigheidsoortReferentiedata(
        code="GES",
        naam="Geschorst",
    )

    non_actief = AfwezigheidsoortReferentiedata(
        code="NON",
        naam="Non-actief",
    )

    onbetaald_verlof = AfwezigheidsoortReferentiedata(
        code="ONB",
        naam="Onbetaald verlof",
    )

    ouderschapsverlof = AfwezigheidsoortReferentiedata(
        code="OUD",
        naam="Ouderschapsverlof",
    )

    verlof_regulier = AfwezigheidsoortReferentiedata(
        code="VER",
        naam="Verlof (regulier)",
    )

    ziek = AfwezigheidsoortReferentiedata(
        code="ZIE",
        naam="Ziek",
    )

    zorgverlof = AfwezigheidsoortReferentiedata(
        code="ZOR",
        naam="Zorgverlof",
    )

    zwangerschapsverlof = AfwezigheidsoortReferentiedata(
        code="ZWA",
        naam="Zwangerschapsverlof",
    )
