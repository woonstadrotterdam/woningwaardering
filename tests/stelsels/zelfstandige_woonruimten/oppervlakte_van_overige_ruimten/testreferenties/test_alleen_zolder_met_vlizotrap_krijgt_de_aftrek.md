# test_alleen_zolder_met_vlizotrap_krijgt_de_aftrek

Alleen een zolder met een vlizotrap krijgt de aftrek voor een zolder zonder vaste trap.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
zolderruimte met vijf verminderd".

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "De
detailsoort draagt eis 1 dus zelf; alleen het `Bouwkundigelement`
`vlizotrap` weerspreekt dat."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                          30.00 m²    22.50 pt
    - Zolder1                                                        10.00 m²
    - Zolder2                                                        10.00 m²
    - Zolder3                                                        10.00 m²
  Correctie: zolder zonder vaste trap                                            -5.00 pt
                                                                    ------      ------
  Totaal                                                             30.00 m²    17.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "zolder1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder1",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "trap",
          "naam": "Trap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "TRA",
            "naam": "Trap"
          }
        }
      ]
    },
    {
      "id": "zolder2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder2",
      "oppervlakte": 10.0
    },
    {
      "id": "zolder3",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder3",
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
  "punten": 17.5,
  "woningwaarderingen": [
    {
      "aantal": 30.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 22.5
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zolder1",
        "naam": "Zolder1",
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
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zolder2",
        "naam": "Zolder2",
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
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zolder3",
        "naam": "Zolder3",
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
        "id": "oppervlakte_van_overige_ruimten__zolder3__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap"
      },
      "punten": -5.0
    }
  ]
}
```
