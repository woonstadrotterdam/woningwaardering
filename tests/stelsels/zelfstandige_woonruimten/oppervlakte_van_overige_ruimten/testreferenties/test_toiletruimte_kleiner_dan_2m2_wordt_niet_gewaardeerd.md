# test_toiletruimte_kleiner_dan_2m2_wordt_niet_gewaardeerd

Een toiletruimte kleiner dan 2 m² wordt niet als overige ruimte gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "De ruimte dient
een oppervlakte te hebben van minimaal 2 m²." en "Een toiletruimte wordt
gewaardeerd als overige ruimte als het voldoet aan de voorwaarden van een
overige ruimte."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Toiletruimte2                                                       2.10 m²
                                                                    ------      ------
  Totaal                                                              2.10 m²     1.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "toiletruimte1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte1",
      "oppervlakte": 1.9
    },
    {
      "id": "toiletruimte2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte2",
      "oppervlakte": 2.1
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
  "punten": 1.5,
  "woningwaarderingen": [
    {
      "aantal": 2.1,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__toiletruimte2",
        "naam": "Toiletruimte2",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
