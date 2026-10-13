# test_aanrecht_is_vanaf_1m_een_open_keuken

Een aanrecht in een verwarmde woonkamer is vanaf 1 meter een open keuken.

Bron: wettekst, Bijlage I onder A, rubriek 3: "Verwarming per vertrek 2
punten".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
er verwarming aanwezig is".

Bron: implementatietoelichting zelfstandige woonruimten, 2.3.2: "Omdat wij
in de package niet (kunnen) controleren op keukenkastjes, doen wij de
aanname dat een aanrecht vanaf 1 meter een open keuken is."

## Rapport

```text
VERKOELING EN VERWARMING
  Verwarmde vertrekken
    - Woonkamer1                                                                  2.00 pt
    - Woonkamer2 met open keuken                                                  4.00 pt
    - Woonkamer3 met open keuken                                                  4.00 pt
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
          "lengte": 500.0
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
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
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__woonkamer1",
        "naam": "Woonkamer1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__woonkamer2",
        "naam": "Woonkamer2 met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__verwarmde_vertrekken__woonkamer3",
        "naam": "Woonkamer3 met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
    }
  ]
}
```
