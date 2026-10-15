# test_rijksbeschermd_stadsgezicht_krijgt_alleen_bij_bouwjaar_voor_1965_opslag[bouwjaar_1964]

Een woonruimte in een rijksbeschermd stadsgezicht krijgt alleen 5% opslag op de maximale huurprijs als de woning vóór 1965 is gebouwd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.6; wettekst,
artikel 8a, vijfde lid.

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Rijksbeschermd stads- of dorpsgezicht                                                         5%
                                                                                ------
  Totaal                                                                          0.00 pt       5%
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1964,
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
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten__rijksbeschermd_stads_of_dorpsgezicht",
        "naam": "Rijksbeschermd stads- of dorpsgezicht"
      },
      "opslagpercentage": 0.05
    }
  ],
  "opslagpercentage": 0.05
}
```
