# test_parkeerplekken_worden_elk_door_hun_eigen_aantal_adressen_en_onzelfstandige_woonruimten_gedeeld

Parkeerplekken met een verschillend aantal adressen en onzelfstandige woonruimten worden elk door hun eigen aantallen gedeeld.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.10.4
- wettekst, Bijlage I onder B, toelichting, inleiding

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Gedeeld met 3 adressen
      - Parkeerplek in inpandige afgesloten parkeergarage (Type I)    1.00 st     1.50 pt
  Gedeeld met 3 onzelfstandige woonruimten
    - Gedeeld met 4 adressen
      - Carport (Type II)                                             1.00 st     0.50 pt
    - Gedeeld met 5 adressen
      - Parkeerplek buiten behorend bij complex (Type III)            1.00 st     0.27 pt
  Afronding op kwartpunten                                                       -0.02 pt
                                                                                ------
  Totaal                                                                          2.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplek_in_inpandige_afgesloten_parkeergarage",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PIP",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in inpandige afgesloten parkeergarage",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 3,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 4,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
    },
    {
      "id": "parkeerplek_buiten_behorend_bij_complex",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek buiten behorend bij complex",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 5,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_3_adressen",
        "naam": "Gedeeld met 3 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_3_adressen__parkeerplek_in_inpandige_afgesloten_parkeergarage_type_i",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage (Type I)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 3 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_4_adressen",
        "naam": "Gedeeld met 4 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_4_adressen__carport_type_ii",
        "naam": "Carport (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_4_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_5_adressen",
        "naam": "Gedeeld met 5 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_5_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_5_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.27
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.02
    }
  ]
}
```
