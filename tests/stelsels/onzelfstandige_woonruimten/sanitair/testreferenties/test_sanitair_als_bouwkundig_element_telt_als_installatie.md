# test_sanitair_als_bouwkundig_element_telt_als_installatie

Sanitair dat als bouwkundig element is meegegeven, telt als de installatie.

Bron:
- implementatietoelichting datamodel-uitbreidingen, "Bouwkundige elementen naast installaties"

## Rapport

```text
SANITAIR
  Privé
    - Badkamer1
      - Wastafel                                                      1.00 st     1.00 pt
    - Toiletruimte
      - Staand Toilet                                                 1.00 st     3.00 pt
    - Doucheruimte
      - Douche                                                        1.00 st     3.00 pt
    - Badkamer2
      - Bad                                                           1.00 st     5.00 pt
    - Badkamer3
      - Bad en douche                                                 1.00 st     6.00 pt
    - Badkamer4
      - Bad en douche                                                 2.00 st    12.00 pt
                                                                                ------
  Totaal                                                                         30.00 pt
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 30.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer1",
        "naam": "Badkamer1",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer1__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer1"
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
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer2",
        "naam": "Badkamer2",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer2__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer2"
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
        "id": "sanitair__prive__badkamer3",
        "naam": "Badkamer3",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer3__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer3"
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
        "id": "sanitair__prive__badkamer4",
        "naam": "Badkamer4",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__prive__badkamer4__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer4"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 12.0
    }
  ]
}
```
