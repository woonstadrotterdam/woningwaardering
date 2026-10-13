# test_gemeenschappelijke_buitenruimte_vanaf_de_minimumafmeting_wordt_gewaardeerd[boven_de_minimumafmeting]

Een gemeenschappelijke buitenruimte met een lengte en breedte van ten minste de minimumafmeting wordt gewaardeerd.

De buitenruimte wordt met 4 onzelfstandige woonruimten op hetzelfde adres
gedeeld.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
diepte)."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

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
      "breedte": 3000.0,
      "lengte": 10000.0,
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
