# test_bouwkundig_element_zonder_detailsoort_geeft_een_waarschuwing

Een bouwkundig element zonder detailsoort is incomplete input en wordt niet gewaardeerd.

## Rapport

```text
KEUKEN
  Keuken
    - Lengte aanrecht                                              2000.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt
```

## Waarschuwingen

- UserWarning: Bouwkundig element aanrecht_2 heeft geen detailsoort en kan daardoor niet gewaardeerd worden.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht_1",
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
        },
        {
          "id": "aanrecht_2",
          "naam": "Aanrecht",
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
  "punten": 7.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__keuken",
        "naam": "Keuken"
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__keuken__lengte_aanrecht_aanrecht_1",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken"
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
