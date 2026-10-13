# test_kast_telt_mee_in_de_oppervlakte_van_een_overige_ruimte

De oppervlakte van een kast telt mee in de oppervlakte van de overige ruimte waarop de kast uitkomt.

De zolder zonder vaste trap hoort bij het scenario: de aftrek voor die
zolder hangt af van de oppervlakte van de andere overige ruimten, en dus
van de berging met haar kast.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Meting van de
oppervlakte vindt plaats van muur tot muur, op een hoogte van 1,50 meter
boven de vloer, inclusief de oppervlakte van alle losse en vaste tot de
woning behorende kasten".

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.4: "De
kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
(4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
onder meer energieprestatie, gemeenschappelijke ruimten en
zoldercorrecties."

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Subtotaal                                                                       3.75 pt
    - Privé
      - Berging (+1 kast)                                             2.60 m²
      - Zolder                                                        2.40 m²
  Correctie: zolder zonder vaste trap                                            -1.50 pt
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
      "oppervlakte": 2.4,
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
          "oppervlakte": 0.2
        }
      ]
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
      "oppervlakte": 2.4,
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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "OOZ",
      "naam": "Oppervlakte van overige ruimten"
    }
  },
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal",
        "naam": "Subtotaal"
      },
      "punten": 3.75
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
      "aantal": 2.6,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive__berging",
        "naam": "Berging (+1 kast)",
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
      "aantal": 2.4,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__subtotaal__prive__zolder",
        "naam": "Zolder",
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
        "id": "oppervlakte_van_overige_ruimten__zolder__correctie_zolder_zonder_vaste_trap",
        "naam": "Correctie: zolder zonder vaste trap"
      },
      "punten": -1.5
    }
  ]
}
```
