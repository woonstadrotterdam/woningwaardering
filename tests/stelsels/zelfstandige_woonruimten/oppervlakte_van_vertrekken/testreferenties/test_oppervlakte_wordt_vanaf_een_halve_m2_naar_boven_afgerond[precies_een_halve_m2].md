# test_oppervlakte_wordt_vanaf_een_halve_m2_naar_boven_afgerond[precies_een_halve_m2]

De oppervlakte van de vertrekken wordt vanaf 0,5 m² naar boven afgerond op hele m².

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "bij 0,5 m² of
meer wordt afgerond naar boven, bij minder dan 0,5 m² naar beneden."

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Woonkamer                                                          10.50 m²
                                                                    ------      ------
  Totaal                                                             10.50 m²    11.00 pt
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
      "oppervlakte": 10.5
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
  "punten": 11.0,
  "woningwaarderingen": [
    {
      "aantal": 10.5,
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
