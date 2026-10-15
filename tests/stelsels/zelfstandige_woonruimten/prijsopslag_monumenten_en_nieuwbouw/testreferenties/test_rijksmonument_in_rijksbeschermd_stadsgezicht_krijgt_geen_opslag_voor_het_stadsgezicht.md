# test_rijksmonument_in_rijksbeschermd_stadsgezicht_krijgt_geen_opslag_voor_het_stadsgezicht

Een rijksmonument in een rijksbeschermd stadsgezicht krijgt de opslag van 5% voor het stadsgezicht niet.

Bron: implementatietoelichting zelfstandige woonruimten, 2.13.1;
implementatietoelichting zelfstandige woonruimten, 2.13.6; wettekst, artikel
8a, vijfde lid.

Een rijksmonument krijgt 35% opslag op de maximale huurprijs.

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

- UserWarning: Eenheid (None): 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.

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
  ]
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
