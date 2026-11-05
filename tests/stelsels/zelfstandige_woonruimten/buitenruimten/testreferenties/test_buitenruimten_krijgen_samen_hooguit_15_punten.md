# test_buitenruimten_krijgen_samen_hooguit_15_punten

Buitenruimten krijgen samen hooguit 15 punten.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.8
- wettekst, Bijlage I onder A, toelichting rubriek 8

## Rapport

```text
BUITENRUIMTEN
  Privé                                                              45.00 m²    15.75 pt
    - Tuin                                                           30.00 m²
    - Balkon                                                         15.00 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Maximaal 15 punten                                                             -2.75 pt
                                                                                ------
  Totaal                                                                         15.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "tuin",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "oppervlakte": 30.0
    },
    {
      "id": "balkon",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "oppervlakte": 15.0
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 15.0,
  "woningwaarderingen": [
    {
      "aantal": 45.0,
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 15.75
    },
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__prive__tuin",
        "naam": "Tuin",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 15.0,
      "criterium": {
        "id": "buitenruimten__prive__balkon",
        "naam": "Balkon",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "buitenruimten__prive_buitenruimten_aanwezig",
        "naam": "Privé buitenruimten aanwezig"
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "buitenruimten__maximering",
        "naam": "Maximaal 15 punten"
      },
      "punten": -2.75
    }
  ]
}
```
