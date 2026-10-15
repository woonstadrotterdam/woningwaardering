# test_gemeenschappelijke_buitenruimte_onder_de_minimumafmeting_wordt_niet_gewaardeerd

Een gemeenschappelijke buitenruimte die in lengte en breedte onder de minimumafmeting blijft, wordt niet gewaardeerd.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.2; wettekst,
Bijlage I onder A, toelichting rubriek 8 (via Bijlage I onder B,
toelichting, inleiding).

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
