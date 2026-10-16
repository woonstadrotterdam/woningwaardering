# test_punten_voor_extra_voorzieningen_worden_gedeeld_door_het_aantal_woonruimten

De punten voor extra voorzieningen worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot de keuken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.3; wettekst,
Bijlage I onder B, onderdeel 5.2.

## Rapport

```text
KEUKEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            1000.00 mm     2.00 pt
      - Extra voorzieningen
        - Inbouw koelkast                                             2.00 st     1.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt
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
          "lengte": 1000.0
        }
      ],
      "installaties": [
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken"
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
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    }
  ]
}
```
