from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.signaleringsoort import (
    Signaleringsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SignaleringdetailsoortReferentiedata(Referentiedata):
    pass


class Signaleringdetailsoort(Referentiedatasoort):
    agressie = SignaleringdetailsoortReferentiedata(
        code="AGS",
        naam="Agressie",
        parent=Signaleringsoort.agressie,
    )
    """
    Algemeen signaal van agressief gedrag, nog niet gespecificeerd als verbaal, fysiek
    of schriftelijk.
    """

    ambulante_begeleiding = SignaleringdetailsoortReferentiedata(
        code="AMB",
        naam="Ambulante begeleiding",
        parent=Signaleringsoort.ondersteuningsbehoefte,
    )
    """
    De relatie krijgt in de eigen omgeving externe hulp om zo zelfstandig mogelijk te
    blijven functioneren.
    """

    beledigend = SignaleringdetailsoortReferentiedata(
        code="BEL",
        naam="Beledigend",
        parent=Signaleringsoort.wangedrag_naar_medewerkers,
    )
    """
    De relatie uit zich op een kleinerende of respectloze manier richting medewerkers,
    zonder direct dreigend te zijn.
    """

    betalingsachterstand = SignaleringdetailsoortReferentiedata(
        code="BET",
        naam="Betalingsachterstand",
        parent=Signaleringsoort.huurschuld,
    )
    """
    Er is sprake van één of meerdere gemiste huurbetalingen.
    """

    bewindvoerder = SignaleringdetailsoortReferentiedata(
        code="BEW",
        naam="Bewindvoerder",
    )
    """
    De relatie staat onder financieel beheer via een bewindvoerder.
    """

    bezoek_met_twee = SignaleringdetailsoortReferentiedata(
        code="BEZ",
        naam="Bezoek met twee",
    )
    """
    Bij contactmomenten of huisbezoeken is er vanwege veiligheid of eerdere ervaringen
    besloten dat de medewerker niet alleen op bezoek gaat, maar samen met een
    collega of derde persoon.
    """

    brandstichting = SignaleringdetailsoortReferentiedata(
        code="BRA",
        naam="Brandstichting",
        parent=Signaleringsoort.agressie,
    )
    """
    Opzettelijke of vermoedelijke brandstichting, al dan niet strafrechtelijk vervolgd.
    """

    deurwaarder = SignaleringdetailsoortReferentiedata(
        code="DEU",
        naam="Deurwaarder",
        parent=Signaleringsoort.huurschuld,
    )
    """
    Een deurwaarder is ingeschakeld voor incasso van openstaande huurschuld.
    """

    drugshandel = SignaleringdetailsoortReferentiedata(
        code="DRU",
        naam="Drugshandel",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
    """
    Handel in drugs vanuit of in de woning.
    """

    fysiek = SignaleringdetailsoortReferentiedata(
        code="FYS",
        naam="Fysiek",
        parent=Signaleringsoort.agressie,
    )
    """
    Fysieke agressie zoals duwen, slaan, spugen of andere vormen van lichamelijk geweld.
    """

    geluidsoverlast = SignaleringdetailsoortReferentiedata(
        code="GEL",
        naam="Geluidsoverlast",
        parent=Signaleringsoort.overlast,
    )
    """
    Overmatige geluidshinder, bijvoorbeeld door harde muziek, geschreeuw of blaffende
    honden.
    """

    hennepkwekerij = SignaleringdetailsoortReferentiedata(
        code="HEN",
        naam="Hennepkwekerij",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
    """
    Illegale teelt van hennep in of rond de woning.
    """

    intimiderend = SignaleringdetailsoortReferentiedata(
        code="INT",
        naam="Intimiderend",
        parent=Signaleringsoort.wangedrag_naar_medewerkers,
    )
    """
    De relatie probeert medewerkers onder druk te zetten of angst aan te jagen,
    bijvoorbeeld door dreigende lichaamstaal of suggestieve uitspraken.
    """

    mutatieschade = SignaleringdetailsoortReferentiedata(
        code="MUT",
        naam="Mutatieschade",
        parent=Signaleringsoort.huurschuld,
    )
    """
    Beschadigingen aan de woning die geconstateerd zijn bij einde huur.
    """

    onacceptabele_toon = SignaleringdetailsoortReferentiedata(
        code="ONA",
        naam="Onacceptabele toon",
        parent=Signaleringsoort.wangedrag_naar_medewerkers,
    )
    """
    De toon van de communicatie is onbeschoft of denigrerend, wat het gesprek verstoort
    of de medewerker ondermijnt.
    """

    onderverhuur = SignaleringdetailsoortReferentiedata(
        code="OND",
        naam="Onderverhuur",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
    """
    Het (gedeeltelijk) verhuren van de woning aan derden zonder toestemming.
    """

    prostitutie = SignaleringdetailsoortReferentiedata(
        code="PRO",
        naam="Prostitutie",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
    """
    De woning wordt (mogelijk) gebruikt voor prostitutie of seksgerelateerde diensten.
    """

    racistich = SignaleringdetailsoortReferentiedata(
        code="RAC",
        naam="Racistich",
        parent=Signaleringsoort.wangedrag_naar_medewerkers,
    )
    """
    De relatie uit zich op een discriminerende of racistische manier richting een
    medewerker.
    """

    schriftelijk = SignaleringdetailsoortReferentiedata(
        code="SCH",
        naam="Schriftelijk",
        parent=Signaleringsoort.agressie,
    )
    """
    Agressie die schriftelijk geuit is, bijvoorbeeld via brief, e-mail of formulier.
    """

    seksueel_ongepast = SignaleringdetailsoortReferentiedata(
        code="SEU",
        naam="Seksueel ongepast",
        parent=Signaleringsoort.wangedrag_naar_medewerkers,
    )
    """
    Er is sprake van seksueel getinte opmerkingen of gedrag dat als ongewenst wordt
    ervaren.
    """

    verbaal = SignaleringdetailsoortReferentiedata(
        code="VEB",
        naam="Verbaal",
        parent=Signaleringsoort.agressie,
    )
    """
    Mondeling geuite agressie, zoals schelden, dreigen of beledigen.
    """

    vervuiling = SignaleringdetailsoortReferentiedata(
        code="VER",
        naam="Vervuiling",
        parent=Signaleringsoort.oneigenlijk_gebruik_woning,
    )
    """
    Ernstige vervuiling in of rondom de woning, wat overlast of onveilige situaties
    veroorzaakt.
    """
