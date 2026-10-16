# test_rijksmonument_zonder_datum_van_de_huurovereenkomst_wordt_met_waarschuwing_naar_de_peildatum_gewaardeerd

Zonder datum van afsluiten van de huurovereenkomst waardeert de package een rijksmonument met een waarschuwing alsof de huurovereenkomst op de peildatum is afgesloten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.14.4;
implementatietoelichting datamodel-uitbreidingen, "Datum afsluiten
huurovereenkomst"; wettekst, artikel 8a, eerste lid.

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
