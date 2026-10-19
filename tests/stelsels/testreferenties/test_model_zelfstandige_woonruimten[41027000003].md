# test_model_zelfstandige_woonruimten[41027000003]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Trappenhuisflat

## Rapport

```text
SAMENVATTING 41027000003
  Oppervlakte van vertrekken                                                     43.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                       10.00 pt
  Buitenruimten                                                                   3.50 pt
  Energieprestatie                                                               -4.00 pt
  Keuken                                                                          4.00 pt
  Sanitair                                                                        9.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      41.50 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                107.00 pt
  Maximaal redelijke huur                                           685.70 EUR

OPPERVLAKTE VAN VERTREKKEN
  Badruimte                                                           2.18 m²
  Slaapkamer 1 (+1 kast)                                             12.10 m²
  Woonkamer (+1 kast)                                                16.65 m²
  Keuken (+1 kast)                                                    4.84 m²
  Slaapkamer 2 (+2 kasten)                                            6.84 m²
                                                                    ------      ------
  Totaal                                                             42.61 m²    43.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Badruimte                                                                   2.00 pt
    - Slaapkamer 1                                                                2.00 pt
    - Woonkamer                                                                   2.00 pt
    - Keuken                                                                      2.00 pt
    - Slaapkamer 2                                                                2.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt

BUITENRUIMTEN
  Privé                                                               4.00 m²     1.40 pt
    - Balkon                                                          3.93 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Afronding op kwartpunten                                                        0.10 pt
                                                                                ------
  Totaal                                                                          3.50 pt

ENERGIEPRESTATIE
  E (Energie-index)                                                              -4.00 pt
                                                                                ------
  Totaal                                                                         -4.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              1833.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt

SANITAIR
  Badruimte
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
  Toiletruimte
    - Staand Toilet                                                   1.00 st     3.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                          9.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       258000.00 EUR
  Onderdeel I                                                                    16.83 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   24.79 pt
    - Oppervlakte van vertrekken en overige ruimten                  43.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.12 pt
                                                                                ------
  Totaal                                                                         41.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "41027000003",
  "bouwjaar": 1948,
  "adres": {
    "huisnummer": "",
    "huisnummerToevoeging": "d",
    "postcode": "",
    "straatnaam": "",
    "woonplaats": {
      "naam": "ROTTERDAM"
    }
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
      "begindatum": "2019-09-19",
      "einddatum": "2029-09-19",
      "registratiedatum": "2020-01-31T12:13:24+01:00",
      "label": {
        "code": "E",
        "naam": "E"
      },
      "waarde": "2.26"
    }
  ],
  "gebruiksoppervlakte": 53,
  "klimaatbeheersing": [
    {
      "code": "IND",
      "naam": "Individueel"
    }
  ],
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
      "id": "Space_82953220",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.668949,
      "oppervlakte": 0.245937,
      "verwarmd": false
    },
    {
      "id": "Space_82952999",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 5.94318,
      "oppervlakte": 2.18499,
      "bouwkundigeElementen": [
        {
          "id": "Douche_82953001",
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
          "id": "Wastafel_82953002",
          "naam": "Wastafel",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "WAS",
            "naam": "Wastafel/Fontein"
          }
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82953785",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.827645,
      "oppervlakte": 0.304281,
      "verwarmd": false
    },
    {
      "id": "Space_82953240",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.632336,
      "oppervlakte": 0.232476,
      "verwarmd": false
    },
    {
      "id": "Space_82952526",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "inhoud": 16.1738,
      "oppervlakte": 5.94624,
      "verbondenRuimten": [
        {
          "id": "Space_82953804",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "TEC",
            "naam": "Technische ruimte"
          },
          "naam": "Technische ruimte",
          "inhoud": 1.26638,
          "oppervlakte": 0.465581,
          "bouwkundigeElementen": [
            {
              "id": "Ketel_82953811",
              "naam": "Ketel",
              "soort": {
                "code": "VER",
                "naam": "Verwarming"
              },
              "detailSoort": {
                "code": "VTO",
                "naam": "Verwarmingstoestellen"
              }
            }
          ],
          "verwarmd": false
        }
      ],
      "verwarmd": false
    },
    {
      "id": "Space_82953212",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.947933,
      "oppervlakte": 0.348505,
      "verwarmd": false
    },
    {
      "id": "Space_82952503",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 31.2036,
      "oppervlakte": 11.4719,
      "verbondenRuimten": [
        {
          "id": "Space_82953226",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 1.69956,
          "oppervlakte": 0.624839,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82953804",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TEC",
        "naam": "Technische ruimte"
      },
      "naam": "Technische ruimte",
      "inhoud": 1.26638,
      "oppervlakte": 0.465581,
      "bouwkundigeElementen": [
        {
          "id": "Ketel_82953811",
          "naam": "Ketel",
          "soort": {
            "code": "VER",
            "naam": "Verwarming"
          },
          "detailSoort": {
            "code": "VTO",
            "naam": "Verwarmingstoestellen"
          }
        }
      ],
      "verwarmd": false
    },
    {
      "id": "Space_82954115",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 2770.0,
      "hoogte": 2720.0,
      "inhoud": 10.6918,
      "lengte": 1420.0,
      "oppervlakte": 3.93079,
      "verwarmd": false
    },
    {
      "id": "Space_82953226",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 1.69956,
      "oppervlakte": 0.624839,
      "verwarmd": false
    },
    {
      "id": "Space_82953233",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 1.18857,
      "oppervlakte": 0.436976,
      "verwarmd": false
    },
    {
      "id": "Space_82956183",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.491232,
      "oppervlakte": 0.1806,
      "verwarmd": false
    },
    {
      "id": "Space_82952020",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 44.6234,
      "oppervlakte": 16.4057,
      "verbondenRuimten": [
        {
          "id": "Space_82953220",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.668949,
          "oppervlakte": 0.245937,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82953205",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.94962,
      "oppervlakte": 0.349125,
      "verwarmd": false
    },
    {
      "id": "Space_82953003",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 2.5885,
      "oppervlakte": 0.951653,
      "bouwkundigeElementen": [
        {
          "id": "Fontein_82953005",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "WAS",
            "naam": "Wastafel/Fontein"
          }
        },
        {
          "id": "Closetcombinatie_82953004",
          "naam": "Closetcombinatie",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "CLO",
            "naam": "Toilet"
          }
        }
      ],
      "verwarmd": false
    },
    {
      "id": "Space_82952732",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 12.5475,
      "oppervlakte": 4.60749,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_82952743",
          "naam": "Aanrecht",
          "omschrijving": "Aanrecht in Keuken",
          "soort": {
            "code": "KEU",
            "naam": "Keuken voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1833.0
        }
      ],
      "verbondenRuimten": [
        {
          "id": "Space_82953240",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.632336,
          "oppervlakte": 0.232476,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82952514",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 16.694,
      "oppervlakte": 6.13751,
      "verbondenRuimten": [
        {
          "id": "Space_82953212",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.947933,
          "oppervlakte": 0.348505,
          "verwarmd": false
        },
        {
          "id": "Space_82953205",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.94962,
          "oppervlakte": 0.349125,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 242000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 244000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 258000.0,
      "waardepeildatum": "2024-01-01"
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
      "punten": 43.0,
      "woningwaarderingen": [
        {
          "aantal": 2.18,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82952999",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 12.1,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82952503",
            "naam": "Slaapkamer 1 (+1 kast)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 16.65,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82952020",
            "naam": "Woonkamer (+1 kast)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 4.84,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82952732",
            "naam": "Keuken (+1 kast)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 6.84,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82952514",
            "naam": "Slaapkamer 2 (+2 kasten)",
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
      "punten": 10.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82952999",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82952503",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82952020",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82952732",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82952514",
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
      "punten": 3.5,
      "woningwaarderingen": [
        {
          "aantal": 4.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 1.4
        },
        {
          "aantal": 3.93,
          "criterium": {
            "id": "buitenruimten__prive__Space_82954115",
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
          "punten": 0.1
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
      "punten": -4.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "E (Energie-index)"
          },
          "punten": -4.0
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
            "id": "keuken__Space_82952732",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 1833.0,
          "criterium": {
            "id": "keuken__Space_82952732__lengte_aanrecht_Aanrecht_82952743",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_82952732"
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
      "punten": 9.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_82952999",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_82952999__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82952999"
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
            "id": "sanitair__Space_82952999__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82952999"
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
            "id": "sanitair__Space_82953003",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_82953003__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82953003"
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
            "id": "sanitair__Space_82953003__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82953003"
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
      "punten": 41.5,
      "woningwaarderingen": [
        {
          "aantal": 258000.0,
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
          "punten": 16.83
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
          "punten": 24.79
        },
        {
          "aantal": 43.0,
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
          "punten": -0.12
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
  "maximaleHuur": 685.7,
  "punten": 107.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 685.7
}
```
