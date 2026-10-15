# test_keuken_en_badkamer_zijn_ook_onder_4m2_een_vertrek

Een keuken en een badkamer zijn ook onder de 4 m² een vertrek.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1;
wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder
B, toelichting, inleiding).

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Keuken                                                          2.00 m²
    - Badkamer met toilet                                             2.00 m²
                                                                                ------
  Totaal                                                                          4.00 pt
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__badkamer_met_toilet",
        "naam": "Badkamer met toilet",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
