# test_rijksbeschermd_stads_of_dorpsgezicht_krijgt_alleen_bij_bouwjaar_voor_1965_opslag[stadsgezicht_bouwjaar_1965]

Een woonruimte in een rijksbeschermd stads- of dorpsgezicht krijgt alleen 5% opslag op de maximale huurprijs als de woning vóór 1965 is gebouwd.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.13.6
- wettekst, artikel 8a, vijfde lid

Dit geval: een woning uit 1965 is niet vóór 1965 gebouwd, dus de woonruimte krijgt geen opslag

## Rapport

Geen waarderingen voor Prijsopslag monumenten en nieuwbouw.

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1965,
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "PMN",
      "naam": "Prijsopslag monumenten en nieuwbouw"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [],
  "opslagpercentage": 0.0
}
```
