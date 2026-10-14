# test_ruimte_zonder_detailsoort_geeft_een_waarschuwing

Een ruimte zonder detailsoort is incomplete input en wordt niet gewaardeerd.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Sanitair.

## Waarschuwingen

- UserWarning: Ruimte 'None' (ruimte) heeft geen detailsoort.

## Input

```json
{
  "ruimten": [
    {
      "id": "ruimte"
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
