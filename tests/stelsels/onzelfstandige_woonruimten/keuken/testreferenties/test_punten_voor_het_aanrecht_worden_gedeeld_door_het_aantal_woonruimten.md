# test_punten_voor_het_aanrecht_worden_gedeeld_door_het_aantal_woonruimten

De punten voor het aanrecht worden gedeeld door het aantal onzelfstandige woonruimten waarmee de keuken wordt gedeeld.

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "De hieronder weergegeven
punten dienen te worden gedeeld door het aantal onzelfstandige woonruimten
dat toegang en gebruiksrecht heeft".

## Rapport

```text
KEUKEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken1
      - Lengte aanrecht                                            1000.00 mm     2.00 pt
    - Keuken2
      - Lengte aanrecht                                            2000.00 mm     3.50 pt
    - Keuken3
      - Lengte aanrecht                                            3001.00 mm     5.00 pt
  Gedeeld met 8 onzelfstandige woonruimten
    - Keuken4
      - Lengte aanrecht                                            3001.00 mm     1.25 pt
                                                                                ------
  Totaal                                                                         11.75 pt
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
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
          "lengte": 2000.0
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
          "lengte": 3001.0
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
          "lengte": 3001.0
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 8
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
  "punten": 11.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken1__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken1"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken2__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken2"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 3.5
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken3",
        "naam": "Keuken3",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3001.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken3__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken3"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 5.0
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 8 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken4",
        "naam": "Keuken4",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3001.0,
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken4__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken4"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 1.25
    }
  ]
}
```
