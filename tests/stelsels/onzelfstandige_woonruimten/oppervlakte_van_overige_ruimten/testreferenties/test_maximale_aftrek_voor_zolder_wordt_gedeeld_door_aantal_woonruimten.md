# test_maximale_aftrek_voor_zolder_wordt_gedeeld_door_aantal_woonruimten

De maximale aftrek van 5 punten voor een gemeenschappelijke zolder zonder vaste trap wordt gedeeld door het aantal onzelfstandige woonruimten.

Het scenario is het voorbeeld uit de implementatietoelichting. Volgens die
toelichting trekt de huurprijscheck hier de volle 5 punten af; de package
volgt de wettekst.

Bron: wettekst, Bijlage I onder B, toelichting rubriek 2: "De punten voor
de oppervlakte van overige ruimten worden gedeeld door het aantal
onzelfstandige woonruimten op één adres dat toegang en gebruiksrecht
heeft."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.3: "De
maximumaftrek van 5 punten wordt gedeeld door het aantal onzelfstandige
woonruimten.", "maximumaftrek: 5 / 4 = 1,25" en "Omdat wettekst en tool
botsen, volgen wij de wettekst (gedeelde cap)."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                                      15.75 pt
    - Privé
      - Berging                                                      10.40 m²
    - Gedeeld met 4 onzelfstandige woonruimten
      - Zolder                                                       40.40 m²
  Correctie: zolder zonder vaste trap                                            -1.25 pt
                                                                                ------
  Totaal                                                                         14.50 pt
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
      "oppervlakte": 10.4
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
      "oppervlakte": 40.4,
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
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
  "punten": 14.5,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal"
      },
      "punten": 15.75
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
      "aantal": 10.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive__berging",
        "naam": "Berging",
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
        "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal"
        }
      }
    },
    {
      "aantal": 40.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_4_onzelfstandige_woonruimten__zolder",
        "naam": "Zolder",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__subtotaal__gedeeld_met_4_onzelfstandige_woonruimten"
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
      "punten": -1.25
    }
  ]
}
```
