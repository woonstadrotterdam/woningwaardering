# gedeelde_parkeerplaats

## Doel

Test dat een met andere adressen gedeelde parkeerplaats niet als buitenruimte wordt geclassificeerd en dus geen punten oplevert onder buitenruimten.

## Beleidsbron

- Implementatietoelichting: [§2.8.3 Gemeenschappelijke buitenruimte als parkeerplek](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#283-gemeenschappelijke-buitenruimte-als-parkeerplek)
- Beleidsboek (quote): "Gedeelde buitenruimten die als parkeerplek voor auto’s bedoeld zijn, worden gewaardeerd volgens rubriek 10."
- NOTE: generieke `Ruimtedetailsoort.parkeerplaats` gedeeld met meerdere adressen telt niet mee in rubriek 8 (en zonder specifieke parkeer-detailsoort ook niet in rubriek 10).
