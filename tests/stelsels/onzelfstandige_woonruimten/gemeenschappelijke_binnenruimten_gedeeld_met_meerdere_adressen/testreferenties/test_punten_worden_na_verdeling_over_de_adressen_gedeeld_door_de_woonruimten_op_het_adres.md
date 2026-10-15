# test_punten_worden_na_verdeling_over_de_adressen_gedeeld_door_de_woonruimten_op_het_adres

De punten voor een gemeenschappelijke binnenruimte worden na verdeling over de meerdere adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
Bijlage I onder B, toelichting rubriek 9.

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Gedeeld met 4 adressen
      - Oppervlakte van vertrekken                                                1.25 pt
        - Keuken                                                     20.00 m²
      - Oppervlakte van overige ruimten                                           0.09 pt
        - Toiletruimte                                                2.00 m²
      - Verkoeling en verwarming
        - Verwarmde vertrekken
          - Keuken                                                                0.13 pt
      - Keuken
        - Keuken
          - Lengte aanrecht                                        2999.00 mm     0.44 pt
          - Extra voorzieningen
            - Inbouw koelkast                                         1.00 st     0.06 pt
            - Inbouw oven elektrisch                                  1.00 st     0.06 pt
            - Inbouw magnetron                                        1.00 st     0.06 pt
      - Sanitair
        - Toiletruimte
          - Hangend toilet                                            1.00 st     0.23 pt
          - Wastafel                                                  1.00 st     0.06 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          2.50 pt
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
      "oppervlakte": 20.0,
      "gedeeldMetAantalAdressen": 4,
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
          "lengte": 2999.0
        },
        {
          "id": "radiator",
          "naam": "Radiator",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "RAD",
            "naam": "Radiator"
          }
        }
      ],
      "verwarmd": true,
      "installaties": [
        {
          "code": "IMA",
          "naam": "Inbouw magnetron"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IOE",
          "naam": "Inbouw oven elektrisch"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
    },
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
      "oppervlakte": 2.0,
      "gedeeldMetAantalAdressen": 4,
      "installaties": [
        {
          "code": "WAS",
          "naam": "Wastafel"
        },
        {
          "code": "HTO",
          "naam": "Hangend toilet"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 2.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen",
        "naam": "Gedeeld met 4 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen"
        }
      },
      "punten": 1.25
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen"
        }
      },
      "punten": 0.09
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__oppervlakte_van_overige_ruimten__toiletruimte",
        "naam": "Toiletruimte",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.13
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken"
        }
      }
    },
    {
      "aantal": 2999.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 0.44
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.06
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_oven_elektrisch",
        "naam": "Inbouw oven elektrisch",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.06
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_magnetron",
        "naam": "Inbouw magnetron",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.06
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair",
        "naam": "Sanitair",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair__toiletruimte",
        "naam": "Toiletruimte",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair__toiletruimte__hangend_toilet",
        "naam": "Hangend toilet",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair__toiletruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.23
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair__toiletruimte__wastafel",
        "naam": "Wastafel",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_4_adressen__sanitair__toiletruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.06
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
