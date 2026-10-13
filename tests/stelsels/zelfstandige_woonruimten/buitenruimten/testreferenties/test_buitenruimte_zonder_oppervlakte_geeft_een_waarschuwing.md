# test_buitenruimte_zonder_oppervlakte_geeft_een_waarschuwing

Een buitenruimte zonder oppervlakte is incomplete input en wordt niet gewaardeerd.

De woning heeft daardoor geen gewaardeerde buitenruimte en krijgt de aftrek
van 5 punten.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5: "Daarom
passen we −5 alleen toe als er geen enkele gewaardeerde buitenruimte is
(bijv. te kleine gedeelde ruimten of privé zonder oppervlakte leveren geen
punten en tellen dus niet mee tegen de aftrek)."

## Rapport

```text
BUITENRUIMTEN
  Geen buitenruimten                                                             -5.00 pt
                                                                                ------
  Totaal                                                                         -5.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Balkon' (balkon) heeft geen oppervlakte

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
      "naam": "Balkon"
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
  "punten": -5.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__geen_buitenruimten",
        "naam": "Geen buitenruimten"
      },
      "punten": -5.0
    }
  ]
}
```
