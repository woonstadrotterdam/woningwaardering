# test_vertrek_met_open_keuken_krijgt_een_punt_voor_de_verkoelingsfunctie

Een verwarmd privévertrek met open keuken krijgt voor de verkoelingsfunctie 1 punt: de open keuken telt alleen voor de verwarming als afzonderlijk vertrek.

De bronnen noemen dit geval niet uitdrukkelijk; de test legt vast hoe de
package ze leest.

Bron: wettekst, Bijlage I onder B, rubriek 3: "Verkoelingsfunctie per
privévertrek (mits deze voorziening tevens een verwarmingsfunctie heeft) 1
punt".

Bron: wettekst, Bijlage I onder A, toelichting rubriek 3: "een open keuken
als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten indien
er verwarming aanwezig is".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Woonkamer met open keuken                                                 4.00 pt
    - Verkoelde vertrekken
      - Woonkamer                                                                 1.00 pt
                                                                                ------
  Totaal                                                                          5.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
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
  "punten": 5.0,
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__woonkamer",
        "naam": "Woonkamer met open keuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 4.0
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
        "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verkoelde_vertrekken"
        }
      },
      "punten": 1.0
    }
  ]
}
```
