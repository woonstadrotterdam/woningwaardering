# test_parkeerplek_zonder_oppervlakte_geeft_een_waarschuwing

Een parkeerplek zonder oppervlakte geeft een waarschuwing over incomplete input.

De package waardeert de parkeerplek niet: zonder oppervlakte is niet vast te
stellen of ze de minimale oppervlakte heeft.

Bron: docs/aan-de-slag, Warnings: "Bij incomplete of onjuiste inputdata
genereert de package een `UserWarning`."

Bron: wettekst, Bijlage I onder A, toelichting rubriek 10: "Een parkeerplek
is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waar een
gangbare personenauto in zijn geheel op past."

Bron: wettekst, Bijlage I onder B, toelichting, inleiding: "Dit betekent
dat de toelichting onder bijlage I, onder A, voor alle rubrieken van
overeenkomstige toepassing is."

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
