# test_model_onzelfstandige_woonruimten[15004000185]

Het stelsel onzelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Onzelfstandige woonruimte in een meergezinswoning uit 1998, zonder energieprestatie: een eigen slaapkamer, en een keuken, hal, toilet en badruimte die met een tweede onzelfstandige woonruimte worden gedeeld.

## Rapport

```text
SAMENVATTING 15004000185
  Oppervlakte van vertrekken                                                     25.00 pt
  Oppervlakte van overige ruimten
  Verkoeling en verwarming                                                        2.00 pt
  Energieprestatie                                                                8.50 pt
  Keuken                                                                          3.50 pt
  Sanitair                                                                        3.00 pt
  Buitenruimten
  Gemeenschappelijke binnenruimten gedeeld met meerdere adressen
  Gemeenschappelijke parkeerruimten
  Punten voor de WOZ-waarde                                                      12.00 pt
  Bijzondere voorzieningen
  Aftrekpunten
  Prijsopslag monumenten
                                                                                ------
  Totaal afgerond op hele punten                                                 54.00 pt
  Maximaal redelijke huur                                           550.19 EUR

OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Slaapkamer                                                     20.04 m²
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken                                                          7.50 m²
    - Badruimte                                                       1.70 m²
                                                                                ------
  Totaal                                                                         25.00 pt

VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Slaapkamer                                                                2.00 pt
                                                                                ------
  Totaal                                                                          2.00 pt

ENERGIEPRESTATIE
  Bouwjaar 1998                                                      24.64 m²     8.62 pt
  Afronding op kwartpunten                                                       -0.12 pt
                                                                                ------
  Totaal                                                                          8.50 pt

KEUKEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Keuken
      - Lengte aanrecht                                            2220.00 mm     3.50 pt
                                                                                ------
  Totaal                                                                          3.50 pt

SANITAIR
  Gedeeld met 2 onzelfstandige woonruimten
    - Toilet
      - Staand Toilet                                                 1.00 st     1.50 pt
    - Badruimte
      - Douche                                                        1.00 st     1.50 pt
                                                                                ------
  Totaal                                                                          3.00 pt

PUNTEN VOOR DE WOZ-WAARDE
  Percentage verschil                                                -0.07       12.00 pt
    - WOZ-waarde op waardepeildatum 01-01-2024                   205000.00 EUR
    - Gebruiksoppervlakte                                            58.00 m²
    - WOZ-waarde per m²                                            3534.48 EUR
    - Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond             3537.00 EUR
                                                                                ------
  Totaal                                                                         12.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (15004000185): 'energieprestaties' is None

## Input

```json
{
  "id": "15004000185",
  "bouwjaar": 1998,
  "adres": {
    "huisnummer": "",
    "huisnummerToevoeging": "",
    "postcode": "",
    "straatnaam": "",
    "woonplaats": {
      "code": "3086",
      "naam": "ROTTERDAM"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "id": "",
    "bagGebruikersOppervlakte": 58,
    "bagIdentificatie": ""
  },
  "energieprestaties": [],
  "monumenten": [],
  "panden": [
    {
      "idExtern": "",
      "soort": {
        "code": "MGW",
        "naam": "Meergezinswoning"
      }
    }
  ],
  "ruimten": [
    {
      "id": "Space_29425491",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 49.4717,
      "oppervlakte": 20.044,
      "bouwkundigeElementen": [
        {
          "id": "Radiator_29424408",
          "naam": "Radiator",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening algemeen"
          },
          "detailSoort": {
            "code": "RAD",
            "naam": "Radiator"
          }
        }
      ],
      "verwarmd": true
    },
    {
      "id": "Space_29425492",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 18.64,
      "oppervlakte": 7.5,
      "bouwkundigeElementen": [
        {
          "id": "Aanrecht_29424502",
          "naam": "Aanrecht",
          "soort": {
            "code": "KEU",
            "naam": "Keuken voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 2220.0
        }
      ],
      "verwarmd": false,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "Space_29425493",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "HAL",
        "naam": "Hal"
      },
      "naam": "Hal",
      "inhoud": 11.6,
      "oppervlakte": 4.7,
      "verwarmd": false,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "Space_29425495",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toilet"
      },
      "naam": "Toilet",
      "inhoud": 2.56,
      "oppervlakte": 1.0,
      "verwarmd": false,
      "installaties": [
        {
          "code": "STO",
          "naam": "Staand toilet"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "Space_29425496",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 4.12,
      "oppervlakte": 1.7,
      "verwarmd": false,
      "installaties": [
        {
          "code": "DOU",
          "naam": "Douche"
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ONZ",
    "naam": "Onzelfstandige woonruimten"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 205000.0,
      "waardepeildatum": "2024-01-01"
    },
    {
      "vastgesteldeWaarde": 184000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 148000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 124000.0,
      "waardepeildatum": "2021-01-01"
    },
    {
      "vastgesteldeWaarde": 108000.0,
      "waardepeildatum": "2020-01-01"
    },
    {
      "vastgesteldeWaarde": 96000.0,
      "waardepeildatum": "2019-01-01"
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
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OVZ",
          "naam": "Oppervlakte van vertrekken"
        }
      },
      "punten": 25.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "oppervlakte_van_vertrekken__prive",
            "naam": "Privé"
          }
        },
        {
          "aantal": 20.04,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__prive__Space_29425491",
            "naam": "Slaapkamer",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_vertrekken__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "criterium": {
            "id": "oppervlakte_van_vertrekken__gedeeld_met_2_onzelfstandige_woonruimten",
            "naam": "Gedeeld met 2 onzelfstandige woonruimten"
          }
        },
        {
          "aantal": 7.5,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425492",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_vertrekken__gedeeld_met_2_onzelfstandige_woonruimten"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 1.7,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425496",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_vertrekken__gedeeld_met_2_onzelfstandige_woonruimten"
            },
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
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
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
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 2.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__prive",
            "naam": "Privé"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__prive"
            }
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__Space_29425491",
            "naam": "Slaapkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 8.5,
      "woningwaarderingen": [
        {
          "aantal": 24.64,
          "criterium": {
            "id": "energieprestatie__bouwjaar",
            "naam": "Bouwjaar 1998",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 8.62
        },
        {
          "criterium": {
            "id": "energieprestatie__afronding_op_kwartpunten",
            "naam": "Afronding op kwartpunten"
          },
          "punten": -0.12
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "KEU",
          "naam": "Keuken"
        }
      },
      "punten": 3.5,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten",
            "naam": "Gedeeld met 2 onzelfstandige woonruimten"
          }
        },
        {
          "criterium": {
            "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425492",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten"
            }
          }
        },
        {
          "aantal": 2220.0,
          "criterium": {
            "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425492__lengte_aanrecht_Aanrecht_29424502",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425492"
            },
            "meeteenheid": {
              "code": "MIL",
              "naam": "Millimeter"
            }
          },
          "punten": 3.5
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "SAN",
          "naam": "Sanitair"
        }
      },
      "punten": 3.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten",
            "naam": "Gedeeld met 2 onzelfstandige woonruimten"
          }
        },
        {
          "criterium": {
            "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425495",
            "naam": "Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten"
            }
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425495__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425495"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 1.5
        },
        {
          "criterium": {
            "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425496",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten"
            }
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425496__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__gedeeld_met_2_onzelfstandige_woonruimten__Space_29425496"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 1.5
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BUI",
          "naam": "Buitenruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GBA",
          "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
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
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "WOZ",
          "naam": "Punten voor de WOZ-waarde"
        }
      },
      "punten": 12.0,
      "woningwaarderingen": [
        {
          "aantal": -0.0711688,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__percentage_verschil",
            "naam": "Percentage verschil"
          },
          "punten": 12.0
        },
        {
          "aantal": 205000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__percentage_verschil__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2024",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__percentage_verschil"
            },
            "meeteenheid": {
              "code": "EUR",
              "naam": "Euro"
            }
          }
        },
        {
          "aantal": 58.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__percentage_verschil__gebruiksoppervlakte",
            "naam": "Gebruiksoppervlakte",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__percentage_verschil"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 3534.48276,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__percentage_verschil__woz_waarde_per_m2",
            "naam": "WOZ-waarde per m²",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__percentage_verschil"
            },
            "meeteenheid": {
              "code": "EUR",
              "naam": "Euro"
            }
          }
        },
        {
          "aantal": 3537.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__percentage_verschil__gemiddelde_woz_waarde_per_m2",
            "naam": "Gemiddelde WOZ-waarde per m² voor Groot-Rijnmond",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__percentage_verschil"
            },
            "meeteenheid": {
              "code": "EUR",
              "naam": "Euro"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
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
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "AFT",
          "naam": "Aftrekpunten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ONZ",
          "naam": "Onzelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "PMO",
          "naam": "Prijsopslag monumenten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 550.19,
  "punten": 54.0,
  "stelsel": {
    "code": "ONZ",
    "naam": "Onzelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 550.19
}
```
