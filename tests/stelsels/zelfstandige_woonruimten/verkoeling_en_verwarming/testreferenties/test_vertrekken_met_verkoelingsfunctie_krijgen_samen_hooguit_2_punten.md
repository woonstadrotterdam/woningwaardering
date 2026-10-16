# test_vertrekken_met_verkoelingsfunctie_krijgen_samen_hooguit_2_punten

Vertrekken met verkoelingsfunctie krijgen daarvoor samen hooguit 2 punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.3.3;
wettekst, Bijlage I onder A, onderdeel 3.

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Slaapkamer1                                                                 2.00 pt
    - Slaapkamer2                                                                 2.00 pt
    - Slaapkamer3                                                                 2.00 pt
  Verkoelde vertrekken
    - Slaapkamer1                                                                 1.00 pt
    - Slaapkamer2                                                                 1.00 pt
    - Slaapkamer3                                                                 1.00 pt
    - Maximaal 2 punten                                                          -1.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true
    },
    {
      "id": "slaapkamer3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer3",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 8.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer3",
        "naam": "Slaapkamer3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken",
        "naam": "Verkoelde vertrekken"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken__slaapkamer3",
        "naam": "Slaapkamer3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken__max_aantal_punten",
        "naam": "Maximaal 2 punten",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": -1.0
    }
  ]
}
```
