# test_minder_dan_8m2_aan_vertrekken_geeft_4_punten_aftrek

Minder dan 8 m² aan vertrekken geeft 4 punten aftrek.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.13
- wettekst, Bijlage I onder B, onderdeel 13

## Rapport

```text
AFTREKPUNTEN
  Oppervlakte van vertrekken is minder dan 8 m²                       7.00 m²    -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt
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
      "oppervlakte": 7.0
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
      "code": "AFT",
      "naam": "Aftrekpunten"
    }
  },
  "punten": -4.0,
  "woningwaarderingen": [
    {
      "aantal": 7.0,
      "criterium": {
        "id": "aftrekpunten__oppervlakte_van_vertrekken_minder_dan_8m2",
        "naam": "Oppervlakte van vertrekken is minder dan 8 m²",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": -4.0
    }
  ]
}
```
