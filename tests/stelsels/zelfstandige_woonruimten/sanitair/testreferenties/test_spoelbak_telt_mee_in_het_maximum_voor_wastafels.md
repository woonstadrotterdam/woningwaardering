# test_spoelbak_telt_mee_in_het_maximum_voor_wastafels

Een spoelbak in een kort aanrecht valt onder het maximum van 1 punt voor wastafels.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.6.1
- wettekst, Bijlage I onder A, onderdeel 6.1

## Rapport

```text
SANITAIR
  Woonkamer
    - Wastafel (spoelbak in aanrecht < 1m)                            1.00 st     1.00 pt
    - Wastafel                                                        2.00 st     2.00 pt
    - Max 1.0 punt voor Wastafel                                                 -2.00 pt
                                                                                ------
  Totaal                                                                          1.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 900.0
        }
      ],
      "installaties": [
        {
          "code": "WAS",
          "naam": "Wastafel"
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 1.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__woonkamer",
        "naam": "Woonkamer"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__woonkamer__spoelbak_in_aanrecht",
        "naam": "Wastafel (spoelbak in aanrecht < 1m)",
        "bovenliggendeCriterium": {
          "id": "sanitair__woonkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__woonkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__woonkamer"
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
        "id": "sanitair__woonkamer__max_punten_wastafel",
        "naam": "Max 1.0 punt voor Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__woonkamer"
        }
      },
      "punten": -2.0
    }
  ]
}
```
