# test_toilet_krijgt_in_toiletruimte_een_punt_meer_dan_in_badkamer

Een toilet krijgt in een toiletruimte een punt meer dan in een badkamer.

De wettekst noemt het hangend toilet in deze tabel een zwevend toilet.

Bron: wettekst, Bijlage I onder B, onderdeel 6.1: een toilet krijgt in een
"Aparte toiletruimte" "3 punten" en "In badkamer" "2 punten"; een "Zwevend
toilet" "3,75 punten" en "2,75 punten".

## Rapport

```text
SANITAIR
  Privé
    - Badkamer
      - Hangend toilet                                                1.00 st     2.75 pt
      - Staand Toilet                                                 1.00 st     2.00 pt
    - Toiletruimte
      - Hangend toilet                                                1.00 st     3.75 pt
      - Staand Toilet                                                 1.00 st     3.00 pt
                                                                                ------
  Totaal                                                                         11.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "STO",
          "naam": "Staand Toilet"
        },
        {
          "code": "HTO",
          "naam": "Hangend toilet"
        }
      ]
    },
    {
      "id": "toiletruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "STO",
          "naam": "Staand Toilet"
        },
        {
          "code": "HTO",
          "naam": "Hangend toilet"
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
  "punten": 11.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer",
        "naam": "Badkamer",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__hangend_toilet",
        "naam": "Hangend toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 2.75
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__staand_toilet",
        "naam": "Staand Toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "sanitair__prive__toiletruimte",
        "naam": "Toiletruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__toiletruimte__hangend_toilet",
        "naam": "Hangend toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.75
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__toiletruimte__staand_toilet",
        "naam": "Staand Toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
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
