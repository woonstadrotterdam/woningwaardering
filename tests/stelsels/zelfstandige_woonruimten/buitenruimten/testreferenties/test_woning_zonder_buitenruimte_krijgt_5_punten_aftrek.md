# test_woning_zonder_buitenruimte_krijgt_5_punten_aftrek

Een woning zonder buitenruimte krijgt 5 punten aftrek.

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

Geen.

## Input

```json
{
  "ruimten": []
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
