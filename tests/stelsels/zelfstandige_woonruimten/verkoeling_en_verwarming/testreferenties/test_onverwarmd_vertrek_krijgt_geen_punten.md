# test_onverwarmd_vertrek_krijgt_geen_punten

Een vertrek zonder verwarming krijgt geen punten.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmd
vertrek wordt, ongeacht de verwarmingswijze, een waardering van twee punten
toegepast, voor zover de verwarming tot de onroerende zaak en zijn
onroerende aanhorigheden behoort."

## Rapport

Geen waarderingen voor Verkoeling en verwarming.

## Waarschuwingen

Geen.

## Input

```json
{
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
      "oppervlakte": 10.0,
      "verwarmd": false
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
