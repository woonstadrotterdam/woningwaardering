# test_aanrecht_korter_dan_1m_krijgt_geen_punten

Een aanrecht korter dan 1 meter krijgt geen punten.

De package geeft daarbij een waarschuwing: de keuken heeft geen aanrecht
van minimaal 1 meter.

Bron: wettekst, Bijlage I onder B, onderdeel 5.1: "Minder dan 1 m 0 punten".

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

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
          },
          "lengte": 999.0
        }
      ]
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
