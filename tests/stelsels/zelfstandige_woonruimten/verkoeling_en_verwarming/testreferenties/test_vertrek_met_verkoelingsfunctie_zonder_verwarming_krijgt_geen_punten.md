# test_vertrek_met_verkoelingsfunctie_zonder_verwarming_krijgt_geen_punten

Een vertrek met verkoelingsfunctie dat niet verwarmd is, krijgt geen punten.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Een
verkoelingsvoorziening moet tevens kunnen verwarmen."

## Rapport

Geen waarderingen voor Verkoeling en verwarming.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 10.0,
      "verwarmd": false,
      "verkoeld": true
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
