# test_sanitair_als_bouwkundig_element_telt_als_installatie

Sanitair dat als bouwkundig element is meegegeven, telt als de installatie.

Bron:
- implementatietoelichting datamodel-uitbreidingen, "Bouwkundige elementen naast installaties"

## Rapport

```text
SANITAIR
  Badkamer1
    - Wastafel                                                        1.00 st     1.00 pt
  Badkamer2
    - Staand Toilet                                                   1.00 st     2.00 pt
  Badkamer3
    - Douche                                                          1.00 st     4.00 pt
  Badkamer4
    - Bad                                                             1.00 st     6.00 pt
  Badkamer5
    - Bad en douche                                                   1.00 st     7.00 pt
  Badkamer6
    - Bad en douche                                                   2.00 st    14.00 pt
                                                                                ------
  Totaal                                                                         34.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "badkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer1",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Wastafel",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "WAS",
            "naam": "Wastafel"
          }
        }
      ]
    },
    {
      "id": "badkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer2",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Closetcombinatie",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "CLO",
            "naam": "Closetcombinatie"
          }
        }
      ]
    },
    {
      "id": "badkamer3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer3",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Douche",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        }
      ]
    },
    {
      "id": "badkamer4",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer4",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Bad",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "BAD",
            "naam": "Bad"
          }
        }
      ]
    },
    {
      "id": "badkamer5",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer5",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Bad",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "BAD",
            "naam": "Bad"
          }
        },
        {
          "id": "element_2",
          "naam": "Douche",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        }
      ]
    },
    {
      "id": "badkamer6",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer6",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Bad",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "BAD",
            "naam": "Bad"
          }
        },
        {
          "id": "element_2",
          "naam": "Bad",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "BAD",
            "naam": "Bad"
          }
        },
        {
          "id": "element_3",
          "naam": "Douche",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        },
        {
          "id": "element_4",
          "naam": "Douche",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
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
  "punten": 34.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__badkamer1",
        "naam": "Badkamer1"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer1__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer1"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "sanitair__badkamer2",
        "naam": "Badkamer2"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer2__staand_toilet",
        "naam": "Staand Toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer2"
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
        "id": "sanitair__badkamer3",
        "naam": "Badkamer3"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer3__douche",
        "naam": "Douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer3"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "sanitair__badkamer4",
        "naam": "Badkamer4"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer4__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer4"
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
        "id": "sanitair__badkamer5",
        "naam": "Badkamer5"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer5__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer5"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 7.0
    },
    {
      "criterium": {
        "id": "sanitair__badkamer6",
        "naam": "Badkamer6"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__badkamer6__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer6"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 14.0
    }
  ]
}
```
