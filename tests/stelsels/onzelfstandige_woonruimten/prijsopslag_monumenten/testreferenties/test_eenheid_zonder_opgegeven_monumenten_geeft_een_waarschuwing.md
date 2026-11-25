# test_eenheid_zonder_opgegeven_monumenten_geeft_een_waarschuwing

Een eenheid waarvan `monumenten` niet is opgegeven, geeft een waarschuwing.

## Rapport

Geen waarderingen voor Prijsopslag monumenten.

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'monumenten' is niet gespecificeerd en de eenheid heeft geen BAG-identificatie om de monumentstatus mee op te halen. Specificeer 'monumenten', met een lege lijst als de eenheid geen monumentstatus heeft.

## Input

```json
{
  "id": "eenheid"
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
      "code": "PMO",
      "naam": "Prijsopslag monumenten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [],
  "opslagpercentage": 0.0
}
```
