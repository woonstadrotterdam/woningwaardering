# test_prive_buitenruimte_onder_de_minimumafmeting_wordt_gewaardeerd

Een privé-buitenruimte wordt ook gewaardeerd als zij onder de minimumafmeting voor gemeenschappelijke buitenruimten blijft.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.1.

## Rapport

```text
BUITENRUIMTEN
  Privé
    - Balkon                                                          1.00 m²     0.35 pt
    - Privé buitenruimten aanwezig                                                2.00 pt
  Afronding op kwartpunten                                                       -0.10 pt
                                                                                ------
  Totaal                                                                          2.25 pt
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
      "breedte": 500.0,
      "lengte": 2000.0,
      "oppervlakte": 1.0
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
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 1.0,
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
      "punten": 0.35
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
    },
    {
      "criterium": {
        "id": "buitenruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.1
    }
  ]
}
```
