# test_punten_voor_bad_en_douche

Een douche krijgt 4 punten, een bad 6 punten en een bad/douche 7 punten.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.6.1
- wettekst, Bijlage I onder A, onderdeel 6.1

## Rapport

```text
SANITAIR
  Badkamer1
    - Douche                                                          1.00 st     4.00 pt
  Badkamer2
    - Bad                                                             1.00 st     6.00 pt
  Badkamer3
    - Bad en douche                                                   1.00 st     7.00 pt
                                                                                ------
  Totaal                                                                         17.00 pt
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
          "code": "DOU",
          "naam": "Douche"
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
          "code": "BDO",
          "naam": "Bad en douche"
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
  "punten": 17.0,
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
        "id": "sanitair__badkamer1__douche",
        "naam": "Douche",
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
        "id": "sanitair__badkamer2__bad",
        "naam": "Bad",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer2"
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
        "id": "sanitair__badkamer3",
        "naam": "Badkamer3"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__badkamer3__bad_en_douche",
        "naam": "Bad en douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer3"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 7.0
    }
  ]
}
```
