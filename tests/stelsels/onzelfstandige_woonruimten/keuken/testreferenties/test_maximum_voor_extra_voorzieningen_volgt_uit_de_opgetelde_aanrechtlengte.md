# test_maximum_voor_extra_voorzieningen_volgt_uit_de_opgetelde_aanrechtlengte

Bij meer dan één aanrecht volgt het maximum voor extra voorzieningen uit de opgetelde aanrechtlengte.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.5.3.

## Rapport

```text
KEUKEN
  Privé
    - Keuken
      - Totale aanrechtlengte                                      2400.00 mm     7.00 pt
        - Lengte aanrecht                                          1500.00 mm
        - Lengte aanrecht                                           900.00 mm
      - Extra voorzieningen
        - Inbouw koelkast                                             8.00 st     8.00 pt
        - Maximaal evenveel punten als aanrecht                                  -1.00 pt
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
          "id": "aanrecht_1",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1500.0
        },
        {
          "id": "aanrecht_2",
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
      ],
      "installaties": [
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
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
  "punten": 14.0,
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
      "aantal": 2400.0,
      "criterium": {
        "id": "keuken__prive__keuken__subtotaal",
        "naam": "Totale aanrechtlengte",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 7.0
    },
    {
      "aantal": 1500.0,
      "criterium": {
        "id": "keuken__prive__keuken__subtotaal__lengte_aanrecht_aanrecht_1",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken__subtotaal"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      }
    },
    {
      "aantal": 900.0,
      "criterium": {
        "id": "keuken__prive__keuken__subtotaal__lengte_aanrecht_aanrecht_2",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken__subtotaal"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      }
    },
    {
      "criterium": {
        "id": "keuken__prive__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken"
        }
      }
    },
    {
      "aantal": 8.0,
      "criterium": {
        "id": "keuken__prive__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 8.0
    },
    {
      "criterium": {
        "id": "keuken__prive__keuken__extra_voorzieningen__maximering_extra_voorzieningen",
        "naam": "Maximaal evenveel punten als aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__prive__keuken__extra_voorzieningen"
        }
      },
      "punten": -1.0
    }
  ]
}
```
