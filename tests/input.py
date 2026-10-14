"""Functies voor testinput: VERA-objecten met standaardwaarden.

Wat een beleidsregel raakt geeft de test zelf mee; de rest krijgt hier een
standaardwaarde. Zie docs/voor-ontwikkelaars/testing.md.
"""

from collections.abc import Sequence

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
    lengte_mm: int | None = None,
    breedte_mm: int | None = None,
    hoogte_mm: int | None = None,
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

    Zonder `lengte_mm`, `breedte_mm` en `hoogte_mm` heeft de ruimte geen
    afmetingen, alleen een oppervlakte.

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
        lengte=lengte_mm,
        breedte=breedte_mm,
        hoogte=hoogte_mm,
    )
    # Het model geeft `aantal` zelf de standaardwaarde 1; alleen een meegegeven
    # aantal komt in de input van de test.
    if aantal is not None:
        nieuwe_ruimte.aantal = aantal
    return nieuwe_ruimte


def badkamer(
    *installaties: InstallatiesoortReferentiedata,
    elementen: Sequence[BouwkundigElementenBouwkundigElement] = (),
    naam: str | None = None,
) -> EenhedenRuimte:
    return ruimte(
        Ruimtedetailsoort.badkamer, *installaties, elementen=elementen, naam=naam
    )


def element(
    detail_soort: BouwkundigelementdetailsoortReferentiedata,
    *,
    id: str | None = None,
    lengte_mm: int | None = None,
) -> BouwkundigElementenBouwkundigElement:
    """Maak een bouwkundig element; id en naam volgen uit de detailsoort."""
    naam = detail_soort.naam or ""
    return BouwkundigElementenBouwkundigElement(
        id=id or naam.lower().replace(" ", "_"),
        naam=naam,
        soort=detail_soort.parent,
        detail_soort=detail_soort,
        lengte=lengte_mm,
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
    lengte_mm: int, *, id: str = "aanrecht"
) -> BouwkundigElementenBouwkundigElement:
    return element(Bouwkundigelementdetailsoort.aanrecht, id=id, lengte_mm=lengte_mm)


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
                lengte_mm=1290,
                breedte_mm=1500,
                hoogte_mm=2600,
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
