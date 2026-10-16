# test_maximum_van_15_punten_geldt_voor_prive_en_gemeenschappelijke_buitenruimten_samen

Privé- en gemeenschappelijke buitenruimten krijgen samen hooguit 15 punten.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8; wettekst,
Bijlage I onder B, onderdeel 8.

## Rapport

```text
BUITENRUIMTEN
  Privé
    - Balkon                                                         20.00 m²     7.00 pt
    - Privé buitenruimten aanwezig                                                2.00 pt
  Gedeeld met 2 onzelfstandige woonruimten
    - Tuin                                                           30.00 m²    11.25 pt
  Maximaal 15 punten                                                             -5.25 pt
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
      "id": "balkon",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "oppervlakte": 20.0
    },
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
      "oppervlakte": 30.0,
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
  "punten": 15.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__prive",
        "naam": "Privé"
      }
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "buitenruimten__prive__balkon",
        "naam": "Balkon",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__prive"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 7.0
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
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__tuin",
        "naam": "Tuin",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 11.25
    },
    {
      "criterium": {
        "id": "buitenruimten__maximaal_15_punten",
        "naam": "Maximaal 15 punten"
      },
      "punten": -5.25
    }
  ]
}
```
