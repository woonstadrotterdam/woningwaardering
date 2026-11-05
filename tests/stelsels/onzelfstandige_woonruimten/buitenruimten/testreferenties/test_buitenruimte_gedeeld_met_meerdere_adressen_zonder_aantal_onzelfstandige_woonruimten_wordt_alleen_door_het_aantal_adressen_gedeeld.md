# test_buitenruimte_gedeeld_met_meerdere_adressen_zonder_aantal_onzelfstandige_woonruimten_wordt_alleen_door_het_aantal_adressen_gedeeld

Een buitenruimte die met meerdere adressen wordt gedeeld en zonder aantal onzelfstandige woonruimten is aangeleverd, wordt alleen door het aantal adressen gedeeld.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.1.4
- implementatietoelichting onzelfstandige woonruimten, 2.8.2

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 adressen
    - Tuin1                                                           6.00 m²     2.25 pt
  Gedeeld met 3 adressen
    - Tuin2                                                           6.00 m²     1.50 pt
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
      "id": "tuin1",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin1",
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 2
    },
    {
      "id": "tuin2",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin2",
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 3
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 3.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen__tuin1",
        "naam": "Tuin1",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.25
    },
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_3_adressen",
        "naam": "Gedeeld met 3 adressen"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_3_adressen__tuin2",
        "naam": "Tuin2",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 1.5
    }
  ]
}
```
