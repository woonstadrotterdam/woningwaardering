# test_maximum_voor_verwarmde_gemeenschappelijke_overige_ruimten_wordt_gedeeld_door_het_aantal_woonruimten

Het maximum van 4 punten voor verwarmde gemeenschappelijke overige ruimten wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3;
wettekst, Bijlage I onder B, onderdeel 3; wettekst, Bijlage I onder A,
toelichting rubriek 3 (via Bijlage I onder B, toelichting, inleiding).

## Rapport

```text
VERKOELING EN VERWARMING
  Gedeeld met 2 onzelfstandige woonruimten
    - Verwarmde overige en verkeersruimten
      - Berging1                                                                  0.50 pt
      - Berging2                                                                  0.50 pt
      - Berging3                                                                  0.50 pt
      - Berging4                                                                  0.50 pt
      - Berging5                                                                  0.50 pt
      - Maximering                                                               -0.50 pt
                                                                                ------
  Totaal                                                                          2.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging1",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "berging2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging2",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "berging3",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging3",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "berging4",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging4",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "berging5",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging5",
      "oppervlakte": 10.0,
      "verwarmd": true,
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
  "punten": 2.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__berging1",
        "naam": "Berging1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__berging2",
        "naam": "Berging2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__berging3",
        "naam": "Berging3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__berging4",
        "naam": "Berging4",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__berging5",
        "naam": "Berging5",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__max_aantal_punten",
        "naam": "Maximering",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": -0.5
    }
  ]
}
```
