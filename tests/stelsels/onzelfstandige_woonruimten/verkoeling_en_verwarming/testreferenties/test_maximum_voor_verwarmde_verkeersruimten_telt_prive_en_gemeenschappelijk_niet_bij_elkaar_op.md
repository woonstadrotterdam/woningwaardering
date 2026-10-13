# test_maximum_voor_verwarmde_verkeersruimten_telt_prive_en_gemeenschappelijk_niet_bij_elkaar_op

Het maximum van 4 punten voor verwarmde verkeersruimten telt privéruimten en gemeenschappelijke ruimten niet bij elkaar op.

Gang1 tot en met Gang3 zijn privé; Gang4 tot en met Gang6 worden met 2
onzelfstandige woonruimten gedeeld.

Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privé overige
ruimte en verkeersruimte 1 punt" en "Verwarming per gemeenschappelijke
overige ruimte en verkeersruimte op hetzelfde adres 1 punt, te delen door
het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".

Bron: beleidsboek onzelfstandige woonruimten, 2.3: "1 punt per verwarmde
privé overige ruimte of privé verkeersruimte (tot maximaal 4 punten)" en "1
punt per verwarmde gemeenschappelijke overige ruimte of gemeenschappelijke
verkeersruimte (tot maximaal 4 punten) / onzelfstandige wooneenheden met
toegang en gebruiksrecht".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3: "De kaders
hierboven geven max. 4 verwarmde overige/verkeersruimten en max. 2
verkoelde vertrekken afzonderlijk voor privé en voor gemeenschappelijk."

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde overige en verkeersruimten
      - Gang1                                                                     1.00 pt
      - Gang2                                                                     1.00 pt
      - Gang3                                                                     1.00 pt
  Gedeeld met 2 onzelfstandige woonruimten
    - Verwarmde overige en verkeersruimten
      - Gang4                                                                     0.50 pt
      - Gang5                                                                     0.50 pt
      - Gang6                                                                     0.50 pt
                                                                                ------
  Totaal                                                                          4.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "gang1",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang1",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "gang2",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang2",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "gang3",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang3",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "gang4",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang4",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "gang5",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang5",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "gang6",
      "soort": {
        "code": "VRK",
        "naam": "Verkeersruimte"
      },
      "detailSoort": {
        "code": "GAN",
        "naam": "Gang"
      },
      "naam": "Gang6",
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
  "punten": 4.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive",
        "naam": "Privé"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten",
        "naam": "Verwarmde overige en verkeersruimten",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__gang1",
        "naam": "Gang1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__gang2",
        "naam": "Gang2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__gang3",
        "naam": "Gang3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
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
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__gang4",
        "naam": "Gang4",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__gang5",
        "naam": "Gang5",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten__gang6",
        "naam": "Gang6",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 0.5
    }
  ]
}
```
