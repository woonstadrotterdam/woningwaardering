# test_model_zelfstandige_woonruimten[woning_2017_zonder_aanbelfunctie_haalt_110_punten_niet]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Controlegeval bij het aanbelfunctiemodel: dezelfde woning uit 2017 zonder aanbelfunctie komt op 109,75 punten voor de rubrieken 1 tot en met 10 en 12 en krijgt geen minimum van 40 punten voor de WOZ-waarde (implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst, Bijlage I onder A, onderdeel 11.2).

Handberekening, peildatum 1 juli 2026:

| Rubriek            | Input                                                                                    | Punten | Bron         |
| ------------------ | ---------------------------------------------------------------------------------------- | ------ | ------------ |
| 1 Vertrekken       | woonkamer 30 m², slaapkamer 10 m², keuken 6 m², badkamer 4 m²                            | 50     | 2.2.1        |
| 3 Verwarming       | vier verwarmde vertrekken, 2 punten per vertrek                                          | 8      | 2.3          |
| 4 Energieprestatie | label B, meergezinswoning                                                                | 30     | 2.4.4        |
| 5 Keuken           | aanrecht van 1,50 m                                                                      | 4      | 2.5.2        |
| 6 Sanitair         | staand toilet in toiletruimte 3, wastafel in badkamer 1, douche 4                        | 8      | 2.6.1        |
| 8 Buitenruimten    | privé-balkon van 22 m²: 2 + 22 × 0,35 = 9,7, op een kwart punt                           | 9,75   | 2.8.1, 2.1.4 |
| 1 t/m 10           |                                                                                          | 109,75 |              |
| 11.1 WOZ-waarde    | € 180.000, waardepeildatum 1 januari 2025: 180.000 / 16.954 + 180.000 / 50 / 268 = 24,05 | 24     | 2.11.2       |
| 12                 | geen zorgwoning, geen aanbelfunctie of laadpaal                                          | 0      |              |

De rubrieken 1 tot en met 10 en 12 zijn samen 109,75 punten, minder dan 110: geen minimum. Totaal: 109,75 + 24 = 133,75, afgerond 134 punten.

## Rapport

```text
SAMENVATTING woning_2017_zonder_aanbelfunctie_haalt_110_punten_niet
  Oppervlakte van vertrekken                                                     50.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                        8.00 pt
  Buitenruimten                                                                   9.75 pt
  Energieprestatie                                                               30.00 pt
  Keuken                                                                          4.00 pt
  Sanitair                                                                        8.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      24.00 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                134.00 pt
  Maximaal redelijke huur                                           871.06 EUR

OPPERVLAKTE VAN VERTREKKEN
  Woonkamer                                                          30.00 m²
  Slaapkamer                                                         10.00 m²
  Keuken                                                              6.00 m²
  Badkamer                                                            4.00 m²
                                                                    ------      ------
  Totaal                                                             50.00 m²    50.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Woonkamer                                                                   2.00 pt
    - Slaapkamer                                                                  2.00 pt
    - Keuken                                                                      2.00 pt
    - Badkamer                                                                    2.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt

BUITENRUIMTEN
  Privé                                                              22.00 m²     7.70 pt
    - Balkon                                                         22.00 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                          9.75 pt

ENERGIEPRESTATIE
  B                                                                              30.00 pt
                                                                                ------
  Totaal                                                                         30.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              1500.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt

SANITAIR
  Badkamer
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
  Toiletruimte
    - Staand Toilet                                                   1.00 st     3.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2025                       180000.00 EUR
  Onderdeel I                                                                    10.62 pt
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                   13.43 pt
    - Oppervlakte van vertrekken en overige ruimten                  50.00 m²
    - Factor II                                                     268.00 EUR
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                         24.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "woning_2017_zonder_aanbelfunctie_haalt_110_punten_niet",
  "bouwjaar": 2017,
  "adres": {
    "huisnummer": "1",
    "huisnummerToevoeging": "",
    "postcode": "3012CJ",
    "woonplaats": {
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagIdentificatie": "0599010000000001"
  },
  "energieprestaties": [
    {
      "soort": {
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2021-02-23",
      "einddatum": "2031-02-23",
      "label": {
        "code": "B",
        "naam": "B"
      }
    }
  ],
  "gebruiksoppervlakte": 50,
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ],
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 30.0,
      "verwarmd": true,
      "aantal": 1
    },
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "aantal": 1
    },
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
      "oppervlakte": 6.0,
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
          "lengte": 1500.0
        }
      ],
      "verwarmd": true,
      "aantal": 1
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
      "oppervlakte": 4.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Wastafel",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "WAS",
            "naam": "Wastafel"
          }
        },
        {
          "id": "element_2",
          "naam": "Douche",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        }
      ],
      "verwarmd": true,
      "aantal": 1
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
      "oppervlakte": 1.2,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Closetcombinatie",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "CLO",
            "naam": "Closetcombinatie"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "balkon",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 4000.0,
      "hoogte": 2600.0,
      "lengte": 5500.0,
      "oppervlakte": 22.0,
      "aantal": 1
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 180000.0,
      "waardepeildatum": "2025-01-01"
    }
  ]
}
```

## Output

```json
{
  "groepen": [
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OVZ",
          "naam": "Oppervlakte van vertrekken"
        }
      },
      "punten": 50.0,
      "woningwaarderingen": [
        {
          "aantal": 30.0,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__woonkamer",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 10.0,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__slaapkamer",
            "naam": "Slaapkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 6.0,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__keuken",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 4.0,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__badkamer",
            "naam": "Badkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OOZ",
          "naam": "Oppervlakte van overige ruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 8.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__woonkamer",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer",
            "naam": "Slaapkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__keuken",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__badkamer",
            "naam": "Badkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BUI",
          "naam": "Buitenruimten"
        }
      },
      "punten": 9.75,
      "woningwaarderingen": [
        {
          "aantal": 22.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 7.7
        },
        {
          "aantal": 22.0,
          "criterium": {
            "id": "buitenruimten__prive__balkon",
            "naam": "Balkon",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "criterium": {
            "id": "buitenruimten__prive_buitenruimten_aanwezig",
            "naam": "Privé buitenruimten aanwezig"
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "buitenruimten__afronding_op_kwartpunten",
            "naam": "Afronding op kwartpunten"
          },
          "punten": 0.05
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 30.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "B"
          },
          "punten": 30.0
        }
      ]
    },
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
      "punten": 4.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "keuken__keuken",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 1500.0,
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
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "SAN",
          "naam": "Sanitair"
        }
      },
      "punten": 8.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__badkamer",
            "naam": "Badkamer"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__badkamer__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__badkamer"
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
            "id": "sanitair__badkamer__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__badkamer"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 4.0
        },
        {
          "criterium": {
            "id": "sanitair__toiletruimte",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__toiletruimte__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__toiletruimte"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 3.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GPA",
          "naam": "Gemeenschappelijke parkeerruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GVR",
          "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "WOZ",
          "naam": "Punten voor de WOZ-waarde"
        }
      },
      "punten": 24.0,
      "woningwaarderingen": [
        {
          "aantal": 180000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2025",
            "meeteenheid": {
              "code": "EUR",
              "naam": "Euro"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__onderdeel_I",
            "naam": "Onderdeel I"
          },
          "punten": 10.62
        },
        {
          "aantal": 16954.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__onderdeel_I__factor_I",
            "naam": "Factor I",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__onderdeel_I"
            },
            "meeteenheid": {
              "code": "EUR",
              "naam": "Euro"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__onderdeel_II",
            "naam": "Onderdeel II"
          },
          "punten": 13.43
        },
        {
          "aantal": 50.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__onderdeel_II__oppervlakte_vertrekken_en_overige_ruimten",
            "naam": "Oppervlakte van vertrekken en overige ruimten",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__onderdeel_II"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 268.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__onderdeel_II__factor_II",
            "naam": "Factor II",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__onderdeel_II"
            },
            "meeteenheid": {
              "code": "EUR",
              "naam": "Euro"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__afronding_op_kwartpunten",
            "naam": "Afronding op kwartpunten"
          },
          "punten": -0.05
        }
      ]
    },
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
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "PMN",
          "naam": "Prijsopslag monumenten en nieuwbouw"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 871.06,
  "punten": 134.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 871.06
}
```
