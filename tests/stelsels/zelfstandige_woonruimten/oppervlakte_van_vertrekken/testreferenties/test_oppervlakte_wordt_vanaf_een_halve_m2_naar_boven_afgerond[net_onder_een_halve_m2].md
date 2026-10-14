# test_oppervlakte_wordt_vanaf_een_halve_m2_naar_boven_afgerond[net_onder_een_halve_m2]

De oppervlakte van de vertrekken wordt vanaf 0,5 m² naar boven afgerond op hele m².

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "bij 0,5 m² of
meer wordt afgerond naar boven, bij minder dan 0,5 m² naar beneden."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Woonkamer                                                          10.49 m²
                                                                    ------      ------
  Totaal                                                             10.49 m²    10.00 pt
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "aantal": 10.49,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__woonkamer",
        "naam": "Woonkamer",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
