# test_energie_index_wordt_op_de_index_gewaardeerd_niet_op_het_label

Een energie-index wordt gewaardeerd op de index, niet op het label dat erbij is meegegeven.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.4.4
- wettekst, Bijlage I onder A, onderdeel 4.1

## Rapport

```text
ENERGIEPRESTATIE
  A -> C (Energie-index)                                                         22.00 pt
                                                                                ------
  Totaal                                                                         22.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1921,
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
      "begindatum": "2020-08-01",
      "einddatum": "2030-08-01",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "1.48"
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
  "punten": 22.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "A -> C (Energie-index)"
      },
      "punten": 22.0
    }
  ]
}
```
