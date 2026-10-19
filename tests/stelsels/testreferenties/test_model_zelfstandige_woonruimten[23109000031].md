# test_model_zelfstandige_woonruimten[23109000031]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Eengezinswoning uit 1922 die een rijksmonument is, met een energie-index B en een terras.

## Rapport

```text
SAMENVATTING 23109000031
  Oppervlakte van vertrekken                                                     45.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                       12.00 pt
  Buitenruimten                                                                   3.00 pt
  Energieprestatie
  Keuken                                                                          4.00 pt
  Sanitair                                                                       11.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      37.50 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw                                            50.00 pt
                                                                                ------
  Totaal afgerond op hele punten                                                163.00 pt
  Maximaal redelijke huur                                          1070.14 EUR

OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer 1                                                       10.79 m²
  Badruimte                                                           4.83 m²
  Woonkamer                                                          14.33 m²
  Slaapkamer 2                                                        9.28 m²
  Keuken                                                              5.79 m²
                                                                    ------      ------
  Totaal                                                             45.02 m²    45.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Slaapkamer 1                                                                2.00 pt
    - Badruimte                                                                   2.00 pt
    - Woonkamer                                                                   2.00 pt
    - Slaapkamer 2                                                                2.00 pt
    - Keuken                                                                      2.00 pt
  Verwarmde overige en verkeersruimten
    - Entree                                                                      1.00 pt
    - Hal                                                                         1.00 pt
                                                                                ------
  Totaal                                                                         12.00 pt

BUITENRUIMTEN
  Privé                                                               3.00 m²     1.05 pt
    - Terras                                                          3.21 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                          3.00 pt

ENERGIEPRESTATIE
  Bouwjaar 1922                                                                 -15.00 pt
  Correctie monument                                                             15.00 pt
                                                                                ------
  Totaal                                                                          0.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              1500.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                          4.00 pt

SANITAIR
  Toiletruimte
    - Staand Toilet                                                   1.00 st     3.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
  Badruimte
    - Staand Toilet                                                   1.00 st     2.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
                                                                                ------
  Totaal                                                                         11.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       238000.00 EUR
  Onderdeel I                                                                    15.53 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   21.85 pt
    - Oppervlakte van vertrekken en overige ruimten                  45.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                         37.50 pt

PRIJSOPSLAG MONUMENTEN EN NIEUWBOUW
  Rijksmonument                                                                  50.00 pt
                                                                                ------
  Totaal                                                                         50.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "23109000031",
  "bouwjaar": 1922,
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
      "begindatum": "2015-05-21",
      "einddatum": "2025-05-21",
      "registratiedatum": "2017-04-06T15:57:35.057000+02:00",
      "label": {
        "code": "B",
        "naam": "B"
      },
      "waarde": "1.27"
    }
  ],
  "klimaatbeheersing": [
    {
      "code": "COL",
      "naam": "Collectief"
    }
  ],
  "monumenten": [
    {
      "code": "RIJ",
      "naam": "Rijksmonument"
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
      "id": "Space_74227409",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 1.31204,
      "oppervlakte": 0.49325,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74227466",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.632016,
      "oppervlakte": 0.2376,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74227558",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 22.2518,
      "oppervlakte": 8.36533,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_74227663",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 2.75842,
      "oppervlakte": 1.037,
      "bouwkundigeElementen": [
        {
          "id": "Closetcombinatie_139398918",
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
          "id": "Fontein_139398919",
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
      "verwarmd": true
    },
    {
      "id": "Space_74227894",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "inhoud": 1.81558,
      "oppervlakte": 0.68255,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74227959",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 28.7042,
      "oppervlakte": 10.7911,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_74235849",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 13.494,
      "oppervlakte": 4.82794,
      "bouwkundigeElementen": [
        {
          "id": "Wastafel_74235854",
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
          "id": "Douche_139399416",
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
          "id": "Closetcombinatie_139399417",
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
      "id": "Space_74235998",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TER",
        "naam": "Terras"
      },
      "naam": "Terras",
      "breedte": 3670.0,
      "inhoud": 8.97171,
      "lengte": 1010.0,
      "oppervlakte": 3.20991,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74236114",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 1.99232,
      "oppervlakte": 0.712817,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74236116",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.880425,
      "oppervlakte": 0.315,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74236118",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 1.99232,
      "oppervlakte": 0.712817,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_74236196",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "inhoud": 13.9727,
      "oppervlakte": 4.99916,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_74236230",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 40.0421,
      "oppervlakte": 14.3263,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_74236234",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 25.9266,
      "oppervlakte": 9.27605,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_74238526",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 16.189,
      "oppervlakte": 5.79214,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_139399905",
          "naam": "Aanrecht",
          "soort": {
            "code": "KEU",
            "naam": "Keuken voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1500.0
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
      "vastgesteldeWaarde": 237000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 238000.0,
      "waardepeildatum": "2024-01-01"
    }
  ],
  "datumAfsluitenHuurovereenkomst": "2019-11-18"
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
      "punten": 45.0,
      "woningwaarderingen": [
        {
          "aantal": 10.79,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_74227959",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 4.83,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_74235849",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 14.33,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_74236230",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 9.28,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_74236234",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 5.79,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_74238526",
            "naam": "Keuken",
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
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_74227959",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_74235849",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_74236230",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_74236234",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_74238526",
            "naam": "Keuken",
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
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_74227558",
            "naam": "Entree",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
            }
          },
          "punten": 1.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_74236196",
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
      "punten": 3.0,
      "woningwaarderingen": [
        {
          "aantal": 3.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 1.05
        },
        {
          "aantal": 3.21,
          "criterium": {
            "id": "buitenruimten__prive__Space_74235998",
            "naam": "Terras",
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
      "punten": 0.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__bouwjaar",
            "naam": "Bouwjaar 1922"
          },
          "punten": -15.0
        },
        {
          "criterium": {
            "id": "energieprestatie__correctie_monument",
            "naam": "Correctie monument"
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
            "id": "keuken__Space_74238526",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 1500.0,
          "criterium": {
            "id": "keuken__Space_74238526__lengte_aanrecht_Aanrecht_139399905",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_74238526"
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
            "id": "sanitair__Space_74227663",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_74227663__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_74227663"
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
            "id": "sanitair__Space_74227663__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_74227663"
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
            "id": "sanitair__Space_74235849",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_74235849__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_74235849"
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
            "id": "sanitair__Space_74235849__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_74235849"
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
            "id": "sanitair__Space_74235849__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_74235849"
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
      "punten": 37.5,
      "woningwaarderingen": [
        {
          "aantal": 238000.0,
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
          "punten": 15.53
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
          "punten": 21.85
        },
        {
          "aantal": 45.0,
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
          "punten": 0.12
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
  "maximaleHuur": 1070.14,
  "punten": 163.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1070.14
}
```
