# test_toilet_in_doucheruimte_telt_als_toilet_in_badkamer

Een toilet in een doucheruimte krijgt de punten van een toilet in een badkamer.

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1.

## Rapport

```text
SANITAIR
  Doucheruimte
    - Staand Toilet                                                   1.00 st     2.00 pt
                                                                                ------
  Totaal                                                                          2.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "doucheruimte",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "DOU",
        "naam": "Doucheruimte"
      },
      "naam": "Doucheruimte",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "STO",
          "naam": "Staand Toilet"
        }
      ]
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 2.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__doucheruimte",
        "naam": "Doucheruimte"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__doucheruimte__staand_toilet",
        "naam": "Staand Toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__doucheruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 2.0
    }
  ]
}
```
