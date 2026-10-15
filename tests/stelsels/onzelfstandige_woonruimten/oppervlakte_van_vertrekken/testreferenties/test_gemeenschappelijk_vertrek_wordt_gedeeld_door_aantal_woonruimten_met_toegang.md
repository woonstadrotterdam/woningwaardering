# test_gemeenschappelijk_vertrek_wordt_gedeeld_door_aantal_woonruimten_met_toegang

Een gemeenschappelijk vertrek wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot dat vertrek.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.2.1; wettekst,
Bijlage I onder B, onderdeel 1.

## Rapport

```text
OPPERVLAKTE VAN VERTREKKEN
  Gedeeld met 6 onzelfstandige woonruimten
    - Woonkamer                                                      12.00 m²
  Gedeeld met 4 onzelfstandige woonruimten
    - Slaapkamer                                                     20.00 m²
                                                                                ------
  Totaal                                                                          7.00 pt
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
      "oppervlakte": 12.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 6
    },
    {
      "id": "slaapkamer",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "SLA",
        "naam": "Slaapkamer"
      },
      "naam": "Slaapkamer",
      "oppervlakte": 20.0,
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
      "code": "OVZ",
      "naam": "Oppervlakte van vertrekken"
    }
  },
  "punten": 7.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_6_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 6 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 12.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_6_onzelfstandige_woonruimten__woonkamer",
        "naam": "Woonkamer",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__gedeeld_met_6_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten__slaapkamer",
        "naam": "Slaapkamer",
        "bovenliggendeCriterium": {
          "id": "oppervlakte_van_vertrekken__gedeeld_met_4_onzelfstandige_woonruimten"
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
