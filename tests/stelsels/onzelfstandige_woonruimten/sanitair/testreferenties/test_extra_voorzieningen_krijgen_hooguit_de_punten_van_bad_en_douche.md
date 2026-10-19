# test_extra_voorzieningen_krijgen_hooguit_de_punten_van_bad_en_douche

Extra voorzieningen in de badkamer krijgen samen hooguit de punten van het bad en de douche.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.6.2
- wettekst, Bijlage I onder B, onderdeel 6.2

## Rapport

```text
SANITAIR
  Privé
    - Badkamer
      - Wastafel                                                      1.00 st     1.00 pt
      - Bad en douche                                                 1.00 st     6.00 pt
      - Extra voorzieningen
        - Bubbelfunctie van het bad                                   1.00 st     1.50 pt
        - Douchewand                                                  1.00 st     1.25 pt
        - Handdoekenradiator                                          1.00 st     0.75 pt
        - Ingebouwd kastje met in- of opgebouwde wastafel             1.00 st     1.00 pt
        - Kastruimte                                                  1.00 st     0.75 pt
        - Stopcontact bij wastafel                                    1.00 st     0.25 pt
        - Éénhandsmengkraan                                           1.00 st     0.25 pt
        - Thermostatische mengkraan                                   1.00 st     0.50 pt
        - Max verdubbeling punten bad en douche                                  -0.25 pt
                                                                                ------
  Totaal                                                                         13.00 pt
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
          "code": "IKW",
          "naam": "Ingebouwd kastje met in- of opgebouwde wastafel"
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 13.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer",
        "naam": "Badkamer",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
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
        "id": "sanitair__prive__badkamer__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 6.0
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen__bubbelfunctie_van_het_bad",
        "naam": "Bubbelfunctie van het bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
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
        "id": "sanitair__prive__badkamer__extra_voorzieningen__douchewand",
        "naam": "Douchewand",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.25
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen__handdoekenradiator",
        "naam": "Handdoekenradiator",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
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
        "id": "sanitair__prive__badkamer__extra_voorzieningen__ingebouwd_kastje_met_in_of_opgebouwde_wastafel",
        "naam": "Ingebouwd kastje met in- of opgebouwde wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
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
        "id": "sanitair__prive__badkamer__extra_voorzieningen__kastruimte",
        "naam": "Kastruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
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
        "id": "sanitair__prive__badkamer__extra_voorzieningen__stopcontact_bij_wastafel",
        "naam": "Stopcontact bij wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.25
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen__eenhandsmengkraan",
        "naam": "Éénhandsmengkraan",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.25
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__extra_voorzieningen__thermostatische_mengkraan",
        "naam": "Thermostatische mengkraan",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
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
        "id": "sanitair__prive__badkamer__extra_voorzieningen__maximering_punten_voorzieningen",
        "naam": "Max verdubbeling punten bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer__extra_voorzieningen"
        }
      },
      "punten": -0.25
    }
  ]
}
```
