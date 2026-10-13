# test_woonkamer_met_keuken_heeft_ook_zonder_aanrecht_een_open_keuken

Een verwarmde privé woonkamer/keuken of woon-/slaapkamer/keuken krijgt ook zonder aanrecht de 4 punten van een vertrek met open keuken.

Bron: beleidsboek onzelfstandige woonruimten, 2.3.2: "Een privé verwarmde
woonkamer met open keuken wordt dus gewaardeerd met 4 punten."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2:
"Ruimtedetailsoorten die de keuken al in zich hebben
(`woonkamer_en_of_keuken`, `woon_en_of_slaapkamer_en_of_keuken`) tellen
altijd als open keuken, ook zonder aanrecht in de input."

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Woonkamer/keuken                                                          4.00 pt
      - Woon-/slaapkamer/keuken                                                   4.00 pt
                                                                                ------
  Totaal                                                                          8.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer/keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOK",
        "naam": "Woonkamer/keuken"
      },
      "naam": "Woonkamer/keuken",
      "oppervlakte": 10.0,
      "verwarmd": true
    },
    {
      "id": "woon-/slaapkamer/keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WSK",
        "naam": "Woon-/slaapkamer/keuken"
      },
      "naam": "Woon-/slaapkamer/keuken",
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
  "punten": 8.0,
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woonkamer/keuken",
        "naam": "Woonkamer/keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woon-/slaapkamer/keuken",
        "naam": "Woon-/slaapkamer/keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    }
  ]
}
```
