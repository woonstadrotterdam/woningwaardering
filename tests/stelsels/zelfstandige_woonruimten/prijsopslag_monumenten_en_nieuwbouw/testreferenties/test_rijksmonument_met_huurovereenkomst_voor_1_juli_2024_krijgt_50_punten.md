# test_rijksmonument_met_huurovereenkomst_voor_1_juli_2024_krijgt_50_punten

Een rijksmonument waarvan de huurovereenkomst vóór 1 juli 2024 is afgesloten, krijgt 50 punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.13.4; wettekst,
artikel 8a, tweede lid.

## Rapport

```text
PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Rijksmonument                                                                  50.00 pt
                                                                                ------
  Totaal                                                                         50.00 pt
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "PMN",
      "naam": "Prijsopslag monumenten en nieuwbouw"
    }
  },
  "punten": 50.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten_en_nieuwbouw__rijksmonument",
        "naam": "Rijksmonument"
      },
      "punten": 50.0
    }
  ],
  "opslagpercentage": 0.0
}
```
