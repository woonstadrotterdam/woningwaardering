# test_buitenruimten_krijgen_samen_hooguit_15_punten

Buitenruimten krijgen samen hooguit 15 punten.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Voor de rubriek
buitenruimten (rubriek 8) kan in totaal maximaal vijftien punten worden
toegekend."

De punten vóór het maximum volgen uit de opgetelde oppervlakte van de tuin
en het balkon.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Indien sprake is
van meerdere buitenruimten die allen tot dezelfde categorie behoren, zijnde
allen gemeenschappelijk of privé, dan worden de oppervlaktes van die
buitenruimtes bij elkaar opgeteld." en "Voor privébuitenruimten worden in
ieder geval twee punten toegekend, en daarna per vierkante meter 0,35
punt."

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
