# test_prive_buitenruimte_krijgt_2_punten_plus_035_punt_per_m2

Een privé-buitenruimte krijgt 2 punten plus 0,35 punt per m².

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Voor
privébuitenruimten worden in ieder geval twee punten toegekend, en daarna
per vierkante meter 0,35 punt."

## Rapport

```text
BUITENRUIMTEN
  Privé                                                              30.00 m²    10.50 pt
    - Tuin                                                           30.00 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
                                                                                ------
  Totaal                                                                         12.50 pt
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
  "punten": 12.5,
  "woningwaarderingen": [
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 10.5
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
      "criterium": {
        "id": "buitenruimten__prive_buitenruimten_aanwezig",
        "naam": "Privé buitenruimten aanwezig"
      },
      "punten": 2.0
    }
  ]
}
```
