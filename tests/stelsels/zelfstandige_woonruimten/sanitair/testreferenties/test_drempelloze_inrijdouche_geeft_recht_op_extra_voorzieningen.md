# test_drempelloze_inrijdouche_geeft_recht_op_extra_voorzieningen

Een drempelloze inrijdouche maakt van de ruimte een doucheruimte met extra voorzieningen.

Bron: beleidsboek zelfstandige woonruimten, 2.6.1: "Als douche wordt iedere,
door de verhuurder aangebrachte, installatie voor het nemen van een stortbad
geteld."

## Rapport

```text
SANITAIR
  Badkamer
    - Wastafel                                                        1.00 st     1.00 pt
    - Drempelloze inrijdouche                                         1.00 st     4.00 pt
    - Extra voorzieningen
      - Handdoekenradiator                                            1.00 st     0.75 pt
      - Thermostatische mengkraan                                     1.00 st     0.50 pt
                                                                                ------
  Totaal                                                                          6.25 pt
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
          "code": "DRD",
          "naam": "Drempelloze inrijdouche"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "HRA",
          "naam": "Handdoekenradiator"
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 6.25,
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
        "id": "sanitair__badkamer__drempelloze_inrijdouche",
        "naam": "Drempelloze inrijdouche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
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
      "punten": 0.75
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
    }
  ]
}
```
