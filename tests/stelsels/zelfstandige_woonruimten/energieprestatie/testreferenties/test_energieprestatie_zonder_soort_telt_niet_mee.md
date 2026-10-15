# test_energieprestatie_zonder_soort_telt_niet_mee

Een energieprestatie zonder soort telt niet mee: de woning wordt op het bouwjaar gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3; wettekst,
Bijlage I onder A, toelichting rubriek 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1921                                                                 -15.00 pt
                                                                                ------
  Totaal                                                                        -15.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
  "energieprestaties": [
    {
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "naam": "C"
      },
      "waarde": "1.48"
    }
  ],
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
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
      "code": "ENE",
      "naam": "Energieprestatie"
    }
  },
  "punten": -15.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921"
      },
      "punten": -15.0
    }
  ]
}
```
