# test_extra_voorzieningen_in_een_ruimte_zonder_aanrecht_krijgen_geen_punten[privekeuken]

Extra voorzieningen in een ruimte zonder aanrecht krijgen geen punten.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.5.1
- wettekst, Bijlage I onder A, toelichting rubriek 5 (via Bijlage I onder B, toelichting, inleiding)

## Rapport

```text
KEUKEN
  Privé
    - Keuken
      - Lengte aanrecht                                            1000.00 mm     4.00 pt
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
          "lengte": 1000.0
        }
      ]
    },
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
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
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
  "punten": 4.0,
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
      "aantal": 1000.0,
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
      "punten": 4.0
    }
  ]
}
```
