# test_woz_waarde_onder_de_minimum_woz_waarde_wordt_niet_verhoogd_tot_dat_minimum

Een vastgestelde WOZ-waarde van € 79.999, lager dan de minimum WOZ-waarde van € 85.806, wordt niet tot dat minimum verhoogd.

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "de voor de woning
laatstelijk vastgestelde waarde op voet van hoofdstuk IV van de Wet
waardering onroerende zaken of 85% van de taxatiewaarde indien er geen
WOZ-waarde is vastgesteld, en anders een minimumwaarde van € 85.806."

Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "De minimum WOZ-waarde
komt pas aan bod als er voor een woonruimte geen relevante WOZ-waarde
aanwezig is én de verhuurder geen taxatierapport (zoals hierboven bedoeld)
heeft ingediend."

De eenheid heeft WOZ-waarden met waardepeildatum 1 januari 2022, 2023 en
2024. De package rekent met de meest recente, die van 1 januari 2024, en
met de kengetallen die bij die waardepeildatum horen.

Bron: beleidsboek zelfstandige woonruimten, 2.11.1: "Met de laatst
vastgestelde WOZ-waarde wordt de meest recent vastgestelde WOZ-waarde op de
peildatum van de procedure bedoeld."

Bron: wettekst, Bijlage I onder A, onderdeel 11.1: "1 punt per € 15.329
voor WOZ-beschikkingen met waardepeildatum 1 januari 2024." en "€ 242 bij
WOZ-beschikkingen met waardepeildatum 1 januari 2024."

De oppervlakte in onderdeel II is die van de drie vertrekken, afgerond op
hele vierkante meters.

Bron: beleidsboek zelfstandige woonruimten, 2.11.2: "Rond hierna de
oppervlakte af op hele vierkante meters."

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                        79999.00 EUR
  Onderdeel I                                                                     5.22 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   11.81 pt
    - Oppervlakte van vertrekken en overige ruimten                  28.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.03 pt
                                                                                ------
  Totaal                                                                         17.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "bouwjaar": 1990,
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
      "begindatum": "2018-06-22",
      "einddatum": "2028-06-22",
      "label": {
        "code": "C",
        "naam": "C"
      },
      "waarde": "1.67"
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
      "oppervlakte": 3.59507,
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
      "oppervlakte": 3.13436,
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
        },
        {
          "id": "element_3",
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
      "oppervlakte": 21.4327,
      "verwarmd": true
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 59999.0,
      "waardepeildatum": "2022-01-01"
    },
    {
      "vastgesteldeWaarde": 69999.0,
      "waardepeildatum": "2023-01-01"
    },
    {
      "vastgesteldeWaarde": 79999.0,
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
  "punten": 17.0,
  "woningwaarderingen": [
    {
      "aantal": 79999.0,
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
      "punten": 5.22
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
      "punten": 11.81
    },
    {
      "aantal": 28.0,
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
      "punten": -0.03
    }
  ]
}
```
