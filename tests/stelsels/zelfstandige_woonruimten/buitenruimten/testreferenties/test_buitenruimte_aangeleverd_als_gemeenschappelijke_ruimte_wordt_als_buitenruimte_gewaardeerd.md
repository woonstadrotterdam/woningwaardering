# test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd

Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
ruimtesoort waarmee het dakterras is gewaardeerd.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Voorbeeld: een
woongebouw met een gemeenschappelijk dakterras van 30 m² waartoe drie
adressen toegang hebben, wordt gewaardeerd met: (0,75 x 30) / 3 = 7,5
punten."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 3 adressen                                             30.00 m²     7.50 pt
    - Dakterras                                                      30.00 m²
                                                                                ------
  Totaal                                                                          7.50 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Dakterras' (dakterras) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Buitenruimte.

## Input

```json
{
  "ruimten": [
    {
      "id": "dakterras",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
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
