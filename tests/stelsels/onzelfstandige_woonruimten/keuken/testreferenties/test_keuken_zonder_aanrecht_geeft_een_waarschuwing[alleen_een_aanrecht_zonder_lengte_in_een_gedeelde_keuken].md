# test_keuken_zonder_aanrecht_geeft_een_waarschuwing[alleen_een_aanrecht_zonder_lengte_in_een_gedeelde_keuken]

Een keuken zonder aanrecht is incomplete input en wordt niet gewaardeerd.

Dit geval: het enige aanrecht heeft geen lengte en telt daarom niet als aanrecht; de keuken wordt met 2 onzelfstandige woonruimten gedeeld.

## Rapport

Geen waarderingen voor Keuken.

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor Keuken.

## Input

```json
{
  "ruimten": [
    {
      "id": "keuken",
      "soort": {
        "code": "VTK",
        "naam": "Vertrek"
      },
      "detailSoort": {
        "code": "KEU",
        "naam": "Keuken"
      },
      "naam": "Keuken",
      "oppervlakte": 10.0,
      "bouwkundigeElementen": [
        {
          "id": "aanrecht",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          }
        }
      ],
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
      "code": "KEU",
      "naam": "Keuken"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
