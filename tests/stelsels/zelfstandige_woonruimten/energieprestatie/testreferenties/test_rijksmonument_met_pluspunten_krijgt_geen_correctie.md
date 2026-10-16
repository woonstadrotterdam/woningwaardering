# test_rijksmonument_met_pluspunten_krijgt_geen_correctie

Een rijksmonument met een positief aantal punten voor de energieprestatie houdt die punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.6.1; wettekst,
Bijlage I onder A, onderdeel 4.2.

## Rapport

```text
ENERGIEPRESTATIE
  C (Energie-index)                                                              22.00 pt
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
      "begindatum": "2017-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.48"
    }
  ],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
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
        "naam": "C (Energie-index)"
      },
      "punten": 22.0
    }
  ]
}
```
