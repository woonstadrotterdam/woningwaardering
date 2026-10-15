# test_punten_voor_sanitair_in_gemeenschappelijke_ruimte_worden_gedeeld_door_het_aantal_adressen

De punten voor sanitair in een gemeenschappelijke ruimte worden gedeeld door het aantal adressen dat toegang heeft.

Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
Bijlage I onder A, toelichting rubriek 9.

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
        - Extra voorzieningen
          - Bubbelfunctie van het bad                                 1.00 st     0.75 pt
          - Douchewand                                                1.00 st     0.63 pt
          - Handdoekenradiator                                        1.00 st     0.38 pt
          - Ingebouwd kastje met in- of opgebouwde wastafel           1.00 st     0.50 pt
          - Kastruimte                                                2.00 st     0.75 pt
          - Maximering voor Kastruimte                                           -0.38 pt
          - Stopcontact bij wastafel                                  1.00 st     0.13 pt
          - Éénhandsmengkraan                                         1.00 st     0.13 pt
          - Thermostatische mengkraan                                 1.00 st     0.25 pt
          - Max verdubbeling punten bad en douche                                -0.13 pt
  Afronding op kwartpunten                                                       -0.01 pt
                                                                                ------
  Totaal                                                                         11.50 pt
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
        },
        {
          "code": "BUB",
          "naam": "Bubbelfunctie van het bad"
        },
        {
          "code": "DOW",
          "naam": "Douchewand"
        },
        {
          "code": "HRA",
          "naam": "Handdoekenradiator"
        },
        {
          "code": "IKW",
          "naam": "Ingebouwd kastje met in- of opgebouwde wastafel"
        },
        {
          "code": "KAS",
          "naam": "Kastruimte"
        },
        {
          "code": "KAS",
          "naam": "Kastruimte"
        },
        {
          "code": "STW",
          "naam": "Stopcontact bij wastafel"
        },
        {
          "code": "EHM",
          "naam": "Éénhandsmengkraan"
        },
        {
          "code": "TME",
          "naam": "Thermostatische mengkraan"
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
  "punten": 11.5,
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
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__bubbelfunctie_van_het_bad",
        "naam": "Bubbelfunctie van het bad",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.75
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__douchewand",
        "naam": "Douchewand",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.63
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__handdoekenradiator",
        "naam": "Handdoekenradiator",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.38
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__ingebouwd_kastje_met_in_of_opgebouwde_wastafel",
        "naam": "Ingebouwd kastje met in- of opgebouwde wastafel",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__kastruimte",
        "naam": "Kastruimte",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.75
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__max_punten_kastruimte",
        "naam": "Maximering voor Kastruimte",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        }
      },
      "punten": -0.38
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__stopcontact_bij_wastafel",
        "naam": "Stopcontact bij wastafel",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.13
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__eenhandsmengkraan",
        "naam": "Éénhandsmengkraan",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.13
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__thermostatische_mengkraan",
        "naam": "Thermostatische mengkraan",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen__maximering_punten_voorzieningen",
        "naam": "Max verdubbeling punten bad en douche",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__sanitair__badkamer__extra_voorzieningen"
        }
      },
      "punten": -0.13
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.01
    }
  ]
}
```
