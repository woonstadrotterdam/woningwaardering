# Naamgeving van classes

Voor de naamgeving van de classes in de woningwaardering module volgen we de VERA referentiedata. Deze referentiedata is gedefinieerd in de referentiedata enums, te vinden onder [/woningwaardering/vera/referentiedata](https://github.com/woonstadrotterdam/woningwaardering/tree/main/woningwaardering/vera/referentiedata).

## Genereren opzet woningwaarderingstelsels en -groepen

Om alle onderstaande naamgevingen correct en consequent door te voeren, is er een task beschikbaar die de opzet van een woningwaarderingstelsel en -groep volgens deze regels voor je kan aanmaken.

Zorg er voor dat [Task](https://taskfile.dev/installation/) en de dev dependencies zijn geïnstalleerd:

```bash
pip install -e ".[dev]"
```

Vervolgens voer je onderstaand command uit:

```bash
task genereer-opzet-woningwaarderinggroep
```

Dit script stelt je een aantal vragen, waarna de code voor het stelsel en de stelselgroep aangemaakt worden.

## Stelsels

De namen voor de stelsels zijn te vinden in de `Woningwaarderingstelsel` Enum. Bijvoorbeeld: het stelsel voor zelfstandige woonruimten wordt aangeduid als `Woningwaarderingstelsel.zelfstandige_woonruimten`. De implementatie van dit `Stelsel` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py](https://github.com/woonstadrotterdam/woningwaardering/blob/main/woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py).
De geldigheid van een stelsel wordt bepaald door de begin- en einddatum, die in de constructor van de corresponderende klasse worden vastgelegd.

## Stelselgroepen

De namen voor de stelselgroepen zijn te vinden in de `Woningwaarderingstelselgroep` Enum. Bijvoorbeeld: de stelselgroep voor oppervlakte van vertrekken wordt aangeduid als `Woningwaarderingstelselgroep.oppervlakte_van_vertrekken`. De implementatie van deze `Stelselgroep` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py](https://github.com/woonstadrotterdam/woningwaardering/blob/main/woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py).
De geldigheid van een stelselgroep wordt bepaald door de begin- en einddatum, die in de constructor van de corresponderende klasse worden vastgelegd. 