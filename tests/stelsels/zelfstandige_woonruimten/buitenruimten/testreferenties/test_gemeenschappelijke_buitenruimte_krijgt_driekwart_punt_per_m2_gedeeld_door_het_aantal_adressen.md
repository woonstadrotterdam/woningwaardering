# test_gemeenschappelijke_buitenruimte_krijgt_driekwart_punt_per_m2_gedeeld_door_het_aantal_adressen

Een gemeenschappelijke buitenruimte krijgt 0,75 punt per m², gedeeld door het aantal adressen dat toegang heeft.

De input is het rekenvoorbeeld uit de wettekst.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Per vierkante
meter geldt een waardering van driekwart punt. Dat wordt daarna gedeeld door
het aantal adressen dat toegang heeft tot de buitenruimte." en "Voorbeeld:
een woongebouw met een gemeenschappelijk dakterras van 30 m² waartoe drie
adressen toegang hebben, wordt gewaardeerd met: (0,75 x 30) / 3 = 7,5
punten."

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 3 adressen                                             30.00 m²     7.50 pt
    - Dakterras                                                      30.00 m²
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
  "punten": 7.5,
  "woningwaarderingen": [
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
    }
  ]
}
```
