# test_gemeenschappelijke_buitenruimte_boven_de_minimumafmeting_wordt_gewaardeerd

Een gemeenschappelijke buitenruimte met een lengte en breedte boven de minimumafmeting wordt gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
diepte)."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
het aantal adressen dat toegang heeft tot de buitenruimte."

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 adressen                                              6.00 m²     2.25 pt
    - Tuin                                                            6.00 m²
                                                                                ------
  Totaal                                                                          2.25 pt
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
      "breedte": 2000.0,
      "lengte": 10000.0,
      "oppervlakte": 6.0,
      "gedeeldMetAantalAdressen": 2
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
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.25
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen__tuin",
        "naam": "Tuin",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_adressen"
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
