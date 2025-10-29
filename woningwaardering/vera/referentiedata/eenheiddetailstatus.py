from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eenheidstatus import (
    Eenheidstatus,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheiddetailstatusReferentiedata(Referentiedata):
    pass


class Eenheiddetailstatus(Referentiedatasoort):
    verhuurd_antikraak = EenheiddetailstatusReferentiedata(
        code="ANT",
        naam="Verhuurd antikraak",
        parent=Eenheidstatus.verhuurd,
    )
    """
    De eenheid wordt verhuurd onder de voorwaarden van anti-kraak
    """

    bouwplannen = EenheiddetailstatusReferentiedata(
        code="BOU",
        naam="Bouwplannen",
        parent=Eenheidstatus.in_ontwikkeling,
    )
    """
    Eenheid is in ontwikkeling, nog in de planfase
    """

    bruikleen = EenheiddetailstatusReferentiedata(
        code="BRU",
        naam="Bruikleen",
        parent=Eenheidstatus.verhuurd,
    )
    """
    De eenheid wordt verhuurd onder een bruikleen constructie
    """

    wacht_op_energie_prestatie_advies = EenheiddetailstatusReferentiedata(
        code="EPA",
        naam="Wacht op Energie Prestatie Advies",
        parent=Eenheidstatus.leegstand,
    )
    """
    Frictieleegstand, ontstaan doordat er nog gewacht wordt op de afgifte van een EPA
    label
    """

    mutatie = EenheiddetailstatusReferentiedata(
        code="MUT",
        naam="Mutatie",
        parent=Eenheidstatus.leegstand,
    )
    """
    Frictieleegstand wegens mutatieonderhoud. De eenheid is in exploitatie, maar niet
    verhuurd. Aansluitende verhuur is niet mogelijk omdat eerst nog onderhoud in de
    woning plaatsvindt.
    """

    wacht_op_nieuwe_huurder_niet_regulier = EenheiddetailstatusReferentiedata(
        code="NIB",
        naam="Wacht op nieuwe huurder - niet-regulier",
        parent=Eenheidstatus.leegstand,
    )
    """
    Frictieleegstand, ontstaan doordat er nog geen nieuwe huurder is gevonden, waarbij
    geldt dat er sprake is van een niet-regulier toewijzingsproces of een
    niet-reguliere beoogd huurder. Het betreft de leegstand vanaf het moment waarop
    de woning klaar is voor verhuur (nadat eventueel mutatieonderhoud is afgerond)
    totdat de overeenkomst met een nieuwe, niet-reguliere, huurder ingaat.
    """

    nieuwbouw = EenheiddetailstatusReferentiedata(
        code="NIE",
        naam="Nieuwbouw",
        parent=Eenheidstatus.in_ontwikkeling,
    )
    """
    Eenheid is in ontwikkeling, realisatie-/bouwfase is gestart
    """

    wacht_op_nieuwe_huurder_regulier = EenheiddetailstatusReferentiedata(
        code="NIH",
        naam="Wacht op nieuwe huurder - regulier",
        parent=Eenheidstatus.leegstand,
    )
    """
    Frictieleegstand, ontstaan doordat er nog geen nieuwe huurder is gevonden, zonder
    dat daar een speciale oorzaak voor is (het reguliere matching proces duurt
    langer dan gewenst). Het betreft de leegstand vanaf het moment waarop de woning
    klaar is voor verhuur (nadat eventueel mutatieonderhoud is afgerond) totdat de
    overeenkomst met een nieuwe huurder ingaat.
    """

    oplevering = EenheiddetailstatusReferentiedata(
        code="OPL",
        naam="Oplevering",
        parent=Eenheidstatus.in_ontwikkeling,
    )
    """
    Eenheid is in ontwikkeling, klaar voor oplevering
    """

    verhuurd_permanent = EenheiddetailstatusReferentiedata(
        code="PER",
        naam="Verhuurd permanent",
        parent=Eenheidstatus.verhuurd,
    )
    """
    Doorlopend contract of voor onbepaalde tijd.
    """

    projectleegstand = EenheiddetailstatusReferentiedata(
        code="PRO",
        naam="Projectleegstand",
        parent=Eenheidstatus.leegstand,
    )
    """
    Leegstand doordat de eenheid deel uitmaakt van een onderhouds- of renovatieproject,
    waarbij de eenheid niet uit exploitatie wordt genomen
    """

    structurele_leegstand = EenheiddetailstatusReferentiedata(
        code="STR",
        naam="Structurele leegstand",
        parent=Eenheidstatus.leegstand,
    )
    """
    (Verwachte) Langdurige frictieleegstand, doordat vraag en aanbod niet op elkaar
    aansluiten
    """

    verhuurd_tijdelijk = EenheiddetailstatusReferentiedata(
        code="TIJD",
        naam="Verhuurd tijdelijk",
        parent=Eenheidstatus.verhuurd,
    )
    """
    Huurcontract met beperkte looptijd (anders dan anti-kraak of onder een bruikleen
    constructie)
    """

    verkoop = EenheiddetailstatusReferentiedata(
        code="VEK",
        naam="Verkoop",
        parent=Eenheidstatus.leegstand,
    )
    """
    Leegstand omdat de eenheid op korte termijn verkocht zal worden, maar nog wel in
    exploitatie is.
    """

    vergunning_verleend = EenheiddetailstatusReferentiedata(
        code="VER",
        naam="Vergunning verleend",
        parent=Eenheidstatus.in_ontwikkeling,
    )
    """
    Eenheid is in ontwikkeling, bouwvergunning is verleend
    """
