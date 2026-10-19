# test_energie_index_zonder_waarde_wordt_met_waarschuwing_op_het_bouwjaar_gewaardeerd

Een energie-index zonder waarde wordt met een waarschuwing op het bouwjaar gewaardeerd.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.4.3

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1990                                                                  14.00 pt
                                                                                ------
  Totaal                                                                         14.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): energie-index mist waarde en kan daarom niet worden gewaardeerd onder stelselgroep Energieprestatie.

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1990,
  "energieprestaties": [
    {
      "soort": {
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2018-06-01",
      "einddatum": "2028-06-01",
      "label": {
        "code": "A",
        "naam": "A"
      }
    }
  ],
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "EGW",
        "naam": "Eengezinswoning"
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
  "punten": 14.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1990"
      },
      "punten": 14.0
    }
  ]
}
```
