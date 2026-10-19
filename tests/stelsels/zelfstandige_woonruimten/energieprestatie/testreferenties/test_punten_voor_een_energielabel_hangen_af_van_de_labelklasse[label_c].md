# test_punten_voor_een_energielabel_hangen_af_van_de_labelklasse[label_c]

De punten voor een energielabel hangen af van de labelklasse.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.4.4
- wettekst, Bijlage I onder A, onderdeel 4.1

## Rapport

```text
ENERGIEPRESTATIE
  C                                                                              22.00 pt
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
        "code": "C",
        "naam": "C"
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
  "punten": 22.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__label",
        "naam": "C"
      },
      "punten": 22.0
    }
  ]
}
```
