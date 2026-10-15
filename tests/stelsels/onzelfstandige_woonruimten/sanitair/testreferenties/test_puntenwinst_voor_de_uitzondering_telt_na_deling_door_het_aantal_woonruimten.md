# test_puntenwinst_voor_de_uitzondering_telt_na_deling_door_het_aantal_woonruimten

De puntenwinst die de uitzonderingsruimte bepaalt, telt na deling door het aantal onzelfstandige woonruimten waarmee de ruimte wordt gedeeld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1.

## Rapport

```text
SANITAIR
  Gedeeld met 20 onzelfstandige woonruimten
    - Slaapkamer
      - Wastafel                                                      3.00 st     0.15 pt
      - Maximering voor Wastafel                                                 -0.10 pt
  Gedeeld met 8 onzelfstandige woonruimten
    - Berging
      - Meerpersoonswastafel                                          2.00 st     0.38 pt
  Afronding op kwartpunten                                                        0.07 pt
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
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 20
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
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
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
        "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 20 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten__slaapkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten__slaapkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.15
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten__slaapkamer__max_punten_wastafel",
        "naam": "Maximering voor Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_20_onzelfstandige_woonruimten__slaapkamer"
        }
      },
      "punten": -0.1
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 8 onzelfstandige woonruimten"
      }
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
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__berging__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
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
      "punten": 0.07
    }
  ]
}
```
