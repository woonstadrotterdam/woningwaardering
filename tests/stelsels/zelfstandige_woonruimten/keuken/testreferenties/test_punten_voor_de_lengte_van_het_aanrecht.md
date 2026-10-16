# test_punten_voor_de_lengte_van_het_aanrecht

De punten voor een aanrecht hangen af van zijn lengte.

Bron: implementatietoelichting zelfstandige woonruimten, 2.5.2; wettekst,
Bijlage I onder A, onderdeel 5.1.

## Rapport

```text
KEUKEN
  Keuken1
    - Lengte aanrecht                                              1000.00 mm     4.00 pt
  Keuken2
    - Lengte aanrecht                                              1999.00 mm     4.00 pt
  Keuken3
    - Lengte aanrecht                                              2000.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                         15.00 pt
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 15.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__keuken1",
        "naam": "Keuken1"
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__keuken1__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken1"
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
        "id": "keuken__keuken2",
        "naam": "Keuken2"
      }
    },
    {
      "aantal": 1999.0,
      "criterium": {
        "id": "keuken__keuken2__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken2"
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
        "id": "keuken__keuken3",
        "naam": "Keuken3"
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__keuken3__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken3"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 7.0
    }
  ]
}
```
