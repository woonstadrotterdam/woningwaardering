# test_carport_zonder_aantal_adressen_krijgt_geen_punten

Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

De package leest het ontbrekende aantal als niet gedeeld met andere
adressen. De carport is dan een privé-buitenruimte en hoort in rubriek 8.

Bron: implementatietoelichting zelfstandige woonruimten, 2.8.3: "Een
`carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
gewaardeerd, gemeenschappelijk in rubriek 10".

De implementatietoelichting zegt dat bij een ontbrekend aantal adressen een
waarschuwing volgt. Bij een carport geeft de package die in deze rubriek
niet; de test legt het huidige gedrag vast.

Bron: implementatietoelichting zelfstandige woonruimten, 2.10.4: "Dit
attribuut dient ook op elk type parkeerplek meegegeven te worden. Ontbreekt
het, dan volgt een `UserWarning` en gaan we uit van niet gedeeld met andere
adressen."

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

Geen.

## Input

```json
{
  "ruimten": [
    {
      "id": "carport",
      "soort": {
        "code": "BTR",
        "naam": "Buitenruimte"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12.0,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal",
          "naam": "Laadpaal",
          "soort": {
            "code": "VOO",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ],
      "aantal": 5
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
      "code": "GPA",
      "naam": "Gemeenschappelijke parkeerruimten"
    }
  },
  "punten": 0.0,
  "woningwaarderingen": []
}
```
