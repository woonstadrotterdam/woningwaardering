# test_gemeenschappelijke_toiletruimte_wordt_als_overige_ruimte_gewaardeerd

Een gemeenschappelijke toiletruimte wordt als overige ruimte gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Met vertrekken en
overige ruimten wordt onder deze rubriek aangesloten bij definities en de
meetmethoden als gegeven onder rubriek 1 en 2."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 2: "Een toiletruimte
wordt gewaardeerd als overige ruimte als het voldoet aan de voorwaarden van
een overige ruimte."

Bron: wettekst, Bijlage I onder A, rubriek 9: "Gemeenschappelijke overige
ruimte 0,75 punt per m² gedeeld door het aantal adressen dat toegang en
gebruiksrecht heeft."

## Rapport

```text
GEMEENSCHAPPELIJKE VERTREKKEN, OVERIGE RUIMTEN EN VOORZIENINGEN
  Gedeeld met 5 adressen
    - Oppervlakte van overige ruimten                                             1.50 pt
      - Toiletruimte1                                                10.00 m²
  Gedeeld met 6 adressen
    - Oppervlakte van overige ruimten                                             1.25 pt
      - Toiletruimte2                                                10.00 m²
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
      "id": "toiletruimte1",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte1",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 5
    },
    {
      "id": "toiletruimte2",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte2",
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
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_5_adressen__oppervlakte_van_overige_ruimten__toiletruimte1",
        "naam": "Toiletruimte1",
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
        "id": "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen__gedeeld_met_6_adressen__oppervlakte_van_overige_ruimten__toiletruimte2",
        "naam": "Toiletruimte2",
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
