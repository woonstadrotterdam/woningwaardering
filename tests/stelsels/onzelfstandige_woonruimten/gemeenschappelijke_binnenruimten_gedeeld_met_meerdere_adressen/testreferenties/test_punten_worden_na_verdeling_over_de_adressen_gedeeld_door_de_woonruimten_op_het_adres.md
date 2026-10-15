# test_punten_worden_na_verdeling_over_de_adressen_gedeeld_door_de_woonruimten_op_het_adres

De punten voor een gemeenschappelijke binnenruimte worden na verdeling over de meerdere adressen nog gedeeld door het aantal onzelfstandige woonruimten op dat adres.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.9.1;
implementatietoelichting onzelfstandige woonruimten, 2.9.2; wettekst,
Bijlage I onder B, toelichting rubriek 9.

## Rapport

```text
GEMEENSCHAPPELIJKE BINNENRUIMTEN GEDEELD MET MEERDERE ADRESSEN
  Gedeeld met 3 onzelfstandige woonruimten
    - Gedeeld met 2 adressen
      - Oppervlakte van overige ruimten                                           0.25 pt
        - Toiletruimte                                                2.00 m²
      - Sanitair
        - Toiletruimte
          - Staand Toilet                                             1.00 st     0.50 pt
                                                                                ------
  Totaal                                                                          0.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "toiletruimte",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "TOI",
        "naam": "Toiletruimte"
      },
      "naam": "Toiletruimte",
      "oppervlakte": 2.0,
      "gedeeldMetAantalAdressen": 2,
      "installaties": [
        {
          "code": "STO",
          "naam": "Staand Toilet"
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
      "code": "GBA",
      "naam": "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"
    }
  },
  "punten": 0.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 3 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten",
        "naam": "Oppervlakte van overige ruimten",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        }
      },
      "punten": 0.25
    },
    {
      "aantal": 2.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten__toiletruimte",
        "naam": "Toiletruimte",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__oppervlakte_van_overige_ruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__sanitair",
        "naam": "Sanitair",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        }
      }
    },
    {
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__sanitair__toiletruimte",
        "naam": "Toiletruimte",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__sanitair"
        }
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__sanitair__toiletruimte__staand_toilet",
        "naam": "Staand Toilet",
        "bovenliggendeCriterium": {
          "id": "gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__gedeeld_met_3_onzelfstandige_woonruimten__gedeeld_met_2_adressen__sanitair__toiletruimte"
        },
        "meeteenheid": {
          "code": "STU",
          "naam": "Stuks"
        }
      },
      "punten": 0.5
    }
  ]
}
```
