# test_woning_kleiner_dan_40_m2_gebouwd_in_2018_tot_en_met_2022_zonder_adres_krijgt_met_waarschuwing_het_gewone_kengetal

Zonder adres krijgt een woning kleiner dan 40 m² die in 2018 tot en met 2022 is gebouwd, met een waarschuwing in onderdeel II het gewone kengetal van € 242.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6.

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       310000.00 EUR
  Onderdeel I                                                                    20.22 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   32.85 pt
    - Oppervlakte van vertrekken en overige ruimten                  39.00 m²
    - Factor II                                                     242.00 EUR
  Afronding op kwartpunten                                                       -0.07 pt
                                                                                ------
  Totaal                                                                         53.00 pt
```

## Waarschuwingen

- UserWarning: Eenheid (eenheid): 'energieprestaties' is None
- UserWarning: Eenheid (eenheid) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (eenheid) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.
- UserWarning: Eenheid (eenheid): geen adres gevonden voor COROP-gebied bepaling

## Input

```json
{
  "id": "eenheid",
  "bouwjaar": 2018,
  "gebruiksoppervlakte": 39,
  "monumenten": [],
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
      "oppervlakte": 39.0
    }
  ],
  "wozEenheden": [
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
  "punten": 53.0,
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
      "punten": 32.85
    },
    {
      "aantal": 39.0,
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
