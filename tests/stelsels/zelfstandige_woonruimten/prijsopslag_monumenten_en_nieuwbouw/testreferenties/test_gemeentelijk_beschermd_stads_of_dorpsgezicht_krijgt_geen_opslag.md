# test_gemeentelijk_beschermd_stads_of_dorpsgezicht_krijgt_geen_opslag

Een woonruimte in een gemeentelijk beschermd stads- of dorpsgezicht krijgt geen opslag.

De opslag geldt alleen voor een rijksbeschermd stads- of dorpsgezicht.

Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
met 5% vermeerderd indien:", "a. die woonruimte behoort tot een
rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34, vierde
lid, van de Omgevingswet," en "b. de woonruimte behoort tot een woning die
is gebouwd voor 1965; en".

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
