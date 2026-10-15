# test_woning_tot_40_m2_gebouwd_na_2022_in_corop_gebied_amsterdam_krijgt_in_onderdeel_ii_het_gewone_kengetal

Een woning tot 40 m² in het COROP-gebied Amsterdam die na 2022 is gebouwd, krijgt in onderdeel II het gewone kengetal van € 242.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6; wettekst,
Bijlage I onder A, onderdeel 11.1.

De package rekent met de meest recent vastgestelde WOZ-waarde.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.1; wettekst,
Bijlage I onder A, onderdeel 11.1.

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       310000.00 EUR
  Onderdeel I                                                                    20.22 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   36.60 pt
    - Oppervlakte van vertrekken en overige ruimten                  35.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.07 pt
                                                                                ------
  Totaal                                                                         56.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 2023,
  "adres": {
    "huisnummer": "2",
    "huisnummerToevoeging": "",
    "postcode": "1012LG",
    "woonplaats": {
      "code": "3594",
      "naam": "Amsterdam"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagIdentificatie": "0363010000000002"
  },
  "energieprestaties": [
    {
      "soort": {
        "code": "energie_index",
        "naam": "Energie-index"
      },
      "status": {
        "code": "DEF",
        "naam": "Definitief"
      },
      "begindatum": "2023-01-01",
      "einddatum": "2033-01-01",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.2"
    }
  ],
  "gebruiksoppervlakte": 35,
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
      "oppervlakte": 20.0,
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
      "oppervlakte": 8.0,
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
          "lengte": 1800.0
        }
      ],
      "verwarmd": true
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
      "oppervlakte": 4.0,
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
      "oppervlakte": 3.0,
      "bouwkundigeElementen": [
        {
          "id": "closetcombinatie",
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
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 300000.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 310000.0,
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
  "punten": 56.75,
  "woningwaarderingen": [
    {
      "aantal": 310000.0,
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
      "punten": 20.22
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
      "punten": 36.6
    },
    {
      "aantal": 35.0,
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
      "punten": -0.07
    }
  ]
}
```
