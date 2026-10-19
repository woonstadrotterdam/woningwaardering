# test_bad_en_douche_in_dezelfde_ruimte_is_een_voorziening

Een bad en een douche in dezelfde ruimte tellen samen als één bad/douche.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.6.1
- wettekst, Bijlage I onder A, toelichting rubriek 6.1

## Rapport

```text
SANITAIR
  Badkamer
    - Bad en douche                                                   1.00 st     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt
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
  "punten": 7.0,
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
      "punten": 7.0
    }
  ]
}
```
