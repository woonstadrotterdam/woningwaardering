# test_kort_aanrechtdeel_telt_mee_naast_een_aanrecht_vanaf_1m

Een aanrechtdeel korter dan 1 meter telt mee in de aanrechtlengte naast een aanrecht vanaf 1 meter.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2.

## Rapport

```text
KEUKEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Keuken
      - Totale aanrechtlengte                                      2000.00 mm     1.75 pt
        - Lengte aanrecht                                           800.00 mm
        - Lengte aanrecht                                          1200.00 mm
                                                                                ------
  Totaal                                                                          1.75 pt
```

## Waarschuwingen

Geen.

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
          "id": "kort_aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 800.0
        },
        {
          "id": "lang_aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1200.0
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
  "punten": 1.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__subtotaal",
        "naam": "Totale aanrechtlengte",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 1.75
    },
    {
      "aantal": 800.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__subtotaal__lengte_aanrecht_kort_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__subtotaal"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      }
    },
    {
      "aantal": 1200.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__subtotaal__lengte_aanrecht_lang_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__subtotaal"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      }
    }
  ]
}
```
