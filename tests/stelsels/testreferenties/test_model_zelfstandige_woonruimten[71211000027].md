# test_model_zelfstandige_woonruimten[71211000027]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Eengezinswoning

## Rapport

```text
SAMENVATTING 71211000027
  Oppervlakte van vertrekken                                                     54.00 pt
  Oppervlakte van overige ruimten                                                 7.00 pt
  Verkoeling en verwarming                                                       12.00 pt
  Buitenruimten                                                                  15.00 pt
  Energieprestatie                                                               14.00 pt
  Keuken                                                                          7.00 pt
  Sanitair                                                                        9.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      24.25 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                142.00 pt
  Maximaal redelijke huur                                           925.98 EUR

OPPERVLAKTE VAN VERTREKKEN
  Woonkamer (+1 kast)                                                15.89 m²
  Keuken                                                             10.63 m²
  Slaapkamer 1                                                        9.08 m²
  Slaapkamer 2                                                        4.73 m²
  Slaapkamer 3                                                        8.72 m²
  Badruimte                                                           4.94 m²
                                                                    ------      ------
  Totaal                                                             53.99 m²    54.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                          16.12 m²    12.00 pt
    - Zolder                                                         11.07 m²
    - Berging                                                         5.05 m²
  Correctie: zolder zonder vaste trap                                            -5.00 pt
                                                                    ------      ------
  Totaal                                                             16.12 m²     7.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Woonkamer                                                                   2.00 pt
    - Keuken                                                                      2.00 pt
    - Slaapkamer 1                                                                2.00 pt
    - Slaapkamer 2                                                                2.00 pt
    - Slaapkamer 3                                                                2.00 pt
    - Badruimte                                                                   2.00 pt
                                                                                ------
  Totaal                                                                         12.00 pt

BUITENRUIMTEN
  Privé                                                              39.00 m²    13.65 pt
    - Tuin 1                                                          4.62 m²
    - Tuin 2                                                         34.41 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Maximaal 15 punten                                                             -0.65 pt
                                                                                ------
  Totaal                                                                         15.00 pt

ENERGIEPRESTATIE
  D (Energie-index)                                                              14.00 pt
                                                                                ------
  Totaal                                                                         14.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              3000.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt

SANITAIR
  Toiletruimte
    - Staand Toilet                                                   1.00 st     3.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
  Badruimte
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
                                                                                ------
  Totaal                                                                          9.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       195000.00 EUR
  Onderdeel I                                                                    12.72 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   11.51 pt
    - Oppervlakte van vertrekken en overige ruimten                  70.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                        0.02 pt
                                                                                ------
  Totaal                                                                         24.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "71211000027",
  "bouwjaar": 1919,
  "adres": {
    "huisnummer": "",
    "huisnummerToevoeging": "",
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
      "begindatum": "2018-10-29",
      "einddatum": "2028-10-29",
      "registratiedatum": "2019-02-13T11:48:42+01:00",
      "label": {
        "code": "D",
        "naam": "D"
      },
      "waarde": "1.85"
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
        "code": "EGW",
        "naam": "Eengezinswoning"
      }
    }
  ],
  "ruimten": [
    {
      "id": "Space_57380186",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 4.42126,
      "oppervlakte": 1.83455,
      "verwarmd": false
    },
    {
      "id": "Space_57375640",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 41.2466,
      "oppervlakte": 15.1086,
      "verbondenRuimten": [
        {
          "id": "Space_57375634",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 2.37417,
          "oppervlakte": 0.78615,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_57375636",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "breedte": 3040.0,
      "hoogte": 3020.0,
      "inhoud": 13.9404,
      "lengte": 1540.0,
      "oppervlakte": 4.61601,
      "verwarmd": false
    },
    {
      "id": "Space_57375630",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 29.0062,
      "oppervlakte": 10.625,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_57375632",
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
          "lengte": 3000.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_57380176",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "OVE",
        "naam": "Overloop"
      },
      "naam": "Overloop",
      "inhoud": 4.42126,
      "oppervlakte": 1.83455,
      "verwarmd": false
    },
    {
      "id": "Space_57376296",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 2.4693,
      "oppervlakte": 0.81765,
      "verwarmd": false
    },
    {
      "id": "Space_57376368",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 2.8742,
      "oppervlakte": 1.035,
      "bouwkundigeElementen": [
        {
          "id": "Fontein_57376370",
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
          "id": "Closetcombinatie_57376369",
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
      "id": "Space_57375634",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 2.37417,
      "oppervlakte": 0.78615,
      "verwarmd": false
    },
    {
      "id": "Space_57375635",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "breedte": 4690.0,
      "hoogte": 3020.0,
      "inhoud": 103.915,
      "lengte": 8970.0,
      "oppervlakte": 34.4089,
      "verwarmd": false
    },
    {
      "id": "Space_57385287",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "inhoud": 8.23437,
      "oppervlakte": 11.0727,
      "bouwkundigeElementen": [
        {
          "id": "Ketel_57384803",
          "naam": "Ketel",
          "omschrijving": "Gashaard",
          "soort": {
            "code": "VER",
            "naam": "Verwarming"
          },
          "detailSoort": {
            "code": "VTO",
            "naam": "Verwarmingstoestellen"
          }
        },
        {
          "id": "Trap_123",
          "naam": "Vlizotrap",
          "omschrijving": "(vaste) trap naar de zolder",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTR",
            "naam": "Vlizotrap"
          }
        }
      ],
      "verwarmd": false
    },
    {
      "id": "Space_57385508",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.066735,
      "oppervlakte": 0.07375,
      "verwarmd": false
    },
    {
      "id": "Space_57376103",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "inhoud": 11.2043,
      "oppervlakte": 5.04697,
      "verwarmd": false
    },
    {
      "id": "Space_57380265",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 15.7465,
      "oppervlakte": 9.08301,
      "verwarmd": true
    },
    {
      "id": "Space_57375639",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 4.85239,
      "oppervlakte": 1.77743,
      "verwarmd": false
    },
    {
      "id": "Space_57381083",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 11.4089,
      "oppervlakte": 4.734,
      "verwarmd": true
    },
    {
      "id": "Space_57375633",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.664864,
      "oppervlakte": 0.24354,
      "verwarmd": false
    },
    {
      "id": "Space_57381076",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 21.0217,
      "oppervlakte": 8.7227,
      "verwarmd": true
    },
    {
      "id": "Space_57380179",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 7.25974,
      "oppervlakte": 4.93741,
      "bouwkundigeElementen": [
        {
          "id": "Douche_57380183",
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
          "id": "Wastafel_57380184",
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
      "id": "Space_57385510",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.0367336,
      "oppervlakte": 0.07375,
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 159000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 169000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 195000.0,
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
      "punten": 54.0,
      "woningwaarderingen": [
        {
          "aantal": 15.89,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57375640",
            "naam": "Woonkamer (+1 kast)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 10.63,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57375630",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 9.08,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57380265",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 4.73,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57381083",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 8.72,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57381076",
            "naam": "Slaapkamer 3",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 4.94,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_57380179",
            "naam": "Badruimte",
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
      "punten": 7.0,
      "woningwaarderingen": [
        {
          "aantal": 16.12,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__subtotaal",
            "naam": "Subtotaal",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 12.0
        },
        {
          "aantal": 11.07,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__subtotaal__Space_57385287",
            "naam": "Zolder",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_overige_ruimten__subtotaal"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 5.05,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__subtotaal__Space_57376103",
            "naam": "Berging",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_overige_ruimten__subtotaal"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_57385287__correctie_zolder_zonder_vaste_trap",
            "naam": "Correctie: zolder zonder vaste trap"
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
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 12.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57375640",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57375630",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57380265",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57381083",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57381076",
            "naam": "Slaapkamer 3",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_57380179",
            "naam": "Badruimte",
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
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 39.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 13.65
        },
        {
          "aantal": 4.62,
          "criterium": {
            "id": "buitenruimten__prive__Space_57375636",
            "naam": "Tuin 1",
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
          "aantal": 34.41,
          "criterium": {
            "id": "buitenruimten__prive__Space_57375635",
            "naam": "Tuin 2",
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
          "punten": -0.65
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
      "punten": 14.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "D (Energie-index)"
          },
          "punten": 14.0
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
      "punten": 7.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "keuken__Space_57375630",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 3000.0,
          "criterium": {
            "id": "keuken__Space_57375630__lengte_aanrecht_Aanrecht_57375632",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_57375630"
            },
            "meeteenheid": {
              "code": "MIL",
              "naam": "Millimeter"
            }
          },
          "punten": 7.0
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
            "id": "sanitair__Space_57376368",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_57376368__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57376368"
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
            "id": "sanitair__Space_57376368__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57376368"
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
            "id": "sanitair__Space_57380179",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_57380179__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57380179"
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
            "id": "sanitair__Space_57380179__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_57380179"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
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
      "punten": 24.25,
      "woningwaarderingen": [
        {
          "aantal": 195000.0,
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
          "punten": 12.72
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
          "punten": 11.51
        },
        {
          "aantal": 70.0,
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
          "punten": 0.02
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
  "maximaleHuur": 925.98,
  "punten": 142.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 925.98
}
```
