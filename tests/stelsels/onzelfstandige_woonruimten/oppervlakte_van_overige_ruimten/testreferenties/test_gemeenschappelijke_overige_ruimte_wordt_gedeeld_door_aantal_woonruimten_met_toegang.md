# test_gemeenschappelijke_overige_ruimte_wordt_gedeeld_door_aantal_woonruimten_met_toegang

Een gemeenschappelijke overige ruimte wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot die ruimte.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.2.2
- wettekst, Bijlage I onder B, onderdeel 2
- wettekst, Bijlage I onder B, toelichting, inleiding

## Rapport

```text
OPPERVLAKTE VAN OVERIGE RUIMTEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Bijkeuken                                                      12.00 m²
  Gedeeld met 6 onzelfstandige woonruimten
    - Garage                                                         12.00 m²
                                                                                ------
  Totaal                                                                          3.75 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 12.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
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
      "oppervlakte": 12.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 6
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
  "punten": 3.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 12.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten__bijkeuken",
        "naam": "Bijkeuken",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_6_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 6 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 12.0,
      "criterium": {
        "id": "oppervlakte_van_overige_ruimten__gedeeld_met_6_onzelfstandige_woonruimten__garage",
        "naam": "Garage",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_overige_ruimten__gedeeld_met_6_onzelfstandige_woonruimten"
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
