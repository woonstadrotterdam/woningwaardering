# test_prive_buitenruimte_krijgt_2_punten_plus_035_punt_per_m2

Een privé-buitenruimte krijgt 2 punten plus 0,35 punt per m².

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.8.1
- wettekst, Bijlage I onder B, onderdeel 8

## Rapport

```text
BUITENRUIMTEN
  Privé
    - Balkon                                                         10.00 m²     3.50 pt
    - Privé buitenruimten aanwezig                                                2.00 pt
                                                                                ------
  Totaal                                                                          5.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 10.0
    }
  ]
}
```

## Output

```json
{
  "criteriumGroep": {
    "stelsel": {
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 5.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 10.0,
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
      },
      "punten": 3.5
    },
    {
      "criterium": {
        "id": "buitenruimten__prive__prive_buitenruimten_aanwezig",
        "naam": "Privé buitenruimten aanwezig",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        }
      },
      "punten": 2.0
    }
  ]
}
```
