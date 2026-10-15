# test_50_punten_voor_een_rijksmonument_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning

De 50 punten voor een rijksmonument met een huurovereenkomst van vóór de inwerkingtreding van de Wet betaalbare huur tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12;
implementatietoelichting zelfstandige woonruimten, 2.13.4; wettekst, artikel
8a, tweede lid; wettekst, Bijlage I onder A, onderdeel 12.

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 14.25 pt
                                                                                ------
  Totaal                                                                         14.25 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid (zorgwoning) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (zorgwoning) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (zorgwoning): geen WOZ-waarde aangeleverd

## Input

```json
{
  "id": "zorgwoning",
  "bouwjaar": 1960,
  "doelgroep": {
    "code": "ZOR",
    "naam": "Zorg"
  },
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 19.1488,
      "verwarmd": true,
      "verkoeld": false
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 14.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__zorgwoning_puntenverhoging",
        "naam": "Zorgwoning 35% puntenverhoging"
      },
      "punten": 14.25
    }
  ]
}
```
