# test_punten_voor_gemeenschappelijk_sanitair_worden_gedeeld_door_het_aantal_woonruimten

De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door het aantal onzelfstandige woonruimten waarmee de ruimte wordt gedeeld.

Het adres heeft 8 onzelfstandige woonruimten. Daardoor geldt het maximum
voor wastafels niet in de slaapkamer, naast de badkamer waar het nooit
geldt.

Bron: wettekst, Bijlage I onder B, onderdeel 6.1: "De hieronder weergegeven
punten dienen te worden gedeeld door het aantal onzelfstandige woonruimten
dat toegang en gebruiksrecht heeft".

Bron: wettekst, Bijlage I onder B, toelichting rubriek 6: "Daarnaast geldt
er voor adressen met 8 of meer onzelfstandige woonruimten dat er voor
maximaal één ruimte, naast de badkamer, een ruimte mag zijn met meer dan
één wastafel die voor waardering in aanmerking komt."

## Rapport

```text
SANITAIR
  Gedeeld met 8 onzelfstandige woonruimten
    - Badkamer
      - Wastafel                                                      2.00 st     0.25 pt
      - Douche                                                        1.00 st     0.38 pt
    - Slaapkamer
      - Wastafel                                                      3.00 st     0.38 pt
  Afronding op kwartpunten                                                       -0.01 pt
                                                                                ------
  Totaal                                                                          1.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
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
          "code": "DOU",
          "naam": "Douche"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 8
    },
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
  "punten": 1.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 8 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__badkamer",
        "naam": "Badkamer",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__badkamer"
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
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__badkamer__douche",
        "naam": "Douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__badkamer"
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
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__slaapkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_8_onzelfstandige_woonruimten__slaapkamer"
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
