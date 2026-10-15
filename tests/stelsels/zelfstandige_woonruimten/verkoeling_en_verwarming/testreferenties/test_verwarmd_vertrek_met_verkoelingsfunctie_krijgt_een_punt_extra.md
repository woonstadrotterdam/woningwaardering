# test_verwarmd_vertrek_met_verkoelingsfunctie_krijgt_een_punt_extra

Een verwarmd vertrek met verkoelingsfunctie krijgt 1 punt naast de 2 punten voor verwarming.

Bron: implementatietoelichting zelfstandige woonruimten, 2.3; wettekst,
Bijlage I onder A, onderdeel 3.

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Slaapkamer                                                                  2.00 pt
  Verkoelde vertrekken
    - Slaapkamer                                                                  1.00 pt
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
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
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken",
        "naam": "Verkoelde vertrekken"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verkoelde_vertrekken__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    }
  ]
}
```
