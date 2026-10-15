# test_rijksmonument_met_huurovereenkomst_voor_1_juli_2024_krijgt_10_punten

Een rijksmonument waarvan de huurovereenkomst vóór 1 juli 2024 is afgesloten, krijgt 10 punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
artikel 8a, tweede lid.

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Rijksmonument                                                                  10.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
  "datumAfsluitenHuurovereenkomst": "2024-06-30"
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
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten__rijksmonument",
        "naam": "Rijksmonument"
      },
      "punten": 10.0
    }
  ],
  "opslagpercentage": 0.0
}
```
