# test_model_zelfstandige_woonruimten[77795000000]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Eengezinswoning uit 2011 van 106 m², met een energie-index A, een collectieve verwarmingsaansluiting en een zolder met een trap.

## Rapport

```text
SAMENVATTING 77795000000
  Oppervlakte van vertrekken                                                     66.00 pt
  Oppervlakte van overige ruimten                                                25.50 pt
  Verkoeling en verwarming                                                       14.00 pt
  Buitenruimten                                                                  15.00 pt
  Energieprestatie                                                               41.00 pt
  Keuken                                                                          7.00 pt
  Sanitair                                                                       11.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      36.00 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                216.00 pt
  Maximaal redelijke huur                                          1433.99 EUR

OPPERVLAKTE VAN VERTREKKEN
  Slaapkamer 1                                                        9.60 m²
  Badruimte                                                           5.71 m²
  Keuken                                                              9.37 m²
  Slaapkamer 2                                                       13.41 m²
  Woonkamer                                                          21.84 m²
  Slaapkamer 3                                                        6.06 m²
                                                                    ------      ------
  Totaal                                                             65.99 m²    66.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Buitenberging                                                       6.54 m²
  Zolder                                                             26.96 m²
                                                                    ------      ------
  Totaal                                                             33.50 m²    25.50 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Slaapkamer 1                                                                2.00 pt
    - Badruimte                                                                   2.00 pt
    - Keuken                                                                      2.00 pt
    - Slaapkamer 2                                                                2.00 pt
    - Woonkamer                                                                   2.00 pt
    - Slaapkamer 3                                                                2.00 pt
  Verwarmde overige en verkeersruimten
    - Entree                                                                      1.00 pt
    - Zolder                                                                      1.00 pt
                                                                                ------
  Totaal                                                                         14.00 pt

BUITENRUIMTEN
  Privé                                                              55.00 m²    19.25 pt
    - Tuin                                                           54.65 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Maximaal 15 punten                                                             -6.25 pt
                                                                                ------
  Totaal                                                                         15.00 pt

ENERGIEPRESTATIE
  A (Energie-index)                                                              41.00 pt
                                                                                ------
  Totaal                                                                         41.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              3600.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt

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
  WOZ-waarde op waardepeildatum 01-01-2024                       336000.00 EUR
  Onderdeel I                                                                    21.92 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   14.02 pt
    - Oppervlakte van vertrekken en overige ruimten                  99.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                        0.06 pt
                                                                                ------
  Totaal                                                                         36.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "77795000000",
  "bouwjaar": 2011,
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
      "begindatum": "2017-12-29",
      "einddatum": "2027-12-29",
      "registratiedatum": "2017-12-29T15:45:50+01:00",
      "label": {
        "code": "A",
        "naam": "A"
      },
      "waarde": "0.97"
    }
  ],
  "gebruiksoppervlakte": 106,
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
      "id": "Space_9946634",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 7.36397,
      "oppervlakte": 3.02,
      "verwarmd": false
    },
    {
      "id": "Space_9946583",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 25.436,
      "oppervlakte": 9.5985,
      "verwarmd": true
    },
    {
      "id": "Space_9946609",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 15.1368,
      "oppervlakte": 5.712,
      "bouwkundigeElementen": [
        {
          "id": "Douche_9946614",
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
          "id": "Wastafel_9946615",
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
          "id": "Closetcombinatie_9946617",
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
      "id": "Space_9944930",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Buitenberging",
      "inhoud": 16.8848,
      "oppervlakte": 6.5445,
      "verwarmd": false
    },
    {
      "id": "Space_9947510",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 11.4974,
      "oppervlakte": 3.16357,
      "verwarmd": false
    },
    {
      "id": "Space_9945004",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 15.7081,
      "oppervlakte": 5.8832,
      "verwarmd": true
    },
    {
      "id": "Space_9947348",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "inhoud": 77.7543,
      "oppervlakte": 26.9637,
      "bouwkundigeElementen": [
        {
          "id": "Ketel_50412169",
          "naam": "Ketel",
          "omschrijving": "Stadsverwarming",
          "soort": {
            "code": "VER",
            "naam": "Verwarming"
          },
          "detailSoort": {
            "code": "VCL",
            "naam": "Collectieve verwarmingsaansluiting"
          }
        },
        {
          "naam": "Trap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "TRA",
            "naam": "Trap"
          }
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_9944876",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 25.019,
      "oppervlakte": 9.3704,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_9944878",
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
          "lengte": 3600.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_9946620",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 35.5365,
      "oppervlakte": 13.41,
      "verwarmd": true
    },
    {
      "id": "Space_9944887",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "breedte": 5670.0,
      "hoogte": 2650.0,
      "inhoud": 144.819,
      "lengte": 11090.0,
      "oppervlakte": 54.6486,
      "verwarmd": false
    },
    {
      "id": "Space_9946605",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "OVE",
        "naam": "Overloop"
      },
      "naam": "Overloop",
      "inhoud": 8.8033,
      "oppervlakte": 3.322,
      "verwarmd": false
    },
    {
      "id": "Space_9944855",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 58.3033,
      "oppervlakte": 21.8364,
      "verwarmd": true
    },
    {
      "id": "Space_9946600",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 16.0463,
      "oppervlakte": 6.0552,
      "verwarmd": true
    },
    {
      "id": "Space_9944863",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 2.99681,
      "oppervlakte": 1.1224,
      "bouwkundigeElementen": [
        {
          "id": "Fontein_9944866",
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
          "id": "Closetcombinatie_9944865",
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
      "id": "Space_9945007",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 8.758,
      "oppervlakte": 3.02,
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 339000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 365000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 336000.0,
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
      "punten": 66.0,
      "woningwaarderingen": [
        {
          "aantal": 9.6,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_9946583",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 5.71,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_9946609",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 9.37,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_9944876",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 13.41,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_9946620",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 21.84,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_9944855",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 6.06,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_9946600",
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
      "punten": 25.5,
      "woningwaarderingen": [
        {
          "aantal": 6.54,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_9944930",
            "naam": "Buitenberging",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 26.96,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_9947348",
            "naam": "Zolder",
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
      "punten": 14.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_9946583",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_9946609",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_9944876",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_9946620",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_9944855",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_9946600",
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
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_9945004",
            "naam": "Entree",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
            }
          },
          "punten": 1.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__Space_9947348",
            "naam": "Zolder",
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
          "aantal": 55.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 19.25
        },
        {
          "aantal": 54.65,
          "criterium": {
            "id": "buitenruimten__prive__Space_9944887",
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
          "punten": -6.25
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
      "punten": 41.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "A (Energie-index)"
          },
          "punten": 41.0
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
            "id": "keuken__Space_9944876",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 3600.0,
          "criterium": {
            "id": "keuken__Space_9944876__lengte_aanrecht_Aanrecht_9944878",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_9944876"
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
      "punten": 11.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_9946609",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_9946609__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_9946609"
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
            "id": "sanitair__Space_9946609__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_9946609"
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
            "id": "sanitair__Space_9946609__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_9946609"
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
            "id": "sanitair__Space_9944863",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_9944863__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_9944863"
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
            "id": "sanitair__Space_9944863__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_9944863"
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
      "punten": 36.0,
      "woningwaarderingen": [
        {
          "aantal": 336000.0,
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
          "punten": 21.92
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
          "punten": 14.02
        },
        {
          "aantal": 99.0,
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
          "punten": 0.06
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
  "maximaleHuur": 1433.99,
  "punten": 216.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1433.99
}
```
