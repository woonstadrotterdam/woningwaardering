# test_zorgwoning_krijgt_3_punten

Een zorgwoning krijgt 3 punten voor de gemeenschappelijke ruimten en voorzieningen.

Bron: beleidsboek zelfstandige woonruimten, 2.9.4: "Om arbeidsintensief
meetwerk te voorkomen kent de Huurcommissie in dat geval een waardering van
3 punten per woning toe."

De eenheid heeft de doelgroep zorg en alleen een eigen woonkamer; de
gemeenschappelijke ruimten zijn niet meegegeven.

Bron: implementatietoelichting zelfstandige woonruimten, 2.9.4: "Dit
voorbeeld toont hoe een zorgwoning wordt aangegeven door de doelgroep op
'zorg' te zetten. Voor een zorgwoning hoeven de gemeenschappelijke ruimten
en voorzieningen niet verder gespecificeerd te worden."

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 3.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__zorgwoning",
        "naam": "Zorgwoning"
      },
      "punten": 3.0
    }
  ]
}
```
