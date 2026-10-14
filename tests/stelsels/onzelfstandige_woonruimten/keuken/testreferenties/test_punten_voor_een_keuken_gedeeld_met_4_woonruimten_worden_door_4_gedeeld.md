# test_punten_voor_een_keuken_gedeeld_met_4_woonruimten_worden_door_4_gedeeld

De punten voor een keuken die 4 onzelfstandige woonruimten delen, worden door 4 gedeeld.

Het scenario is het rekenvoorbeeld uit de toelichting bij de wettekst: 7
punten voor het aanrecht en 3 voor de voorzieningen.

Bron: wettekst, Bijlage I onder B, toelichting rubriek 5: "Er is één
keuken, waarvoor 10 punten worden toegekend (7 voor het aanrecht, en 3 voor
de voorzieningen). Omdat de keuken wordt gedeeld door vier onzelfstandige
woonruimten, geldt 10/4 = 2,5 punt per onzelfstandige woonruimte."

## Rapport

```text
KEUKEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            2500.00 mm     1.75 pt
      - Extra voorzieningen
        - Inbouw kookplaat keramisch                                  1.00 st     0.25 pt
        - Inbouw koelkast                                             1.00 st     0.25 pt
        - Inbouw oven elektrisch                                      1.00 st     0.25 pt
                                                                                ------
  Totaal                                                                          2.50 pt
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
          "lengte": 2500.0
        }
      ],
      "installaties": [
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKK",
          "naam": "Inbouw kookplaat keramisch"
        },
        {
          "code": "IOE",
          "naam": "Inbouw oven elektrisch"
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
  "punten": 2.5,
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
      "aantal": 2500.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
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
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_kookplaat_keramisch",
        "naam": "Inbouw kookplaat keramisch",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.25
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.25
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_oven_elektrisch",
        "naam": "Inbouw oven elektrisch",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_4_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.25
    }
  ]
}
```
