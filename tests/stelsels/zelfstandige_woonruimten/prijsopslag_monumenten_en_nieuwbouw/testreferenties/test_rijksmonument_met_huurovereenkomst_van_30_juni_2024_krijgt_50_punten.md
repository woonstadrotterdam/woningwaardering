# test_rijksmonument_met_huurovereenkomst_van_30_juni_2024_krijgt_50_punten

Een rijksmonument waarvan de huurovereenkomst op 30 juni 2024 is afgesloten, krijgt 50 punten.

Bron: wettekst, artikel 8a, tweede lid: "Indien de woonruimte bestaat uit
of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de
Erfgoedwet en de huurovereenkomst betreffende die woonruimte is afgesloten
voor het tijdstip van inwerkingtreding van de Wet betaalbare huur, wordt de
waardering voor een zelfstandige woonruimte in bijlage I, onder A, met 50
punten vermeerderd en de waardering voor een onzelfstandige woonruimte in
bijlage I, onder B, met 10 punten vermeerderd."

Bron: beleidsboek zelfstandige woonruimten, 2.13.4: "als de
huurovereenkomst is afgesloten vóór 1 juli 2024 dan worden 50 punten extra
toegekend."

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
