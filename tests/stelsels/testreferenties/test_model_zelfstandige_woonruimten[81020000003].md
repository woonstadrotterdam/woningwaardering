# test_model_zelfstandige_woonruimten[81020000003]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Eengezinswoning

## Rapport

```text
SAMENVATTING 81020000003
  Oppervlakte van vertrekken                                                     80.00 pt
  Oppervlakte van overige ruimten                                                 3.75 pt
  Verkoeling en verwarming                                                       13.00 pt
  Buitenruimten                                                                  15.00 pt
  Energieprestatie                                                               52.00 pt
  Keuken                                                                          4.00 pt
  Sanitair                                                                       11.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      41.50 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                220.00 pt
  Maximaal redelijke huur                                          1461.49 EUR

OPPERVLAKTE VAN VERTREKKEN
  Badruimte                                                           4.80 m²
  Slaapkamer 1                                                       15.74 m²
  Keuken                                                              5.92 m²
  Slaapkamer 2                                                       15.15 m²
  Woonkamer (+1 kast)                                                26.54 m²
  Slaapkamer 3                                                       12.23 m²
                                                                    ------      ------
  Totaal                                                             80.38 m²    80.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Berging                                                             5.19 m²
                                                                    ------      ------
  Totaal                                                              5.19 m²     3.75 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Badruimte                                                                   2.00 pt
    - Slaapkamer 1                                                                2.00 pt
    - Keuken                                                                      2.00 pt
    - Slaapkamer 2                                                                2.00 pt
    - Woonkamer                                                                   2.00 pt
    - Slaapkamer 3                                                                2.00 pt
  Verwarmde overige en verkeersruimten
    - Hal                                                                         1.00 pt
                                                                                ------
  Totaal                                                                         13.00 pt

BUITENRUIMTEN
  Privé                                                              54.00 m²    18.90 pt
    - Tuin                                                           53.58 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Maximaal 15 punten                                                             -5.90 pt
                                                                                ------
  Totaal                                                                         15.00 pt

ENERGIEPRESTATIE
  A -> A++ (Energie-index)                                                       52.00 pt
                                                                                ------
  Totaal                                                                         52.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              1800.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt

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
  WOZ-waarde op waardepeildatum 01-01-2024                       367000.00 EUR
  Onderdeel I                                                                    23.94 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   17.63 pt
    - Oppervlakte van vertrekken en overige ruimten                  86.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.07 pt
                                                                                ------
  Totaal                                                                         41.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "81020000003",
  "bouwjaar": 1923,
  "adres": {
    "huisnummer": "",
    "huisnummerToevoeging": "b",
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
      "begindatum": "2017-09-29",
      "einddatum": "2027-09-29",
      "registratiedatum": "2017-10-01T10:55:54.577000+02:00",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "0.33"
    }
  ],
  "gebruiksoppervlakte": 100,
  "klimaatbeheersing": [
    {
      "code": "COL",
      "naam": "Collectief"
    }
  ],
  "monumenten": [],
  "panden": [
    {
      "soort": {
        "code": "EGW",
        "naam": "Eengezinswoning"
      }
    }
  ],
  "ruimten": [
    {
      "id": "Space_57363513",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 6.07616,
      "oppervlakte": 3.04095,
      "verwarmd": false
    },
    {
      "id": "Space_57358391",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 12.5634,
      "oppervlakte": 4.7952,
      "bouwkundigeElementen": [
        {
          "id": "Douche_57358399",
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
          "id": "Wastafel_57358397",
          "naam": "Wastafel",
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
          "id": "Closetcombinatie_57358395",
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
      "verwarmd": true
    },
    {
      "id": "Space_57363515",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.11125,
      "oppervlakte": 0.125,
      "verwarmd": false
    },
    {
      "id": "Space_57358401",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 8.42276,
      "oppervlakte": 2.9195,
      "verwarmd": false
    },
    {
      "id": "Space_57349838",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.165259,
      "oppervlakte": 0.062362,
      "verwarmd": false
    },
    {
      "id": "Space_57351371",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "breedte": 5070.0,
      "hoogte": 2915.0,
      "inhoud": 156.194,
      "lengte": 11740.0,
      "oppervlakte": 53.5828,
      "verwarmd": false
    },
    {
      "id": "Space_57358406",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.3275,
      "oppervlakte": 0.125,
      "verwarmd": false
    },
    {
      "id": "Space_57349819",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 3.32571,
      "oppervlakte": 1.25499,
      "bouwkundigeElementen": [
        {
          "id": "Fontein_57349824",
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
          "id": "Closetcombinatie_57349822",
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
      "id": "Space_57363510",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 34.8061,
      "oppervlakte": 15.7365,
      "verwarmd": true
    },
    {
      "id": "Space_57349825",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 15.6978,
      "oppervlakte": 5.9237,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_57349829",
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
          "lengte": 1800.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_57349808",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 3.62043,
      "oppervlakte": 1.242,
      "verwarmd": false
    },
    {
      "id": "Space_57351351",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "inhoud": 12.2548,
      "oppervlakte": 5.19273,
      "verwarmd": false
    },
    {
      "id": "Space_57363512",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "OVE",
        "naam": "Overloop"
      },
      "naam": "Overloop",
      "inhoud": 19.9283,
      "oppervlakte": 8.94465,
      "verwarmd": false
    },
    {
      "id": "Space_57358381",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 39.6909,
      "oppervlakte": 15.1492,
      "verwarmd": true
    },
    {
      "id": "Space_57349813",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 67.0453,
      "oppervlakte": 25.3001,
      "verbondenRuimten": [
        {
          "id": "Space_57349808",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 3.62043,
          "oppervlakte": 1.242,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_57363951",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.480087,
      "oppervlakte": 0.21,
      "verwarmd": false
    },
    {
      "id": "Space_57349834",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "inhoud": 8.41705,
      "oppervlakte": 3.17625,
      "verwarmd": true
    },
    {
      "id": "Space_57364049",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 6.43338,
      "oppervlakte": 11.0352,
      "verwarmd": false
    },
    {
      "id": "Space_57358403",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang",
      "inhoud": 9.01542,
      "oppervlakte": 3.441,
      "verwarmd": false
    },
    {
      "id": "Space_57349831",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.841269,
      "oppervlakte": 0.31746,
      "verwarmd": false
    },
    {
      "id": "Space_57358387",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 32.0531,
      "oppervlakte": 12.234,
      "verwarmd": true
    },
    {
      "id": "Space_57349811",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 4.68401,
      "oppervlakte": 1.61275,
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 347000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 349000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 367000.0,
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
      "punten": 80.0,
      "woningwaarderingen": [
        {
          "aantal": 4.8,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57358391",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.74,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57363510",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 5.92,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57349825",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.15,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57358381",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 26.54,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57349813",
            "naam": "Woonkamer (+1 kast)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 12.23,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57358387",
            "naam": "Slaapkamer 3",
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
      "punten": 3.75,
      "woningwaarderingen": [
        {
          "aantal": 5.19,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_57351351",
            "naam": "Berging",
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
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 13.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57358391",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57363510",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57349825",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57358381",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57349813",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57358387",
            "naam": "Slaapkamer 3",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten",
            "naam": "Verwarmde overige en verkeersruimten"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_57349834",
            "naam": "Hal",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
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
          "code": "BUI",
          "naam": "Buitenruimten"
        }
      },
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 54.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 18.9
        },
        {
          "aantal": 53.58,
          "criterium": {
            "id": "buitenruimten__prive__Space_57351371",
            "naam": "Tuin",
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
            "id": "buitenruimten__maximering",
            "naam": "Maximaal 15 punten"
          },
          "punten": -5.9
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
      "punten": 52.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "A -> A++ (Energie-index)"
          },
          "punten": 52.0
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
            "id": "keuken__Space_57349825",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 1800.0,
          "criterium": {
            "id": "keuken__Space_57349825__lengte_aanrecht_Aanrecht_57349829",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_57349825"
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
      "punten": 11.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_57358391",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_57358391__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57358391"
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
            "id": "sanitair__Space_57358391__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57358391"
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
            "id": "sanitair__Space_57358391__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57358391"
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
            "id": "sanitair__Space_57349819",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_57349819__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57349819"
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
            "id": "sanitair__Space_57349819__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57349819"
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
          "aantal": 367000.0,
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
          "punten": 23.94
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
          "punten": 17.63
        },
        {
          "aantal": 86.0,
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
          "punten": -0.07
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
  "maximaleHuur": 1461.49,
  "punten": 220.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1461.49
}
```
