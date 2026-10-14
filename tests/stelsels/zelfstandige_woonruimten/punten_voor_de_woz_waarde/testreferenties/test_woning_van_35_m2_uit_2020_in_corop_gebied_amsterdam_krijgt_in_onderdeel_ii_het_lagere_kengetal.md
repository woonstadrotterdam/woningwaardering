# test_woning_van_35_m2_uit_2020_in_corop_gebied_amsterdam_krijgt_in_onderdeel_ii_het_lagere_kengetal

Een woning van 35 m² uit 2020 in het COROP-gebied Amsterdam krijgt in onderdeel II het lagere kengetal van € 103.

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "a. indien sprake is van
een woning tot 40 m² gebouwd in het kalenderjaar 2018, 2019, 2020, 2021 of
2022 die is gelegen in een gemeente, gelegen in het COROP-gebied Amsterdam
of Utrecht, vervolgens gedeeld door" en "€ 103 voor WOZ-beschikkingen met
waardepeildatum 1 januari 2024."

De package toetst de 40 m² aan de gebruiksoppervlakte van de eenheid en
bepaalt het COROP-gebied met de woonplaatscode: 3594 is Amsterdam, in het
COROP-gebied Groot-Amsterdam.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6: "Wij gaan
er vanuit dat de 40m2 verwijst naar de gebruiksoppervlakte van de woning."
en "Het COROP-gebied wordt bepaald op basis van de woonplaatscode van de
woonplaats waarin de eenheid zich bevindt."

De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2023 en 2024. De
package rekent met de meest recente, die van 1 januari 2024.

Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
peildatum van de procedure bedoeld."

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
voor WOZ-beschikkingen met waardepeildatum 1 januari 2024."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       310000.00 EUR
  Onderdeel I                                                                    20.22 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   85.99 pt
    - Oppervlakte van vertrekken en overige ruimten                  35.00 m²
    - Factor II                                                     103.00 EUR
  Afronding op kwartpunten                                                        0.04 pt
                                                                                ------
  Totaal                                                                        106.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 2020,
  "adres": {
    "huisnummer": "1",
    "huisnummerToevoeging": "",
    "postcode": "1012LG",
    "woonplaats": {
      "code": "3594",
      "naam": "Amsterdam"
    }
  },
  "adresseerbaarObjectBasisregistratie": {
    "bagIdentificatie": "0363010012111931"
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
      "begindatum": "2020-01-01",
      "einddatum": "2030-01-01",
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
      "oppervlakte": 3.0
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
  "punten": 106.25,
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
      "punten": 85.99
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
      "aantal": 103.0,
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
      "punten": 0.04
    }
  ]
}
```
