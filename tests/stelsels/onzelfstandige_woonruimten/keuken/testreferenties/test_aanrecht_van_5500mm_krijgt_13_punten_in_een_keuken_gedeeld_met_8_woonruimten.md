# test_aanrecht_van_5500mm_krijgt_13_punten_in_een_keuken_gedeeld_met_8_woonruimten

Een aanrecht van 5,5 meter krijgt 13 punten als de keuken met 8 onzelfstandige woonruimten wordt gedeeld.

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "5 m en meer (indien er
minimaal 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot
deze keuken) 13 punten" en "De hieronder weergegeven punten dienen te
worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en
gebruiksrecht heeft".

## Rapport

```text
KEUKEN
  Gedeeld met 8 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            5500.00 mm     1.63 pt
  Afronding op kwartpunten                                                        0.12 pt
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
          "lengte": 5500.0
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
  "punten": 1.75,
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
      "aantal": 5500.0,
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
      "punten": 1.63
    },
    {
      "criterium": {
        "id": "keuken__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
