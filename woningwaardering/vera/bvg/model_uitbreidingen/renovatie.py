from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenPand,
)


class _Renovatie(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: Optional[str] = None
    """
    De primaire sleutel van het gegeven in het bronsysteem. Je verstuurt een entiteit altijd met het eigen id. Id kan leeg zijn.
    """
    id_extern: Optional[str] = Field(default=None, alias="idExtern")
    """
    De primaire sleutel van het gegeven in het doelsysteem. Deze idExtern wisselt om met id afhankelijk van de richting van de gegevensuitwisseling.
    """
    id_gegevensbeheerder: Optional[str] = Field(
        default=None, alias="idGegevensbeheerder"
    )
    """
    De primaire sleutel van het gegeven van de gegevensbeheerder. Bijv. de overheid of andere standaarden.
    """
    code: Optional[str] = None
    """
    De unieke code (Bijvoorbeeld om te tonen of te zoeken)
    """
    omschrijving: Optional[str] = None
    """
    De omschrijving van de renovatie(s) behorend bij de eenheid.
    """
    datum: Optional[date] = None
    """
    De datum dat het object is gerenoveerd.
    """
    eenheden: Optional[list[EenhedenEenheid]] = None
    """
    Verwijzing naar de eenheden waarvoor de renovatie is gedaan.
    """
    panden: Optional[list[EenhedenPand]] = None
    """
    Verwijzing naar de panden waarvoor de renovatie is gedaan.
    """
