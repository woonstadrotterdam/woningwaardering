# test_laadpaal_bij_een_garage_van_een_adres_krijgt_2_punten

Een laadpaal bij een garage van één adres krijgt 2 punten.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3; wettekst,
Bijlage I onder A, onderdeel 12.

Een garage van één adres krijgt in rubriek 10 geen punten; de laadpalen
worden daarom in deze rubriek gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.12.3; wettekst,
Bijlage I onder A, toelichting rubriek 10.

## Rapport

```text
BIJZONDERE VOORZIENINGEN
  Privé
    - Laadpalen                                                       2.00 st     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "2 laadpalen",
  "ruimten": [
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
      "oppervlakte": 19.1488,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        },
        {
          "id": "element_2",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "verwarmd": true,
      "verkoeld": false
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
      "code": "BIJ",
      "naam": "Bijzondere voorzieningen"
    }
  },
  "punten": 4.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "bijzondere_voorzieningen__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "bijzondere_voorzieningen__prive__laadpalen",
        "naam": "Laadpalen",
        "bovenliggendeCriterium": {
          "id": "bijzondere_voorzieningen__prive"
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
