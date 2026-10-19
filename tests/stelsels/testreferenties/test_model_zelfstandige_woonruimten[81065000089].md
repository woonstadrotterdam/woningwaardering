# test_model_zelfstandige_woonruimten[81065000089]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Zolder met vlizotrap aanwezig

## Rapport

```text
SAMENVATTING 81065000089
  Oppervlakte van vertrekken                                                     58.00 pt
  Oppervlakte van overige ruimten                                                 4.75 pt
  Verkoeling en verwarming                                                       11.00 pt
  Buitenruimten                                                                  -5.00 pt
  Energieprestatie                                                               34.00 pt
  Keuken                                                                          7.00 pt
  Sanitair                                                                        4.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      30.25 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                144.00 pt
  Maximaal redelijke huur                                           939.73 EUR

OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer 1                                                       11.63 m²
  Slaapkamer 2                                                        7.62 m²
  Woonkamer                                                          17.77 m²
  Keuken                                                             12.72 m²
  Slaapkamer 3                                                        8.34 m²
                                                                    ------      ------
  Totaal                                                             58.08 m²    58.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                          13.09 m²     9.75 pt
    - Zolder                                                         10.23 m²
    - Wasruimte                                                       2.86 m²
  Correctie: zolder zonder vaste trap                                            -5.00 pt
                                                                    ------      ------
  Totaal                                                             13.09 m²     4.75 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Slaapkamer 1                                                                2.00 pt
    - Slaapkamer 2                                                                2.00 pt
    - Woonkamer                                                                   2.00 pt
    - Keuken                                                                      2.00 pt
    - Slaapkamer 3                                                                2.00 pt
  Verwarmde overige en verkeersruimten
    - Wasruimte                                                                   1.00 pt
                                                                                ------
  Totaal                                                                         11.00 pt

BUITENRUIMTEN
  Geen buitenruimten                                                             -5.00 pt
                                                                                ------
  Totaal                                                                         -5.00 pt

ENERGIEPRESTATIE
  B                                                                              34.00 pt
                                                                                ------
  Totaal                                                                         34.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              2507.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt

SANITAIR
  Wasruimte
    - Douche                                                          1.00 st     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       245000.00 EUR
  Onderdeel I                                                                    15.98 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   14.26 pt
    - Oppervlakte van vertrekken en overige ruimten                  71.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                        0.01 pt
                                                                                ------
  Totaal                                                                         30.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "81065000089",
  "bouwjaar": 1921,
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
        "code": "NTA",
        "naam": "Energielabel conform NTA8800"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2024-02-13",
      "einddatum": "2034-02-13",
      "registratiedatum": "2024-02-21T11:09:37+01:00",
      "label": {
        "code": "B",
        "naam": "B"
      },
      "waarde": "173.08"
    }
  ],
  "gebruiksoppervlakte": 82,
  "klimaatbeheersing": [
    {
      "code": "IND",
      "naam": "Individueel"
    }
  ],
  "monumenten": [],
  "oppervlakten": [
    {
      "soort": {
        "code": "GTZ",
        "naam": "Gebruiksoppervlakte thermische zone"
      },
      "waarde": "78.84"
    }
  ],
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
      "id": "Space_29475563",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 4.02467,
      "oppervlakte": 0.025811,
      "verwarmd": false
    },
    {
      "id": "Space_29474431",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "inhoud": 2.60078,
      "oppervlakte": 0.858344,
      "verwarmd": false
    },
    {
      "id": "Space_31299076",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "inhoud": 32.7376,
      "oppervlakte": 10.2305,
      "bouwkundigeElementen": [
        {
          "naam": "Vlizotrap",
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
      "id": "Space_29489751",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 29.0723,
      "oppervlakte": 11.6289,
      "verwarmd": true
    },
    {
      "id": "Space_29489753",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 5.49399,
      "oppervlakte": 2.24108,
      "verwarmd": false
    },
    {
      "id": "Space_29474433",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 4.02467,
      "oppervlakte": 1.27409,
      "verwarmd": false
    },
    {
      "id": "Space_29489749",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 19.0458,
      "oppervlakte": 7.61833,
      "verwarmd": true
    },
    {
      "id": "Space_29474434",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 53.8483,
      "oppervlakte": 17.7717,
      "verwarmd": true
    },
    {
      "id": "Space_29489754",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "OVE",
        "naam": "Overloop"
      },
      "naam": "Overloop",
      "inhoud": 9.17199,
      "oppervlakte": 3.66757,
      "verwarmd": false
    },
    {
      "id": "Space_29474435",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 4.51051,
      "oppervlakte": 1.48862,
      "verwarmd": false
    },
    {
      "id": "Space_29489752",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "WAS",
        "naam": "Wasruimte"
      },
      "naam": "Wasruimte",
      "inhoud": 7.15234,
      "oppervlakte": 2.86093,
      "bouwkundigeElementen": [
        {
          "id": "Douche_29481807",
          "naam": "Douche",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_29474432",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 3.78946,
      "oppervlakte": 1.25065,
      "verwarmd": false
    },
    {
      "id": "Space_29474430",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 38.5381,
      "oppervlakte": 12.7166,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_29467536",
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
          "lengte": 2507.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_29489750",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 20.8602,
      "oppervlakte": 8.34408,
      "verwarmd": true
    },
    {
      "id": "Space_29474436",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.524294,
      "oppervlakte": 0.173034,
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 216000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 226000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 245000.0,
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
      "punten": 58.0,
      "woningwaarderingen": [
        {
          "aantal": 11.63,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_29489751",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 7.62,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_29489749",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 17.77,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_29474434",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 12.72,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_29474430",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 8.34,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_29489750",
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
      "punten": 4.75,
      "woningwaarderingen": [
        {
          "aantal": 13.09,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__subtotaal",
            "naam": "Subtotaal",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 9.75
        },
        {
          "aantal": 10.23,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__subtotaal__Space_31299076",
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
          "aantal": 2.86,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__subtotaal__Space_29489752",
            "naam": "Wasruimte",
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
            "id": "oppervlakte_van_overige_ruimten__Space_31299076__correctie_zolder_zonder_vaste_trap",
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
      "punten": 11.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_29489751",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_29489749",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_29474434",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_29474430",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_29489750",
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
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_29489752",
            "naam": "Wasruimte",
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
      "punten": 34.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "B"
          },
          "punten": 34.0
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
            "id": "keuken__Space_29474430",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 2507.0,
          "criterium": {
            "id": "keuken__Space_29474430__lengte_aanrecht_Aanrecht_29467536",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_29474430"
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
      "punten": 4.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_29489752",
            "naam": "Wasruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_29489752__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_29489752"
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
      "punten": 30.25,
      "woningwaarderingen": [
        {
          "aantal": 245000.0,
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
          "punten": 15.98
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
          "punten": 14.26
        },
        {
          "aantal": 71.0,
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
          "punten": 0.01
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
  "maximaleHuur": 939.73,
  "punten": 144.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 939.73
}
```
