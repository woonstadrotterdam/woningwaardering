# test_spoelbak_in_aanrecht_korter_dan_1m_telt_als_wastafel[precies_1m]

Een spoelbak in een aanrecht korter dan 1 meter telt als wastafel.

Bron: implementatietoelichting zelfstandige woonruimten, 2.6.1.

Dit geval: de keuken heeft een aanrecht van minimaal 1 meter, dus de spoelbak hoort bij de keuken en is geen wastafel

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
          "lengte": 1000.0
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
