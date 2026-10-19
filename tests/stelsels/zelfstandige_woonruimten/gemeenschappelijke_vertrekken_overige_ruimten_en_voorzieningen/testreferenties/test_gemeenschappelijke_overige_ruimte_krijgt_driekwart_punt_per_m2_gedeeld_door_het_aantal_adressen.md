# test_gemeenschappelijke_overige_ruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen

Een gemeenschappelijke overige ruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.9
- wettekst, Bijlage I onder A, onderdeel 9

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 5 adressen
    - Oppervlakte van overige ruimten                                             1.50 pt
      - Berging1                                                     10.00 m²
  Gedeeld met 6 adressen
    - Oppervlakte van overige ruimten                                             1.25 pt
      - Berging2                                                     10.00 m²
                                                                                ------
  Totaal                                                                          2.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "berging1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging1",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 5
    },
    {
      "id": "berging2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BER",
        "naam": "Berging"
      },
      "naam": "Berging2",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 6
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
  "punten": 2.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen",
        "naam": "Gedeeld met 5 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen"
        }
      },
      "punten": 1.5
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_overige_ruimten__berging1",
        "naam": "Berging1",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_6_adressen",
        "naam": "Gedeeld met 6 adressen"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_6_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_6_adressen"
        }
      },
      "punten": 1.25
    },
    {
      "aantal": 10.0,
      "criterium": {
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_6_adressen__oppervlakte_van_overige_ruimten__berging2",
        "naam": "Berging2",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_6_adressen__oppervlakte_van_overige_ruimten"
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
