# test_extra_voorzieningen_zonder_bad_of_douche_krijgen_geen_punten

Extra voorzieningen in een ruimte zonder bad of douche krijgen geen punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.2; wettekst,
Bijlage I onder A, toelichting rubriek 6.2 (via Bijlage I onder B,
toelichting, inleiding).

## Rapport

```text
SANITAIR
  Privé
    - Toiletruimte
      - Hangend toilet                                                1.00 st     3.75 pt
                                                                                ------
  Totaal                                                                          3.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "toiletruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "HTO",
          "naam": "Hangend toilet"
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 3.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__toiletruimte",
        "naam": "Toiletruimte",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__toiletruimte__hangend_toilet",
        "naam": "Hangend toilet",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__toiletruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.75
    }
  ]
}
```
