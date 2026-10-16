# test_voor_verwarmde_overige_ruimten_geldt_geen_maximum_van_4_punten

Voor verwarmde gemeenschappelijke overige ruimten geldt in deze rubriek geen maximum van 4 punten.

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
      - Oppervlakte van overige ruimten                                           9.38 pt
        - Berging1                                                   10.00 m²
        - Berging2                                                   10.00 m²
        - Berging3                                                   10.00 m²
        - Berging4                                                   10.00 m²
        - Berging5                                                   10.00 m²
      - Verkoeling en verwarming
        - Verwarmde overige en verkeersruimten
          - Berging1                                                              0.25 pt
          - Berging2                                                              0.25 pt
          - Berging3                                                              0.25 pt
          - Berging4                                                              0.25 pt
          - Berging5                                                              0.25 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                         10.75 pt
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
      "gedeeldMetAantalAdressen": 2,
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
      "gedeeldMetAantalAdressen": 2,
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
      "gedeeldMetAantalAdressen": 2,
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
      "gedeeldMetAantalAdressen": 2,
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
      "gedeeldMetAantalAdressen": 2,
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
  "punten": 10.75,
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        }
      },
      "punten": 9.38
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__berging1",
        "naam": "Berging1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__berging2",
        "naam": "Berging2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__berging3",
        "naam": "Berging3",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__berging4",
        "naam": "Berging4",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__berging5",
        "naam": "Berging5",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
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
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging1",
        "naam": "Berging1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging2",
        "naam": "Berging2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging3",
        "naam": "Berging3",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging4",
        "naam": "Berging4",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten__berging5",
        "naam": "Berging5",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__verkoeling_en_verwarming__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.25
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
