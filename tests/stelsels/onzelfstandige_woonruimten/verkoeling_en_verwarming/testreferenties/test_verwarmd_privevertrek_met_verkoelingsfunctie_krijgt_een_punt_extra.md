# test_verwarmd_privevertrek_met_verkoelingsfunctie_krijgt_een_punt_extra

Een verwarmd privévertrek met verkoelingsfunctie krijgt 1 punt naast de 2 punten voor verwarming.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.3.3
- wettekst, Bijlage I onder B, onderdeel 3

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Slaapkamer                                                                2.00 pt
    - Verkoelde vertrekken
      - Slaapkamer                                                                1.00 pt
                                                                                ------
  Totaal                                                                          3.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 10.0,
      "verwarmd": true,
      "verkoeld": true
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
  "punten": 3.0,
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__slaapkamer",
        "naam": "Slaapkamer",
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
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    }
  ]
}
```
