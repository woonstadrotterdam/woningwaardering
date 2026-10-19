# test_monument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht[rijksmonument]

Een monument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.14.6
- wettekst, artikel 8a, vijfde lid

Dit geval: het rijksmonument krijgt zelf 35% opslag

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Rijksmonument                                                                                35%
                                                                                ------
  Totaal                                                                          0.00 pt      35%
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1964,
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
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
        "id": "prijsopslag_monumenten__rijksmonument",
        "naam": "Rijksmonument"
      },
      "opslagpercentage": 0.35
    }
  ],
  "opslagpercentage": 0.35
}
```
