# test_aanrecht_van_5m_of_meer_krijgt_10_punten_bij_minder_dan_8_woonruimten

Een aanrecht van 5 meter of meer krijgt 10 punten als minder dan 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot de keuken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2; wettekst,
Bijlage I onder B, onderdeel 5.1.

De punten worden gedeeld door het aantal onzelfstandige woonruimten met
toegang en gebruiksrecht.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2; wettekst,
Bijlage I onder B, onderdeel 5.1.

## Rapport

```text
KEUKEN
  Gedeeld met 7 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            5500.00 mm     1.43 pt
  Afronding op kwartpunten                                                        0.07 pt
                                                                                ------
  Totaal                                                                          1.50 pt
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 7
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
  "punten": 1.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__gedeeld_met_7_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 7 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "keuken__gedeeld_met_7_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_7_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 5500.0,
      "criterium": {
        "id": "keuken__gedeeld_met_7_onzelfstandige_woonruimten__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__gedeeld_met_7_onzelfstandige_woonruimten__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 1.43
    },
    {
      "criterium": {
        "id": "keuken__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.07
    }
  ]
}
```
