# test_model_onzelfstandige_woonruimten[toe_te_rekenen_oppervlakte_10_40]

Het stelsel onzelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

Eerst delen, dan salderen, dan éénmaal afronden (#391): privé 10,40 m² + gemeenschappelijk 40,40 m² / 4, energielabel A.

Verwacht: vertrekken 21 punten, overige 15,75 punten, energieprestatie 13,25 punten (20,50 × 0,65).

## Rapport

```text
SAMENVATTING toe_te_rekenen_oppervlakte_10_40
  Oppervlakte van vertrekken                                                     21.00 pt
  Oppervlakte van overige ruimten                                                15.75 pt
  Verkoeling en verwarming
  Energieprestatie                                                               13.25 pt
  Keuken
  Sanitair
  Buitenruimten
  Gemeenschappelijke binnenruimten gedeeld met meerdere adressen
  Gemeenschappelijke parkeerruimten
  Punten voor de WOZ-waarde                                                      12.00 pt
  Bijzondere voorzieningen
  Aftrekpunten
  Prijsopslag monumenten
                                                                                ------
  Totaal afgerond op hele punten                                                 62.00 pt
  Maximaal redelijke huur                                           621.84 EUR

OPPERVLAKTE VAN VERTREKKEN
  Privé
    - Slaapkamer                                                     10.40 m²
  Gedeeld met 4 onzelfstandige woonruimten
    - Woonkamer                                                      40.40 m²
                                                                                ------
  Totaal                                                                         21.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Berging                                                        10.40 m²
  Gedeeld met 4 onzelfstandige woonruimten
    - Berging gedeeld                                                40.40 m²
                                                                                ------
  Totaal                                                                         15.75 pt

ENERGIEPRESTATIE
  A                                                                  20.50 m²    13.33 pt
  Afronding op kwartpunten                                                       -0.08 pt
                                                                                ------
  Totaal                                                                         13.25 pt

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

Geen.

## Input

```json
{
  "id": "toe_te_rekenen_oppervlakte_10_40",
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
      "begindatum": "2021-01-01",
      "einddatum": "2031-01-01",
      "registratiedatum": "2021-01-15T00:00:00+01:00",
      "label": {
        "code": "A",
        "naam": "A"
      }
    }
  ],
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
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.4
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
      "oppervlakte": 40.4,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
    },
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "oppervlakte": 10.4
    },
    {
      "id": "berging_gedeeld",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging gedeeld",
      "oppervlakte": 40.4,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
      "punten": 21.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "oppervlakte_van_vertrekken__prive",
            "naam": "Privé"
          }
        },
        {
          "aantal": 10.4,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__prive__slaapkamer",
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
            "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten",
            "naam": "Gedeeld met 4 onzelfstandige woonruimten"
          }
        },
        {
          "aantal": 40.4,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten__woonkamer",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten"
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
      "punten": 15.75,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__prive",
            "naam": "Privé"
          }
        },
        {
          "aantal": 10.4,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__prive__berging",
            "naam": "Berging",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_overige_ruimten__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten",
            "naam": "Gedeeld met 4 onzelfstandige woonruimten"
          }
        },
        {
          "aantal": 40.4,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten__berging_gedeeld",
            "naam": "Berging gedeeld",
            "bovenliggendeCriterium": {
              "id": "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten"
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
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
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
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 13.25,
      "woningwaarderingen": [
        {
          "aantal": 20.5,
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "A",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 13.33
        },
        {
          "criterium": {
            "id": "energieprestatie__afronding_op_kwartpunten",
            "naam": "Afronding op kwartpunten"
          },
          "punten": -0.08
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
          "code": "SAN",
          "naam": "Sanitair"
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
  "maximaleHuur": 621.84,
  "punten": 62.0,
  "stelsel": {
    "code": "ONZ",
    "naam": "Onzelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 621.84
}
```
