# test_rijksmonument_met_huurovereenkomst_van_1_juli_2024_krijgt_35_procent_opslag

Een rijksmonument waarvan de huurovereenkomst op of na 1 juli 2024 is afgesloten, krijgt 35% opslag op de maximale huurprijs.

Bron: implementatietoelichting zelfstandige woonruimten, 2.13.4; wettekst,
artikel 8a, eerste lid.

## Rapport

```text
PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Rijksmonument                                                                                35%
                                                                                ------
  Totaal                                                                          0.00 pt      35%
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
  "datumAfsluitenHuurovereenkomst": "2024-07-01"
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
  "punten": 0.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "prijsopslag_monumenten_en_nieuwbouw__rijksmonument",
        "naam": "Rijksmonument"
      },
      "opslagpercentage": 0.35
    }
  ],
  "opslagpercentage": 0.35
}
```
