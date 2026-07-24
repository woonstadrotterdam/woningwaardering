from __future__ import annotations

from datetime import date
from pathlib import Path

from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheid,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRuimte,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Pandsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)


def voorbeeld1_json_input_path() -> Path:
    """Pad naar het JSON input-voorbeeld zoals gebruikt in docs/tests."""
    return Path("tests/data/generiek/input/37101000032.json")


def voorbeeld2_python_eenheid() -> EenhedenEenheid:
    """Python object input uit docs/aan-de-slag, voorbeeld 2."""
    return EenhedenEenheid(
        id="37101000032",
        bouwjaar=1924,
        woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
        adres=EenhedenEenheidadres(
            straatnaam="",
            huisnummer="",
            huisnummer_toevoeging="",
            postcode="",
            woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            id="", bag_identificatie=""
        ),
        panden=[
            EenhedenPand(
                soort=Pandsoort.eengezinswoning,
            )
        ],
        woz_eenheden=[
            EenhedenWozEenheid(waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=618000),
            EenhedenWozEenheid(waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=643000),
            EenhedenWozEenheid(waardepeildatum=date(2024, 1, 1), vastgestelde_waarde=694000),
        ],
        energieprestaties=[
            EenhedenEnergieprestatie(
                soort=Energieprestatiesoort.energie_index,
                status=Energieprestatiestatus.definitief,
                begindatum=date(2019, 2, 25),
                einddatum=date(2029, 2, 25),
                registratiedatum="2019-02-26T14:51:38+01:00",
                label=Energielabel.c,
                waarde="1.58",
            )
        ],
        gebruiksoppervlakte=187,
        monumenten=[],
        ruimten=[
            EenhedenRuimte(
                id="Space_108014589",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.slaapkamer,
                naam="Slaapkamer",
                inhoud=60.4048,
                oppervlakte=21.047,
                verwarmd=True,
            ),
            EenhedenRuimte(
                id="Space_108006229",
                soort=Ruimtesoort.vertrek,
                detail_soort=Ruimtedetailsoort.keuken,
                naam="Keuken",
                inhoud=57.4359,
                oppervlakte=20.3673,
                verwarmd=True,
                bouwkundige_elementen=[
                    BouwkundigElementenBouwkundigElement(
                        id="Aanrecht_108006231",
                        naam="Aanrecht",
                        omschrijving="Aanrecht in Keuken",
                        soort=Bouwkundigelementsoort.voorziening,
                        detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                        lengte=2700,
                    )
                ],
            ),
        ],
    )

