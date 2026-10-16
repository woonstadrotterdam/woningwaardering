# test_parkeerplek_zonder_aantal_adressen_wordt_als_prive_parkeerplek_gewaardeerd

Een parkeerplek zonder aantal adressen wordt gewaardeerd als een privé-parkeerplek van één adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2; wettekst,
Bijlage I onder A, toelichting rubriek 10 (via Bijlage I onder B,
toelichting, inleiding).

## Rapport

```text
GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Privé
    - Parkeerplek buiten behorend bij complex (Type III)              1.00 st     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt
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
      "oppervlakte": 12.0
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
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_parkeerruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 1.0,
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
      "punten": 4.0
    }
  ]
}
```
