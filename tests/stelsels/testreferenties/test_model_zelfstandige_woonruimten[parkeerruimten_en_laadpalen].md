# test_model_zelfstandige_woonruimten[parkeerruimten_en_laadpalen]

Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt.

eenheid met alle parkeerruimten en laadpalen die zonder waarschuwing gewaardeerd worden

## Rapport

```text
SAMENVATTING parkeerruimten_en_laadpalen
  Oppervlakte van vertrekken                                                     57.00 pt
  Oppervlakte van overige ruimten                                                15.00 pt
  Verkoeling en verwarming                                                        6.00 pt
  Buitenruimten                                                                  15.00 pt
  Energieprestatie                                                               -9.00 pt
  Keuken                                                                          7.00 pt
  Sanitair                                                                       10.00 pt
  Gemeenschappelijke parkeerruimten                                              27.75 pt
  Gemeenschappelijke vertrekken, overige ruimten en voorzieningen
  Punten voor de WOZ-waarde                                                      30.50 pt
  Bijzondere voorzieningen                                                        6.00 pt
  Prijsopslag monumenten en nieuwbouw
                                                                                ------
  Totaal afgerond op hele punten                                                165.00 pt
  Maximaal redelijke huur                                          1083.88 EUR

OPPERVLAKTE VAN VERTREKKEN
  Keuken                                                             15.74 m²
  Slaapkamer                                                         39.82 m²
  Badruimte                                                           1.77 m²
                                                                    ------      ------
  Totaal                                                             57.33 m²    57.00 pt

OPPERVLAKTE VAN OVERIGE RUIMTEN
  Berging                                                            19.67 m²
                                                                    ------      ------
  Totaal                                                             19.67 m²    15.00 pt

VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Keuken                                                                      2.00 pt
    - Slaapkamer                                                                  2.00 pt
    - Badruimte                                                                   2.00 pt
                                                                                ------
  Totaal                                                                          6.00 pt

BUITENRUIMTEN
  Privé                                                              40.00 m²    14.00 pt
    - Carport 1                                                      15.00 m²
    - Parkeerplaats                                                  15.00 m²
    - Carport 2                                                      10.00 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Maximaal 15 punten                                                             -1.00 pt
                                                                                ------
  Totaal                                                                         15.00 pt

ENERGIEPRESTATIE
  F                                                                              -9.00 pt
                                                                                ------
  Totaal                                                                         -9.00 pt

KEUKEN
  Keuken
    - Lengte aanrecht                                              2100.00 mm     7.00 pt
                                                                                ------
  Totaal                                                                          7.00 pt

SANITAIR
  Keuken
    - Wastafel                                                        1.00 st     1.00 pt
  Badruimte
    - Wastafel                                                        1.00 st     1.00 pt
    - Douche                                                          1.00 st     4.00 pt
  Toiletruimte
    - Staand Toilet                                                   1.00 st     3.00 pt
    - Wastafel                                                        1.00 st     1.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt

GEMEENSCHAPPELIJKE PARKEERRUIMTEN
  Privé
    - Parkeerplek in inpandige afgesloten parkeergarage 1 (Type I)    1.00 st     9.00 pt
    - Laadpaal                                                        1.00 st     2.00 pt
    - Parkeerplek in uitpandige afgesloten parkeergarage (Type I)     1.00 st     9.00 pt
  Gedeeld met 3 adressen
    - Parkeerplek in inpandige afgesloten parkeergarage 2 (Type I)    1.00 st     3.00 pt
    - Laadpaal                                                        1.00 st     0.67 pt
    - Parkeerplek buiten behorend bij complex (Type III)              1.00 st     1.33 pt
    - Laadpaal                                                        1.00 st     0.67 pt
    - Parkeerplek buiten met dak behorend bij complex (Type II)       1.00 st     2.00 pt
  Afronding op kwartpunten                                                        0.08 pt
                                                                                ------
  Totaal                                                                         27.75 pt

PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       264000.00 EUR
  Onderdeel I                                                                    17.22 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   13.30 pt
    - Oppervlakte van vertrekken en overige ruimten                  82.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.02 pt
                                                                                ------
  Totaal                                                                         30.50 pt

BIJZONDERE VOORZIENINGEN
  Privé
    - Laadpalen                                                       3.00 st     6.00 pt
                                                                                ------
  Totaal                                                                          6.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "id": "parkeerruimten_en_laadpalen",
  "bouwjaar": 1993,
  "adres": {
    "huisnummer": "",
    "huisnummerToevoeging": "",
    "postcode": "",
    "straatnaam": ""
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
      "begindatum": "2024-03-27",
      "einddatum": "2034-03-27",
      "registratiedatum": "2024-03-27T14:51:32.980000+01:00",
      "label": {
        "code": "F",
        "naam": "F"
      },
      "waarde": "160.92"
    }
  ],
  "monumenten": [],
  "oppervlakten": [
    {
      "soort": {
        "code": "GTZ",
        "naam": "Gebruiksoppervlakte thermische zone"
      },
      "waarde": "82.77"
    }
  ],
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
      "id": "Space_90696842",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "inhoud": 67.8456,
      "oppervlakte": 15.7414,
      "bouwkundigeElementen": [
        {
          "id": "Wastafel_90696845",
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
          "id": "Aanrecht_90696849",
          "naam": "Aanrecht",
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
      "verwarmd": true
    },
    {
      "id": "Space_90696852",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "inhoud": 171.627,
      "oppervlakte": 39.8206,
      "bouwkundigeElementen": [],
      "verwarmd": true
    },
    {
      "id": "Space_90696911",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "inhoud": 84.788,
      "oppervlakte": 19.6724,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_90696915",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BAD",
        "naam": "Badruimte"
      },
      "naam": "Badruimte",
      "inhoud": 7.62224,
      "oppervlakte": 1.7685,
      "bouwkundigeElementen": [
        {
          "id": "Douche_90696919",
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
          "id": "Wastafel_90696922",
          "naam": "Wastafel",
          "soort": {
            "code": "SAN",
            "naam": "Sanitaire voorziening"
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
      "id": "Space_90696925",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "SCH",
        "naam": "Schacht"
      },
      "naam": "Schacht",
      "inhoud": 3.76263,
      "oppervlakte": 0.873,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "Space_90696929",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimtes"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "inhoud": 5.0427,
      "oppervlakte": 1.17,
      "bouwkundigeElementen": [
        {
          "id": "Closetcombinatie_90696933",
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
          "id": "Fontein_90696936",
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
      "verwarmd": false
    },
    {
      "id": "Space_90696940",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "ENT",
        "naam": "Entree"
      },
      "naam": "Entree",
      "inhoud": 20.2936,
      "oppervlakte": 4.7085,
      "bouwkundigeElementen": [],
      "verwarmd": false
    },
    {
      "id": "pip_prive",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PIP",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in inpandige afgesloten parkeergarage",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 1,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "pip_3_adressen",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PIP",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in inpandige afgesloten parkeergarage",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 3,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "pbc_3_adressen",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek buiten behorend bij complex",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 3,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "pup_prive",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PUP",
        "naam": "Parkeerplek in uitpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in uitpandige afgesloten parkeergarage",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 1,
      "aantal": 1
    },
    {
      "id": "pbd_3_adressen",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBD",
        "naam": "Parkeerplek buiten met dak behorend bij complex"
      },
      "naam": "Parkeerplek buiten met dak behorend bij complex",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 3,
      "aantal": 1
    },
    {
      "id": "pip_10m2",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PIP",
        "naam": "Parkeerplek in inpandige afgesloten parkeergarage"
      },
      "naam": "Parkeerplek in inpandige afgesloten parkeergarage",
      "breedte": 2000.0,
      "lengte": 5000.0,
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 1,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "carport_prive",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 1,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "parkeerplaats_prive",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "PAR",
        "naam": "Parkeerplaats"
      },
      "naam": "Parkeerplaats",
      "breedte": 3000.0,
      "lengte": 5000.0,
      "oppervlakte": 15.0,
      "gedeeldMetAantalAdressen": 1,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 1
    },
    {
      "id": "carport_prive_10m2",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "breedte": 2000.0,
      "lengte": 5000.0,
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 1,
      "aantal": 1
    }
  ],
  "Woningwaarderingstelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimte"
  },
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 264000.0,
      "waardepeildatum": "2024-01-01"
    },
    {
      "vastgesteldeWaarde": 261000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 250000.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 205000.0,
      "waardepeildatum": "2021-01-01"
    },
    {
      "vastgesteldeWaarde": 166000.0,
      "waardepeildatum": "2020-01-01"
    },
    {
      "vastgesteldeWaarde": 142000.0,
      "waardepeildatum": "2019-01-01"
    },
    {
      "vastgesteldeWaarde": 137000.0,
      "waardepeildatum": "2018-01-01"
    },
    {
      "vastgesteldeWaarde": 128000.0,
      "waardepeildatum": "2017-01-01"
    },
    {
      "vastgesteldeWaarde": 61000.0,
      "waardepeildatum": "2016-01-01"
    },
    {
      "vastgesteldeWaarde": 59000.0,
      "waardepeildatum": "2015-01-01"
    },
    {
      "vastgesteldeWaarde": 59000.0,
      "waardepeildatum": "2014-01-01"
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
      "punten": 57.0,
      "woningwaarderingen": [
        {
          "aantal": 15.74,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_90696842",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 39.82,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_90696852",
            "naam": "Slaapkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 1.77,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_90696915",
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
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 19.67,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_90696911",
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
      "punten": 6.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          }
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_90696842",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_90696852",
            "naam": "Slaapkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__verwarmde_vertrekken__Space_90696915",
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
          "aantal": 40.0,
          "criterium": {
            "id": "buitenruimten__prive",
            "naam": "Privé",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 14.0
        },
        {
          "aantal": 15.0,
          "criterium": {
            "id": "buitenruimten__prive__carport_prive",
            "naam": "Carport 1",
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
          "aantal": 15.0,
          "criterium": {
            "id": "buitenruimten__prive__parkeerplaats_prive",
            "naam": "Parkeerplaats",
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
          "aantal": 10.0,
          "criterium": {
            "id": "buitenruimten__prive__carport_prive_10m2",
            "naam": "Carport 2",
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
          "punten": -1.0
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
      "punten": -9.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "F"
          },
          "punten": -9.0
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
            "id": "keuken__Space_90696842",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 2100.0,
          "criterium": {
            "id": "keuken__Space_90696842__lengte_aanrecht_Aanrecht_90696849",
            "naam": "Lengte aanrecht",
            "bovenliggendeCriterium": {
              "id": "keuken__Space_90696842"
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
      "punten": 10.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "sanitair__Space_90696842",
            "naam": "Keuken"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_90696842__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_90696842"
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
            "id": "sanitair__Space_90696915",
            "naam": "Badruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_90696915__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_90696915"
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
            "id": "sanitair__Space_90696915__douche",
            "naam": "Douche",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_90696915"
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
            "id": "sanitair__Space_90696929",
            "naam": "Toiletruimte"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_90696929__staand_toilet",
            "naam": "Staand Toilet",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_90696929"
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
            "id": "sanitair__Space_90696929__wastafel",
            "naam": "Wastafel",
            "bovenliggendeCriterium": {
              "id": "sanitair__Space_90696929"
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
      "punten": 27.75,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__prive",
            "naam": "Privé"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__prive__parkeerplek_in_inpandige_afgesloten_parkeergarage_1_type_i",
            "naam": "Parkeerplek in inpandige afgesloten parkeergarage 1 (Type I)",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__prive"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 9.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__prive__parkeerplek_in_inpandige_afgesloten_parkeergarage_1_type_i_laadpaal",
            "naam": "Laadpaal",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__prive"
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
            "id": "gemeenschappelijke_parkeerruimten__prive__parkeerplek_in_uitpandige_afgesloten_parkeergarage_type_i",
            "naam": "Parkeerplek in uitpandige afgesloten parkeergarage (Type I)",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__prive"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 9.0
        },
        {
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen",
            "naam": "Gedeeld met 3 adressen"
          }
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__parkeerplek_in_inpandige_afgesloten_parkeergarage_2_type_i",
            "naam": "Parkeerplek in inpandige afgesloten parkeergarage 2 (Type I)",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
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
            "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__parkeerplek_in_inpandige_afgesloten_parkeergarage_2_type_i_laadpaal",
            "naam": "Laadpaal",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 0.67
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii",
            "naam": "Parkeerplek buiten behorend bij complex (Type III)",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 1.33
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__parkeerplek_buiten_behorend_bij_complex_type_iii_laadpaal",
            "naam": "Laadpaal",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 0.67
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen__parkeerplek_buiten_met_dak_behorend_bij_complex_type_ii",
            "naam": "Parkeerplek buiten met dak behorend bij complex (Type II)",
            "bovenliggendeCriterium": {
              "id": "gemeenschappelijke_parkeerruimten__gedeeld_met_3_adressen"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "gemeenschappelijke_parkeerruimten__afronding_op_kwartpunten",
            "naam": "Afronding op kwartpunten"
          },
          "punten": 0.08
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
      "punten": 30.5,
      "woningwaarderingen": [
        {
          "aantal": 264000.0,
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
          "punten": 17.22
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
          "punten": 13.3
        },
        {
          "aantal": 82.0,
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
          "punten": -0.02
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
      "punten": 6.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "bijzondere_voorzieningen__prive",
            "naam": "Privé"
          }
        },
        {
          "aantal": 3.0,
          "criterium": {
            "id": "bijzondere_voorzieningen__prive__laadpalen",
            "naam": "Laadpalen",
            "bovenliggendeCriterium": {
              "id": "bijzondere_voorzieningen__prive"
            },
            "meeteenheid": {
              "code": "STU",
              "naam": "Stuks"
            }
          },
          "punten": 6.0
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
          "code": "PMN",
          "naam": "Prijsopslag monumenten en nieuwbouw"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1083.88,
  "punten": 165.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1083.88
}
```
