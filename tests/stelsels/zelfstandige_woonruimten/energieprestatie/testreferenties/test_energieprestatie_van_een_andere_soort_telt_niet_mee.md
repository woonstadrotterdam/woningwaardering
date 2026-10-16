# test_energieprestatie_van_een_andere_soort_telt_niet_mee

Een energieprestatie van een andere soort dan een energielabel, energie-index of primair energieverbruik telt niet mee.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3.

Zonder geldige energieprestatie bepaalt het bouwjaar de punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.5; wettekst,
Bijlage I onder A, onderdeel 4.1.

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
      "soort": {
        "code": "COM",
        "naam": "Compactheid"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2021-02-23",
      "einddatum": "2031-02-23",
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
