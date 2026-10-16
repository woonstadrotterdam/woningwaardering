# test_gemeentelijk_beschermd_stads_of_dorpsgezicht_krijgt_geen_opslag

Een woonruimte in een gemeentelijk beschermd stads- of dorpsgezicht krijgt geen opslag.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6; wettekst,
artikel 8a, vijfde lid.

## Rapport

Geen waarderingen voor Prijsopslag monumenten.

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
