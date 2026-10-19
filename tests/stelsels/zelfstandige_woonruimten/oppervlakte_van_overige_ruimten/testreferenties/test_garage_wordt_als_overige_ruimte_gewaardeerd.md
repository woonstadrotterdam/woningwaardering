# test_garage_wordt_als_overige_ruimte_gewaardeerd

Een garage die bij de woning hoort, wordt als overige ruimte gewaardeerd.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.2.2.5
- wettekst, Bijlage I onder A, toelichting rubriek 2

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Garage                                                             10.00 m²
                                                                    ------      ------
  Totaal                                                             10.00 m²     7.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
      "oppervlakte": 10.0
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 7.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__garage",
        "naam": "Garage",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
