# test_zoldervertrek_met_alleen_een_vlizotrap_krijgt_de_aftrek

Een zoldervertrek dat alleen via een vlizotrap bereikbaar is, krijgt als overige ruimte 5 punten aftrek.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
zolderruimte met vijf verminderd".

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.2.3: "Een
zolderruimte van minimaal 2m2 wordt daarmee altijd gewaardeerd onder
`Oppervlakte van overige ruimten`. Is er een `vlizotrap` en geen `trap`, dan
geldt daarbij de puntenaftrek van 2.2.2.3."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                          10.00 m²     7.50 pt
    - Zoldervertrek                                                  10.00 m²
  Correctie: zolder zonder vaste trap                                            -5.00 pt
                                                                    ------      ------
  Totaal                                                             10.00 m²     2.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "zoldervertrek",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "ZVT",
        "naam": "Zoldervertrek"
      },
      "naam": "Zoldervertrek",
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
  "punten": 2.5,
  "woningwaarderingen": [
    {
      "aantal": 10.0,
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
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__zoldervertrek",
        "naam": "Zoldervertrek",
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
        "id": "oppervlakte_van_overige_ruimten__zoldervertrek__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap"
      },
      "punten": -5.0
    }
  ]
}
```
