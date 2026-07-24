# Naamgeving van classes

Voor de naamgeving van de classes in de woningwaardering module volgen we de VERA referentiedata. Deze referentiedata is gedefinieerd in de referentiedata enums, te vinden onder [/woningwaardering/vera/referentiedata](https://github.com/woonstadrotterdam/woningwaardering/tree/main/woningwaardering/vera/referentiedata).

Bij een nieuwe stelselgroep: kopieer een bestaande implementatie onder `woningwaardering/stelsels/` als uitgangspunt, volg de naamgeving hieronder, en bouw de output met de builders in `woningwaardering/stelsels/builders.py` (zie [opzet](../introductie/opzet.md)).

## Stelsels

De namen voor de stelsels zijn te vinden in de `Woningwaarderingstelsel` Enum. Bijvoorbeeld: het stelsel voor zelfstandige woonruimten wordt aangeduid als `Woningwaarderingstelsel.zelfstandige_woonruimten`. De implementatie van dit `Stelsel` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py](https://github.com/woonstadrotterdam/woningwaardering/blob/main/woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py).

## Stelselgroepen

De namen voor de stelselgroepen zijn te vinden in de `Woningwaarderingstelselgroep` Enum. Bijvoorbeeld: de stelselgroep voor oppervlakte van vertrekken wordt aangeduid als `Woningwaarderingstelselgroep.oppervlakte_van_vertrekken`. De implementatie van deze `Stelselgroep` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py](https://github.com/woonstadrotterdam/woningwaardering/blob/main/woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py).
