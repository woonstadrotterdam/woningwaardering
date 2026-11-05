# test_vanaf_8_onzelfstandige_woonruimten_geldt_het_wastafelmaximum_niet_voor_een_ruimte[7_woonruimten]

Op een adres met 8 of meer onzelfstandige woonruimten geldt het maximum voor wastafels niet voor één ruimte buiten de badkamer.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.6.1
- wettekst, Bijlage I onder B, onderdeel 6.1

Dit geval: het adres blijft net onder de grens, dus het maximum geldt in elke ruimte buiten de badkamer

## Rapport

```text
SANITAIR
  Privé
    - Badkamer
      - Wastafel                                                      2.00 st     2.00 pt
      - Meerpersoonswastafel                                          2.00 st     3.00 pt
  Gedeeld met 7 onzelfstandige woonruimten
    - Woonkamer1
      - Wastafel                                                      3.00 st     0.43 pt
      - Maximering voor Wastafel                                                 -0.29 pt
      - Meerpersoonswastafel                                          3.00 st     0.64 pt
      - Maximering voor Meerpersoonswastafel                                     -0.43 pt
    - Woonkamer2
      - Wastafel                                                      2.00 st     0.29 pt
      - Maximering voor Wastafel                                                 -0.14 pt
      - Meerpersoonswastafel                                          2.00 st     0.43 pt
      - Maximering voor Meerpersoonswastafel                                     -0.21 pt
  Afronding op kwartpunten                                                        0.03 pt
                                                                                ------
  Totaal                                                                          5.75 pt
```

## Waarschuwingen

Geen.

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
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        }
      ]
    },
    {
      "id": "woonkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer1",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 7
    },
    {
      "id": "woonkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer2",
      "oppervlakte": 10.0,
      "installaties": [
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        },
        {
          "code": "MPW",
          "naam": "Meerpersoonswastafel"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 7
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
  "punten": 5.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "sanitair__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "sanitair__prive__badkamer",
        "naam": "Badkamer",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 2.0
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__prive__badkamer__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__prive__badkamer"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 3.0
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 7 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1",
        "naam": "Woonkamer1",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 3.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.43
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1__max_punten_wastafel",
        "naam": "Maximering voor Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1"
        }
      },
      "punten": -0.29
    },
    {
      "aantal": 3.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.64
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1__max_punten_meerpersoonswastafel",
        "naam": "Maximering voor Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer1"
        }
      },
      "punten": -0.43
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2",
        "naam": "Woonkamer2",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.29
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2__max_punten_wastafel",
        "naam": "Maximering voor Wastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2"
        }
      },
      "punten": -0.14
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2__meerpersoonswastafel",
        "naam": "Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.43
    },
    {
      "criterium": {
        "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2__max_punten_meerpersoonswastafel",
        "naam": "Maximering voor Meerpersoonswastafel",
        "bovenliggendeCriterium": {
          "id": "sanitair__gedeeld_met_7_onzelfstandige_woonruimten__woonkamer2"
        }
      },
      "punten": -0.21
    },
    {
      "criterium": {
        "id": "sanitair__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.03
    }
  ]
}
```
