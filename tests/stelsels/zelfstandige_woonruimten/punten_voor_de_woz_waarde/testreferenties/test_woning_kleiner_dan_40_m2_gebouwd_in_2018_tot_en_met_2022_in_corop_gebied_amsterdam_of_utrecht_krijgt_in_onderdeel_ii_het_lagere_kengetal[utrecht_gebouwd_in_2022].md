# test_woning_kleiner_dan_40_m2_gebouwd_in_2018_tot_en_met_2022_in_corop_gebied_amsterdam_of_utrecht_krijgt_in_onderdeel_ii_het_lagere_kengetal[utrecht_gebouwd_in_2022]

Een woning kleiner dan 40 m² die in 2018 tot en met 2022 is gebouwd en in het COROP-gebied Amsterdam of Utrecht ligt, krijgt in onderdeel II het lagere kengetal van € 103.

Bron: implementatietoelichting zelfstandige woonruimten, 2.11.6; wettekst,
Bijlage I onder A, onderdeel 11.1.

## Rapport

```text
PUNTEN VOOR DE WOZ-WAARDE
  WOZ-waarde op waardepeildatum 01-01-2024                       310000.00 EUR
  Onderdeel I                                                                    20.22 pt
    - Factor I                                                    15329.00 EUR
  Onderdeel II                                                                   77.17 pt
    - Oppervlakte van vertrekken en overige ruimten                  39.00 m²
    - Factor II                                                     103.00 EUR
  Afronding op kwartpunten                                                        0.11 pt
                                                                                ------
  Totaal                                                                         97.50 pt
```

## Waarschuwingen

- UserWarning: Eenheid (None): 'energieprestaties' is None
- UserWarning: Eenheid (None) heeft geen pandsoort Eengezinswoning of Meergezinswoning en komt daarom niet in aanmerking voor waardering onder stelselgroep Energieprestatie.
- UserWarning: Eenheid (None) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "bouwjaar": 2022,
  "adres": {
    "woonplaats": {
      "code": "3295"
    }
  },
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
  "punten": 97.5,
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
      "punten": 77.17
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
      "punten": 0.11
    }
  ]
}
```
