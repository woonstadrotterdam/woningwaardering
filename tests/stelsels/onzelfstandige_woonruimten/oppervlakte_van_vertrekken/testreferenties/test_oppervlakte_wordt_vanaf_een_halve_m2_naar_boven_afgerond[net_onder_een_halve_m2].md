# test_oppervlakte_wordt_vanaf_een_halve_m2_naar_boven_afgerond[net_onder_een_halve_m2]

De oppervlakte van de vertrekken wordt vanaf 0,5 m² naar boven afgerond op hele m².

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.1.1
- wettekst, Bijlage I onder A, toelichting rubriek 1 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Woonkamer                                                      10.49 m²
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "oppervlakte": 10.49
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
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 10.49,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__prive__woonkamer",
        "naam": "Woonkamer",
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
