# test_punten_van_alle_buitenruimten_worden_na_het_optellen_afgerond_op_een_kwart_punt

De punten van privé- en gemeenschappelijke buitenruimten worden pas na het optellen afgerond op een kwart punt.

Bron:
- implementatietoelichting onzelfstandige woonruimten, 2.8.6
- wettekst, Bijlage I onder B, toelichting rubriek 8

## Rapport

```text
BUITENRUIMTEN
  Privé
    - Balkon1                                                         1.00 m²     0.35 pt
    - Privé buitenruimten aanwezig                                                2.00 pt
  Gedeeld met 4 onzelfstandige woonruimten
    - Balkon2                                                         4.50 m²     0.84 pt
    - Gedeeld met 5 adressen
      - Dakterras                                                    52.00 m²     1.95 pt
  Afronding op kwartpunten                                                        0.11 pt
                                                                                ------
  Totaal                                                                          5.25 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "balkon1",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon1",
      "oppervlakte": 1.0
    },
    {
      "id": "balkon2",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon2",
      "oppervlakte": 4.5,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
    },
    {
      "id": "dakterras",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "DAK",
        "naam": "Dakterras"
      },
      "naam": "Dakterras",
      "oppervlakte": 52.0,
      "gedeeldMetAantalAdressen": 5,
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 5.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 1.0,
      "criterium": {
        "id": "buitenruimten__prive__balkon1",
        "naam": "Balkon1",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 0.35
    },
    {
      "criterium": {
        "id": "buitenruimten__prive__prive_buitenruimten_aanwezig",
        "naam": "Privé buitenruimten aanwezig",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        }
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 4.5,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__balkon2",
        "naam": "Balkon2",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 0.84
    },
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_5_adressen",
        "naam": "Gedeeld met 5 adressen",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        }
      }
    },
    {
      "aantal": 52.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_5_adressen__dakterras",
        "naam": "Dakterras",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__gedeeld_met_5_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 1.95
    },
    {
      "criterium": {
        "id": "buitenruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": 0.11
    }
  ]
}
```
