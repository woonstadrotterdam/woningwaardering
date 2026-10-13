# test_verwarmde_prive_overige_ruimten_krijgen_samen_hooguit_4_punten

Verwarmde privé overige ruimten krijgen samen hooguit 4 punten.

Bron: wettekst, Bijlage I onder B, rubriek 3: "Verwarming per privé overige
ruimte en verkeersruimte 1 punt".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Per verwarmde
overige ruimte en verkeersruimte wordt, ongeacht de verwarmingswijze, een
waardering van één punt toegepast, voor zover de verwarming tot de
onroerende zaak en zijn onroerende aanhorigheden behoort. Hiervoor geldt
een maximum van vier punten."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde overige en verkeersruimten
      - Berging1                                                                  1.00 pt
      - Berging2                                                                  1.00 pt
      - Berging3                                                                  1.00 pt
      - Berging4                                                                  1.00 pt
      - Berging5                                                                  1.00 pt
      - Maximaal 4 punten                                                        -1.00 pt
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
      "verwarmd": true
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
      "verwarmd": true
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
      "verwarmd": true
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
      "verwarmd": true
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
      "verwarmd": true
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__berging1",
        "naam": "Berging1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__berging2",
        "naam": "Berging2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__berging3",
        "naam": "Berging3",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__berging4",
        "naam": "Berging4",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__berging5",
        "naam": "Berging5",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten__max_aantal_punten",
        "naam": "Maximaal 4 punten",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_overige_en_verkeersruimten"
        }
      },
      "punten": -1.0
    }
  ]
}
```
