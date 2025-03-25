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
    VERVALLEN - gebruik GNV of NUL - Label dat aangeeft dat de woning intern
    toegankelijk is voor minder validen: de belangrijkste vertrekken (woonkamer,
    keuken, toilet, badkamer en één slaapkamer) zijn bereikbaar zonder gebruik te
    hoeven maken van een trap (d.w.z. gelegen op één verdieping laag of meerdere
    verdiepingslagen die zonder trap - maar bijvoorbeeld met traplift - bereikbaar
    zijn). Een gelijkvloerse woning voldoet niet per definitie aan het criterium
    'nultredenwoning' omdat de woning daarvoor ook extern toegankelijk moet zijn
    voor minder validen.
    """

    gelijkvloerse_woning_geen_nultredenwoning = ToegankelijkheidslabelReferentiedata(
        code="GNV",
        naam="Gelijkvloerse woning (geen nultredenwoning)",
    )
    """
    Label dat aangeeft dat de woning intern toegankelijk is voor minder validen, omdat
    de belangrijkste vertrekken (woonkamer, keuken, toilet, badkamer en één
    slaapkamer) bereikbaar zijn zonder trapgebruik. De woning is extern echter niet
    volledig toegankelijk (bijvoorbeeld door drempels of trappen bij de ingang).
    Deze woning voldoet niet aan het criterium nultredenwoning.
    """

    nultredenwoning = ToegankelijkheidslabelReferentiedata(
        code="NUL",
        naam="Nultredenwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is voor minder
    validen. De belangrijkste vertrekken (woonkamer, keuken, toilet, badkamer en één
    slaapkamer) zijn zonder trapgebruik en zonder drempels bereikbaar. Deze woning
    voldoet aan de eisen voor een nultredenwoning.
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
    """
    Label dat aangeeft dat de woning niet speciaal is ontworpen of aangepast voor
    toegankelijkheid. De woning heeft geen specifieke aanpassingen voor minder
    validen en kan zowel intern als extern ontoegankelijk zijn.
    """
