# test_zorgwoning_krijgt_35_procent_van_de_punten_van_de_rubrieken_1_tot_en_met_11_1_als_verhoging

Een zorgwoning krijgt 35% van de punten van de rubrieken 1 tot en met 11.1 als verhoging.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12; wettekst,
Bijlage I onder A, onderdeel 12.

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 14.25 pt
                                                                                ------
  Totaal                                                                         14.25 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid (zorgwoning): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (zorgwoning) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (zorgwoning) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (zorgwoning): geen WOZ-waarde aangeleverd
- UserWarning: Eenheid (zorgwoning): geen bouwjaar gevonden. Kan niet bepalen of woning onder nieuwbouw valt.

## Input

```json
{
  "id": "zorgwoning",
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
      "oppervlakte": 19.1488,
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
