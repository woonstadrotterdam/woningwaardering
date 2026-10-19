# test_gemeenschappelijke_buitenruimte_vanaf_de_minimumafmeting_wordt_gewaardeerd

Een gemeenschappelijke buitenruimte met een lengte, breedte en hoogte van ten minste de minimumafmeting wordt gewaardeerd.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.8.2
- wettekst, Bijlage I onder A, toelichting rubriek 8

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
      "breedte": 1500.0,
      "hoogte": 2000.0,
      "lengte": 1500.0,
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
