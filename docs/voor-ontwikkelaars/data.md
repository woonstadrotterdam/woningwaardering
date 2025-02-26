# Data

Dit onderdeel bevat informatie over de verschillende datastructuren die gebruikt worden in het woningwaardering project.

## Datamodellen

De datamodellen in de `woningwaardering` package zijn gebaseerd op de OpenAPI-specificatie van het [VERA BVG domein](https://aedes-datastandaarden.github.io/vera-openapi/Ketenprocessen/BVG.html).

Wanneer je deze modellen wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) en de dev dependencies zijn geïnstalleerd:

```bash
pip install -e ".[dev]"
```

Update het versienummer van de VERA OpenAPI-specificatie in `pyproject.toml`

Vervolgens kan je met dit commando de modellen in deze repository bijwerken:

```bash
task genereer-vera-bvg-modellen
```

De classes voor deze modellen worden gegeneerd in `woningwaardering/vera/bvg/generated.py`

### Datamodellen uitbreiden

Wanneer de VERA modellen niet toereikend zijn om de woningwaardering te berekenen, kan het VERA model uitgebreid worden.

Maak hiervoor altijd eerst een issue aan in de [VERA OpenApi repository](https://github.com/Aedes-datastandaarden/vera-openapi).

Maak vervolgens in de map [woningwaardering/vera/bvg/model_uitbreidingen](https://github.com/woonstadrotterdam/woningwaardering/tree/main/woningwaardering/vera/bvg/model_uitbreidingen) een class aan met de missende attributen. De naamgeving voor deze classes is: `_{classNaam}`.

Zet in de class bij het toegevoegde attribuut een comment met een link naar het issue in de VERA OpenApi repository zodat duidelijk is waar de toevoeging voor dient, en we kunnen volgen of de aanpassing is doorgevoerd in de VERA modellen.

Daarnaast neem je in de class een docstring op met uitleg over het gebruik en doel van de uitbreiding.

Bijvoorbeeld: voor het uitbreiden van de class `EenhedenRuimte` maak je een class `_EenhedenRuimte` aan:

```python
from typing import Optional

from pydantic import BaseModel, Field


class _EenhedenRuimte(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/44
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden"
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld. Deze waarde wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging.
    """
```

De task `genereer-vera-bvg-modellen` zal de body van deze classes samenvoegen met de gelijknamige VERA class en zo de toegevoegde attributen beschikbaar maken.

## Referentiedata

We maken gebruik van de [VERA Referentiedata](https://github.com/Aedes-datastandaarden/vera-referentiedata).

Wanneer je de referentiedata wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd

Update het versienummer van de referentiedata in `pyproject.toml`
Vervolgens kan je met dit commando de referentiedata in deze repository bijwerken:

```bash
task genereer-vera-referentiedata
```

De referentiedata wordt gegenereerd in `woningwaardering/vera/referentiedata`

## Woonplaatsen en COROP-gebieden

Om te bepalen in welk COROP-gebied een woonplaats ligt, maken we gebruik van de CBS datasets "Woonplaatsen in Nederland" en "Gebieden in Nederland".
Het CBS publiceert eens per jaar nieuwe datasets, daarom hebben we een script gemaakt dat een extract van deze data als resource in de package opslaat in `woningwaardering/data/corop/corop.generated.csv`.

Wanneer je deze data bij wilt werken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd.

Vervolgens kan je met dit commando de woonplaatsen en COROP-gebieden in deze repository bijwerken:

```bash
task genereer-corop-data
```

## Gemiddelde WOZ-waarden per vierkante meter per COROP-gebied

Bij het beleidsboek wordt een bijlage gepubliceerd met de gemiddelde WOZ-waarden per vierkante meter per COROP-gebied. Na publicatie van een nieuwe bijlage dient het bestand `woningwaardering/stelsels/onzelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen/corop_gebied_gemiddelde_woz_waarde_per_m2.csv` bijgewerkt te worden, door een kolom toe te voegen met als kolomnaam het jaar van de waardepeildatum waarvoor de nieuwe gemiddelde waarden gelden. 