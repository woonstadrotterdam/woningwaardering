# test_rijksbeschermd_stadsgezicht_krijgt_alleen_bij_bouwjaar_voor_1965_opslag[bouwjaar_1964]

Een woonruimte in een rijksbeschermd stadsgezicht krijgt alleen 5% opslag op de maximale huurprijs als de woning vóór 1965 is gebouwd.

Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
met 5% vermeerderd indien:", "a. die woonruimte behoort tot een
rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34, vierde
lid, van de Omgevingswet," en "b. de woonruimte behoort tot een woning die
is gebouwd voor 1965; en".

## Rapport

```text
PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Rijksbeschermd stads- of dorpsgezicht                                                         5%
                                                                                ------
  Totaal                                                                          0.00 pt       5%
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1964,
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
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten_en_nieuwbouw__rijksbeschermd_stads_of_dorpsgezicht",
        "naam": "Rijksbeschermd stads- of dorpsgezicht"
      },
      "opslagpercentage": 0.05
    }
  ],
  "opslagpercentage": 0.05
}
```
