# test_extra_voorzieningen_zonder_bad_of_douche_krijgen_geen_punten

Extra voorzieningen tellen alleen in een ruimte met een bad of een douche.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.6.2
- wettekst, Bijlage I onder A, toelichting rubriek 6.2

## Rapport

```text
SANITAIR
  Badkamer
    - Wastafel                                                        1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                          1.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Badkamer' (badkamer): geen bad of douche aanwezig in Badkamer, extra voorzieningen worden niet gewaardeerd.

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
          "code": "BUB",
          "naam": "Bubbelfunctie van het bad"
        },
        {
          "code": "DOW",
          "naam": "Douchewand"
        },
        {
          "code": "HRA",
          "naam": "Handdoekenradiator"
        },
        {
          "code": "KAS",
          "naam": "Kastruimte"
        },
        {
          "code": "KAS",
          "naam": "Kastruimte"
        },
        {
          "code": "STW",
          "naam": "Stopcontact bij wastafel"
        },
        {
          "code": "EHM",
          "naam": "Éénhandsmengkraan"
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
  "punten": 1.0,
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
    }
  ]
}
```
