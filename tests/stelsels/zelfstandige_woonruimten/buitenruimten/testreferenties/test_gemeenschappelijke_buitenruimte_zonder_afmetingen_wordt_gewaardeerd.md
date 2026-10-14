# test_gemeenschappelijke_buitenruimte_zonder_afmetingen_wordt_gewaardeerd

Een gemeenschappelijke buitenruimte zonder lengte, breedte en hoogte wordt gewaardeerd.

De package toetst de minimumafmeting alleen op de afmetingen die zijn
ingevuld.

Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2: "Alleen als
een waarde is ingevuld wordt deze getoetst tegen 2000 × 1500 × 1500 mm."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
het aantal adressen dat toegang heeft tot de buitenruimte."

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 adressen                                             20.00 m²     7.50 pt
    - Dakterras                                                      20.00 m²
                                                                                ------
  Totaal                                                                          7.50 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
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
      "oppervlakte": 20.0,
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
  "punten": 7.5,
  "woningwaarderingen": [
    {
      "aantal": 20.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen",
        "naam": "Gedeeld met 2 adressen",
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 7.5
    },
    {
      "aantal": 20.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_adressen__dakterras",
        "naam": "Dakterras",
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
