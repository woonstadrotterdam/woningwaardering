# test_maximum_van_15_punten_geldt_voor_prive_en_gemeenschappelijke_buitenruimten_samen

Privé- en gemeenschappelijke buitenruimten krijgen samen hooguit 15 punten.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.8
- wettekst, Bijlage I onder A, toelichting rubriek 8

## Rapport

```text
BUITENRUIMTEN
  Privé                                                              30.00 m²    10.50 pt
    - Tuin                                                           30.00 m²
  Gedeeld met 3 adressen                                             30.00 m²     7.50 pt
    - Dakterras                                                      30.00 m²
  Privé buitenruimten aanwezig                                                    2.00 pt
  Maximaal 15 punten                                                             -5.00 pt
                                                                                ------
  Totaal                                                                         15.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "tuin",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin",
      "oppervlakte": 30.0
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
      "oppervlakte": 30.0,
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
    },
    "stelselgroep": {
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": 15.0,
  "woningwaarderingen": [
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 10.5
    },
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__prive__tuin",
        "naam": "Tuin",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_3_adressen",
        "naam": "Gedeeld met 3 adressen",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 7.5
    },
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_3_adressen__dakterras",
        "naam": "Dakterras",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_3_adressen"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      }
    },
    {
      "criterium": {
        "id": "buitenruimten__prive_buitenruimten_aanwezig",
        "naam": "Privé buitenruimten aanwezig"
      },
      "punten": 2.0
    },
    {
      "criterium": {
        "id": "buitenruimten__maximering",
        "naam": "Maximaal 15 punten"
      },
      "punten": -5.0
    }
  ]
}
```
