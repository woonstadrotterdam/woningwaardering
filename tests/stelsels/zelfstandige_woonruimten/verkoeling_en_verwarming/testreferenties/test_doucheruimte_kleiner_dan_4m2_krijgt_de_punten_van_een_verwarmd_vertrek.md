# test_doucheruimte_kleiner_dan_4m2_krijgt_de_punten_van_een_verwarmd_vertrek

Een verwarmde doucheruimte kleiner dan 4 m² krijgt de 2 punten van een verwarmd vertrek.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
badkamer of doucheruimte altijd een vertrek."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmd
vertrek wordt, ongeacht de verwarmingswijze, een waardering van twee punten
toegepast".

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Doucheruimte                                                                2.00 pt
                                                                                ------
  Totaal                                                                          2.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "doucheruimte",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "DOU",
        "naam": "Doucheruimte"
      },
      "naam": "Doucheruimte",
      "oppervlakte": 2.0,
      "verwarmd": true
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 2.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__doucheruimte",
        "naam": "Doucheruimte",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    }
  ]
}
```
