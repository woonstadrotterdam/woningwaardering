# test_zorgwoning_krijgt_35_procent_van_de_punten_van_de_rubrieken_1_tot_en_met_11_als_verhoging

Een zorgwoning krijgt 35% van de punten van de rubrieken 1 tot en met 11 als verhoging.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.12; wettekst,
Bijlage I onder B, onderdeel 12.

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 39.50 pt
                                                                                ------
  Totaal                                                                         39.50 pt
```

## Waarschuwingen

- UserWarning: Eenheid (zorgwoning): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (zorgwoning): 'energieprestaties' is None
- UserWarning: Eenheid zorgwoning: geen WOZ-waarde aangeleverd

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
      "oppervlakte": 98.0,
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
