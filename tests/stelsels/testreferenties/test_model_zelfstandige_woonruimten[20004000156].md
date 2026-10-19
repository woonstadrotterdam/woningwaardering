# test_model_zelfstandige_woonruimten[20004000156]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

eenheid van stadswonen

## Rapport

```text
SAMENVATTING 20004000156
  Oppervlakte van vertrekken                                                     80.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                        4.00 pt
  Buitenruimten                                                                  11.75 pt
  Energieprestatie                                                               15.00 pt
  Keuken
  Sanitair                                                                       11.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      35.25 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw                                            50.00 pt
                                                                                ------
  Totaal afgerond op hele punten                                                207.00 pt
  Maximaal redelijke huur                                          1372.24 EUR

OPPERVLAKTE VAN VERTREKKEN
  Badruimte                                                           5.27 m²
  Slaapkamer 1                                                       18.52 m²
  Keuken                                                              4.10 m²
  Woonkamer                                                          43.92 m²
  Slaapkamer 2                                                        7.97 m²
                                                                    ------      ------
  Totaal                                                             79.78 m²    80.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Badruimte                                                                   2.00 pt
    - Slaapkamer 2                                                                2.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt

BUITENRUIMTEN
  Privé                                                              28.00 m²     9.80 pt
    - Balkon 1                                                        7.17 m²
    - Balkon 2                                                       14.99 m²
    - Balkon 3                                                        5.89 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                         11.75 pt

ENERGIEPRESTATIE
  C (Energie-index)                                                              15.00 pt
                                                                                ------
  Totaal                                                                         15.00 pt

SANITAIR
  Badruimte
    - Staand Toilet                                                   1.00 st     2.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
  Toiletruimte
    - Staand Toilet                                                   1.00 st     3.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                         11.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       302000.00 EUR
  Onderdeel I                                                                    19.70 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   15.60 pt
    - Oppervlakte van vertrekken en overige ruimten                  80.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                         35.25 pt

PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Rijksmonument                                                                  50.00 pt
                                                                                ------
  Totaal                                                                         50.00 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (Space_88559330) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor Keuken.
- UserWarning: Eenheid (20004000156) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "id": "20004000156",
  "bouwjaar": 1993,
  "adres": {
    "huisnummer": "",
    "huisnummerToevoeging": "",
    "postcode": "",
    "straatnaam": ""
  },
  "adresseerbaarObjectBasisregistratie": {
    "id": "",
    "bagIdentificatie": ""
  },
  "energieprestaties": [
    {
      "soort": {
        "code": "EI",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2017-03-21",
      "einddatum": "2027-03-21",
      "registratiedatum": "2018-01-31T08:32:39.580000+01:00",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.74"
    }
  ],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
    }
  ],
  "oppervlakten": [],
  "panden": [
    {
      "idExtern": "",
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ],
  "ruimten": [
    {
      "id": "Space_88554482",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 19.9694,
      "oppervlakte": 5.26896,
      "bouwkundigeElementen": [
        {
          "id": "Radiator_88554483",
          "naam": "Radiator",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening algemeen"
          },
          "detailSoort": {
            "code": "RAD",
            "naam": "Radiator"
          }
        },
        {
          "id": "Wastafel_88554484",
          "naam": "Wastafel",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "WAS",
            "naam": "Wastafel"
          }
        },
        {
          "id": "Douche_88554485",
          "naam": "Douche",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        },
        {
          "id": "Closetcombinatie_88554486",
          "naam": "Closetcombinatie",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "CLO",
            "naam": "Closetcombinatie (Toilet)"
          }
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_88554487",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 4.01892,
      "oppervlakte": 1.0604,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88554488",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 70.1937,
      "oppervlakte": 18.5208,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88554489",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 24.1445,
      "oppervlakte": 6.26911,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88554490",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 956.0,
      "hoogte": 3728.0,
      "inhoud": 26.7435,
      "lengte": 7500.0,
      "oppervlakte": 7.1724,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88559327",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 2030.0,
      "hoogte": 3118.0,
      "inhoud": 46.731,
      "lengte": 7382.0,
      "oppervlakte": 14.9869,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88559328",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 811.0,
      "hoogte": 2794.0,
      "inhoud": 16.4526,
      "lengte": 7260.0,
      "oppervlakte": 5.8875,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88559330",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 16.963,
      "oppervlakte": 4.10198,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88559333",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "VID",
        "naam": "Vide"
      },
      "naam": "Vide",
      "inhoud": 11.8862,
      "oppervlakte": 2.87211,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88559334",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 174.15,
      "oppervlakte": 43.9219,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_88559335",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 30.3863,
      "oppervlakte": 7.96514,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_88559336",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 4.7445,
      "oppervlakte": 1.14601,
      "bouwkundigeElementen": [
        {
          "id": "Closetcombinatie_88559337",
          "naam": "Closetcombinatie",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "CLO",
            "naam": "Closetcombinatie (Toilet)"
          }
        },
        {
          "id": "Fontein_88559338",
          "naam": "Fontein",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "FON",
            "naam": "Fontein"
          }
        }
      ],
      "verwarmd": false
    },
    {
      "id": "Space_88559339",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "OVE",
        "naam": "Overloop"
      },
      "naam": "Overloop",
      "inhoud": 8.27235,
      "oppervlakte": 1.99815,
      "bouwkundigeElementen": [],
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 302000.0,
      "waardepeildatum": "2024-01-01"
    },
    {
      "vastgesteldeWaarde": 301000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 277000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 248000.0,
      "waardepeildatum": "2021-01-01"
    },
    {
      "vastgesteldeWaarde": 195000.0,
      "waardepeildatum": "2020-01-01"
    },
    {
      "vastgesteldeWaarde": 166000.0,
      "waardepeildatum": "2019-01-01"
    },
    {
      "vastgesteldeWaarde": 151000.0,
      "waardepeildatum": "2018-01-01"
    },
    {
      "vastgesteldeWaarde": 139000.0,
      "waardepeildatum": "2017-01-01"
    },
    {
      "vastgesteldeWaarde": 133000.0,
      "waardepeildatum": "2016-01-01"
    },
    {
      "vastgesteldeWaarde": 130000.0,
      "waardepeildatum": "2015-01-01"
    },
    {
      "vastgesteldeWaarde": 130000.0,
      "waardepeildatum": "2014-01-01"
    }
  ],
  "datumAfsluitenHuurovereenkomst": "2024-05-29"
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
      "punten": 80.0,
      "woningwaarderingen": [
        {
          "aantal": 5.27,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_88554482",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 18.52,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_88554488",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 4.1,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_88559330",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 43.92,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_88559334",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 7.97,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_88559335",
            "naam": "Slaapkamer 2",
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
      "punten": 4.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_88554482",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_88559335",
            "naam": "Slaapkamer 2",
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
      "punten": 11.75,
      "woningwaarderingen": [
        {
          "aantal": 28.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 9.8
        },
        {
          "aantal": 7.17,
          "criterium": {
            "id": "buitenruimten__prive__Space_88554490",
            "naam": "Balkon 1",
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
          "aantal": 14.99,
          "criterium": {
            "id": "buitenruimten__prive__Space_88559327",
            "naam": "Balkon 2",
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
          "aantal": 5.89,
          "criterium": {
            "id": "buitenruimten__prive__Space_88559328",
            "naam": "Balkon 3",
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
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "C (Energie-index)"
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
          "code": "SAN",
          "naam": "Sanitair"
        }
      },
      "punten": 11.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_88554482",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_88554482__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_88554482"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 2.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_88554482__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_88554482"
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
            "id": "sanitair__Space_88554482__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_88554482"
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
            "id": "sanitair__Space_88559336",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_88559336__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_88559336"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 3.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_88559336__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_88559336"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 1.0
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
      "punten": 35.25,
      "woningwaarderingen": [
        {
          "aantal": 302000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2024",
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
          "punten": 19.7
        },
        {
          "aantal": 15329.0,
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
          "punten": 15.6
        },
        {
          "aantal": 80.0,
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
          "aantal": 242.0,
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
      "punten": 50.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "prijsopslag_monumenten_en_nieuwbouw__rijksmonument",
            "naam": "Rijksmonument"
          },
          "punten": 50.0
        }
      ],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1372.24,
  "punten": 207.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1372.24
}
```
