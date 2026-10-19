# test_drempelloze_inrijdouche_geeft_recht_op_extra_voorzieningen

Een drempelloze inrijdouche telt als douche voor het recht op extra voorzieningen.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.6.2
- wettekst, Bijlage I onder A, toelichting rubriek 6.2 (via Bijlage I onder B, toelichting, inleiding)

Een drempelloze inrijdouche telt als douche.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.6.1
- wettekst, Bijlage I onder A, toelichting rubriek 6.1 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
SANITAIR
  Privé
    - Badkamer
      - Wastafel                                                      1.00 st     1.00 pt
      - Drempelloze inrijdouche                                       1.00 st     3.00 pt
      - Extra voorzieningen
        - Handdoekenradiator                                          1.00 st     0.75 pt
        - Thermostatische mengkraan                                   1.00 st     0.50 pt
                                                                                ------
  Totaal                                                                          5.25 pt
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 5.25,
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
        "id": "sanitair__prive__badkamer__drempelloze_inrijdouche",
        "naam": "Drempelloze inrijdouche",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
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
    }
  ]
}
```
