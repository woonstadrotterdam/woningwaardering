# test_punten_van_meerdere_parkeerplekken_worden_opgeteld_en_gedeeld_door_de_adressen_en_de_onzelfstandige_woonruimten

De punten van meerdere parkeerplekken worden opgeteld, gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.4; wettekst,
Bijlage I onder B, toelichting rubriek 10.

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Gedeeld met 10 adressen
      - Parkeerplek buiten behorend bij complex (Type III)            5.00 st     0.50 pt
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
      "aantal": 5,
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 5.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    }
  ]
}
```
