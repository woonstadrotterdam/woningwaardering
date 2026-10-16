# test_aanrecht_is_vanaf_1m_een_open_keuken

Een aanrecht in een verwarmde privéwoonkamer is vanaf 1 meter een open keuken.

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
      - Woonkamer1                                                                2.00 pt
      - Woonkamer2 met open keuken                                                4.00 pt
      - Woonkamer3 met open keuken                                                4.00 pt
                                                                                ------
  Totaal                                                                         10.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer1",
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
          "lengte": 999.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "woonkamer2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer2",
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
          "lengte": 1000.0
        }
      ],
      "verwarmd": true
    },
    {
      "id": "woonkamer3",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer3",
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
          "lengte": 1001.0
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
  "punten": 10.0,
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woonkamer1",
        "naam": "Woonkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woonkamer2",
        "naam": "Woonkamer2 met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woonkamer3",
        "naam": "Woonkamer3 met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    }
  ]
}
```
