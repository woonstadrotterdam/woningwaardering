# test_aftrek_is_niet_hoger_dan_de_punten_voor_de_gemeenschappelijke_zolder

De aftrek voor een gemeenschappelijke zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3; wettekst,
Bijlage I onder A, toelichting rubriek 2.

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 2 adressen
    - Oppervlakte van overige ruimten
      - Subtotaal                                                    12.33 m²     4.50 pt
        - Berging                                                     6.00 m²
        - Zolder                                                      6.33 m²
      - Correctie: zolder zonder vaste trap                                      -2.25 pt
                                                                                ------
  Totaal                                                                          2.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 2
    },
    {
      "id": "zolder",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "oppervlakte": 6.33,
      "gedeeldMetAantalAdressen": 2,
      "bouwkundigeElementen": [
        {
          "id": "vlizotrap",
          "naam": "Vlizotrap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTR",
            "naam": "Vlizotrap"
          }
        }
      ]
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
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen"
        }
      }
    },
    {
      "aantal": 12.33,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 4.5
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 6.33,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal__zolder",
        "naam": "Zolder",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__zolder__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
        }
      },
      "punten": -2.25
    }
  ]
}
```
