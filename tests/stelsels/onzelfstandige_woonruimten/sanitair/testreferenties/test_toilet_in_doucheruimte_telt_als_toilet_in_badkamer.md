# test_toilet_in_doucheruimte_telt_als_toilet_in_badkamer

Een toilet in een doucheruimte krijgt de punten van een toilet in een badkamer.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1.

## Rapport

```text
SANITAIR
  Privé
    - Doucheruimte
      - Staand Toilet                                                 1.00 st     2.00 pt
      - Wastafel                                                      1.00 st     1.00 pt
      - Douche                                                        1.00 st     3.00 pt
                                                                                ------
  Totaal                                                                          6.00 pt
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
        },
        {
          "code": "DOU",
          "naam": "Douche"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 6.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__doucheruimte",
        "naam": "Doucheruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__doucheruimte__staand_toilet",
        "naam": "Staand Toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__doucheruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 2.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__doucheruimte__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__doucheruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__doucheruimte__douche",
        "naam": "Douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__doucheruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    }
  ]
}
```
