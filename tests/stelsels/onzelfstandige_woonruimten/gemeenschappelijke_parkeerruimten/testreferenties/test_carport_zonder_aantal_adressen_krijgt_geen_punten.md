# test_carport_zonder_aantal_adressen_krijgt_geen_punten

Een carport zonder aantal adressen krijgt in deze rubriek geen punten.

Ook het aantal onzelfstandige woonruimten is niet aangeleverd. De package
leest beide ontbrekende aantallen als niet gedeeld. De carport is dan een
privé-buitenruimte en hoort in rubriek 8.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.8.3: "Een
`carport` of `parkeerplaats` is een VERA-buitenruimte: privé wordt die hier
gewaardeerd, gemeenschappelijk in rubriek 10".

De implementatietoelichting vraagt beide attributen op elk type
parkeerplek. Bij een carport waarschuwt de package in deze rubriek niet dat
ze ontbreken; de test legt het huidige gedrag vast.

Bron: implementatietoelichting onzelfstandige woonruimten, 2.10.2: "Deze
attributen dienen ook op elk type parkeerplek meegegeven te worden wanneer
het een onzelfstandige woonruimte betreft."

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

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
      "code": "ONZ",
      "naam": "Onzelfstandige woonruimten"
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
