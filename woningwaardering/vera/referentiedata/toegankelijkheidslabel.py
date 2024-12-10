from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ToegankelijkheidslabelReferentiedata(Referentiedata):
    pass


class Toegankelijkheidslabel(Referentiedatasoort):
    gelijkvloerse_woning = ToegankelijkheidslabelReferentiedata(
        code="GEL",
        naam="Gelijkvloerse woning",
    )
    """
    Label dat aangeeft dat de woning intern toegankelijk is voor minder validen: de
    belangrijkste vertrekken (woonkamer, keuken, toilet, badkamer en één slaapkamer)
    zijn bereikbaar zonder gebruik te hoeven maken van een trap (d.w.z. gelegen op
    één verdieping laag of meerdere verdiepingslagen die zonder trap - maar
    bijvoorbeeld met traplift - bereikbaar zijn). Een gelijkvloerse woning voldoet
    niet per definitie aan het criterium 'nultredenwoning' omdat de woning daarvoor
    ook extern toegankelijk moet zijn voor minder validen.
    """

    rollatorwoning = ToegankelijkheidslabelReferentiedata(
        code="ROA",
        naam="Rollatorwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is met een
    rollator. De woning voldoet hiermee automatisch aan het criterium
    'nultredenwoning', maar is niet per definitie ook een 'rolstoelwoning' omdat er
    bijvoorbeeld drempels aanwezig kunnen zijn.
    """

    rolstoelwoning = ToegankelijkheidslabelReferentiedata(
        code="ROL",
        naam="Rolstoelwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is, met een
    rolstoel. De woning voldoet hiermee automatisch aan het criterium
    'nultredewoning'. Een rolstoelwoning voldoet per definitie ook aan het label
    Rollatorwoning, maar is niet per definitie ook een 'extra ruime rolstoelwoning'.
    """

    extra_ruime_rolstoelwoning = ToegankelijkheidslabelReferentiedata(
        code="RUI",
        naam="Extra ruime rolstoelwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is, met een
    grote (elektrische) rolstoel. De woning voldoet hiermee automatisch aan het
    criterium 'nultredenwoning'. Een extra ruime rolstoelwoning voldoet per
    definitie ook aan het label Rolstoelwoning.
    """

    woning_zonder_bijzondere_toegankelijkheid = ToegankelijkheidslabelReferentiedata(
        code="ZON",
        naam="Woning zonder bijzondere toegankelijkheid",
    )
