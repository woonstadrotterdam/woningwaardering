# test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijke_zolder_zonder_vaste_trap

De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijke zolder zonder vaste trap.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
woning behorende kasten" en "Indien geen vaste trap aanwezig is, wordt het
aantal punten van de vloeroppervlakte van de zolderruimte met vijf
verminderd, doch niet met meer punten dan voor de oppervlakte van de
zolderruimten wordt gegeven."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
(4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
onder meer energieprestatie, gemeenschappelijke ruimten en
zoldercorrecties."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
overige ruimten wordt onder deze rubriek aangesloten bij definities en de
meetmethoden als gegeven onder rubriek 1 en 2.", "Gemeenschappelijke overige
ruimten worden met driekwart punt per m² gewaardeerd." en "Deel dit aantal
punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke
binnenruimten."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Gedeeld met 2 adressen
    - Oppervlakte van overige ruimten
      - Subtotaal                                                     9.50 m²     3.75 pt
        - Berging                                                     6.00 m²
        - Zolder (+1 kast)                                            3.50 m²
      - Correctie: zolder zonder vaste trap                                      -1.50 pt
                                                                                ------
  Totaal                                                                          2.25 pt
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
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 2
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
      "oppervlakte": 2.6,
      "gedeeldMetAantalAdressen": 2,
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
      "verbondenRuimten": [
        {
          "id": "kast",
          "soort": {
            "code": "OVR",
            "naam": "Overige ruimten"
          },
          "detailSoort": {
            "code": "KAS",
            "naam": "Kast"
          },
          "naam": "Kast",
          "oppervlakte": 0.9
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen"
        }
      }
    },
    {
      "aantal": 9.5,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 3.75
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal__berging",
        "naam": "Berging",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 3.5,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal__zolder",
        "naam": "Zolder (+1 kast)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__subtotaal"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__zolder__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
        }
      },
      "punten": -1.5
    }
  ]
}
```
