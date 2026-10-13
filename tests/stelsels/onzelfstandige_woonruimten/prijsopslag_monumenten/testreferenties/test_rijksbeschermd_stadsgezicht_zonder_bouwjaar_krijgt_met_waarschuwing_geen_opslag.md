# test_rijksbeschermd_stadsgezicht_zonder_bouwjaar_krijgt_met_waarschuwing_geen_opslag

Een woonruimte in een rijksbeschermd stadsgezicht zonder bouwjaar krijgt met een waarschuwing geen opslag.

De opslag geldt alleen voor een woning die vóór 1965 is gebouwd. Zonder
bouwjaar kan de package die voorwaarde niet toetsen.

Bron: wettekst, artikel 8a, vijfde lid: "De maximale huurprijsgrens wordt
met 5% vermeerderd indien:" en "b. de woonruimte behoort tot een woning die
is gebouwd voor 1965; en".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6: "Het
bouwjaar is van belang omdat alleen woningen gebouwd vóór 1965 in
aanmerking komen voor de opslag van 5%."

De implementatietoelichting noemt niet dat de package bij een ontbrekend
bouwjaar waarschuwt en geen opslag toekent; de test legt het huidige gedrag
vast.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Prijsopslag monumenten.

## Waarschuwingen

- UserWarning: Eenheid (eenheid): geen bouwjaar gevonden

## Input

```json
{
  "id": "eenheid",
  "monumenten": [
    {
      "code": "SGR",
      "naam": "Rijksbeschermd stadsgezicht"
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
      "code": "PMO",
      "naam": "Prijsopslag monumenten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": [],
  "opslagpercentage": 0.0
}
```
