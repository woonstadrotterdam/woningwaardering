# test_parkeerplek_zonder_aantal_adressen_wordt_als_parkeerplek_van_een_adres_gewaardeerd

Een parkeerplek zonder aantal adressen wordt gewaardeerd als een parkeerplek van één adres.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4; wettekst,
Bijlage I onder A, toelichting rubriek 10.

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Privé
    - Parkeerplek buiten behorend bij complex (Type III)              2.00 st     8.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Parkeerplek buiten behorend bij complex' (parkeerplek_buiten_behorend_bij_complex) heeft geen 'gedeeld_met_aantal_adressen'. De waardering gaat uit van 1 (niet gedeeld). Zet 'gedeeld_met_aantal_adressen' >= 2 wanneer de ruimte gedeeld is.

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
      "aantal": 2
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
  "punten": 8.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__prive__parkeerplek_buiten_behorend_bij_complex_type_iii",
        "naam": "Parkeerplek buiten behorend bij complex (Type III)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_parkeerruimten__prive"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 8.0
    }
  ]
}
```
