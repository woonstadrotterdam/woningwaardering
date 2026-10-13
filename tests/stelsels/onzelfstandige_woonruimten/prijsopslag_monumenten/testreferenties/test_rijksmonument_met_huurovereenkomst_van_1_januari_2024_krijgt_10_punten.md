# test_rijksmonument_met_huurovereenkomst_van_1_januari_2024_krijgt_10_punten

Een rijksmonument waarvan de huurovereenkomst op 1 januari 2024 is afgesloten, krijgt 10 punten.

Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
bijlage I, onder B, met 10 punten vermeerderd."

Bron: beleidsboek onzelfstandige woonruimten, 2.14.4: "als de
huurovereenkomst is afgesloten vóór 1 juli 2024 dan worden 10 punten extra
toegekend."

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
  "datumAfsluitenHuurovereenkomst": "2024-01-01"
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
