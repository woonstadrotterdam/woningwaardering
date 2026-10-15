# test_verwarmde_overige_ruimten_krijgen_samen_hooguit_4_punten

Verwarmde overige ruimten krijgen samen hooguit 4 punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.3; wettekst,
Bijlage I onder A, onderdeel 3.

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde overige en verkeersruimten
    - Berging1                                                                    1.00 pt
    - Berging2                                                                    1.00 pt
    - Berging3                                                                    1.00 pt
    - Berging4                                                                    1.00 pt
    - Berging5                                                                    1.00 pt
    - Maximaal 4 punten                                                          -1.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging1",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "berging2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging2",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "berging3",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging3",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "berging4",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging4",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "berging5",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging5",
      "oppervlakte": 10.0,
      "verwarmd": true
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
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging1",
        "naam": "Berging1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging2",
        "naam": "Berging2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging3",
        "naam": "Berging3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging4",
        "naam": "Berging4",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging5",
        "naam": "Berging5",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__max_aantal_punten",
        "naam": "Maximaal 4 punten",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": -1.0
    }
  ]
}
```
