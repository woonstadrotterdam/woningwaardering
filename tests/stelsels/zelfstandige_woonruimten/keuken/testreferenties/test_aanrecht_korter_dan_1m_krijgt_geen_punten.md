# test_aanrecht_korter_dan_1m_krijgt_geen_punten

Een aanrecht korter dan 1 meter krijgt geen punten.

Bron:
- implementatietoelichting zelfstandige woonruimten, 2.5.2
- wettekst, Bijlage I onder A, onderdeel 5.1

## Rapport

Geen waarderingen voor Keuken.

## Waarschuwingen

- UserWarning: Ruimte 'Keuken' (keuken) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor Keuken.
- UserWarning: Eenheid (eenheid) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

## Input

```json
{
  "id": "eenheid",
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
      "code": "ZEL",
      "naam": "Zelfstandige woonruimten"
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
