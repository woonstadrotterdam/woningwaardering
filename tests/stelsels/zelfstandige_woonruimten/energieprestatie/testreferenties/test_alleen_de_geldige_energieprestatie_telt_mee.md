# test_alleen_de_geldige_energieprestatie_telt_mee

Alleen een geldige energieprestatie bepaalt de punten.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.4.3
- wettekst, Bijlage I onder A, toelichting rubriek 4.1

## Rapport

```text
ENERGIEPRESTATIE
  A                                                                              37.00 pt
                                                                                ------
  Totaal                                                                         37.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1993,
  "energieprestaties": [
    {
      "soort": {
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2014-03-27",
      "einddatum": "2024-03-27",
      "label": {
        "code": "F",
        "naam": "F"
      },
      "waarde": "160"
    },
    {
      "soort": {
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2021-03-27",
      "einddatum": "2031-03-27",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "170"
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
  "punten": 37.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A"
      },
      "punten": 37.0
    }
  ]
}
```
