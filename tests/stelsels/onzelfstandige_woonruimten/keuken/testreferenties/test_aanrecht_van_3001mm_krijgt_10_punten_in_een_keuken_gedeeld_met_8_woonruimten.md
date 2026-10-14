# test_aanrecht_van_3001mm_krijgt_10_punten_in_een_keuken_gedeeld_met_8_woonruimten

Een aanrecht van net iets meer dan 3 meter krijgt 10 punten, ook in een keuken die met 8 onzelfstandige woonruimten wordt gedeeld.

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten",
"5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
gebruiksrecht hebben tot deze keuken) 13 punten" en "De hieronder
weergegeven punten dienen te worden gedeeld door het aantal onzelfstandige
woonruimten dat toegang en gebruiksrecht heeft".

## Rapport

```text
KEUKEN
  Gedeeld met 8 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            3001.00 mm     1.25 pt
                                                                                ------
  Totaal                                                                          1.25 pt
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
  "punten": 1.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 8 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3001.0,
      "criterium": {
        "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_8_onzelfstandige_woonruimten__keuken"
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
