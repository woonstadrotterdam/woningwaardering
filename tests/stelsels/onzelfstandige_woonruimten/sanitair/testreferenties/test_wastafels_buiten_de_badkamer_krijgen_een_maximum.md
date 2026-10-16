# test_wastafels_buiten_de_badkamer_krijgen_een_maximum

Buiten de badkamer geldt per ruimte een maximum van 1 punt voor wastafels en 1,5 punt voor meerpersoonswastafels.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1; wettekst,
Bijlage I onder B, onderdeel 6.1.

## Rapport

```text
SANITAIR
  Privé
    - Toiletruimte
      - Wastafel                                                      2.00 st     2.00 pt
      - Max 1.0 punt voor Wastafel                                               -1.00 pt
      - Meerpersoonswastafel                                          2.00 st     3.00 pt
      - Max 1.5 punt voor Meerpersoonswastafel                                   -1.50 pt
                                                                                ------
  Totaal                                                                          2.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
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
  "punten": 2.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
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
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__prive__toiletruimte__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
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
        "id": "sanitair__prive__toiletruimte__max_punten_wastafel",
        "naam": "Max 1.0 punt voor Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
        }
      },
      "punten": -1.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__prive__toiletruimte__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    },
    {
      "criterium": {
        "id": "sanitair__prive__toiletruimte__max_punten_meerpersoonswastafel",
        "naam": "Max 1.5 punt voor Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
        }
      },
      "punten": -1.5
    }
  ]
}
```
