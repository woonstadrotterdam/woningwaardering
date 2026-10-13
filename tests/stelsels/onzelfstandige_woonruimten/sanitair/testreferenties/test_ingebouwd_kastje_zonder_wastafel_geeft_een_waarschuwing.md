# test_ingebouwd_kastje_zonder_wastafel_geeft_een_waarschuwing

Een ingebouwd kastje met wastafel zonder wastafel in de ruimte is onjuiste input.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.2: "Voor een
ingebouwde kast met wastafel moet de wastafel als aparte voorziening worden
meegegeven."

## Rapport

Geen waarderingen voor Sanitair.

## Waarschuwingen

- UserWarning: Ruimte 'Toiletruimte' (toiletruimte): 0 wastafel(s) zijn minder dan het aantal ingebouwde kasten met wastafel (1). Een wastafel in een Ingebouwd kastje met in- of opgebouwde wastafel moet apart worden meegegeven.

## Input

```json
{
  "ruimten": [
    {
      "id": "toiletruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
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
