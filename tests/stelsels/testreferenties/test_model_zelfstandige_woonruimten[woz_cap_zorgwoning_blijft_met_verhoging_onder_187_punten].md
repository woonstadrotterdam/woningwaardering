# test_model_zelfstandige_woonruimten[woz_cap_zorgwoning_blijft_met_verhoging_onder_187_punten]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Controlegeval: zorgwoning die ook met de 35%-verhoging van rubriek 12 onder 187 punten blijft, zodat de cap op de WOZ niet geldt (2.11.7).

## Rapport

```text
SAMENVATTING woz_cap_zorgwoning_blijft_met_verhoging_onder_187_punten
  Oppervlakte van vertrekken                                                     37.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                        8.00 pt
  Buitenruimten                                                                  -5.00 pt
  Energieprestatie                                                               15.00 pt
  Keuken                                                                          4.00 pt
  Sanitair                                                                        8.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen                 3.00 pt
  Punten voor de WOZ-waarde                                                      62.00 pt
  Bijzondere voorzieningen                                                       46.25 pt
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                178.00 pt
  Maximaal redelijke huur                                          1173.15 EUR

OPPERVLAKTE VAN VERTREKKEN
  Woonkamer                                                          17.00 m²
  Slaapkamer                                                         10.00 m²
  Keuken                                                              6.00 m²
  Badkamer                                                            4.00 m²
                                                                    ------      ------
  Totaal                                                             37.00 m²    37.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Woonkamer                                                                   2.00 pt
    - Slaapkamer                                                                  2.00 pt
    - Keuken                                                                      2.00 pt
    - Badkamer                                                                    2.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt

BUITENRUIMTEN
  Geen buitenruimten                                                             -5.00 pt
                                                                                ------
  Totaal                                                                         -5.00 pt

ENERGIEPRESTATIE
  C                                                                              15.00 pt
                                                                                ------
  Totaal                                                                         15.00 pt

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

GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Zorgwoning                                                                      3.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2025                       388000.00 EUR
  Onderdeel I                                                                    22.89 pt
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                   39.13 pt
    - Oppervlakte van vertrekken en overige ruimten                  37.00 m²
    - Factor II                                                     268.00 EUR
  Afronding op kwartpunten                                                       -0.02 pt
                                                                                ------
  Totaal                                                                         62.00 pt

BIJZONDERE VOORZIENINGEN
  Zorgwoning 35% puntenverhoging                                                 46.25 pt
                                                                                ------
  Totaal                                                                         46.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "woz_cap_zorgwoning_blijft_met_verhoging_onder_187_punten",
  "bouwjaar": 2000,
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
  "doelgroep": {
    "code": "ZOR",
    "naam": "Zorg"
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
        "code": "C",
        "naam": "C"
      }
    }
  ],
  "gebruiksoppervlakte": 40,
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
      "oppervlakte": 17.0,
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
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 388000.0,
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
      "punten": 37.0,
      "woningwaarderingen": [
        {
          "aantal": 17.0,
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
      "punten": -5.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "buitenruimten__geen_buitenruimten",
            "naam": "Geen buitenruimten"
          },
          "punten": -5.0
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
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "C"
          },
          "punten": 15.0
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
      "punten": 3.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__zorgwoning",
            "naam": "Zorgwoning"
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
          "code": "WOZ",
          "naam": "Punten voor de WOZ-waarde"
        }
      },
      "punten": 62.0,
      "woningwaarderingen": [
        {
          "aantal": 388000.0,
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
          "punten": 22.89
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
          "punten": 39.13
        },
        {
          "aantal": 37.0,
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
          "punten": -0.02
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
      "punten": 46.25,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "bijzondere_voorzieningen__zorgwoning_puntenverhoging",
            "naam": "Zorgwoning 35% puntenverhoging"
          },
          "punten": 46.25
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
          "code": "PMN",
          "naam": "Prijsopslag monumenten en nieuwbouw"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1173.15,
  "punten": 178.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1173.15
}
```
