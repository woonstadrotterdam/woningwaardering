# test_woning_gebouwd_voor_2015_met_renovatie_buiten_2015_tot_en_met_2019_krijgt_geen_minimum_van_40_punten[renovatie_eind_2014]

Een woning gebouwd voor 2015 die buiten 2015 tot en met 2019 is gerenoveerd, krijgt geen minimum van 40 punten voor de WOZ-waarde.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.5; wettekst,
Bijlage I onder A, onderdeel 11.2.

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       259999.00 EUR
  Onderdeel I                                                                    16.96 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   17.91 pt
    - Oppervlakte van vertrekken en overige ruimten                  60.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.12 pt
                                                                                ------
  Totaal                                                                         34.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "meergezinswoning_van_71_m2",
  "bouwjaar": 1912,
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
      "begindatum": "2021-02-23",
      "einddatum": "2027-02-23",
      "label": {
        "code": "AP4",
        "naam": "A++++"
      },
      "waarde": "1.48"
    }
  ],
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
  "renovatie": {
    "omschrijving": "hoogniveau renovatie",
    "datum": "2014-12-31",
    "bedragInvestering": 10000.0
  },
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
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 219999.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 239999.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 259999.0,
      "waardepeildatum": "2024-01-01"
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
  "punten": 34.75,
  "woningwaarderingen": [
    {
      "aantal": 259999.0,
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
      "punten": 16.96
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
      "punten": 17.91
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
      "punten": -0.12
    }
  ]
}
```
