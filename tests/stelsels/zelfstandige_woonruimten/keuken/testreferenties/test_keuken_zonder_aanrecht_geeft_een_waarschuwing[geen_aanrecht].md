# test_keuken_zonder_aanrecht_geeft_een_waarschuwing[geen_aanrecht]

Een keuken zonder aanrecht is incomplete input en wordt niet gewaardeerd.

## Rapport

Geen waarderingen voor Keuken.

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor Keuken.
- UserWarning: Eenheid (eenheid) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "id": "eenheid",
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
