# test_eenheid_zonder_adres_krijgt_met_waarschuwing_geen_waardering

Een eenheid zonder adres krijgt met een waarschuwing geen waardering voor de WOZ-waarde.

## Rapport

Geen waarderingen voor Punten voor de WOZ-waarde.

## Waarschuwingen

- UserWarning: Eenheid eenheid: adres met woonplaatscode of postcode en huisnummer ontbreekt, COROP-gebied kan niet bepaald worden voor gemiddelde WOZ waarde

## Input

```json
{
  "id": "eenheid",
  "adresseerbaarObjectBasisregistratie": {
    "bagGebruikersOppervlakte": 58
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 148000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 184000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 205000.0,
      "waardepeildatum": "2024-01-01"
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "WOZ",
      "naam": "Punten voor de WOZ-waarde"
    }
  },
  "woningwaarderingen": []
}
```
