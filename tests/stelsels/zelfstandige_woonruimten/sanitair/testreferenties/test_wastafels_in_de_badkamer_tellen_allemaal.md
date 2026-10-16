# test_wastafels_in_de_badkamer_tellen_allemaal

In een badkamer geldt geen maximum voor wastafels.

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1; wettekst,
Bijlage I onder A, onderdeel 6.1.

## Rapport

```text
SANITAIR
  Badkamer
    - Wastafel                                                        2.00 st     2.00 pt
    - Meerpersoonswastafel                                            2.00 st     3.00 pt
                                                                                ------
  Totaal                                                                          5.00 pt
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
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
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
  "punten": 5.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__badkamer",
        "naam": "Badkamer"
      }
    },
    {
      "aantal": 2.0,
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
      "punten": 2.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__badkamer__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    }
  ]
}
```
