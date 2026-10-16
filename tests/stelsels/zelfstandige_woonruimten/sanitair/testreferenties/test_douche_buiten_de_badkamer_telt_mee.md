# test_douche_buiten_de_badkamer_telt_mee

Een douche telt ook mee buiten de badkamer.

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.

## Rapport

```text
SANITAIR
  Slaapkamer
    - Douche                                                          1.00 st     4.00 pt
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
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.0,
      "installaties": [
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
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__slaapkamer",
        "naam": "Slaapkamer"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__slaapkamer__douche",
        "naam": "Douche",
        "bovenliggendeCriterium": {
          "id": "sanitair__slaapkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    }
  ]
}
```
