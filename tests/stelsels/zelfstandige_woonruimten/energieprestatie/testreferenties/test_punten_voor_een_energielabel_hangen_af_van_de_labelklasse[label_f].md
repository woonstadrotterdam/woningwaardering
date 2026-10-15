# test_punten_voor_een_energielabel_hangen_af_van_de_labelklasse[label_f]

De punten voor een energielabel hangen af van de labelklasse.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.4; wettekst,
Bijlage I onder A, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  F                                                                              -9.00 pt
                                                                                ------
  Totaal                                                                         -9.00 pt
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
        "code": "F",
        "naam": "F"
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
  "punten": -9.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "F"
      },
      "punten": -9.0
    }
  ]
}
```
