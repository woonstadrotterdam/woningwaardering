# test_gemeenschappelijke_buitenruimte_onder_de_minimumafmeting_wordt_niet_gewaardeerd

Een gemeenschappelijke buitenruimte die in lengte, breedte of hoogte onder de minimumafmeting blijft, wordt niet gewaardeerd.

Bron: implementatietoelichting zelfstandige woonruimten, 2.8.2; wettekst,
Bijlage I onder A, toelichting rubriek 8.

Een woning zonder gewaardeerde buitenruimte krijgt 5 punten aftrek.

Bron: implementatietoelichting zelfstandige woonruimten, 2.8.5; wettekst,
Bijlage I onder A, toelichting rubriek 8.

## Rapport

```text
BUITENRUIMTEN
  Geen buitenruimten                                                             -5.00 pt
                                                                                ------
  Totaal                                                                         -5.00 pt
```

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "balkon1",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon1",
      "breedte": 2800.0,
      "hoogte": 3170.0,
      "lengte": 1150.0,
      "oppervlakte": 3.14196,
      "gedeeldMetAantalAdressen": 2
    },
    {
      "id": "balkon2",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon2",
      "breedte": 1150.0,
      "hoogte": 3170.0,
      "lengte": 2800.0,
      "oppervlakte": 3.14196,
      "gedeeldMetAantalAdressen": 2
    },
    {
      "id": "balkon3",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "BAL",
        "naam": "Balkon"
      },
      "naam": "Balkon3",
      "breedte": 2800.0,
      "hoogte": 1150.0,
      "lengte": 3170.0,
      "oppervlakte": 3.14196,
      "gedeeldMetAantalAdressen": 2
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
      "code": "BUI",
      "naam": "Buitenruimten"
    }
  },
  "punten": -5.0,
  "woningwaarderingen": [
    {
      "criterium": {
        "id": "buitenruimten__geen_buitenruimten",
        "naam": "Geen buitenruimten"
      },
      "punten": -5.0
    }
  ]
}
```
