# test_wastafels_buiten_de_badkamer_krijgen_een_maximum_per_ruimte

Buiten de badkamer krijgen wastafels per ruimte hooguit de punten van één wastafel.

Het maximum geldt apart voor wastafels (1 punt) en voor
meerpersoonswastafels (1,5 punt).

Bron: wettekst, Bijlage I onder A, onderdeel 6.1: "Wastafel 1 punt (tot een
maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer)" en
"Meerpersoonswastafel (minimale breedte van 70cm en met twee kranen) 1,5
punten (tot een maximum van 1,5 punt per vertrek of overige ruimte m.u.v. de
badkamer)".

## Rapport

```text
SANITAIR
  Toiletruimte
    - Wastafel                                                        2.00 st     2.00 pt
    - Max 1.0 punt voor Wastafel                                                 -1.00 pt
    - Meerpersoonswastafel                                            2.00 st     3.00 pt
    - Max 1.5 punt voor Meerpersoonswastafel                                     -1.50 pt
  Woonkamer
    - Wastafel                                                        2.00 st     2.00 pt
    - Max 1.0 punt voor Wastafel                                                 -1.00 pt
    - Meerpersoonswastafel                                            2.00 st     3.00 pt
    - Max 1.5 punt voor Meerpersoonswastafel                                     -1.50 pt
                                                                                ------
  Totaal                                                                          5.00 pt
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
    },
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
          "lengte": 1000.0
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 5.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__toiletruimte",
        "naam": "Toiletruimte"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__toiletruimte__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__toiletruimte"
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
        "id": "sanitair__toiletruimte__max_punten_wastafel",
        "naam": "Max 1.0 punt voor Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__toiletruimte"
        }
      },
      "punten": -1.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__toiletruimte__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__toiletruimte"
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
        "id": "sanitair__toiletruimte__max_punten_meerpersoonswastafel",
        "naam": "Max 1.5 punt voor Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__toiletruimte"
        }
      },
      "punten": -1.5
    },
    {
      "criterium": {
        "id": "sanitair__woonkamer",
        "naam": "Woonkamer"
      }
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
      "punten": -1.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__woonkamer__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__woonkamer"
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
        "id": "sanitair__woonkamer__max_punten_meerpersoonswastafel",
        "naam": "Max 1.5 punt voor Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__woonkamer"
        }
      },
      "punten": -1.5
    }
  ]
}
```
