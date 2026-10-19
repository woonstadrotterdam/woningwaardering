# test_model_zelfstandige_woonruimten[12006000004]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Galerijflat

Veel ingebouwde kasten die met vertrek moeten worden meegerekend.

Op 2 mei 2024 had deze eenheid geen geldige energieprestatie

## Rapport

```text
SAMENVATTING 12006000004
  Oppervlakte van vertrekken                                                     60.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                       11.00 pt
  Buitenruimten                                                                   2.75 pt
  Energieprestatie                                                               37.00 pt
  Keuken                                                                          7.00 pt
  Sanitair                                                                        9.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      42.75 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                170.00 pt
  Maximaal redelijke huur                                          1118.23 EUR

OPPERVLAKTE VAN VERTREKKEN
  Badruimte                                                           3.58 m²
  Keuken (+2 kasten)                                                 10.18 m²
  Woonkamer (+1 kast)                                                26.82 m²
  Slaapkamer 1                                                        6.49 m²
  Slaapkamer 2                                                       12.98 m²
                                                                    ------      ------
  Totaal                                                             60.05 m²    60.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Badruimte                                                                   2.00 pt
    - Keuken                                                                      2.00 pt
    - Woonkamer                                                                   2.00 pt
    - Slaapkamer 1                                                                2.00 pt
    - Slaapkamer 2                                                                2.00 pt
  Verwarmde overige en verkeersruimten
    - Hal                                                                         1.00 pt
                                                                                ------
  Totaal                                                                         11.00 pt

BUITENRUIMTEN
  Privé                                                               2.00 m²     0.70 pt
    - Balkon                                                          1.82 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Afronding op kwartpunten                                                        0.05 pt
                                                                                ------
  Totaal                                                                          2.75 pt

ENERGIEPRESTATIE
  A                                                                              37.00 pt
                                                                                ------
  Totaal                                                                         37.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              2100.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt

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
  WOZ-waarde op waardepeildatum 01-01-2024                       318000.00 EUR
  Onderdeel I                                                                    20.74 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   21.90 pt
    - Oppervlakte van vertrekken en overige ruimten                  60.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                        0.11 pt
                                                                                ------
  Totaal                                                                         42.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "12006000004",
  "bouwjaar": 1981,
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
      "begindatum": "2024-07-18",
      "einddatum": "2034-07-18",
      "registratiedatum": "2024-07-24T00:00:00+01:00",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "80.17"
    }
  ],
  "gebruiksoppervlakte": 71,
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
      "id": "Space_82124154",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "breedte": 1500.0,
      "hoogte": 2600.0,
      "inhoud": 4.73874,
      "lengte": 1290.0,
      "oppervlakte": 1.82259,
      "verwarmd": false
    },
    {
      "id": "Space_82123527",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TEC",
        "naam": "Technische ruimte"
      },
      "naam": "Technische ruimte",
      "inhoud": 0.89856,
      "oppervlakte": 0.3456,
      "bouwkundigeElementen": [
        {
          "id": "Ketel_82123536",
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
      "id": "Space_82123555",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.6566,
      "oppervlakte": 0.2345,
      "verwarmd": false
    },
    {
      "id": "Space_82123416",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 9.3184,
      "oppervlakte": 3.584,
      "bouwkundigeElementen": [
        {
          "id": "Douche_82123432",
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
          "id": "Wastafel_82123438",
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
      "id": "Space_82123569",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 24.8469,
      "oppervlakte": 9.5565,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_82123576",
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
          "lengte": 2100.0
        }
      ],
      "verbondenRuimten": [
        {
          "id": "Space_82123559",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.8008,
          "oppervlakte": 0.308,
          "verwarmd": false
        },
        {
          "id": "Space_82123527",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "TEC",
            "naam": "Technische ruimte"
          },
          "naam": "Technische ruimte",
          "inhoud": 0.89856,
          "oppervlakte": 0.3456,
          "bouwkundigeElementen": [
            {
              "id": "Ketel_82123536",
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
          "id": "Space_82123518",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.8112,
          "oppervlakte": 0.312,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82123563",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 67.496,
      "oppervlakte": 25.96,
      "verbondenRuimten": [
        {
          "id": "Space_82123551",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 2.2256,
          "oppervlakte": 0.856,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82123455",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "inhoud": 16.1148,
      "oppervlakte": 6.198,
      "verbondenRuimten": [
        {
          "id": "Space_82123445",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 0.9295,
          "oppervlakte": 0.3575,
          "verwarmd": false
        },
        {
          "id": "Space_82123507",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "MET",
            "naam": "Meterruimte"
          },
          "naam": "Meterruimte",
          "inhoud": 0.5733,
          "oppervlakte": 0.2205,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_82123469",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 16.8636,
      "oppervlakte": 6.486,
      "verwarmd": true
    },
    {
      "id": "Space_82123551",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 2.2256,
      "oppervlakte": 0.856,
      "verwarmd": false
    },
    {
      "id": "Space_82123507",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "inhoud": 0.5733,
      "oppervlakte": 0.2205,
      "verwarmd": false
    },
    {
      "id": "Space_82123518",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.8112,
      "oppervlakte": 0.312,
      "verwarmd": false
    },
    {
      "id": "Space_82123484",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 3.28575,
      "oppervlakte": 1.26375,
      "bouwkundigeElementen": [
        {
          "id": "Fontein_82123493",
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
          "id": "Closetcombinatie_82123500",
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
      "id": "Space_82123559",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.8008,
      "oppervlakte": 0.308,
      "verwarmd": false
    },
    {
      "id": "Space_82123399",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 33.7428,
      "oppervlakte": 12.978,
      "verwarmd": true
    },
    {
      "id": "Space_82123445",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 0.9295,
      "oppervlakte": 0.3575,
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 111000.0,
      "waardepeildatum": "2014-01-01"
    },
    {
      "vastgesteldeWaarde": 113000.0,
      "waardepeildatum": "2015-01-01"
    },
    {
      "vastgesteldeWaarde": 120000.0,
      "waardepeildatum": "2016-01-01"
    },
    {
      "vastgesteldeWaarde": 135000.0,
      "waardepeildatum": "2017-01-01"
    },
    {
      "vastgesteldeWaarde": 167000.0,
      "waardepeildatum": "2018-01-01"
    },
    {
      "vastgesteldeWaarde": 200000.0,
      "waardepeildatum": "2019-01-01"
    },
    {
      "vastgesteldeWaarde": 233000.0,
      "waardepeildatum": "2020-01-01"
    },
    {
      "vastgesteldeWaarde": 266000.0,
      "waardepeildatum": "2021-01-01"
    },
    {
      "vastgesteldeWaarde": 297000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 309000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 318000.0,
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
      "punten": 60.0,
      "woningwaarderingen": [
        {
          "aantal": 3.58,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82123416",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 10.18,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82123569",
            "naam": "Keuken (+2 kasten)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 26.82,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82123563",
            "naam": "Woonkamer (+1 kast)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 6.49,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82123469",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 12.98,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_82123399",
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
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82123416",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82123569",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82123563",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82123469",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_82123399",
            "naam": "Slaapkamer 2",
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
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_82123455",
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
      "punten": 2.75,
      "woningwaarderingen": [
        {
          "aantal": 2.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 0.7
        },
        {
          "aantal": 1.82,
          "criterium": {
            "id": "buitenruimten__prive__Space_82124154",
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
      "punten": 37.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "A"
          },
          "punten": 37.0
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
            "id": "keuken__Space_82123569",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 2100.0,
          "criterium": {
            "id": "keuken__Space_82123569__lengte_aanrecht_Aanrecht_82123576",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_82123569"
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
            "id": "sanitair__Space_82123416",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_82123416__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82123416"
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
            "id": "sanitair__Space_82123416__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82123416"
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
            "id": "sanitair__Space_82123484",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_82123484__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82123484"
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
            "id": "sanitair__Space_82123484__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_82123484"
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
      "punten": 42.75,
      "woningwaarderingen": [
        {
          "aantal": 318000.0,
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
          "punten": 20.74
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
          "punten": 21.9
        },
        {
          "aantal": 60.0,
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
          "punten": 0.11
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
  "maximaleHuur": 1118.23,
  "punten": 170.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1118.23
}
```
