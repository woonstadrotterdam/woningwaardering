# test_oppervlakte_wordt_afgerond_na_optellen_van_alle_vertrekken

De oppervlakten van alle vertrekken worden eerst opgeteld en dan afgerond op hele m².

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.2.1.1
- wettekst, Bijlage I onder A, toelichting rubriek 1

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Woonkamer                                                          15.49 m²
  Keuken                                                             11.24 m²
                                                                    ------      ------
  Totaal                                                             26.73 m²    27.00 pt
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
      "oppervlakte": 15.49
    },
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
      "oppervlakte": 11.24
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
  "punten": 27.0,
  "woningwaarderingen": [
    {
      "aantal": 15.49,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__woonkamer",
        "naam": "Woonkamer",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 11.24,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
