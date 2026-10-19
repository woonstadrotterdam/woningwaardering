# test_gemeentelijk_beschermd_stads_of_dorpsgezicht_krijgt_geen_opslag

Een woonruimte in een gemeentelijk beschermd stads- of dorpsgezicht krijgt geen opslag.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.13.6
- wettekst, artikel 8a, vijfde lid

## Rapport

Geen waarderingen voor Prijsopslag monumenten en nieuwbouw.

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1964,
  "monumenten": [
    {
      "code": "SGG",
      "naam": "Gemeentelijk beschermd stadsgezicht"
    },
    {
      "code": "DGG",
      "naam": "Gemeentelijk beschermd dorpsgezicht"
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
