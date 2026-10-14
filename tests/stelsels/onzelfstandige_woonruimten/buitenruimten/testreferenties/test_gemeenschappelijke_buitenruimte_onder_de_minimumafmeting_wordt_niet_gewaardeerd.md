# test_gemeenschappelijke_buitenruimte_onder_de_minimumafmeting_wordt_niet_gewaardeerd

Een gemeenschappelijke buitenruimte die in lengte en breedte onder de minimumafmeting blijft, wordt niet gewaardeerd.

De tuin is 1 meter lang en 1 meter breed; de hoogte van 2,5 meter voldoet
wel aan de minimumafmeting.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 8: "Er geldt een
minimumafmeting van 2 m x 1,5 m x 1,5 m (respectievelijk hoogte, breedte,
diepte)."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2: "Indien
een van deze afmetingen kleiner is dan noodzakelijk voor waardering leidt
dat ertoe dat de ruimte niet wordt gewaardeerd."

## Rapport

Geen waarderingen voor Buitenruimten.

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
      "breedte": 1000.0,
      "hoogte": 2500.0,
      "lengte": 1000.0,
      "oppervlakte": 6.0,
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
  "punten": 0.0,
  "woningwaarderingen": []
}
```
