# test_voor_vertrekken_met_verkoelingsfunctie_geldt_geen_maximum_van_2_punten

Voor gemeenschappelijke vertrekken met verkoelingsfunctie geldt in deze rubriek geen maximum van 2 punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
Bijlage I onder A, toelichting rubriek 9 (via Bijlage I onder B,
toelichting, inleiding); wettekst, Bijlage I onder A, toelichting rubriek 3
(via Bijlage I onder B, toelichting, inleiding).

Elk punt wordt gedeeld door het aantal adressen en daarna door het aantal
onzelfstandige woonruimten op het adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
Bijlage I onder B, toelichting rubriek 9.

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Gedeeld met 2 adressen
      - Oppervlakte van vertrekken                                               15.00 pt
        - Woonkamer                                                  20.00 m²
        - Keuken1                                                    20.00 m²
        - Keuken2                                                    20.00 m²
      - Verkoeling en verwarming
        - Verwarmde vertrekken
          - Woonkamer                                                             0.50 pt
          - Keuken1                                                               0.50 pt
          - Keuken2                                                               0.50 pt
        - Verkoelde vertrekken
          - Woonkamer                                                             0.25 pt
          - Keuken1                                                               0.25 pt
          - Keuken2                                                               0.25 pt
      - Keuken
        - Keuken1
          - Lengte aanrecht                                        3001.00 mm     2.50 pt
        - Keuken2
          - Lengte aanrecht                                        3001.00 mm     2.50 pt
                                                                                ------
  Totaal                                                                         22.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
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
      "gedeeldMetAantalAdressen": 2,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "keuken1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken1",
      "oppervlakte": 20.0,
      "gedeeldMetAantalAdressen": 2,
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
          "lengte": 3001.0
        }
      ],
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "keuken2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken2",
      "oppervlakte": 20.0,
      "gedeeldMetAantalAdressen": 2,
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
          "lengte": 3001.0
        }
      ],
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    }
  ]
}
```

## Output

```json
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
  "punten": 22.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        }
      },
      "punten": 15.0
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken",
        "naam": "Verkoelde vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken"
        }
      }
    },
    {
      "aantal": 3001.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken__keuken1__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken__keuken1"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 2.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken"
        }
      }
    },
    {
      "aantal": 3001.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken__keuken2__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__keuken__keuken2"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 2.5
    }
  ]
}
```
