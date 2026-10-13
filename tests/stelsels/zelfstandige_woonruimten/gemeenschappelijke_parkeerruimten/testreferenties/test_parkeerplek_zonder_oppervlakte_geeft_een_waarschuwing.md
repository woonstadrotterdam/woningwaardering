# test_parkeerplek_zonder_oppervlakte_geeft_een_waarschuwing

Een parkeerplek zonder oppervlakte is incomplete input en wordt niet gewaardeerd.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Zonder oppervlakte is niet vast te stellen of de parkeerplek de minimale
oppervlakte heeft.

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
gangbare personenauto in zijn geheel op past."

## Rapport

Geen waarderingen voor Gemeenschappelijke parkeerruimten.

## Waarschuwingen

- UserWarning: Ruimte 'Parkeerplek' (parkeerplek) heeft geen oppervlakte

## Input

```json
{
  "ruimten": [
    {
      "id": "parkeerplek",
      "soort": {
        "code": "GEM",
        "naam": "Gemeenschappelijke ruimten en voorzieningen"
      },
      "detailSoort": {
        "code": "PBC",
        "naam": "Parkeerplek buiten behorend bij complex"
      },
      "naam": "Parkeerplek",
      "gedeeldMetAantalAdressen": 10,
      "aantal": 2
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
