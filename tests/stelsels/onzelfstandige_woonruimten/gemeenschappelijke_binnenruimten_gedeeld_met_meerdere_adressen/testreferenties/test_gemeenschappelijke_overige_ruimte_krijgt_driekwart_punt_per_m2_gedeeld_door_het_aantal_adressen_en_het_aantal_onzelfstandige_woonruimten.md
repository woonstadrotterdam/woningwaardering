# test_gemeenschappelijke_overige_ruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen_en_het_aantal_onzelfstandige_woonruimten

Een gemeenschappelijke overige ruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.9;
implementatietoelichting onzelfstandige woonruimten, 2.9.1; wettekst,
Bijlage I onder B, onderdeel 9.

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Gedeeld met 10 adressen
      - Oppervlakte van overige ruimten                                           0.71 pt
        - Berging                                                    19.00 m²
      - Verkoeling en verwarming
        - Verwarmde overige en verkeersruimten
          - Berging                                                               0.05 pt
  Afronding op kwartpunten                                                       -0.01 pt
                                                                                ------
  Totaal                                                                          0.75 pt
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
      "oppervlakte": 19.0,
      "gedeeldMetAantalAdressen": 10,
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 0.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen",
        "naam": "Gedeeld met 10 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        }
      },
      "punten": 0.71
    },
    {
      "aantal": 19.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__oppervlakte_van_overige_ruimten__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_10_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.05
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.01
    }
  ]
}
```
