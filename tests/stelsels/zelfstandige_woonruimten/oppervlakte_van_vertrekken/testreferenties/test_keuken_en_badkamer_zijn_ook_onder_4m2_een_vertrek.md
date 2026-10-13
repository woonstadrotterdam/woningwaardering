# test_keuken_en_badkamer_zijn_ook_onder_4m2_een_vertrek

Een keuken en een badkamer zijn ook onder de 4 m² een vertrek.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "In afwijking van
bovenstaande eisen is een ruimte die uitsluitend als keuken dient en een
badkamer of doucheruimte altijd een vertrek."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Keuken                                                              2.00 m²
  Badkamer met toilet                                                 2.00 m²
                                                                    ------      ------
  Totaal                                                              4.00 m²     4.00 pt
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
      "oppervlakte": 2.0
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
      "oppervlakte": 2.0
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
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "aantal": 2.0,
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
      "aantal": 2.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__badkamer_met_toilet",
        "naam": "Badkamer met toilet",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
