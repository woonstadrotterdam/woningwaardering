# test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd

Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.8

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Balkon                                                          6.00 m²     2.25 pt
                                                                                ------
  Totaal                                                                          2.25 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Balkon' (balkon) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Buitenruimte.

## Input

```json
{
  "ruimten": [
    {
      "id": "balkon",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "oppervlakte": 6.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__balkon",
        "naam": "Balkon",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.25
    }
  ]
}
```
