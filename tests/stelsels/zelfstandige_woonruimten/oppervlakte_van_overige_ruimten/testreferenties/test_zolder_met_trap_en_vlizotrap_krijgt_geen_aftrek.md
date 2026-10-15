# test_zolder_met_trap_en_vlizotrap_krijgt_geen_aftrek

Een zolder met zowel een trap als een vlizotrap krijgt geen aftrek.

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3.

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Zolder                                                             10.00 m²
                                                                    ------      ------
  Totaal                                                             10.00 m²     7.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "element_1",
          "naam": "Trap",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "TRA",
            "naam": "Trap"
          }
        },
        {
          "id": "element_2",
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
  "punten": 7.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__zolder",
        "naam": "Zolder",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
