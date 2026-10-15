# test_rijksbeschermd_dorpsgezicht_krijgt_bij_bouwjaar_voor_1965_5_procent_opslag

Een woonruimte in een rijksbeschermd dorpsgezicht die vóór 1965 is gebouwd, krijgt 5% opslag op de maximale huurprijs.

Bron: implementatietoelichting zelfstandige woonruimten, 2.13.6; wettekst,
artikel 8a, vijfde lid.

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
