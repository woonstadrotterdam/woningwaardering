# test_eenheid_zonder_opgegeven_monumenten_geeft_een_waarschuwing

Een eenheid waarvan `monumenten` niet is opgegeven, geeft een waarschuwing.

De package vraagt om een lege lijst wanneer de eenheid geen monumentstatus
heeft. De implementatietoelichting noemt die keuze niet; de test legt het
huidige gedrag vast.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Na de waarschuwing zoekt de package de monumentstatus zelf op met de
BAG-identificatie van de eenheid (README.md, Installatie). Deze eenheid
heeft geen BAG-identificatie en krijgt geen waardering.

## Rapport

Geen waarderingen voor Prijsopslag monumenten.

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.

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
