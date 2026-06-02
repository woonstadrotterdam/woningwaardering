import json
import warnings
from datetime import date
from pathlib import Path

from woningwaardering import Woningwaardering
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


def _regen_json_input(wws: Woningwaardering) -> None:
    input_path = Path("tests/data/generiek/input/37101000032.json")
    output_path = Path("tests/docs/output_json_json_voorbeeld.json")

    eenheid = EenhedenEenheid.model_validate_json(input_path.read_text())
    resultaat = wws.waardeer(eenheid)
    output_path.write_text(
        resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True) + "\n"
    )


def _regen_python_input(wws: Woningwaardering) -> None:
    output_path = Path("tests/docs/output_json_python_voorbeeld.json")

    eenheid = EenhedenEenheid(
        id="37101000032",
        bouwjaar=1924,
        woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
        adres=EenhedenEenheidadres(
            straatnaam="Nieuwe Boezemstraat",
            huisnummer="27",
            huisnummer_toevoeging="",
            postcode="3034PH",
            woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
        ),
        adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
            id="0599010000485697", bag_identificatie="0599010000485697"
        ),
        panden=[EenhedenPand(soort=Pandsoort.eengezinswoning)],
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

    resultaat = wws.waardeer(eenheid)
    output_path.write_text(
        resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True) + "\n"
    )


def main() -> int:
    peildatum = date(2026, 1, 1)
    wws = Woningwaardering(peildatum=peildatum)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        _regen_json_input(wws)
        _regen_python_input(wws)

    # sanity: JSON files should be valid JSON
    json.loads(Path("tests/docs/output_json_json_voorbeeld.json").read_text())
    json.loads(Path("tests/docs/output_json_python_voorbeeld.json").read_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

