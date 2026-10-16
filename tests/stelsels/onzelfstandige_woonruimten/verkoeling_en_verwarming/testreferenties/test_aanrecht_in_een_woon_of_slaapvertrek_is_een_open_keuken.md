# test_aanrecht_in_een_woon_of_slaapvertrek_is_een_open_keuken

Een aanrecht in een verwarmd privé woon- of slaapvertrek is een open keuken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.

Een open keuken geldt als afzonderlijk verwarmd vertrek.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2;
wettekst, Bijlage I onder A, toelichting rubriek 3 (via Bijlage I onder
B, toelichting, inleiding).

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Slaapkamer met open keuken                                                4.00 pt
      - Woon-/slaapkamer met open keuken                                          4.00 pt
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
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 2700.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "woon-/slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WSL",
        "naam": "Woon-/slaapkamer"
      },
      "naam": "Woon-/slaapkamer",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 2700.0
        }
      ],
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__slaapkamer",
        "naam": "Slaapkamer met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woon-/slaapkamer",
        "naam": "Woon-/slaapkamer met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    }
  ]
}
```
