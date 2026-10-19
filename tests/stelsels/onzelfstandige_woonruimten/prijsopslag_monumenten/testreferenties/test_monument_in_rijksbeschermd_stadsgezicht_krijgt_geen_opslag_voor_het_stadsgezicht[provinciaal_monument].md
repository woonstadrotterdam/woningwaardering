# test_monument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht[provinciaal_monument]

Een monument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.14.6
- wettekst, artikel 8a, vijfde lid

Dit geval: het provinciaal monument krijgt zelf 15% opslag

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Gemeentelijk of provinciaal monument                                                         15%
                                                                                ------
  Totaal                                                                          0.00 pt      15%
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1964,
  "monumenten": [
    {
      "code": "PRO",
      "naam": "Provinciaal monument"
    },
    {
      "code": "SGR",
      "naam": "Rijksbeschermd stadsgezicht"
    }
  ],
  "datumAfsluitenHuurovereenkomst": "2024-07-01"
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
        "id": "prijsopslag_monumenten__gemeentelijk_of_provinciaal_monument",
        "naam": "Gemeentelijk of provinciaal monument"
      },
      "opslagpercentage": 0.15
    }
  ],
  "opslagpercentage": 0.15
}
```
