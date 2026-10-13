# test_rijksbeschermd_stadsgezicht_krijgt_alleen_bij_bouwjaar_voor_1965_opslag[bouwjaar_1965]

Een woonruimte in een rijksbeschermd stadsgezicht krijgt alleen 5% opslag op de maximale huurprijs als de woning vóór 1965 is gebouwd.

Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
met 5% vermeerderd indien:", "a. die woonruimte behoort tot een
rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34, vierde
lid, van de Omgevingswet," en "b. de woonruimte behoort tot een woning die
is gebouwd voor 1965; en".

Dit geval: een woning uit 1965 is niet vóór 1965 gebouwd, dus de woonruimte krijgt geen opslag

## Rapport

Geen waarderingen voor Prijsopslag monumenten.

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
