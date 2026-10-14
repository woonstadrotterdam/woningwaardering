# test_buitenruimte_gedeeld_met_meerdere_adressen_wordt_door_het_aantal_adressen_en_daarna_door_het_aantal_onzelfstandige_woonruimten_gedeeld

Een gemeenschappelijke buitenruimte die met meerdere adressen wordt gedeeld, krijgt 0,75 punt per m², gedeeld door het aantal adressen en daarna door het aantal onzelfstandige woonruimten op het adres.

Tuin1 wordt met 2 adressen gedeeld en Tuin2 met 3 adressen; tot beide
hebben 2 onzelfstandige woonruimten op het adres toegang.

Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
buitenruimten gedeeld met meerdere adressen", "0,75 punt per m², gedeeld
door het aantal adressen dat toegang en gebruiksrecht heeft, en daarna
gedeeld door het aantal onzelfstandige woonruimten op dat adres".

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Gedeeld met 2 adressen
      - Tuin1                                                         6.00 m²     1.13 pt
    - Gedeeld met 3 adressen
      - Tuin2                                                         6.00 m²     0.75 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          2.00 pt
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
      "gedeeldMetAantalAdressen": 2,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
      "gedeeldMetAantalAdressen": 3,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 2
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
  "punten": 2.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen__tuin1",
        "naam": "Tuin1",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_2_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 1.13
    },
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_3_adressen",
        "naam": "Gedeeld met 3 adressen",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_3_adressen__tuin2",
        "naam": "Tuin2",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 0.75
    },
    {
      "criterium": {
        "id": "buitenruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.12
    }
  ]
}
```
