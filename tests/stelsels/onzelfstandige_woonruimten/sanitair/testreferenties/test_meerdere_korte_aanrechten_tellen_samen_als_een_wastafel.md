# test_meerdere_korte_aanrechten_tellen_samen_als_een_wastafel

Meerdere aanrechten korter dan 1 meter in dezelfde ruimte tellen samen als één wastafel.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.6.1.

## Rapport

```text
SANITAIR
  Privé
    - Keuken
      - Wastafel (spoelbak in aanrecht < 1m)                          1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                          1.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht1",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 800.0
        },
        {
          "id": "aanrecht2",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 900.0
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
  "punten": 1.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "sanitair__prive__keuken__spoelbak_in_aanrecht",
        "naam": "Wastafel (spoelbak in aanrecht < 1m)",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__keuken"
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
