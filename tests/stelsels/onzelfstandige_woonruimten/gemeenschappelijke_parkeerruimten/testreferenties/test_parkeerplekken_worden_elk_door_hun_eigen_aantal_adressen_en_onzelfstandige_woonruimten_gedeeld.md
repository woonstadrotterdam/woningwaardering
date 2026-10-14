# test_parkeerplekken_worden_elk_door_hun_eigen_aantal_adressen_en_onzelfstandige_woonruimten_gedeeld

Parkeerplekken met een verschillend aantal adressen en onzelfstandige woonruimten worden elk door hun eigen aantallen gedeeld.

De parkeerplek in de parkeergarage wordt met 3 adressen en 2 onzelfstandige
woonruimten gedeeld, de carport met 4 adressen en 3 onzelfstandige
woonruimten en de parkeerplek buiten met 5 adressen en 3 onzelfstandige
woonruimten.

Bron: beleidsboek onzelfstandige woonruimten, 2.10.4: "Het puntenaantal moet
worden berekend door het puntenaantal per gemeenschappelijke parkeerplek te
delen door aantal adressen dat toegang heeft tot de parkeerplek. Dit getal
moet daarna worden gedeeld door het aantal onzelfstandige woonruimten op het
eigen woonadres, om tot het puntenaantal voor de onzelfstandige woonruimte
te komen."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Wanneer op een
adres slechts een aantal onzelfstandige woonruimten gebruik mogen maken van
een gemeenschappelijk vertrek, ruimte of voorziening, en dus niet alle
aanwezige onzelfstandige woonruimten, worden de punten enkel gedeeld door
het aantal onzelfstandige woonruimten dat krachtens de huurovereenkomst
toegang en gebruiksrecht heeft tot dat vertrek, die ruimte of die
voorziening(en)."

Bron: wettekst, Bijlage I onder B, rubriek 10: "Type I Parkeerplek in
afgesloten parkeergarage behorende tot het complex 9 punten", "Type II
Parkeerplek buiten behorende tot het complex met dak 6 punten" en "Type III
Parkeerplek buiten behorende tot het complex zonder dak 4 punten".

De gemeenschappelijke carport is een parkeerplek van Type II.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.3: "Type II:
`Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex` (`PBD`)
en, wanneer die gemeenschappelijk is, `Ruimtedetailsoort.carport` (`CAR`)."

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
