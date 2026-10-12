# test_douche_buiten_de_badkamer_telt_mee

Een douche in een slaapkamer krijgt dezelfde punten als in een badkamer.

Bron: beleidsboek zelfstandige woonruimten, 2.6: "De waardering van sanitair
is niet beperkt tot de badkamer en toiletruimte, maar kan ook gaan over
sanitaire voorzieningen in andere ruimten. Bijvoorbeeld een douche in een
woon- of slaapkamer."

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
