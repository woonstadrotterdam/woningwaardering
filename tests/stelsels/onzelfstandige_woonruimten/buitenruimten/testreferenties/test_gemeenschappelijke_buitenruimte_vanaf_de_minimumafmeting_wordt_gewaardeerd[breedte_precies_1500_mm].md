# test_gemeenschappelijke_buitenruimte_vanaf_de_minimumafmeting_wordt_gewaardeerd[breedte_precies_1500_mm]

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

Dit geval: de breedte van 1,5 meter is precies de minimumafmeting; het balkon is het gemeenschappelijke balkon uit het rekenvoorbeeld in de toelichting bij de wettekst

## Rapport

```text
BUITENRUIMTEN
  Gedeeld met 4 onzelfstandige woonruimten
    - Balkon                                                          4.50 m²     0.84 pt
  Afronding op kwartpunten                                                       -0.09 pt
                                                                                ------
  Totaal                                                                          0.75 pt
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
      "breedte": 1500.0,
      "lengte": 3000.0,
      "oppervlakte": 4.5,
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
  "punten": 0.75,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten",
        "naam": "Gedeeld met 4 onzelfstandige woonruimten"
      }
    },
    {
      "aantal": 4.5,
      "criterium": {
        "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten__balkon",
        "naam": "Balkon",
        "bovenliggendeCriterium": {
          "id": "buitenruimten__gedeeld_met_4_onzelfstandige_woonruimten"
        },
        "meeteenheid": {
          "code": "M2",
          "naam": "Vierkante meter, m2"
        }
      },
      "punten": 0.84
    },
    {
      "criterium": {
        "id": "buitenruimten__afronding_op_kwartpunten",
        "naam": "Afronding op kwartpunten"
      },
      "punten": -0.09
    }
  ]
}
```
