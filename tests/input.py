"""Functies voor testinput: VERA-objecten met standaardwaarden.

Wat een beleidsregel raakt geeft de test zelf mee; de rest krijgt hier een
standaardwaarde. Zie docs/voor-ontwikkelaars/testing.md.
"""

from collections.abc import Sequence
from datetime import date

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRenovatie,
    EenhedenRuimte,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    BouwkundigelementdetailsoortReferentiedata,
    Doelgroep,
    EenheidmonumentReferentiedata,
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    InstallatiesoortReferentiedata,
    Pandsoort,
    Ruimtedetailsoort,
    RuimtedetailsoortReferentiedata,
    RuimtesoortReferentiedata,
)


def ruimte(
    detail_soort: RuimtedetailsoortReferentiedata,
    *installaties: InstallatiesoortReferentiedata,
    elementen: Sequence[BouwkundigElementenBouwkundigElement] = (),
    naam: str | None = None,
    oppervlakte: float = 10.0,
    soort: RuimtesoortReferentiedata | None = None,
    verbonden_ruimten: Sequence[EenhedenRuimte] = (),
    gedeeld_met_aantal_onzelfstandige_woonruimten: int | None = None,
    gedeeld_met_aantal_adressen: int | None = None,
    verwarmd: bool | None = None,
    verkoeld: bool | None = None,
    lengte: int | None = None,
    breedte: int | None = None,
    hoogte: int | None = None,
    aantal: int | None = None,
) -> EenhedenRuimte:
    """Maak een ruimte; de naam volgt uit de detailsoort en de id uit de naam.

    Nummer de ruimten met `naam` wanneer een eenheid meer ruimten van dezelfde
    detailsoort heeft: "Badkamer1", "Badkamer2".

    De soort volgt uit de detailsoort. Geef `soort` mee wanneer de ruimte met
    een andere ruimtesoort is aangeleverd, zoals een schuur als vertrek.

    Zonder `gedeeld_met_aantal_onzelfstandige_woonruimten` is de ruimte privé.
    Zonder `gedeeld_met_aantal_adressen` is ze niet met andere adressen gedeeld.

    Zonder `verwarmd` is de ruimte niet verwarmd, zonder `verkoeld` heeft ze
    geen verkoelingsfunctie.

    Zonder `lengte`, `breedte` en `hoogte` heeft de ruimte geen
    afmetingen, alleen een oppervlakte. Afmetingen zijn in mm, zoals in VERA.

    Zonder `aantal` is de ruimte één parkeerplek. Geef `aantal` mee wanneer de
    ruimte voor meer dan één parkeerplek van dezelfde soort staat.
    """
    naam = naam or detail_soort.naam or ""
    nieuwe_ruimte = EenhedenRuimte(
        id=naam.lower().replace(" ", "_"),
        naam=naam,
        soort=soort or detail_soort.parent,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        installaties=list(installaties) or None,
        bouwkundige_elementen=list(elementen) or None,
        verbonden_ruimten=list(verbonden_ruimten) or None,
        gedeeld_met_aantal_onzelfstandige_woonruimten=(
            gedeeld_met_aantal_onzelfstandige_woonruimten
        ),
        gedeeld_met_aantal_adressen=gedeeld_met_aantal_adressen,
        verwarmd=verwarmd,
        verkoeld=verkoeld,
        lengte=lengte,
        breedte=breedte,
        hoogte=hoogte,
    )
    # Het model geeft `aantal` zelf de standaardwaarde 1; alleen een meegegeven
    # aantal komt in de input van de test.
    if aantal is not None:
        nieuwe_ruimte.aantal = aantal
    return nieuwe_ruimte


def element(
    detail_soort: BouwkundigelementdetailsoortReferentiedata,
    *,
    id: str | None = None,
    lengte: int | None = None,
) -> BouwkundigElementenBouwkundigElement:
    """Maak een bouwkundig element; id en naam volgen uit de detailsoort.

    De `lengte` is in mm, zoals in VERA.
    """
    naam = detail_soort.naam or ""
    return BouwkundigElementenBouwkundigElement(
        id=id or naam.lower().replace(" ", "_"),
        naam=naam,
        soort=detail_soort.parent,
        detail_soort=detail_soort,
        lengte=lengte,
    )


def elementen(
    *detail_soorten: BouwkundigelementdetailsoortReferentiedata,
) -> list[BouwkundigElementenBouwkundigElement]:
    """Maak een bouwkundig element per detailsoort, elk met een eigen id."""
    return [
        element(detail_soort, id=f"element_{nummer}")
        for nummer, detail_soort in enumerate(detail_soorten, start=1)
    ]


def aanrecht(
    lengte: int, *, id: str = "aanrecht"
) -> BouwkundigElementenBouwkundigElement:
    return element(Bouwkundigelementdetailsoort.aanrecht, id=id, lengte=lengte)


def meergezinswoning_van_71_m2(
    *,
    bouwjaar: int,
    woz_eenheden: Sequence[EenhedenWozEenheid] = (),
    energieprestaties: Sequence[EenhedenEnergieprestatie] = (),
    renovatie: EenhedenRenovatie | None = None,
    aanrecht_mm: int | None = 2100,
) -> EenhedenEenheid:
    """Maak een meergezinswoning van 71 m² met vijftien ruimten, waaronder vijf vertrekken en een balkon.

    Gebruik haar voor een beleidsregel die het puntentotaal van andere rubrieken
    nodig heeft, zoals het minimum en de cap van de punten voor de WOZ-waarde.

    Met `aanrecht_mm=None` heeft de keuken geen aanrecht.
    """
    # De vaste kasten, de meterruimte en de technische ruimte zijn ruimten van
    # de eenheid en ook de verbonden ruimten van de keuken, de woonkamer en de
    # hal.
    kast1 = ruimte(Ruimtedetailsoort.kast, naam="Kast1", oppervlakte=0.856)
    kast2 = ruimte(Ruimtedetailsoort.kast, naam="Kast2", oppervlakte=0.312)
    kast3 = ruimte(Ruimtedetailsoort.kast, naam="Kast3", oppervlakte=0.308)
    kast4 = ruimte(Ruimtedetailsoort.kast, naam="Kast4", oppervlakte=0.3575)
    meterruimte = ruimte(Ruimtedetailsoort.meterruimte, oppervlakte=0.2205)
    technische_ruimte = ruimte(
        Ruimtedetailsoort.technische_ruimte,
        oppervlakte=0.3456,
        elementen=[element(Bouwkundigelementdetailsoort.verwarmingstoestellen)],
    )
    return EenhedenEenheid(
        id="meergezinswoning_van_71_m2",
        bouwjaar=bouwjaar,
        renovatie=renovatie,
        adres=EenhedenEenheidadres(
            huisnummer="44",
            huisnummer_toevoeging="",
            postcode="3012CJ",
            woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            bag_identificatie="0599010000320510"
        ),
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=list(woz_eenheden) or None,
        energieprestaties=list(energieprestaties),
        gebruiksoppervlakte=71,
        monumenten=[],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.balkon,
                oppervlakte=1.82259,
                lengte=1290,
                breedte=1500,
                hoogte=2600,
            ),
            technische_ruimte,
            ruimte(Ruimtedetailsoort.schuur, oppervlakte=0.2345),
            ruimte(
                Ruimtedetailsoort.badkamer,
                oppervlakte=3.584,
                verwarmd=True,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.douche,
                    Bouwkundigelementdetailsoort.wastafel,
                ),
            ),
            ruimte(
                Ruimtedetailsoort.keuken,
                oppervlakte=9.5565,
                verwarmd=True,
                elementen=[aanrecht(aanrecht_mm)] if aanrecht_mm is not None else [],
                verbonden_ruimten=[kast3, technische_ruimte, kast2],
            ),
            ruimte(
                Ruimtedetailsoort.woonkamer,
                oppervlakte=25.96,
                verwarmd=True,
                verbonden_ruimten=[kast1],
            ),
            ruimte(
                Ruimtedetailsoort.hal,
                oppervlakte=6.198,
                verwarmd=True,
                verbonden_ruimten=[kast4, meterruimte],
            ),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                oppervlakte=6.486,
                verwarmd=True,
            ),
            kast1,
            meterruimte,
            kast2,
            ruimte(
                Ruimtedetailsoort.toiletruimte,
                oppervlakte=1.26375,
                elementen=elementen(
                    Bouwkundigelementdetailsoort.wastafel,
                    Bouwkundigelementdetailsoort.closetcombinatie,
                ),
            ),
            kast3,
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                oppervlakte=12.978,
                verwarmd=True,
            ),
            kast4,
        ],
    )


def zorgwoning_van_71_m2(
    *,
    bouwjaar: int,
    monumenten: Sequence[EenheidmonumentReferentiedata] = (),
    datum_afsluiten_huurovereenkomst: date | None = None,
) -> EenhedenEenheid:
    """Maak de meergezinswoning van 71 m² als zorgwoning: de eenheid heeft de doelgroep zorg.

    Gebruik haar voor een beleidsregel over de verhoging van een zorgwoning, die
    het puntentotaal van de rubrieken 1 tot en met 11 nodig heeft.

    Zonder `monumenten` is de woning geen monument, en zonder
    `datum_afsluiten_huurovereenkomst` heeft ze er geen.
    """
    zorgwoning = meergezinswoning_van_71_m2(bouwjaar=bouwjaar)
    zorgwoning.doelgroep = Doelgroep.zorg
    zorgwoning.monumenten = list(monumenten)
    zorgwoning.datum_afsluiten_huurovereenkomst = datum_afsluiten_huurovereenkomst
    return zorgwoning


def meergezinswoning_van_79_m2(
    *,
    begin_bouwdatum: date,
    in_exploitatiedatum: date,
    woz_eenheden: Sequence[EenhedenWozEenheid] = (),
) -> EenhedenEenheid:
    """Maak een meergezinswoning van 79 m² met elf ruimten, waaronder vijf vertrekken en een balkon.

    Gebruik haar voor een beleidsregel die het puntentotaal van alle rubrieken
    nodig heeft, zoals de opslag voor nieuwbouw.

    De woning heeft geen bouwjaar. De keuken heeft geen aanrecht en de badkamer
    en de toiletruimte hebben geen sanitair.
    """
    return EenhedenEenheid(
        id="meergezinswoning_van_79_m2",
        begin_bouwdatum=begin_bouwdatum,
        in_exploitatiedatum=in_exploitatiedatum,
        panden=[EenhedenPand(soort=Pandsoort.meergezinswoning)],
        woz_eenheden=list(woz_eenheden) or None,
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2019, 7, 3),
                einddatum=date(2029, 7, 3),
                label=Energielabel.b,
                waarde="1.24",
            )
        ],
        gebruiksoppervlakte=79,
        monumenten=[],
        ruimten=[
            ruimte(
                Ruimtedetailsoort.balkon,
                oppervlakte=4.61588,
                lengte=1680,
                breedte=3080,
                hoogte=2440,
            ),
            ruimte(Ruimtedetailsoort.meterruimte, oppervlakte=0.27125),
            ruimte(Ruimtedetailsoort.woonkamer, oppervlakte=30.1218, verwarmd=True),
            ruimte(Ruimtedetailsoort.entree, oppervlakte=7.14345, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer1",
                oppervlakte=11.718,
                verwarmd=True,
            ),
            ruimte(Ruimtedetailsoort.berging, naam="Berging1", oppervlakte=5.09507),
            ruimte(Ruimtedetailsoort.badkamer, oppervlakte=4.644, verwarmd=True),
            ruimte(
                Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer2",
                oppervlakte=9.2092,
                verwarmd=True,
            ),
            ruimte(Ruimtedetailsoort.keuken, oppervlakte=5.76, verwarmd=True),
            ruimte(Ruimtedetailsoort.berging, naam="Berging2", oppervlakte=1.8836),
            ruimte(Ruimtedetailsoort.toiletruimte, oppervlakte=1.28113),
        ],
    )


def woz_eenheden_voor_149_punten() -> list[EenhedenWozEenheid]:
    """Geef de WOZ-waarden die `meergezinswoning_van_79_m2` op 149 punten brengen.

    Daarmee valt de woning in de middensector (144 t/m 186 punten).
    """
    waarden = {
        2024: 313000,
        2023: 307000,
        2022: 341000,
        2021: 283000,
        2020: 273000,
        2019: 237000,
        2018: 201000,
        2017: 163000,
        2016: 142000,
        2015: 135000,
        2014: 125000,
    }
    return [
        EenhedenWozEenheid(waardepeildatum=date(jaar, 1, 1), vastgestelde_waarde=waarde)
        for jaar, waarde in waarden.items()
    ]
