# test_maximum_voor_verkoelingsfunctie_geldt_apart_voor_prive_en_gemeenschappelijke_vertrekken

Het maximum van 2 punten voor vertrekken met verkoelingsfunctie geldt apart voor privévertrekken en voor gemeenschappelijke vertrekken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
wettekst, Bijlage I onder B, onderdeel 3.

De punten van een gemeenschappelijke ruimte worden gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3; wettekst,
Bijlage I onder B, onderdeel 3.

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Slaapkamer1                                                               2.00 pt
      - Slaapkamer2                                                               2.00 pt
      - Slaapkamer3                                                               2.00 pt
    - Verkoelde vertrekken
      - Slaapkamer1                                                               1.00 pt
      - Slaapkamer2                                                               1.00 pt
      - Slaapkamer3                                                               1.00 pt
      - Maximaal 2 punten                                                        -1.00 pt
  Gedeeld met 2 onzelfstandige woonruimten
    - Verwarmde vertrekken
      - Slaapkamer4                                                               1.00 pt
      - Slaapkamer5                                                               1.00 pt
      - Slaapkamer6                                                               1.00 pt
    - Verkoelde vertrekken
      - Slaapkamer4                                                               0.50 pt
      - Slaapkamer5                                                               0.50 pt
      - Slaapkamer6                                                               0.50 pt
      - Maximering                                                               -0.50 pt
                                                                                ------
  Totaal                                                                         12.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "verwarmd": true,
      "verkoeld": true
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
      "verwarmd": true,
      "verkoeld": true
    },
    {
      "id": "slaapkamer3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer3",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true
    },
    {
      "id": "slaapkamer4",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer4",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "slaapkamer5",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer5",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "slaapkamer6",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer6",
      "oppervlakte": 10.0,
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
      "code": "VKV",
      "naam": "Verkoeling en verwarming"
    }
  },
  "punten": 12.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__slaapkamer3",
        "naam": "Slaapkamer3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken",
        "naam": "Verkoelde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken__slaapkamer3",
        "naam": "Slaapkamer3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken__max_aantal_punten",
        "naam": "Maximaal 2 punten",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken"
        }
      },
      "punten": -1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__slaapkamer4",
        "naam": "Slaapkamer4",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__slaapkamer5",
        "naam": "Slaapkamer5",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__slaapkamer6",
        "naam": "Slaapkamer6",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken",
        "naam": "Verkoelde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__slaapkamer4",
        "naam": "Slaapkamer4",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__slaapkamer5",
        "naam": "Slaapkamer5",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__slaapkamer6",
        "naam": "Slaapkamer6",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__max_aantal_punten",
        "naam": "Maximering",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken"
        }
      },
      "punten": -0.5
    }
  ]
}
```
