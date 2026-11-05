# test_woonruimte_zonder_buitenruimte_krijgt_geen_aftrek

Een onzelfstandige woonruimte zonder buitenruimte krijgt geen aftrek.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.8
- wettekst, Bijlage I onder B, onderdeel 8

## Rapport

Geen waarderingen voor Buitenruimten.

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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
