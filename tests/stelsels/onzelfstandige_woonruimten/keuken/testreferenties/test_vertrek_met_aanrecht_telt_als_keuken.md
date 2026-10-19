# test_vertrek_met_aanrecht_telt_als_keuken

Een vertrek telt voor de keuken mee zodra er een aanrecht in staat.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.5.1

## Rapport

```text
KEUKEN
  Privé
    - Woonkamer/keuken
      - Lengte aanrecht                                            2000.00 mm     7.00 pt
    - Woonkamer
      - Lengte aanrecht                                            1000.00 mm     4.00 pt
    - Woon-/slaapkamer
      - Lengte aanrecht                                            2000.00 mm     7.00 pt
    - Slaapkamer1
      - Lengte aanrecht                                            1000.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                         22.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer/keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOK",
        "naam": "Woonkamer/keuken"
      },
      "naam": "Woonkamer/keuken",
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
          "lengte": 2000.0
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
      ]
    },
    {
      "id": "woon-/slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WSL",
        "naam": "Woon-/slaapkamer"
      },
      "naam": "Woon-/slaapkamer",
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
          "lengte": 2000.0
        }
      ]
    },
    {
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
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
      ]
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 10.0
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 22.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "keuken__prive__woonkamer/keuken",
        "naam": "Woonkamer/keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__prive__woonkamer/keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__woonkamer/keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 7.0
    },
    {
      "criterium": {
        "id": "keuken__prive__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__prive__woonkamer__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__woonkamer"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "keuken__prive__woon-/slaapkamer",
        "naam": "Woon-/slaapkamer",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__prive__woon-/slaapkamer__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__woon-/slaapkamer"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 7.0
    },
    {
      "criterium": {
        "id": "keuken__prive__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__prive__slaapkamer1__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__slaapkamer1"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 4.0
    }
  ]
}
```
