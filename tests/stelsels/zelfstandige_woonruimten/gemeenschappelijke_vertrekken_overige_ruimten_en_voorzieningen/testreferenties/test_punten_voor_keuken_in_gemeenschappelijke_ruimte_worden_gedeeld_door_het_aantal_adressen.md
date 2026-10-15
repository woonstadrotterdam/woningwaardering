# test_punten_voor_keuken_in_gemeenschappelijke_ruimte_worden_gedeeld_door_het_aantal_adressen

De punten voor een keuken in een gemeenschappelijke ruimte worden gedeeld door het aantal adressen dat toegang heeft.

Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2; wettekst,
Bijlage I onder A, toelichting rubriek 9.

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 5 adressen
    - Oppervlakte van vertrekken                                                  2.00 pt
      - Keuken                                                       10.00 m²
    - Verkoeling en verwarming
      - Verwarmde vertrekken
        - Keuken                                                                  0.40 pt
    - Keuken
      - Keuken
        - Lengte aanrecht                                          1000.00 mm     0.80 pt
        - Extra voorzieningen
          - Inbouw koelkast                                           2.00 st     0.40 pt
  Afronding op kwartpunten                                                       -0.10 pt
                                                                                ------
  Totaal                                                                          3.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 5,
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
          "lengte": 1000.0
        }
      ],
      "verwarmd": true,
      "installaties": [
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
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
  "punten": 3.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen",
        "naam": "Gedeeld met 5 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen"
        }
      },
      "punten": 2.0
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.4
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken"
        }
      }
    },
    {
      "aantal": 1000.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 0.8
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken__extra_voorzieningen",
        "naam": "Extra voorzieningen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken"
        }
      }
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken__extra_voorzieningen__extra_voorziening_inbouw_koelkast",
        "naam": "Inbouw koelkast",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__keuken__keuken__extra_voorzieningen"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.4
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.1
    }
  ]
}
```
