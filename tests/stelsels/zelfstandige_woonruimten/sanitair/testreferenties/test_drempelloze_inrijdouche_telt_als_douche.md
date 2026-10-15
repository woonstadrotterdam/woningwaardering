# test_drempelloze_inrijdouche_telt_als_douche

Een drempelloze inrijdouche telt als een gewone douche.

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1; wettekst,
Bijlage I onder A, toelichting rubriek 6.1.

## Rapport

```text
SANITAIR
  Badkamer1
    - Drempelloze inrijdouche                                         1.00 st     4.00 pt
  Badkamer2
    - Bad en douche                                                   1.00 st     7.00 pt
  Badkamer3
    - Douche                                                          1.00 st     4.00 pt
    - Drempelloze inrijdouche                                         1.00 st     4.00 pt
  Badkamer4
    - Bad en douche                                                   1.00 st     7.00 pt
    - Drempelloze inrijdouche                                         1.00 st     4.00 pt
  Badkamer5
    - Bad en douche                                                   1.00 st     7.00 pt
    - Bad                                                             1.00 st     6.00 pt
                                                                                ------
  Totaal                                                                         43.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "badkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer1",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "DRD",
          "naam": "Drempelloze inrijdouche"
        }
      ]
    },
    {
      "id": "badkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer2",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "DRD",
          "naam": "Drempelloze inrijdouche"
        },
        {
          "code": "BAD",
          "naam": "Bad"
        }
      ]
    },
    {
      "id": "badkamer3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer3",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "DRD",
          "naam": "Drempelloze inrijdouche"
        },
        {
          "code": "DOU",
          "naam": "Douche"
        }
      ]
    },
    {
      "id": "badkamer4",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer4",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "DRD",
          "naam": "Drempelloze inrijdouche"
        },
        {
          "code": "BAD",
          "naam": "Bad"
        },
        {
          "code": "DOU",
          "naam": "Douche"
        }
      ]
    },
    {
      "id": "badkamer5",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badkamer"
      },
      "naam": "Badkamer5",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "DRD",
          "naam": "Drempelloze inrijdouche"
        },
        {
          "code": "BAD",
          "naam": "Bad"
        },
        {
          "code": "BAD",
          "naam": "Bad"
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
  "punten": 43.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__badkamer1",
        "naam": "Badkamer1"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer1__drempelloze_inrijdouche",
        "naam": "Drempelloze inrijdouche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer1"
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
        "id": "sanitair__badkamer2",
        "naam": "Badkamer2"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer2__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer2"
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
        "id": "sanitair__badkamer3",
        "naam": "Badkamer3"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer3__douche",
        "naam": "Douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer3"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer3__drempelloze_inrijdouche",
        "naam": "Drempelloze inrijdouche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer3"
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
        "id": "sanitair__badkamer4",
        "naam": "Badkamer4"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer4__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer4"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 7.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer4__drempelloze_inrijdouche",
        "naam": "Drempelloze inrijdouche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer4"
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
        "id": "sanitair__badkamer5",
        "naam": "Badkamer5"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer5__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer5"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 7.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer5__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer5"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 6.0
    }
  ]
}
```
