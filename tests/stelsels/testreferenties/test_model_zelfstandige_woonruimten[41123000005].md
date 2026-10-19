# test_model_zelfstandige_woonruimten[41123000005]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Eengezinswoning uit 1896 van 170 m², met twee keukens, drie badruimten, een zolder met een trap en een energie-index B.

## Rapport

```text
SAMENVATTING 41123000005
  Oppervlakte van vertrekken                                                    113.00 pt
  Oppervlakte van overige ruimten                                                 8.25 pt
  Verkoeling en verwarming                                                       22.00 pt
  Buitenruimten                                                                  14.25 pt
  Energieprestatie                                                               34.00 pt
  Keuken                                                                          8.00 pt
  Sanitair                                                                       18.00 pt
  Gemeenschappelijke parkeerruimten
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      74.75 pt
  Bijzondere voorzieningen
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                292.00 pt
  Maximaal redelijke huur                                          1955.52 EUR

OPPERVLAKTE VAN VERTREKKEN
  Woonkamer 1                                                        18.64 m²
  Slaapkamer 1                                                       12.19 m²
  Slaapkamer 2                                                       17.26 m²
  Badruimte 1                                                         6.80 m²
  Slaapkamer 3                                                       10.24 m²
  Keuken 1                                                            5.76 m²
  Keuken 2                                                            5.38 m²
  Badruimte 2                                                         1.75 m²
  Woonkamer 2                                                        23.73 m²
  Badruimte 3                                                         1.89 m²
  Slaapkamer 4 (+1 kast)                                              9.16 m²
                                                                    ------      ------
  Totaal                                                            112.80 m²   113.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Zolder                                                              8.71 m²
  Berging                                                             2.44 m²
                                                                    ------      ------
  Totaal                                                             11.15 m²     8.25 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Woonkamer 1                                                                 2.00 pt
    - Slaapkamer 1                                                                2.00 pt
    - Slaapkamer 2                                                                2.00 pt
    - Badruimte 1                                                                 2.00 pt
    - Slaapkamer 3                                                                2.00 pt
    - Keuken 1                                                                    2.00 pt
    - Keuken 2                                                                    2.00 pt
    - Badruimte 2                                                                 2.00 pt
    - Woonkamer 2                                                                 2.00 pt
    - Badruimte 3                                                                 2.00 pt
    - Slaapkamer 4                                                                2.00 pt
                                                                                ------
  Totaal                                                                         22.00 pt

BUITENRUIMTEN
  Privé                                                              35.00 m²    12.25 pt
    - Dakterras                                                       4.46 m²
    - Tuin                                                           30.65 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
                                                                                ------
  Totaal                                                                         14.25 pt

ENERGIEPRESTATIE
  B (Energie-index)                                                              34.00 pt
                                                                                ------
  Totaal                                                                         34.00 pt

KEUKEN
  Keuken 1
    - Lengte aanrecht                                              1875.00 mm     4.00 pt
  Keuken 2
    - Lengte aanrecht                                              1920.00 mm     4.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt

SANITAIR
  Badruimte 1
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
  Badruimte 2
    - Staand Toilet                                                   1.00 st     2.00 pt
    - Douche                                                          1.00 st     4.00 pt
  Badruimte 3
    - Staand Toilet                                                   1.00 st     2.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
                                                                                ------
  Totaal                                                                         18.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       759000.00 EUR
  Onderdeel I                                                                    49.51 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   25.29 pt
    - Oppervlakte van vertrekken en overige ruimten                 124.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.05 pt
                                                                                ------
  Totaal                                                                         74.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "41123000005",
  "bouwjaar": 1896,
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
      "begindatum": "2019-05-13",
      "einddatum": "2029-05-13",
      "registratiedatum": "2019-11-21T10:55:31+01:00",
      "label": {
        "code": "B",
        "naam": "B"
      },
      "waarde": "1.39"
    }
  ],
  "gebruiksoppervlakte": 170,
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
      "id": "Space_23702354",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 56.3198,
      "oppervlakte": 18.6425,
      "verwarmd": true
    },
    {
      "id": "Space_23703105",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "inhoud": 16.1584,
      "oppervlakte": 8.70953,
      "bouwkundigeElementen": [
        {
          "id": "Trap_123",
          "naam": "Trap",
          "omschrijving": "(vaste) trap naar de zolder",
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
      "verwarmd": false
    },
    {
      "id": "Space_23702793",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "OVE",
        "naam": "Overloop"
      },
      "naam": "Overloop",
      "inhoud": 15.3509,
      "oppervlakte": 5.11304,
      "verbondenRuimten": [
        {
          "id": "Space_23702802",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 1.18008,
          "oppervlakte": 0.396,
          "verwarmd": false
        }
      ],
      "verwarmd": false
    },
    {
      "id": "Space_23703132",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "inhoud": 5.21066,
      "oppervlakte": 2.43587,
      "verwarmd": false
    },
    {
      "id": "Space_72739147",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.325386,
      "oppervlakte": 0.10919,
      "verwarmd": false
    },
    {
      "id": "Space_23702848",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "DAK",
        "naam": "Dakterras"
      },
      "naam": "Dakterras",
      "breedte": 2410.0,
      "hoogte": 3280.0,
      "inhoud": 14.6212,
      "lengte": 1860.0,
      "oppervlakte": 4.4577,
      "verwarmd": false
    },
    {
      "id": "Space_72738750",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.328662,
      "oppervlakte": 0.10919,
      "verwarmd": false
    },
    {
      "id": "Space_23703095",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 25.7295,
      "oppervlakte": 12.1949,
      "verwarmd": true
    },
    {
      "id": "Space_23702802",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 1.18008,
      "oppervlakte": 0.396,
      "verwarmd": false
    },
    {
      "id": "Space_23702358",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 51.9543,
      "oppervlakte": 17.2606,
      "verwarmd": true
    },
    {
      "id": "Space_23703087",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 14.5435,
      "oppervlakte": 6.79878,
      "bouwkundigeElementen": [
        {
          "id": "Douche_23703090",
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
          "id": "Wastafel_23703089",
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
      "id": "Space_23703107",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 24.3432,
      "oppervlakte": 10.2396,
      "verwarmd": true
    },
    {
      "id": "Space_23702760",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 17.1534,
      "oppervlakte": 5.75616,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_72739118",
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
          "lengte": 1875.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_23702332",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 16.9645,
      "oppervlakte": 5.37699,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_72738742",
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
          "lengte": 1920.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_23702457",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "breedte": 4790.0,
      "hoogte": 2438.0,
      "inhoud": 74.7335,
      "lengte": 7590.0,
      "oppervlakte": 30.6486,
      "verwarmd": false
    },
    {
      "id": "Space_23702799",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 5.22735,
      "oppervlakte": 1.75414,
      "bouwkundigeElementen": [
        {
          "id": "Douche_72739130",
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
          "id": "Closetcombinatie_23702800",
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
      "id": "Space_72738748",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.328662,
      "oppervlakte": 0.10919,
      "verwarmd": false
    },
    {
      "id": "Space_23702771",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "inhoud": 70.7283,
      "oppervlakte": 23.7343,
      "verwarmd": true
    },
    {
      "id": "Space_23702450",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "TRH",
        "naam": "Trappenhuis"
      },
      "naam": "Trappenhuis",
      "inhoud": 7.95425,
      "oppervlakte": 2.57427,
      "verwarmd": false
    },
    {
      "id": "Space_72739125",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 0.325386,
      "oppervlakte": 0.10919,
      "verwarmd": false
    },
    {
      "id": "Space_23702339",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 6.05195,
      "oppervlakte": 1.88741,
      "bouwkundigeElementen": [
        {
          "id": "Douche_72738747",
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
          "id": "Wastafel_72738745",
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
          "id": "Closetcombinatie_23702340",
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
      "id": "Space_72739133",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast",
      "inhoud": 1.23491,
      "oppervlakte": 0.4144,
      "verwarmd": false
    },
    {
      "id": "Space_72739122",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 26.0682,
      "oppervlakte": 8.74772,
      "verbondenRuimten": [
        {
          "id": "Space_72739133",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimtes"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "inhoud": 1.23491,
          "oppervlakte": 0.4144,
          "verwarmd": false
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_23702451",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 9.27641,
      "oppervlakte": 3.08186,
      "verwarmd": false
    },
    {
      "id": "Space_72738788",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 10.9249,
      "oppervlakte": 3.62953,
      "verwarmd": false
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 978000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 987000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 759000.0,
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
      "punten": 113.0,
      "woningwaarderingen": [
        {
          "aantal": 18.64,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702354",
            "naam": "Woonkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 12.19,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23703095",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 17.26,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702358",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 6.8,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23703087",
            "naam": "Badruimte 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 10.24,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23703107",
            "naam": "Slaapkamer 3",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 5.76,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702760",
            "naam": "Keuken 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 5.38,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702332",
            "naam": "Keuken 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 1.75,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702799",
            "naam": "Badruimte 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 23.73,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702771",
            "naam": "Woonkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 1.89,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_23702339",
            "naam": "Badruimte 3",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 9.16,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_72739122",
            "naam": "Slaapkamer 4 (+1 kast)",
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
      "punten": 8.25,
      "woningwaarderingen": [
        {
          "aantal": 8.71,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_23703105",
            "naam": "Zolder",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 2.44,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_23703132",
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
      "punten": 22.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702354",
            "naam": "Woonkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23703095",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702358",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23703087",
            "naam": "Badruimte 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23703107",
            "naam": "Slaapkamer 3",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702760",
            "naam": "Keuken 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702332",
            "naam": "Keuken 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702799",
            "naam": "Badruimte 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702771",
            "naam": "Woonkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_23702339",
            "naam": "Badruimte 3",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_72739122",
            "naam": "Slaapkamer 4",
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
      "punten": 14.25,
      "woningwaarderingen": [
        {
          "aantal": 35.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 12.25
        },
        {
          "aantal": 4.46,
          "criterium": {
            "id": "buitenruimten__prive__Space_23702848",
            "naam": "Dakterras",
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
          "aantal": 30.65,
          "criterium": {
            "id": "buitenruimten__prive__Space_23702457",
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
            "naam": "B (Energie-index)"
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
      "punten": 8.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "keuken__Space_23702760",
            "naam": "Keuken 1"
          }
        },
        {
          "aantal": 1875.0,
          "criterium": {
            "id": "keuken__Space_23702760__lengte_aanrecht_Aanrecht_72739118",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_23702760"
            },
            "meeteenheid": {
              "code": "MIL",
              "naam": "Millimeter"
            }
          },
          "punten": 4.0
        },
        {
          "criterium": {
            "id": "keuken__Space_23702332",
            "naam": "Keuken 2"
          }
        },
        {
          "aantal": 1920.0,
          "criterium": {
            "id": "keuken__Space_23702332__lengte_aanrecht_Aanrecht_72738742",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_23702332"
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
      "punten": 18.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_23703087",
            "naam": "Badruimte 1"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_23703087__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23703087"
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
            "id": "sanitair__Space_23703087__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23703087"
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
            "id": "sanitair__Space_23702799",
            "naam": "Badruimte 2"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_23702799__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23702799"
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
            "id": "sanitair__Space_23702799__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23702799"
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
            "id": "sanitair__Space_23702339",
            "naam": "Badruimte 3"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_23702339__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23702339"
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
            "id": "sanitair__Space_23702339__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23702339"
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
            "id": "sanitair__Space_23702339__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_23702339"
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
      "punten": 74.75,
      "woningwaarderingen": [
        {
          "aantal": 759000.0,
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
          "punten": 49.51
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
          "punten": 25.29
        },
        {
          "aantal": 124.0,
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
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1955.52,
  "punten": 292.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1955.52
}
```
