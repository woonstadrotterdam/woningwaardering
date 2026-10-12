# test_rekenvoorbeeld_extra_voorzieningen_uit_het_beleidsboek

Het rekenvoorbeeld van het beleidsboek: extra voorzieningen blijven onder het maximum.

Het beleidsboek komt op 16,75 punten en noemt geen wastafel. De package
waardeert extra voorzieningen alleen in een ruimte met een wastafel; die
staat daarom in de input en levert 1 punt extra op.

Bron: beleidsboek zelfstandige woonruimten, 2.6.2: "De punten worden voor de
extra sanitaire voorzieningen (5,75 punten) worden niet afgetopt, omdat het
puntenaantal lager is dan het totaal aantal punten voor de douche en
bad/douchecombinatie (11 punten)."

## Rapport

```text
SANITAIR
  Badkamer
    - Wastafel                                                        1.00 st     1.00 pt
    - Bad en douche                                                   1.00 st     7.00 pt
    - Extra voorzieningen
      - Bubbelfunctie van het bad                                     1.00 st     1.50 pt
      - Douchewand                                                    1.00 st     1.25 pt
      - Handdoekenradiator                                            2.00 st     1.50 pt
      - Stopcontact bij wastafel                                      2.00 st     0.50 pt
      - Éénhandsmengkraan                                             2.00 st     0.50 pt
      - Thermostatische mengkraan                                     1.00 st     0.50 pt
  Slaapkamer
    - Douche                                                          1.00 st     4.00 pt
                                                                                ------
  Totaal                                                                         17.75 pt
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
      "installaties": [
        {
          "code": "BAD",
          "naam": "Bad"
        },
        {
          "code": "DOU",
          "naam": "Douche"
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
          "code": "HRA",
          "naam": "Handdoekenradiator"
        },
        {
          "code": "STW",
          "naam": "Stopcontact bij wastafel"
        },
        {
          "code": "STW",
          "naam": "Stopcontact bij wastafel"
        },
        {
          "code": "TME",
          "naam": "Thermostatische mengkraan"
        },
        {
          "code": "EHM",
          "naam": "Éénhandsmengkraan"
        },
        {
          "code": "EHM",
          "naam": "Éénhandsmengkraan"
        }
      ]
    },
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "DOU",
          "naam": "Douche"
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 17.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__badkamer",
        "naam": "Badkamer"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 7.0
    },
    {
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen__bubbelfunctie_van_het_bad",
        "naam": "Bubbelfunctie van het bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.5
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen__douchewand",
        "naam": "Douchewand",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.25
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen__handdoekenradiator",
        "naam": "Handdoekenradiator",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.5
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__badkamer__extra_voorzieningen__stopcontact_bij_wastafel",
        "naam": "Stopcontact bij wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
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
        "id": "sanitair__badkamer__extra_voorzieningen__eenhandsmengkraan",
        "naam": "Éénhandsmengkraan",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
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
        "id": "sanitair__badkamer__extra_voorzieningen__thermostatische_mengkraan",
        "naam": "Thermostatische mengkraan",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "sanitair__slaapkamer",
        "naam": "Slaapkamer"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__slaapkamer__douche",
        "naam": "Douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__slaapkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    }
  ]
}
```
