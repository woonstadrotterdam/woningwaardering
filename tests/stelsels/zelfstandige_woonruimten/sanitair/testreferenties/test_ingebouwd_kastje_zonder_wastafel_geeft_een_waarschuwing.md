# test_ingebouwd_kastje_zonder_wastafel_geeft_een_waarschuwing

Een ingebouwd kastje met wastafel zonder wastafel in de ruimte is onjuiste input.

## Rapport

Geen waarderingen voor Sanitair.

## Waarschuwingen

- UserWarning: Ruimte 'Badkamer' (badkamer): 0 wastafel(s) zijn minder dan het aantal ingebouwde kasten met wastafel (1). Een wastafel in een Ingebouwd kastje met in- of opgebouwde wastafel moet apart worden meegegeven.
- UserWarning: Ruimte 'Badkamer' (badkamer): geen wastafel aanwezig in Badkamer, extra voorzieningen worden niet gewaardeerd.

## Input

```json
{
  "ruimten": [
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "IKW",
          "naam": "Ingebouwd kastje met in- of opgebouwde wastafel"
        }
      ]
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
