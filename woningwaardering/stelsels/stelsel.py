from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd

from woningwaardering.stelsels.stelselgroep import (
    Stelselgroep,
)
from woningwaardering.stelsels.utils import (
    is_geldig,
    rond_af,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class Stelsel:
    """Initialiseert een Stelsel object.

    Parameters:
        stelsel (Woningwaarderingstelsel): Het stelsel dat wordt berekend.
        begindatum (date): De begindatum van de geldigheid van het stelsel.
        einddatum (date, optional): De einddatum van de geldigheid van het stelsel.
        peildatum (date, optional): De peildatum voor de waardering.
            Standaard is de huidige datum.
        stelselgroepen (list[type[Stelselgroep]] | None, optional): De stelselgroepen die worden berekend.

    Raises:
        ValueError: Als het stelsel niet geldig is op de peildatum.
    """

    def __init__(
        self,
        stelsel: Woningwaarderingstelsel,
        begindatum: date,
        einddatum: date = date.max,
        peildatum: date = date.today(),
        stelselgroepen: list[type[Stelselgroep]] | None = None,
    ) -> None:
        self.stelsel = stelsel
        if not is_geldig(begindatum, einddatum, peildatum):
            raise ValueError(
                f"Stelsel {stelsel.value.naam} met begindatum {begindatum} en einddatum {einddatum} is niet geldig op peildatum {peildatum}."
            )
        self.peildatum = peildatum
        self.stelselgroepen = [
            stelselgroep(peildatum) for stelselgroep in stelselgroepen or []
        ]
        self.df_maximale_huur = pd.read_csv(
            files("woningwaardering").joinpath(
                f"stelsels/{stelsel.name}/maximale_huurprijzen.csv"
            )
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        *,
        negeer_stelselgroep: type[Stelselgroep] | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """Berekent de woningwaardering voor een stelsel.

        Parameters:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.
            negeer_stelselgroep (type[Stelselgroep] | None, optional): Een stelselgroep die moet worden overgeslagen.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het bijgewerkte resultaat van de woningwaardering.
        """

        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
        resultaat.stelsel = self.stelsel.value

        resultaat.groepen = []

        for stelselgroep in self.stelselgroepen:
            if negeer_stelselgroep is not None and isinstance(
                stelselgroep, negeer_stelselgroep
            ):
                continue

            resultaat.groepen.append(stelselgroep.bereken(eenheid, resultaat))

        # Het puntentotaal per woning wordt na eindsaldering (met inbegrip van de bij
        # zorgwoningen geldende toeslag) afgerond op hele punten. Bij 0,5 punten of
        # meer wordt afgerond naar boven op hele punten, bij minder dan 0,5 punten
        # wordt afgerond naar beneden op hele punten.
        #
        # https://wetten.overheid.nl/BWBR0003237/2024-01-01#BijlageI_DivisieA_Divisie_Divisie15

        resultaat.punten = Stelsel.bereken_puntentotaal(resultaat)

        resultaat.opslagpercentage = (
            sum(
                woningwaardering_groep.opslagpercentage
                for woningwaardering_groep in resultaat.groepen or []
                if woningwaardering_groep.opslagpercentage is not None
            )
            or None
        )

        maximale_huur = self.bereken_maximale_huur(resultaat)

        resultaat.maximale_huur = float(maximale_huur)

        if resultaat.opslagpercentage is not None:
            resultaat.huurprijsopslag = float(
                rond_af(
                    maximale_huur * Decimal(str(resultaat.opslagpercentage)),
                    decimalen=2,
                )
            )

        resultaat.maximale_huur_inclusief_opslag = float(
            maximale_huur + Decimal(str(resultaat.huurprijsopslag or 0))
        )

        return resultaat

    @staticmethod
    def bereken_puntentotaal(
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> float:
        return float(
            rond_af(
                sum(
                    woningwaardering_groep.punten
                    for woningwaardering_groep in resultaat.groepen or []
                    if woningwaardering_groep.punten is not None
                ),
                decimalen=0,
            ),
        )

    def bereken_maximale_huur(
        self, resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
    ) -> Decimal:
        punten = Decimal(str(resultaat.punten))

        df_maximale_huur = self.df_maximale_huur

        begrensde_punten = min(
            max(punten, df_maximale_huur["Punten"].min()),
            df_maximale_huur["Punten"].max(),
        )

        maximale_huur = Decimal(
            df_maximale_huur[df_maximale_huur["Punten"] == begrensde_punten][
                "Bedrag"
            ].item()
        )

        hoogste_twee = df_maximale_huur.nlargest(2, "Punten")
        hoogste_punten = Decimal(hoogste_twee.iloc[0]["Punten"])
        hoogste_bedrag = Decimal(hoogste_twee.iloc[0]["Bedrag"])
        een_na_hoogste_bedrag = Decimal(hoogste_twee.iloc[1]["Bedrag"])

        bedrag_verschil = hoogste_bedrag - een_na_hoogste_bedrag

        punten_boven_hoogste = max(punten - hoogste_punten, Decimal(0))
        aanvullende_waarde = punten_boven_hoogste * bedrag_verschil

        maximale_huur += aanvullende_waarde

        return maximale_huur
