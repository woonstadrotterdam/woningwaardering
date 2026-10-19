# test_zorgwoning_krijgt_3_punten

Een zorgwoning krijgt 3 punten voor de gemeenschappelijke ruimten en voorzieningen.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.9.4

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Zorgwoning                                                                      3.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "doelgroep": {
    "code": "ZOR",
    "naam": "Zorg"
  },
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__zorgwoning",
        "naam": "Zorgwoning"
      },
      "punten": 3.0
    }
  ]
}
```
