# test_keuken_wordt_altijd_als_vertrek_gewaardeerd

Een keuken wordt altijd als vertrek gewaardeerd, ook als ze met een andere ruimtesoort is aangeleverd.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.2.1.2
- wettekst, Bijlage I onder A, toelichting rubriek 1

De punten van een gemeenschappelijke ruimte worden gedeeld door het aantal
adressen dat toegang heeft.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.9.2
- wettekst, Bijlage I onder A, toelichting rubriek 9

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 4 adressen
    - Oppervlakte van vertrekken                                                  2.50 pt
      - Keuken                                                       10.00 m²
    - Verkoeling en verwarming
      - Verwarmde vertrekken
        - Keuken                                                                  0.50 pt
    - Keuken
      - Keuken
        - Lengte aanrecht                                          2000.00 mm     1.75 pt
                                                                                ------
  Totaal                                                                          4.75 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.
- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.
- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.
- UserWarning: Ruimte 'Keuken' (keuken) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Vertrek.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 4,
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
          "lengte": 2000.0
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
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 4.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen",
        "naam": "Gedeeld met 4 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
        }
      },
      "punten": 2.5
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__oppervlakte_van_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming",
        "naam": "Verkoeling en verwarming",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken",
        "naam": "Verwarmde vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__verkoeling_en_verwarming__verwarmde_vertrekken"
        }
      },
      "punten": 0.5
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken__keuken",
        "naam": "Keuken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken"
        }
      }
    },
    {
      "aantal": 2000.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken__keuken__lengte_aanrecht_aanrecht",
        "naam": "Lengte aanrecht",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_4_adressen__keuken__keuken"
        },
        "meeteenheid": {
          "code": "MIL",
          "naam": "Millimeter"
        }
      },
      "punten": 1.75
    }
  ]
}
```
