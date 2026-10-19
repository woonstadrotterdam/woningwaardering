# test_punten_voor_sanitair_in_gemeenschappelijke_ruimte_worden_gedeeld_door_het_aantal_adressen

De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door het aantal adressen dat toegang heeft.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.9.2
- wettekst, Bijlage I onder A, toelichting rubriek 9

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 2 adressen
    - Oppervlakte van vertrekken                                                  5.00 pt
      - Badkamer                                                     10.00 m²
    - Sanitair
      - Badkamer
        - Wastafel                                                    1.00 st     0.50 pt
        - Bad                                                         1.00 st     3.00 pt
                                                                                ------
  Totaal                                                                          8.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "badkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 2,
      "installaties": [
        {
          "code": "BAD",
          "naam": "Bad"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        }
      ]
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
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 8.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen"
        }
      },
      "punten": 5.0
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__badkamer",
        "naam": "Badkamer",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair",
        "naam": "Sanitair",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer",
        "naam": "Badkamer",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    }
  ]
}
```
