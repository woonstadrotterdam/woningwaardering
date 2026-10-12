# test_kort_aanrechtdeel_naast_aanrecht_vanaf_1m_is_geen_wastafel

Een kort aanrechtdeel telt niet als wastafel naast een aanrecht vanaf 1 meter.

Het korte deel telt dan mee in de aanrechtlengte van de keuken (rubriek 5).

Bron: wettekst, Bijlage I onder A, toelichting rubriek 5: "Een spoelbak in
een keuken die voldoet aan het basisniveau, krijgt geen waardering."

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1: "Staat in
dezelfde ruimte ook een aanrecht vanaf 1 meter, dan telt het korte deel mee
in de aanrechtlengte van de keuken en niet als wastafel."

## Rapport

Geen waarderingen voor Sanitair.

## Waarschuwingen

Geen.

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
          "id": "aanrecht_1",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 800.0
        },
        {
          "id": "aanrecht_2",
          "naam": "Aanrecht",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "AAN",
            "naam": "Aanrecht"
          },
          "lengte": 1200.0
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
      "code": "SAN",
      "naam": "Sanitair"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
