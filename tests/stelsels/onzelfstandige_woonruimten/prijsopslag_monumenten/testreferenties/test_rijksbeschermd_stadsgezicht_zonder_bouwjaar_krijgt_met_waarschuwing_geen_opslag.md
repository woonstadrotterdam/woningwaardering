# test_rijksbeschermd_stadsgezicht_zonder_bouwjaar_krijgt_met_waarschuwing_geen_opslag

Een woonruimte in een rijksbeschermd stadsgezicht zonder bouwjaar krijgt met een waarschuwing geen opslag.

## Rapport

Geen waarderingen voor Prijsopslag monumenten.

## Waarschuwingen

- UserWarning: Eenheid (eenheid): geen bouwjaar gevonden

## Input

```json
{
  "id": "eenheid",
  "monumenten": [
    {
      "code": "SGR",
      "naam": "Rijksbeschermd stadsgezicht"
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
      "code": "PMO",
      "naam": "Prijsopslag monumenten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [],
  "opslagpercentage": 0.0
}
```
