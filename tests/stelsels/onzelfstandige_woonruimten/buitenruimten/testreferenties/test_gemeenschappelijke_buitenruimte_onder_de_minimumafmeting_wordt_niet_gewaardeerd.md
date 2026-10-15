# test_gemeenschappelijke_buitenruimte_onder_de_minimumafmeting_wordt_niet_gewaardeerd

Een gemeenschappelijke buitenruimte die in lengte, breedte of hoogte onder de minimumafmeting blijft, wordt niet gewaardeerd.

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
      "id": "tuin1",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin1",
      "breedte": 1500.0,
      "hoogte": 2000.0,
      "lengte": 1499.0,
      "oppervlakte": 6.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
    },
    {
      "id": "tuin2",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin2",
      "breedte": 1499.0,
      "hoogte": 2000.0,
      "lengte": 1500.0,
      "oppervlakte": 6.0,
      "gedeeldMetAantalOnzelfstandigeWoonruimten": 4
    },
    {
      "id": "tuin3",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "TUI",
        "naam": "Tuin"
      },
      "naam": "Tuin3",
      "breedte": 1500.0,
      "hoogte": 1999.0,
      "lengte": 1500.0,
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
