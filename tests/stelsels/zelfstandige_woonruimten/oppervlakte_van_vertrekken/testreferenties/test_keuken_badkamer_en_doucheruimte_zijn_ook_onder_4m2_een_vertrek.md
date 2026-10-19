# test_keuken_badkamer_en_doucheruimte_zijn_ook_onder_4m2_een_vertrek

Een keuken, badkamer en doucheruimte zijn ook onder de 4 m² een vertrek.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.2.1
- wettekst, Bijlage I onder A, toelichting rubriek 1

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Keuken                                                              3.99 m²
  Badkamer                                                            3.99 m²
  Badkamer met toilet                                                 3.99 m²
  Doucheruimte                                                        3.99 m²
                                                                    ------      ------
  Totaal                                                             15.96 m²    16.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 3.99
    },
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
      "oppervlakte": 3.99
    },
    {
      "id": "badkamer_met_toilet",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAT",
        "naam": "Badkamer met toilet"
      },
      "naam": "Badkamer met toilet",
      "oppervlakte": 3.99
    },
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
      "oppervlakte": 3.99
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 16.0,
  "woningwaarderingen": [
    {
      "aantal": 3.99,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 3.99,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__badkamer",
        "naam": "Badkamer",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 3.99,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__badkamer_met_toilet",
        "naam": "Badkamer met toilet",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 3.99,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__doucheruimte",
        "naam": "Doucheruimte",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
