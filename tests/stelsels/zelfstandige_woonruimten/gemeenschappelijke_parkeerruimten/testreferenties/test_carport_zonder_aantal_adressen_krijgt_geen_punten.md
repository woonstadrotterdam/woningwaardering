# test_carport_zonder_aantal_adressen_krijgt_geen_punten

Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4;
implementatietoelichting zelfstandige woonruimten, 2.8.3.

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12.0
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
