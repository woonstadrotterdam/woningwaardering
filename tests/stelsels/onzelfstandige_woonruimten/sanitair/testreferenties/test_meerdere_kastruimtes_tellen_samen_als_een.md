# test_meerdere_kastruimtes_tellen_samen_als_een

Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.2; wettekst,
Bijlage I onder B, onderdeel 6.2.

## Rapport

```text
SANITAIR
  Privé
    - Badkamer
      - Wastafel                                                      1.00 st     1.00 pt
      - Bad                                                           1.00 st     5.00 pt
      - Extra voorzieningen
        - Kastruimte                                                  2.00 st     1.50 pt
        - Max 0.75 punten voor Kastruimte                                        -0.75 pt
                                                                                ------
  Totaal                                                                          6.75 pt
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
          "code": "BAD",
          "naam": "Bad"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "KAS",
          "naam": "Kastruimte"
        },
        {
          "code": "KAS",
          "naam": "Kastruimte"
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
  "punten": 6.75,
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
        "id": "sanitair__prive__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
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
        "id": "sanitair__prive__badkamer__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 5.0
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen__kastruimte",
        "naam": "Kastruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.5
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen__max_punten_kastruimte",
        "naam": "Max 0.75 punten voor Kastruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
        }
      },
      "punten": -0.75
    }
  ]
}
```
