# test_keuken_gedeeld_met_andere_adressen_telt_niet_mee

Een keuken die met andere adressen wordt gedeeld, krijgt in rubriek 5 geen punten.

Zo'n keuken hoort bij rubriek 9. De package geeft hier een waarschuwing,
omdat de eenheid zonder deze keuken geen keuken heeft.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 9: "Bepaal eventueel
van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7".

Bron: implementatietoelichting zelfstandige woonruimten, 2.9.2: "Een waarde
van 2 of hoger wordt geïnterpreteerd als een gemeenschappelijke ruimte."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

## Rapport

Geen waarderingen voor Keuken.

## Waarschuwingen

- UserWarning: Eenheid (None) kan niet gewaardeerd worden voor stelselgroep Keuken omdat er geen keuken is gevonden.

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
      "gedeeldMetAantalAdressen": 4,
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
          "lengte": 3150.0
        }
      ],
      "installaties": [
        {
          "code": "IKI",
          "naam": "Inbouw kookplaat inductie"
        },
        {
          "code": "EHM",
          "naam": "Éénhandsmengkraan"
        },
        {
          "code": "IKO",
          "naam": "Inbouw koelkast"
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
