# test_meerdere_korte_aanrechten_tellen_ook_in_een_gemeenschappelijke_keuken_als_een_wastafel

Meerdere aanrechten korter dan 1 meter tellen ook in een gemeenschappelijke keuken samen als één wastafel.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.6.1

De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door
het aantal onzelfstandige woonruimten.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.6
- wettekst, Bijlage I onder B, onderdeel 6.1

## Rapport

```text
SANITAIR
  Gedeeld met 4 onzelfstandige woonruimten
    - Keuken
      - Wastafel (spoelbak in aanrecht < 1m)                          1.00 st     0.25 pt
                                                                                ------
  Totaal                                                                          0.25 pt
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
          "id": "aanrecht1",
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
          "id": "aanrecht2",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 900.0
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 0.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_4_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_4_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_4_onzelfstandige_woonruimten__keuken__spoelbak_in_aanrecht",
        "naam": "Wastafel (spoelbak in aanrecht < 1m)",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_4_onzelfstandige_woonruimten__keuken"
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
