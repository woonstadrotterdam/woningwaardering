# test_buitenruimte_zonder_oppervlakte_geeft_een_waarschuwing

Een buitenruimte zonder oppervlakte geeft een waarschuwing over incomplete input.

## Rapport

Geen waarderingen voor Buitenruimten.

## Waarschuwingen

- UserWarning: Ruimte 'Balkon' (balkon) heeft geen oppervlakte

## Input

```json
{
  "ruimten": [
    {
      "id": "balkon",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon"
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
