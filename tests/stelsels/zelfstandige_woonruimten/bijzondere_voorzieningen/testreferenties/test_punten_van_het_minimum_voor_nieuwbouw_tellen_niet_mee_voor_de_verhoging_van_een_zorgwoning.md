# test_punten_van_het_minimum_voor_nieuwbouw_tellen_niet_mee_voor_de_verhoging_van_een_zorgwoning

De punten waarmee het minimum voor nieuwbouw de punten voor de WOZ-waarde aanvult, tellen niet mee in de punten waarover een zorgwoning 35% verhoging krijgt.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12; wettekst,
Bijlage I onder A, onderdeel 12.

Het minimum voor nieuwbouw is 40 punten voor de WOZ-waarde bij een woning
uit 2015 tot en met 2019 met minimaal 110 punten in de andere rubrieken.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
Bijlage I onder A, onderdeel 11.2.

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 38.00 pt
                                                                                ------
  Totaal                                                                         38.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid (zorgwoning): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (zorgwoning) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (zorgwoning) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (zorgwoning): geen WOZ-waarde aangeleverd
- UserWarning: Eenheid (zorgwoning): geen adres gevonden voor COROP-gebied bepaling

## Input

```json
{
  "id": "zorgwoning",
  "bouwjaar": 2018,
  "doelgroep": {
    "code": "ZOR",
    "naam": "Zorg"
  },
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
      "oppervlakte": 100.0,
      "verwarmd": true,
      "verkoeld": false
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
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 38.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__zorgwoning_puntenverhoging",
        "naam": "Zorgwoning 35% puntenverhoging"
      },
      "punten": 38.0
    }
  ]
}
```
