# test_energielabel_afgegeven_van_2015_tot_2021_telt_niet_mee[afgegeven_op_31_december_2020]

Een energielabel dat is afgegeven van 1 januari 2015 tot 1 januari 2021, telt niet mee.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.3.

Zonder geldige energieprestatie bepaalt het bouwjaar de punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.4.5; wettekst,
Bijlage I onder A, onderdeel 4.1.

## Rapport

```text
ENERGIEPRESTATIE
  Bouwjaar 1990                                                                  14.00 pt
                                                                                ------
  Totaal                                                                         14.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1990,
  "energieprestaties": [
    {
      "soort": {
        "code": "VEL",
        "naam": "Voorlopig energielabel"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2020-12-31",
      "einddatum": "2030-12-31",
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
