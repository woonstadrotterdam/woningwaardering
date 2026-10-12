# test_meerdere_kastruimtes_tellen_samen_als_een

Meerdere kastruimtes in een badkamer krijgen samen 0,75 punt.

Bron: wettekst, Bijlage I onder A, onderdeel 6.2: "Kastruimte (minimale
breedte van 40 cm, en minimale hoogte van 40 cm) 0,75 punt (tot een maximum
van 0,75)".

## Rapport

```text
SANITAIR
  Badkamer
    - Wastafel                                                        1.00 st     1.00 pt
    - Bad                                                             1.00 st     6.00 pt
    - Extra voorzieningen
      - Kastruimte                                                    2.00 st     1.50 pt
      - Max 0.75 punten voor Kastruimte                                          -0.75 pt
                                                                                ------
  Totaal                                                                          7.75 pt
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 7.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__badkamer",
        "naam": "Badkamer"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
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
        "id": "sanitair__badkamer__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 6.0
    },
    {
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen__kastruimte",
        "naam": "Kastruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
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
        "id": "sanitair__badkamer__extra_voorzieningen__max_punten_kastruimte",
        "naam": "Max 0.75 punten voor Kastruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
        }
      },
      "punten": -0.75
    }
  ]
}
```
