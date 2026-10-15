# test_eenheid_zonder_woz_waarde_wordt_met_waarschuwing_gewaardeerd_met_de_minimum_woz_waarde

Een eenheid zonder WOZ-waarde wordt met een waarschuwing gewaardeerd met de minimum WOZ-waarde van € 85.806.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
Bijlage I onder A, onderdeel 11.1.

Een woning gebouwd in 2015 tot en met 2019 die voor de rubrieken 1 tot en
met 10 en 12 minstens 110 punten haalt, krijgt minimaal 40 punten voor de
WOZ-waarde.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
Bijlage I onder A, onderdeel 11.2.

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  Minimum WOZ-waarde (geen relevante WOZ-waarde beschikbaar)      85806.00 EUR
  Onderdeel I                                                                     5.06 pt
    - Minimum WOZ-waarde gebruikt voor berekening                 85806.00 EUR
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                    5.34 pt
    - Minimum WOZ-waarde gebruikt voor berekening                 85806.00 EUR
    - Oppervlakte van vertrekken en overige ruimten                  60.00 m²
    - Factor II                                                     268.00 EUR
  Nieuwbouw: min. 40 punten                                                      29.60 pt
                                                                                ------
  Totaal                                                                         40.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (meergezinswoning_van_71_m2): 'energieprestaties' is None
- UserWarning: Eenheid (meergezinswoning_van_71_m2): geen WOZ-waarde aangeleverd

## Input

```json
{
  "id": "meergezinswoning_van_71_m2",
  "bouwjaar": 2016,
  "adres": {
    "huisnummer": "44",
    "huisnummerToevoeging": "",
    "postcode": "3012CJ",
    "woonplaats": {
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagIdentificatie": "0599010000320510"
  },
  "energieprestaties": [],
  "gebruiksoppervlakte": 71,
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
      "id": "balkon",
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
      "lengte": 1290.0,
      "oppervlakte": 1.82259
    },
    {
      "id": "technische_ruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TEC",
        "naam": "Technische ruimte"
      },
      "naam": "Technische ruimte",
      "oppervlakte": 0.3456,
      "bouwkundigeElementen": [
        {
          "id": "verwarmingstoestellen",
          "naam": "Verwarmingstoestellen",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTO",
            "naam": "Verwarmingstoestellen"
          }
        }
      ]
    },
    {
      "id": "schuur",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schuur"
      },
      "naam": "Schuur",
      "oppervlakte": 0.2345
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
      "oppervlakte": 3.584,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Douche",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "DOU",
            "naam": "Douche"
          }
        },
        {
          "id": "element_2",
          "naam": "Wastafel",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "WAS",
            "naam": "Wastafel"
          }
        }
      ],
      "verwarmd": true
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
      "oppervlakte": 9.5565,
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
          "lengte": 2100.0
        }
      ],
      "verbondenRuimten": [
        {
          "id": "kast3",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast3",
          "oppervlakte": 0.308
        },
        {
          "id": "technische_ruimte",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "TEC",
            "naam": "Technische ruimte"
          },
          "naam": "Technische ruimte",
          "oppervlakte": 0.3456,
          "bouwkundigeElementen": [
            {
              "id": "verwarmingstoestellen",
              "naam": "Verwarmingstoestellen",
              "soort": {
                "code": "VOO",
                "naam": "Voorziening"
              },
              "detailSoort": {
                "code": "VTO",
                "naam": "Verwarmingstoestellen"
              }
            }
          ]
        },
        {
          "id": "kast2",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast2",
          "oppervlakte": 0.312
        }
      ],
      "verwarmd": true
    },
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
      "oppervlakte": 25.96,
      "verbondenRuimten": [
        {
          "id": "kast1",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast1",
          "oppervlakte": 0.856
        }
      ],
      "verwarmd": true
    },
    {
      "id": "hal",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "oppervlakte": 6.198,
      "verbondenRuimten": [
        {
          "id": "kast4",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast4",
          "oppervlakte": 0.3575
        },
        {
          "id": "meterruimte",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "MET",
            "naam": "Meterruimte"
          },
          "naam": "Meterruimte",
          "oppervlakte": 0.2205
        }
      ],
      "verwarmd": true
    },
    {
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 6.486,
      "verwarmd": true
    },
    {
      "id": "kast1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast1",
      "oppervlakte": 0.856
    },
    {
      "id": "meterruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "MET",
        "naam": "Meterruimte"
      },
      "naam": "Meterruimte",
      "oppervlakte": 0.2205
    },
    {
      "id": "kast2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast2",
      "oppervlakte": 0.312
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
      "oppervlakte": 1.26375,
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
      ]
    },
    {
      "id": "kast3",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast3",
      "oppervlakte": 0.308
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 12.978,
      "verwarmd": true
    },
    {
      "id": "kast4",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "KAS",
        "naam": "Kast"
      },
      "naam": "Kast4",
      "oppervlakte": 0.3575
    }
  ]
}
```

## Output

```json
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
  "punten": 40.0,
  "woningwaarderingen": [
    {
      "aantal": 85806.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__woz_waarde",
        "naam": "Minimum WOZ-waarde (geen relevante WOZ-waarde beschikbaar)",
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
      "punten": 5.06
    },
    {
      "aantal": 85806.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_I__minimum_woz_waarde",
        "naam": "Minimum WOZ-waarde gebruikt voor berekening",
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
      "punten": 5.34
    },
    {
      "aantal": 85806.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__onderdeel_II__minimum_woz_waarde",
        "naam": "Minimum WOZ-waarde gebruikt voor berekening",
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
        "id": "punten_voor_de_woz_waarde__nieuwbouw_minimum_punten",
        "naam": "Nieuwbouw: min. 40 punten"
      },
      "punten": 29.6
    }
  ]
}
```
