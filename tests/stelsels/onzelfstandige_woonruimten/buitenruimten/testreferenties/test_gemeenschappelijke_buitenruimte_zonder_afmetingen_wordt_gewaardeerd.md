# test_gemeenschappelijke_buitenruimte_zonder_afmetingen_wordt_gewaardeerd

Een gemeenschappelijke buitenruimte zonder lengte, breedte en hoogte wordt gewaardeerd.

De package toetst de minimumafmeting alleen op de afmetingen die zijn
ingevuld.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2: "Alleen
als een waarde is ingevuld wordt deze getoetst tegen 2000 × 1500 × 1500
mm."

Bron: wettekst, Bijlage I onder B, rubriek 8: "Gemeenschappelijke
buitenruimte(n) op hetzelfde adres", "0,75 punt per m², gedeeld door het
aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft".

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Tuin                                                           30.00 m²     5.63 pt
  Afronding op kwartpunten                                                        0.12 pt
                                                                                ------
  Totaal                                                                          5.75 pt
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
      "oppervlakte": 30.0,
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
  "punten": 5.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 30.0,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__tuin",
        "naam": "Tuin",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 5.63
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
