# test_bad_douche_naast_los_bad_en_losse_douche_zijn_twee_voorzieningen

Een bad/douche naast een los bad en een losse douche telt als twee keer bad/douche.

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1.

## Rapport

```text
SANITAIR
  Badkamer
    - Bad en douche                                                   2.00 st    14.00 pt
                                                                                ------
  Totaal                                                                         14.00 pt
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
          "code": "BDO",
          "naam": "Bad en douche"
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
  "punten": 14.0,
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
      "punten": 14.0
    }
  ]
}
```
