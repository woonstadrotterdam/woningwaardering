# test_buitenruimte_zonder_oppervlakte_geeft_een_waarschuwing

Een buitenruimte zonder oppervlakte geeft een waarschuwing over incomplete input.

Een woning zonder gewaardeerde buitenruimte krijgt 5 punten aftrek.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.8.5
- wettekst, Bijlage I onder A, toelichting rubriek 8

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
