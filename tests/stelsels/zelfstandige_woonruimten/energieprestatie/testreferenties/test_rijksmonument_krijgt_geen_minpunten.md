# test_rijksmonument_krijgt_geen_minpunten

Een rijksmonument krijgt geen minpunten voor de energieprestatie.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.6.1; wettekst,
Bijlage I onder A, onderdeel 4.2.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1921                                                                 -15.00 pt
  Correctie monument                                                             15.00 pt
                                                                                ------
  Totaal                                                                          0.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 1921,
  "energieprestaties": [],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
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
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "energieprestatie__bouwjaar",
        "naam": "Bouwjaar 1921"
      },
      "punten": -15.0
    },
    {
      "criterium": {
        "id": "energieprestatie__correctie_monument",
        "naam": "Correctie monument"
      },
      "punten": 15.0
    }
  ]
}
```
