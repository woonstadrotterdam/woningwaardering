# test_extra_voorzieningen_krijgen_hooguit_de_punten_van_het_aanrecht[voorzieningen_boven_het_maximum]

Extra voorzieningen krijgen samen hooguit de punten van het aanrecht.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.5.3
- wettekst, Bijlage I onder A, onderdeel 5.2

## Rapport

```text
KEUKEN
  Keuken
    - Lengte aanrecht                                              1000.00 mm     4.00 pt
    - Extra voorzieningen
      - Inbouw koelkast                                               4.00 st     4.00 pt
      - Inbouw oven elektrisch                                        1.00 st     1.00 pt
      - Maximaal evenveel punten als aanrecht                                    -1.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt
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
          "code": "IOE",
          "naam": "Inbouw oven elektrisch"
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 8.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "keuken__keuken",
        "naam": "Keuken"
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "keuken__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken"
        }
      }
    },
    {
      "aantal": 4.0,
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 4.0
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_oven_elektrisch",
        "naam": "Inbouw oven elektrisch",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen__maximering_extra_voorzieningen",
        "naam": "Maximaal evenveel punten als aanrecht",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken__extra_voorzieningen"
        }
      },
      "punten": -1.0
    }
  ]
}
```
