# test_verwarmde_overige_ruimten_en_verkeersruimten_delen_het_maximum_van_4_punten

Verwarmde overige ruimten en verkeersruimten krijgen samen hooguit 4 punten.

Bron: wettekst, Bijlage I onder A, rubriek 3: "verwarming per overige ruimte
en verkeersruimte 1 punt (maximaal 4 punten)".

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde overige en verkeersruimten
    - Berging1                                                                    1.00 pt
    - Berging2                                                                    1.00 pt
    - Berging3                                                                    1.00 pt
    - Gang1                                                                       1.00 pt
    - Gang2                                                                       1.00 pt
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
      "id": "gang1",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang1",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "gang2",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang2",
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
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__gang1",
        "naam": "Gang1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__gang2",
        "naam": "Gang2",
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
