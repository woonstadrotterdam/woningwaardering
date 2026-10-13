# test_verwarmd_vertrek_met_verkoelingsfunctie_krijgt_een_punt_extra

Een verwarmd vertrek met verkoelingsfunctie krijgt 1 punt naast de 2 punten voor verwarming.

Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
punten" en "Verkoelingsfunctie per vertrek (mits deze voorziening tevens een
verwarmingsfunctie heeft) 1 punt (maximaal 2 punten bij meerdere vertrekken
met verkoelingsfunctie)".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "Dit betekent dat
een vertrek met verkoelingsvoorziening (die ook kan verwarmen) ook als
verwarmd vertrek geldt en aanspraak kan maken op bijbehorende waardering."

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
