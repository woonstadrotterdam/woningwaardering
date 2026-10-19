# test_punten_voor_de_woz_waarde_zijn_de_som_van_onderdeel_i_en_ii_afgerond_op_een_kwart_punt

De punten voor de WOZ-waarde zijn de som van onderdeel I en onderdeel II, afgerond op een kwart punt.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.11.2

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2025                       300000.00 EUR
  Onderdeel I                                                                    17.69 pt
    - Factor I                                                    16954.00 EUR
  Onderdeel II                                                                   18.66 pt
    - Oppervlakte van vertrekken en overige ruimten                  60.00 m²
    - Factor II                                                     268.00 EUR
  Afronding op kwartpunten                                                       -0.10 pt
                                                                                ------
  Totaal                                                                         36.25 pt
```

## Waarschuwingen

- UserWarning: Eenheid (None): 'energieprestaties' is None
- UserWarning: Eenheid (None): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.
- UserWarning: Eenheid (None) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (None) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "bouwjaar": 1990,
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
      "oppervlakte": 60.0,
      "verwarmd": true
    }
  ],
  "wozEenheden": [
    {
      "vastgesteldeWaarde": 300000.0,
      "waardepeildatum": "2025-01-01"
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
  "punten": 36.25,
  "woningwaarderingen": [
    {
      "aantal": 300000.0,
      "criterium": {
        "id": "punten_voor_de_woz_waarde__woz_waarde",
        "naam": "WOZ-waarde op waardepeildatum 01-01-2025",
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
      "punten": 17.69
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
      "punten": 18.66
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
        "id": "punten_voor_de_woz_waarde__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.1
    }
  ]
}
```
