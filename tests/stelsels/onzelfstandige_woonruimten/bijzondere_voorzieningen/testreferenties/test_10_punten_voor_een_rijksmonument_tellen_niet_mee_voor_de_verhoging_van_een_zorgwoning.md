# test_10_punten_voor_een_rijksmonument_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning

De 10 punten voor een rijksmonument met een huurovereenkomst van vóór de inwerkingtreding van de Wet betaalbare huur tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.12;
implementatietoelichting onzelfstandige woonruimten, 2.14.4; wettekst,
artikel 8a, tweede lid; wettekst, Bijlage I onder B, onderdeel 12.

Een rijksmonument krijgt in rubriek 4 geen minpunten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.4.6.1;
wettekst, Bijlage I onder B, onderdeel 4.2.

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 39.50 pt
                                                                                ------
  Totaal                                                                         39.50 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid zorgwoning: geen WOZ-waarde aangeleverd

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
      "oppervlakte": 98.0,
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 39.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__zorgwoning_puntenverhoging",
        "naam": "Zorgwoning 35% puntenverhoging"
      },
      "punten": 39.5
    }
  ]
}
```
