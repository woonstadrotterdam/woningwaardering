# test_punten_voor_een_energie_index_hangen_af_van_de_klasse[index_1_4]

De punten voor een energie-index hangen af van de klasse waarin de index valt.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.4.4
- wettekst, Bijlage I onder A, onderdeel 4.1

## Rapport

```text
ENERGIEPRESTATIE
  Energie-index                                                                  34.00 pt
                                                                                ------
  Totaal                                                                         34.00 pt
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
      "waarde": "1.4"
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
  "punten": 34.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "Energie-index"
      },
      "punten": 34.0
    }
  ]
}
```
