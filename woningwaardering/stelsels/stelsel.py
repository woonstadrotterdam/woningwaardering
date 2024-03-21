from datetime import date, datetime

from loguru import logger

from woningwaardering.stelsels.config.config import Config
from woningwaardering.stelsels.zelfstandig.oppervlakte_van_vertrekken.basis import (
    OppervlakteVanVertrekken,
)
from woningwaardering.utils import import_stelselgroep_versie
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelsel:
    def __init__(
        self,
        stelsel: str,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = stelsel
        self.peildatum = peildatum
        self.stelsel_config = Config.load(stelsel=self.stelsel).model_dump()["stelsel"][
            self.stelsel
        ]

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        main
        """
        resultaat.groepen = []

        for stelselgroep, stelselgroep_config in self.stelsel_config[
            "stelselgroepen"
        ].items():
            for versie in stelselgroep_config["versies"]:  # type: ignore[attr-defined]
                for versie_class_naam, geldigheid in versie.items():
                    begindatum: str = str(geldigheid["begindatum"])
                    einddatum: str = str(geldigheid["einddatum"])
                    if (
                        datetime.strptime(begindatum, "%d-%m-%Y").date()
                        <= self.peildatum
                        <= datetime.strptime(einddatum, "%d-%m-%Y").date()
                    ):
                        logger.debug(
                            f"Stelselgroepversie '{versie_class_naam}' is geldig voor stelsel '{self.stelsel}' en stelselgroep '{stelselgroep}' met peildatum '{self.peildatum}'."
                        )
                        stelselgroep_versie = import_stelselgroep_versie(
                            f"woningwaardering.stelsels.{self.stelsel}.{stelselgroep}",
                            versie_class_naam,
                        )

                    resultaat.groepen.append(
                        stelselgroep_versie.bereken(
                            eenheid=eenheid,
                            woningwaardering_resultaat=resultaat,
                        )
                    )

        return resultaat


# from woningwaardering.stelsels.zelfstandig_ import Zelfstandig

f = open("./woningwaardering/41164000002.json", "r+")
eenheid = EenhedenEenheid.model_validate_json(f.read())
woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()


opp = OppervlakteVanVertrekken("01-02-2024")
print(opp.bereken(eenheid, woningwaardering_resultaat))

# moet de config aan pydantic model worden?
# with open("./woningwaardering/config.yml", "r") as file:
#     config = yaml.safe_load(file)

# f = open("./woningwaardering/41164000002.json", "r+")


# # woningwaardering_resultaat.groepen = []

# zelfstandig = Stelsel(
#     code="zelfstandig",
#     config=config,
#     eenheid=eenheid,
#     resultaat=woningwaardering_resultaat,
# )

# woningwaardering_resultaat = zelfstandig.main()

# woningwaardering_resultaat.punten = sum(
#     woningwaardering_groep.punten
#     for woningwaardering_groep in woningwaardering_resultaat.groepen or []
#     if woningwaardering_groep.punten is not None
# )

# print(
#     woningwaardering_resultaat.model_dump_json(
#         by_alias=True, exclude_unset=True, indent=2
#     )
# )
