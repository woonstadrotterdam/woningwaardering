# test_meerdere_korte_aanrechten_tellen_ook_in_een_gemeenschappelijke_keuken_als_een_wastafel

Meerdere aanrechten korter dan 1 meter tellen ook in een gemeenschappelijke keuken samen als één wastafel.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1.

De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door
het aantal onzelfstandige woonruimten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6; wettekst,
Bijlage I onder B, onderdeel 6.1.

## Rapport

```text
SANITAIR
  Gedeeld met 8 onzelfstandige woonruimten
    - Keuken
      - Wastafel (spoelbak in aanrecht < 1m)                          1.00 st     0.13 pt
    - Berging
      - Wastafel                                                      3.00 st     0.38 pt
  Afronding op kwartpunten                                                       -0.01 pt
                                                                                ------
  Totaal                                                                          0.50 pt
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 8
    },
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 0.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 8 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__keuken__spoelbak_in_aanrecht",
        "naam": "Wastafel (spoelbak in aanrecht < 1m)",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__keuken"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.13
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__berging__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__berging"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.38
    },
    {
      "criterium": {
        "id": "sanitair__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.01
    }
  ]
}
```
