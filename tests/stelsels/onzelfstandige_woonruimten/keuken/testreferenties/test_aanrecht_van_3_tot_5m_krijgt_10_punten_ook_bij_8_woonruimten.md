# test_aanrecht_van_3_tot_5m_krijgt_10_punten_ook_bij_8_woonruimten

Een aanrecht van 3 tot 5 meter krijgt 10 punten, ook als minimaal 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot de keuken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2; wettekst,
Bijlage I onder B, onderdeel 5.1.

De punten worden gedeeld door het aantal onzelfstandige woonruimten met
toegang en gebruiksrecht.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.2; wettekst,
Bijlage I onder B, onderdeel 5.1.

## Rapport

```text
KEUKEN
  Gedeeld met 8 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            4999.00 mm     1.25 pt
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
          "lengte": 4999.0
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
      "aantal": 4999.0,
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
