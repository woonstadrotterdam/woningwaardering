# test_rekenvoorbeeld_met_keuken_en_toilet_uit_de_wettekst

Het rekenvoorbeeld uit de wettekst: een keuken van 20 m² en een toilet van 2 m² die vier adressen delen, geven een van de vier onzelfstandige woonruimten op een adres 2,50 punten.

Bron: wettekst, Bijlage I onder B, toelichting rubriek 9: "(A) een
gemeenschappelijke binnenruimte met keuken van 20 m², en daarnaast (B) een
gedeeld toilet van 2 m². Tot beiden hebben vier adressen toegang. Op één
van deze adressen zijn vier onzelfstandige woonruimten. Vertrek A voldoet
aan de eisen van een vertrek en wordt gewaardeerd met 20 m² x 1 punt (= 20
punten) conform rubriek 1. Ruimte B voldoet aan de eisen van een overige
ruimte en wordt gewaardeerd met 2 m² x 0,75 punten (= 1,5 punt) conform
rubriek 2. Vertrek A is verwarmd middels een radiator en krijgt daarvoor 2
punten conform rubriek 3. Het toilet is onverwarmd en ontvangt daarvoor
geen punten. In vertrek A wordt voldaan aan de minimumeisen van een keuken
conform rubriek 5. Voor deze rubriek wordt 10 punten toegekend (7 voor het
aanrecht, en 3 voor de voorzieningen). De toiletruimte B krijgt 4,75 punt
(3,75 voor het hangend toilet en 1 voor de wastafel). Saldering levert op:
20 + 1,5 + 2 + 10 + 4,75 = 38,25 punten. Delen door het aantal adressen
levert op: 38,25 punten / 4 = 9,5625 punten per adres. Vervolgens wordt
gedeeld door het aantal onzelfstandige woonruimten op het adres, dus
9,5625/4 = 2,390625 punten per onzelfstandige woonruimte. Afronden
geschiedt op een kwart punt per onzelfstandige woonruimte op 2,50 punten."

De 7 punten voor het aanrecht zijn in de input een aanrecht van 2.999 mm,
de 3 punten voor de voorzieningen een inbouwkoelkast, een elektrische
inbouwoven en een inbouwmagnetron.

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "2 tot 3 m 7 punten".

Bron: wettekst, Bijlage I onder B, onderdeel 5.2: "Inbouw koelkast 1 punt",
"Inbouw oven elektrisch 1 punt" en "Inbouw magnetron 1 punt".

De radiator is in de input een bouwkundig element van de keuken. De package
leest de verwarming af aan `verwarmd`.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3: "Daarom
hebben wij `verwarmd` en `verkoeld` als boolean-kenmerken van een
`EenhedenRuimte` toegevoegd."

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
