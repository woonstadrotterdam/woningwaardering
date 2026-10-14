# test_rijksbeschermd_dorpsgezicht_krijgt_bij_bouwjaar_voor_1965_5_procent_opslag

Een woonruimte in een rijksbeschermd dorpsgezicht die vóór 1965 is gebouwd, krijgt 5% opslag op de maximale huurprijs.

Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
met 5% vermeerderd indien:", "a. die woonruimte behoort tot een
rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34, vierde
lid, van de Omgevingswet," en "b. de woonruimte behoort tot een woning die
is gebouwd voor 1965; en".

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
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
      "code": "DGR",
      "naam": "Rijksbeschermd dorpsgezicht"
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
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten__rijksbeschermd_stads_of_dorpsgezicht",
        "naam": "Rijksbeschermd stads- of dorpsgezicht"
      },
      "opslagpercentage": 0.05
    }
  ],
  "opslagpercentage": 0.05
}
```
