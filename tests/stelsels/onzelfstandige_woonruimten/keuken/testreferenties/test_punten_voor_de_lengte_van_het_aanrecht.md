# test_punten_voor_de_lengte_van_het_aanrecht

De punten voor een aanrecht hangen af van zijn lengte.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.5.2
- wettekst, Bijlage I onder B, onderdeel 5.1

## Rapport

```text
KEUKEN
  Privé
    - Keuken1
      - Lengte aanrecht                                            1000.00 mm     4.00 pt
    - Keuken2
      - Lengte aanrecht                                            1999.00 mm     4.00 pt
    - Keuken3
      - Lengte aanrecht                                            2000.00 mm     7.00 pt
    - Keuken4
      - Lengte aanrecht                                            2999.00 mm     7.00 pt
    - Keuken5
      - Lengte aanrecht                                            3500.00 mm    10.00 pt
                                                                                ------
  Totaal                                                                         32.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken1",
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
      "id": "keuken2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken2",
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
          "lengte": 1999.0
        }
      ]
    },
    {
      "id": "keuken3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken3",
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
      "id": "keuken4",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken4",
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
          "lengte": 2999.0
        }
      ]
    },
    {
      "id": "keuken5",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken5",
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
          "lengte": 3500.0
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 32.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "keuken__prive__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__prive__keuken1__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken1"
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
        "id": "keuken__prive__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 1999.0,
      "criterium": {
        "id": "keuken__prive__keuken2__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken2"
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
        "id": "keuken__prive__keuken3",
        "naam": "Keuken3",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__prive__keuken3__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken3"
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
        "id": "keuken__prive__keuken4",
        "naam": "Keuken4",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 2999.0,
      "criterium": {
        "id": "keuken__prive__keuken4__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken4"
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
        "id": "keuken__prive__keuken5",
        "naam": "Keuken5",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 3500.0,
      "criterium": {
        "id": "keuken__prive__keuken5__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken5"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 10.0
    }
  ]
}
```
