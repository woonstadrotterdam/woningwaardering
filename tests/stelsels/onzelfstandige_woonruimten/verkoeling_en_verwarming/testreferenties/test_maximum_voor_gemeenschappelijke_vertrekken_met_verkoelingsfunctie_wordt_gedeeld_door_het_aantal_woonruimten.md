# test_maximum_voor_gemeenschappelijke_vertrekken_met_verkoelingsfunctie_wordt_gedeeld_door_het_aantal_woonruimten

Het maximum van 2 punten voor gemeenschappelijke vertrekken met verkoelingsfunctie wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.3
- wettekst, Bijlage I onder B, onderdeel 3

## Rapport

```text
VERKOELING EN VERWARMING
  Gedeeld met 2 onzelfstandige woonruimten
    - Verwarmde vertrekken
      - Slaapkamer1                                                               1.00 pt
      - Slaapkamer2                                                               1.00 pt
      - Slaapkamer3                                                               1.00 pt
    - Verkoelde vertrekken
      - Slaapkamer1                                                               0.50 pt
      - Slaapkamer2                                                               0.50 pt
      - Slaapkamer3                                                               0.50 pt
      - Maximering                                                               -0.50 pt
                                                                                ------
  Totaal                                                                          4.00 pt
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
      "verwarmd": true,
      "verkoeld": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 4.0,
  "woningwaarderingen": [
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
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__slaapkamer3",
        "naam": "Slaapkamer3",
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
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__slaapkamer1",
        "naam": "Slaapkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__slaapkamer2",
        "naam": "Slaapkamer2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verkoelde_vertrekken__slaapkamer3",
        "naam": "Slaapkamer3",
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
