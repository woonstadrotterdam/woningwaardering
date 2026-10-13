# test_zolderruimte_die_geen_vertrek_kan_zijn_wordt_als_overige_ruimte_gewaardeerd

Een zolderruimte die als vertrek is aangeleverd maar niet aan de eisen van een vertrek voldoet, wordt als overige ruimte gewaardeerd.

De package waarschuwt bij de ruimte met de detailsoort `zolder`.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Onder overige
ruimten, voor zover zij niet voldoen aan de eisen voor een vertrek, worden
onder andere verstaan: bijkeukens, bergingen, wasruimten, schuren, zolders
en kelders."

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Voldoet
een zolderruimte niet aan die eisen, dan wordt gekeken of deze als overige
ruimte kan worden gewaardeerd. Dat gebeurt ook wanneer de ruimte is
ingeschoten met `ruimtesoort` `vertrek`, net zoals bij andere vertrekken die
de minimale oppervlakte van 4m2 niet halen (zie 2.2.1.2)."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                          23.00 m²    17.25 pt
    - Zoldervertrek1                                                  3.00 m²
    - Zoldervertrek2                                                 10.00 m²
    - Zolder                                                         10.00 m²
  Correctie: zolder zonder vaste trap                                            -5.00 pt
                                                                    ------      ------
  Totaal                                                             23.00 m²    12.25 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Zolder' (zolder) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.
- UserWarning: Ruimte 'Zolder' (zolder) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.

## Input

```json
{
  "ruimten": [
    {
      "id": "zoldervertrek1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek1",
      "oppervlakte": 3.0
    },
    {
      "id": "zoldervertrek2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek2",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "vlizotrap",
          "naam": "Vlizotrap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "VTR",
            "naam": "Vlizotrap"
          }
        }
      ]
    },
    {
      "id": "zolder",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "oppervlakte": 10.0
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 12.25,
  "woningwaarderingen": [
    {
      "aantal": 23.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 17.25
    },
    {
      "aantal": 3.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zoldervertrek1",
        "naam": "Zoldervertrek1",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
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
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zoldervertrek2",
        "naam": "Zoldervertrek2",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
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
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zolder",
        "naam": "Zolder",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__zoldervertrek2__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap"
      },
      "punten": -5.0
    }
  ]
}
```
