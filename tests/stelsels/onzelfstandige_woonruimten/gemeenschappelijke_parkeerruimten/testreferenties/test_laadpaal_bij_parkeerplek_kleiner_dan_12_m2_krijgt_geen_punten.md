# test_laadpaal_bij_parkeerplek_kleiner_dan_12_m2_krijgt_geen_punten

Een laadpaal bij een parkeerplek met een oppervlakte onder 12 m² krijgt in deze rubriek geen punten.

De gemeenschappelijke carport van 10 m² krijgt zelf geen punten.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
gangbare personenauto in zijn geheel op past."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

De laadpaal volgt de carport en hoort dan in rubriek 12.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.12.3: "Krijgt
die ruimte in rubriek 10 punten, dan wordt de laadpaal daar gewaardeerd; in
alle andere gevallen hier, met dezelfde deler (aantal adressen × aantal
onzelfstandige woonruimten)."

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 10.0,
      "gedeeldMetAantalAdressen": 3,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 1
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
