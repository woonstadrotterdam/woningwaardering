# test_buitenruimte_aangeleverd_als_gemeenschappelijke_ruimte_wordt_als_buitenruimte_gewaardeerd

Een buitenruimte die als gemeenschappelijke ruimte is aangeleverd, wordt als buitenruimte gewaardeerd.

De package waarschuwt dat de aangeleverde ruimtesoort afwijkt van de
ruimtesoort waarmee het balkon is gewaardeerd. Dat de package het balkon
naar zijn detailsoort waardeert, is een keuze die in geen bron staat.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 2 onzelfstandige woonruimten
    - Balkon                                                          6.00 m²     2.25 pt
                                                                                ------
  Totaal                                                                          2.25 pt
```

## Waarschuwingen

- UserWarning: Ruimte 'Balkon' (balkon) is aangeleverd als Gemeenschappelijke ruimten en voorzieningen maar wordt gewaardeerd als Buitenruimte.

## Input

```json
{
  "ruimten": [
    {
      "id": "balkon",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon",
      "oppervlakte": 6.0,
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
  "punten": 2.25,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 2 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 6.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten__balkon",
        "naam": "Balkon",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_2_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 2.25
    }
  ]
}
```
