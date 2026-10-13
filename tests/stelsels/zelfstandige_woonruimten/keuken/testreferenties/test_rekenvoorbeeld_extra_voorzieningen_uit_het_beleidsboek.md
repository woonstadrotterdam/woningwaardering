# test_rekenvoorbeeld_extra_voorzieningen_uit_het_beleidsboek

Het rekenvoorbeeld van het beleidsboek: de extra voorzieningen worden afgetopt op de punten van het aanrecht.

Bron: beleidsboek zelfstandige woonruimten, 2.5.3: "Voor deze extra
voorzieningen zou 4,5 punt gekregen kunnen worden. Maar omdat voor het
aanrechtblad 4 punten zijn toegekend, wordt het aantal punten voor de extra
voorzieningen afgetopt (gemaximeerd) op 4 punten. Deze keuken krijgt in
totaal dus 8 punten."

## Rapport

```text
KEUKEN
  Keuken
    - Lengte aanrecht                                              1600.00 mm     4.00 pt
    - Extra voorzieningen
      - Inbouw afzuiginstallatie                                      1.00 st     0.75 pt
      - Inbouw kookplaat inductie                                     1.00 st     1.75 pt
      - Inbouw koelkast                                               1.00 st     1.00 pt
      - Inbouw oven elektrisch                                        1.00 st     1.00 pt
      - Maximaal evenveel punten als aanrecht                                    -0.50 pt
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
          "lengte": 1600.0
        }
      ],
      "installaties": [
        {
          "code": "IKI",
          "naam": "Inbouw kookplaat inductie"
        },
        {
          "code": "IAF",
          "naam": "Inbouw afzuiginstallatie"
        },
        {
          "code": "IOE",
          "naam": "Inbouw oven elektrisch"
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
      "aantal": 1600.0,
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
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_afzuiginstallatie",
        "naam": "Inbouw afzuiginstallatie",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.75
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_kookplaat_inductie",
        "naam": "Inbouw kookplaat inductie",
        "bovenliggendeCriterium": {
          "id": "keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 1.75
    },
    {
      "aantal": 1.0,
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
      "punten": 1.0
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
      "punten": -0.5
    }
  ]
}
```
