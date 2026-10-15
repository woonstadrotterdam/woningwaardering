# test_garage_wordt_als_overige_ruimte_gewaardeerd

Een garage die bij de woning hoort, wordt als overige ruimte gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.5; wettekst,
Bijlage I onder A, toelichting rubriek 2.

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Garage1                                                            15.00 m²
  Garage2                                                            15.00 m²
                                                                    ------      ------
  Totaal                                                             30.00 m²    22.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "garage1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage1",
      "oppervlakte": 15.0
    },
    {
      "id": "garage2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage2",
      "oppervlakte": 15.0
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
  "punten": 22.5,
  "woningwaarderingen": [
    {
      "aantal": 15.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__garage1",
        "naam": "Garage1",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 15.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__garage2",
        "naam": "Garage2",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
