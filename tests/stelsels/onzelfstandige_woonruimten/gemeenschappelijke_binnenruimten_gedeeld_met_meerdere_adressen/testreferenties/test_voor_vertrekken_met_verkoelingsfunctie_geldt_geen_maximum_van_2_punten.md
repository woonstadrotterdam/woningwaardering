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
      - Oppervlakte van vertrekken                                                7.50 pt
        - Woonkamer                                                  10.00 m²
        - Slaapkamer1                                                10.00 m²
        - Slaapkamer2                                                10.00 m²
      - Verkoeling en verwarming
        - Verwarmde vertrekken
          - Woonkamer                                                             0.50 pt
          - Slaapkamer1                                                           0.50 pt
          - Slaapkamer2                                                           0.50 pt
        - Verkoelde vertrekken
          - Woonkamer                                                             0.25 pt
          - Slaapkamer1                                                           0.25 pt
          - Slaapkamer2                                                           0.25 pt
                                                                                ------
  Totaal                                                                          9.75 pt
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
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 2,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "slaapkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer1",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 2,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "slaapkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer2",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 2,
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
  "punten": 9.75,
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
      "punten": 7.5
    },
    {
      "aantal": 10.0,
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
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
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
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 0.25
    }
  ]
}
```
