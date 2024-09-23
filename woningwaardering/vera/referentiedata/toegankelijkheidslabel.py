from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Toegankelijkheidslabel(Enum):
    gelijkvloerse_woning = Referentiedata(
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

    rollatorwoning = Referentiedata(
        code="ROA",
        naam="Rollatorwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is met een
    rollator. De woning voldoet hiermee automatisch aan het criterium
    'nultredenwoning', maar is niet per definitie ook een 'rolstoelwoning' omdat er
    bijvoorbeeld drempels aanwezig kunnen zijn.
    """

    rolstoelwoning = Referentiedata(
        code="ROL",
        naam="Rolstoelwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is, met een
    rolstoel. De woning voldoet hiermee automatisch aan het criterium
    'nultredewoning'. Een rolstoelwoning voldoet per definitie ook aan het label
    Rollatorwoning, maar is niet per definitie ook een 'extra ruime rolstoelwoning'.
    """

    extra_ruime_rolstoelwoning = Referentiedata(
        code="RUI",
        naam="Extra ruime rolstoelwoning",
    )
    """
    Label dat aangeeft dat de woning zowel intern als extern toegankelijk is, met een
    grote (elektrische) rolstoel. De woning voldoet hiermee automatisch aan het
    criterium 'nultredenwoning'. Een extra ruime rolstoelwoning voldoet per
    definitie ook aan het label Rolstoelwoning.
    """

    woning_zonder_bijzondere_toegankelijkheid = Referentiedata(
        code="ZON",
        naam="Woning zonder bijzondere toegankelijkheid",
    )

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
