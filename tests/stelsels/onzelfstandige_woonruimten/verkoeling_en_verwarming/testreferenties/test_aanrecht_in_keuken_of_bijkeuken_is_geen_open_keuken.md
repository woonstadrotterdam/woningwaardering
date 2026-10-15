# test_aanrecht_in_keuken_of_bijkeuken_is_geen_open_keuken

Een aanrecht in een verwarmde keuken, of in een verwarmde bijkeuken die als vertrek is aangeleverd, is geen open keuken.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.3.2.

## Rapport

```text
VERKOELING EN VERWARMING
  Privé
    - Verwarmde vertrekken
      - Keuken1                                                                   2.00 pt
  Gedeeld met 2 onzelfstandige woonruimten
    - Verwarmde vertrekken
      - Keuken2                                                                   1.00 pt
      - Bijkeuken                                                                 1.00 pt
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
      "id": "keuken1",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken1",
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
      "id": "keuken2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken2",
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
    },
    {
      "id": "bijkeuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "BIJ",
        "naam": "Bijkeuken"
      },
      "naam": "Bijkeuken",
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
          "lengte": 1500.0
        }
      ],
      "verwarmd": true,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken__keuken1",
        "naam": "Keuken1",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__prive__verwarmde_vertrekken"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__keuken2",
        "naam": "Keuken2",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    },
    {
      "criterium": {
        "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken__bijkeuken",
        "naam": "Bijkeuken",
        "bovenliggendeCriterium": {
          "id": "verkoeling_en_verwarming__gedeeld_met_2_onzelfstandige_woonruimten__verwarmde_vertrekken"
        }
      },
      "punten": 1.0
    }
  ]
}
```
