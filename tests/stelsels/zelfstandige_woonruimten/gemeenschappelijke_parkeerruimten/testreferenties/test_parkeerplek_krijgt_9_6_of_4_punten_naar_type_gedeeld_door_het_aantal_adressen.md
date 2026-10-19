# test_parkeerplek_krijgt_9_6_of_4_punten_naar_type_gedeeld_door_het_aantal_adressen

Een parkeerplek krijgt 9 punten als Type I, 6 punten als Type II en 4 punten als Type III, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.10.3
- wettekst, Bijlage I onder A, onderdeel 10

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 10 adressen
    - Parkeerplek in inpandige afgesloten parkeergarage (Type I)      1.00 st     0.90 pt
    - Parkeerplek in uitpandige afgesloten parkeergarage (Type I)     1.00 st     0.90 pt
    - Parkeerplek buiten met dak behorend bij complex (Type II)       1.00 st     0.60 pt
    - Parkeerplek buiten behorend bij complex (Type III)              1.00 st     0.40 pt
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                          2.75 pt
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
      "gedeeldMetAantalAdressen": 10
    },
    {
      "id": "parkeerplek_in_uitpandige_afgesloten_parkeergarage",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PUP",
        "naam": "Parkeerplek in uitpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in uitpandige afgesloten parkeergarage",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 10
    },
    {
      "id": "parkeerplek_buiten_met_dak_behorend_bij_complex",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBD",
        "naam": "Parkeerplek buiten met dak behorend bij complex"
      },
      "naam": "Parkeerplek buiten met dak behorend bij complex",
      "oppervlakte": 12.0,
      "gedeeldMetAantalAdressen": 10
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
      "gedeeldMetAantalAdressen": 10
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 2.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__parkeerplek_in_inpandige_afgesloten_parkeergarage_type_i",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage (Type I)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.9
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__parkeerplek_in_uitpandige_afgesloten_parkeergarage_type_i",
        "naam": "Parkeerplek in uitpandige afgesloten parkeergarage (Type I)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.9
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__parkeerplek_buiten_met_dak_behorend_bij_complex_type_ii",
        "naam": "Parkeerplek buiten met dak behorend bij complex (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.6
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.4
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.05
    }
  ]
}
```
