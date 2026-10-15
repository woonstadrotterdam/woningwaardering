# test_rijksmonument_zonder_datum_van_de_huurovereenkomst_krijgt_met_waarschuwing_35_procent_opslag

Een rijksmonument zonder datum van afsluiten van de huurovereenkomst krijgt met een waarschuwing 35% opslag op de maximale huurprijs.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
artikel 8a, eerste lid.

## Rapport

```text
PRIJSOPSLAG MONUMENTEN
  Rijksmonument                                                                                35%
                                                                                ------
  Totaal                                                                          0.00 pt      35%
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.

## Input

```json
{
  "id": "eenheid",
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
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
        "id": "prijsopslag_monumenten__rijksmonument",
        "naam": "Rijksmonument"
      },
      "opslagpercentage": 0.35
    }
  ],
  "opslagpercentage": 0.35
}
```
