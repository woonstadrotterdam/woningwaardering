# test_parkeerplek_krijgt_9_6_of_4_punten_naar_type_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten

Een parkeerplek krijgt 9 punten als Type I, 6 punten als Type II en 4 punten als Type III, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft en daarna door het aantal onzelfstandige woonruimten op het adres.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.10.3
- implementatietoelichting onzelfstandige woonruimten, 2.10.4
- wettekst, Bijlage I onder B, onderdeel 10

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Gedeeld met 10 adressen
      - Parkeerplek in inpandige afgesloten parkeergarage (Type I)    1.00 st     0.45 pt
      - Parkeerplek in uitpandige afgesloten parkeergarage (Type I)   1.00 st     0.45 pt
      - Parkeerplek buiten met dak behorend bij complex (Type II)     1.00 st     0.30 pt
      - Parkeerplek buiten behorend bij complex (Type III)            1.00 st     0.20 pt
  Afronding op kwartpunten                                                        0.10 pt
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
      "gedeeldMetAantalAdressen": 10,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "gedeeldMetAantalAdressen": 10,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "gedeeldMetAantalAdressen": 10,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "gedeeldMetAantalAdressen": 10,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 1.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__parkeerplek_in_inpandige_afgesloten_parkeergarage_type_i",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage (Type I)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.45
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__parkeerplek_in_uitpandige_afgesloten_parkeergarage_type_i",
        "naam": "Parkeerplek in uitpandige afgesloten parkeergarage (Type I)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.45
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__parkeerplek_buiten_met_dak_behorend_bij_complex_type_ii",
        "naam": "Parkeerplek buiten met dak behorend bij complex (Type II)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.3
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.2
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.1
    }
  ]
}
```
