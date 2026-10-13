# test_alleen_zolder_met_vlizotrap_krijgt_de_aftrek

Alleen een zolder met een vlizotrap krijgt de aftrek voor een zolder zonder vaste trap.

Zolder2 is als vertrek aangeleverd; de package waardeert haar als overige
ruimte en waarschuwt daarbij. Zolder3 is gemeenschappelijk voor drie
onzelfstandige woonruimten, waardoor de maximale aftrek door drie wordt
gedeeld.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Indien geen vaste
trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de
zolderruimte met vijf verminderd".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: beleidsboek onzelfstandige woonruimten, 2.1.6: "Het totaal aantal
punten wordt per rubriek afgerond op 0,25 punt".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1.3: "De
detailsoort draagt eis 1 dus zelf; alleen het `Bouwkundigelement`
`vlizotrap` weerspreekt dat." en "Dat gebeurt ook wanneer de ruimte is
ingeschoten met `ruimtesoort` `vertrek`".

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3: "De
maximumaftrek van 5 punten wordt gedeeld door het aantal onzelfstandige
woonruimten."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                                      17.25 pt
    - Privé
      - Zolder1                                                      10.00 m²
      - Zolder2                                                      10.00 m²
    - Gedeeld met 3 onzelfstandige woonruimten
      - Zolder3                                                      10.00 m²
  Correctie: zolder zonder vaste trap                                            -1.67 pt
  Afronding op kwartpunten                                                       -0.08 pt
                                                                                ------
  Totaal                                                                         15.50 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Zolder2' (zolder2) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.
- UserWarning: Ruimte 'Zolder2' (zolder2) is aangeleverd als Vertrek maar wordt gewaardeerd als Overige ruimten.

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
      "oppervlakte": 10.0
    },
    {
      "id": "zolder2",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
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
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
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
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 15.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal"
      },
      "punten": 17.25
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive",
        "naam": "Privé",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
        }
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive__zolder1",
        "naam": "Zolder1",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal__prive"
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
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive__zolder2",
        "naam": "Zolder2",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_3_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 3 onzelfstandige woonruimten",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
        }
      }
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_3_onzelfstandige_woonruimten__zolder3",
        "naam": "Zolder3",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_3_onzelfstandige_woonruimten"
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
      "punten": -1.67
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.08
    }
  ]
}
```
