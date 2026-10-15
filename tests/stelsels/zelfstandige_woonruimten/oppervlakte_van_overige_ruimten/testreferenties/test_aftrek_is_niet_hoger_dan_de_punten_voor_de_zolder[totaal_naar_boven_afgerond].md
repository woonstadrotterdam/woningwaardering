# test_aftrek_is_niet_hoger_dan_de_punten_voor_de_zolder[totaal_naar_boven_afgerond]

De aftrek voor een zolder zonder vaste trap is niet hoger dan de punten die voor de zolder worden gegeven.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3; wettekst,
Bijlage I onder A, toelichting rubriek 2.

Dit geval: de zolder van 2,67 m² brengt het totaal van 6,85 op 9,52 m², afgerond van 7 op 10 m²; de 2,25 punten voor die 3 m² vervallen.

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                           9.52 m²     7.50 pt
    - Berging                                                         6.85 m²
    - Zolder                                                          2.67 m²
  Correctie: zolder zonder vaste trap                                            -2.25 pt
                                                                    ------      ------
  Totaal                                                              9.52 m²     5.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging",
      "oppervlakte": 6.85
    },
    {
      "id": "zolder",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "ZOL",
        "naam": "Zolder"
      },
      "naam": "Zolder",
      "oppervlakte": 2.67,
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
  "punten": 5.25,
  "woningwaarderingen": [
    {
      "aantal": 9.52,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 7.5
    },
    {
      "aantal": 6.85,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__berging",
        "naam": "Berging",
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
      "aantal": 2.67,
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
        "id": "oppervlakte_van_overige_ruimten__zolder__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap"
      },
      "punten": -2.25
    }
  ]
}
```
