from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from woningwaardering.vera.bvg.generated import Referentiedata


class _EenhedenOppervlakte(BaseModel):
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
    soort: Optional[Referentiedata] = None
    """
    Het soort oppervlakte. Bijv. GO (Gebruiksoppervlakte) of BVO (Brutovloeroppervlak) Referentiedatasoort OPPERVLAKTESOORT.
    """
    waarde: Optional[str] = None
    """
    De waarde van de oppervlakte in vierkante meters (m2)
    """
