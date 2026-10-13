# test_aanrecht_van_5500mm_krijgt_10_punten_in_een_privekeuken

Een aanrecht van 5,5 meter krijgt in een privékeuken 10 punten.

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "3 m en meer 10 punten"
en "5 m en meer (indien er minimaal 8 onzelfstandige woonruimten toegang en
gebruiksrecht hebben tot deze keuken) 13 punten".

## Rapport

```text
KEUKEN
  Privé
    - Keuken
      - Lengte aanrecht                                            5500.00 mm    10.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt
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
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 5500.0
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 10.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "keuken__prive__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "keuken__prive"
        }
      }
    },
    {
      "aantal": 5500.0,
      "criterium": {
        "id": "keuken__prive__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 10.0
    }
  ]
}
```
