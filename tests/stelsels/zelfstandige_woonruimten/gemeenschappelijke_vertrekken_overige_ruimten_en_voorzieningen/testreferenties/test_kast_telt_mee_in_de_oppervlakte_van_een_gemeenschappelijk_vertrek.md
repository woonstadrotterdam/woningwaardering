# test_kast_telt_mee_in_de_oppervlakte_van_een_gemeenschappelijk_vertrek

De oppervlakte van een kast telt mee in de oppervlakte van een gemeenschappelijk vertrek.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
overige ruimten wordt onder deze rubriek aangesloten bij definities en de
meetmethoden als gegeven onder rubriek 1 en 2."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 1: "Meting van de
oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van
1,50 meter boven de vloer, inclusief de oppervlakte van alle tot de woning
behorende losse en vaste kasten."

Bron: implementatietoelichting zelfstandige woonruimten, 2.2.4: "De
kastoppervlakte telt ook mee bij de drempeltoets in `classificeer_ruimte`
(4,00 m² voor vertrek, 2,00 m² voor overige ruimte) en bij totalen voor
onder meer energieprestatie, gemeenschappelijke ruimten en
zoldercorrecties."

Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke vertrek 1
punt per m² gedeeld door het aantal adressen dat toegang en gebruiksrecht
heeft."

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 2 adressen
    - Oppervlakte van vertrekken                                                  6.00 pt
      - Woonkamer (+1 kast)                                          12.00 m²
                                                                                ------
  Totaal                                                                          6.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "woonkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "WOO",
        "naam": "Woonkamer"
      },
      "naam": "Woonkamer",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 2,
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
          "oppervlakte": 2.0
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
      "code": "GVR",
      "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
    }
  },
  "punten": 6.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_vertrekken",
        "naam": "Oppervlakte van vertrekken",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen"
        }
      },
      "punten": 6.0
    },
    {
      "aantal": 12.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_vertrekken__woonkamer",
        "naam": "Woonkamer (+1 kast)",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_2_adressen__oppervlakte_van_vertrekken"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    }
  ]
}
```
