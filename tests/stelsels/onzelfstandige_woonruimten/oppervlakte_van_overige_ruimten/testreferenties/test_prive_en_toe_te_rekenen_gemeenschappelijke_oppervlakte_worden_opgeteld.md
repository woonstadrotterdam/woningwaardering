# test_prive_en_toe_te_rekenen_gemeenschappelijke_oppervlakte_worden_opgeteld

De oppervlakte van privé overige ruimten en de toe te rekenen oppervlakte van gemeenschappelijke overige ruimten worden opgeteld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.2.1;
wettekst, Bijlage I onder B, toelichting rubriek 2.

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Privé
    - Slaapkamer                                                      4.00 m²
  Gedeeld met 3 onzelfstandige woonruimten
    - Garage                                                         19.34 m²
    - Bijkeuken                                                       6.06 m²
                                                                                ------
  Totaal                                                                          9.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "slaapkamer",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 4.0
    },
    {
      "id": "garage",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "GAR",
        "naam": "Garage"
      },
      "naam": "Garage",
      "oppervlakte": 19.34,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 3
    },
    {
      "id": "bijkeuken",
      "soort": {
        "code": "OVR",
        "naam": "Overige ruimten"
      },
      "detailSoort": {
        "code": "BIJ",
        "naam": "Bijkeuken"
      },
      "naam": "Bijkeuken",
      "oppervlakte": 6.06,
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
  "punten": 9.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 4.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__prive__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_3_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 3 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 19.34,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_3_onzelfstandige_woonruimten__garage",
        "naam": "Garage",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__gedeeld_met_3_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 6.06,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_3_onzelfstandige_woonruimten__bijkeuken",
        "naam": "Bijkeuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__gedeeld_met_3_onzelfstandige_woonruimten"
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
